"""Load a specific, directory-installed version of a package by name.

The mechanism, step by step (see ``load_package``):

  * Snapshot ``sys.path`` and ``sys.modules``.
  * Evict the target top-level package *and every currently-imported module*
    from ``sys.modules``.  We are deliberately heavy-handed: we drop everything
    that isn't part of the standard library so that the package's transitive
    dependencies (urllib3, idna, certifi, ...) get re-imported from *this*
    version's directory rather than reused from a previous load.
  * Prepend the version's install directory to ``sys.path`` and import.
  * Snapshot the freshly-created module objects (the package + anything new in
    ``sys.modules``), then restore the original ``sys.path`` / ``sys.modules``.

The returned module keeps working after restoration because Python modules hold
direct references to their submodules; they don't need to stay in
``sys.modules`` once fully imported.
"""

from __future__ import annotations

import importlib
import sys
import types
from contextlib import contextmanager
from pathlib import Path


# Modules that are safe (and necessary) to keep across an isolated import:
# the standard library and the import machinery itself.  Everything else gets
# evicted so the target version brings in its own copy.
def _is_stdlib_or_builtin(name: str) -> bool:
    root = name.split(".", 1)[0]
    if root in sys.builtin_module_names:
        return True
    mod = sys.modules.get(root)
    if mod is None:
        return False
    # No __file__ -> builtin/frozen.  Otherwise: lives under the stdlib dir?
    spec = getattr(mod, "__spec__", None)
    origin = getattr(spec, "origin", None) or getattr(mod, "__file__", None)
    if origin in (None, "built-in", "frozen"):
        return True
    try:
        stdlib_dir = Path(importlib.__file__).resolve().parents[1]
        return stdlib_dir in Path(origin).resolve().parents
    except (ValueError, OSError):
        return False


@contextmanager
def _isolated_import_environment(extra_path: str):
    saved_path = list(sys.path)
    saved_modules = dict(sys.modules)
    try:
        # Drop non-stdlib modules so the target dir wins for the whole subtree.
        for name in list(sys.modules):
            if not _is_stdlib_or_builtin(name):
                del sys.modules[name]
        sys.path.insert(0, extra_path)
        importlib.invalidate_caches()
        yield
    finally:
        sys.path[:] = saved_path
        sys.modules.clear()
        sys.modules.update(saved_modules)
        importlib.invalidate_caches()


def load_package(package_name: str, install_dir: str | Path) -> types.ModuleType:
    """Import ``package_name`` from ``install_dir`` in an isolated fashion.

    Returns the module object.  It is NOT left in ``sys.modules`` — so a later
    ``import {package_name}`` (or another ``load_package`` call) is unaffected.
    """
    install_dir = str(Path(install_dir).resolve())
    with _isolated_import_environment(install_dir):
        module = importlib.import_module(package_name)
        # Force-import the bits of requests we care about while the isolated
        # environment is active, so their submodule references are wired up to
        # this version before we restore sys.modules.
        for sub in ("sessions", "models", "exceptions", "adapters", "api"):
            try:
                importlib.import_module(f"{package_name}.{sub}")
            except ModuleNotFoundError:
                pass
        return module


if __name__ == "__main__":  # tiny smoke test
    here = Path(__file__).parent
    v28 = load_package("requests", here / "libs" / "requests_v2_28")
    v31 = load_package("requests", here / "libs" / "requests_v2_31")
    print("v2.28 dir:", v28.__version__)
    print("v2.31 dir:", v31.__version__)
    assert v28.__version__ == "2.28.2", v28.__version__
    assert v31.__version__ == "2.31.0", v31.__version__
    assert v28 is not v31
    print("ok")
