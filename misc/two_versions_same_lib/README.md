# Two versions of the same library in one Python process

This project demonstrates loading **two different versions of `requests`**
(2.28.2 and 2.31.0) inside a single Python process, using `sys.path` +
`importlib` juggling. As a bonus, a *third* `requests` installed normally in
your environment keeps working untouched.

(Why 2.28.2 and not something older like 2.20.0? Pre-2.20 `requests` vendors an
old `urllib3`/`six` whose import-time `sys.meta_path` trickery is broken on
Python 3.14. Pick versions that each work on your interpreter.)

## The idea

`import requests` is cached in `sys.modules`. Once it's loaded, every later
`import requests` — including the ones *inside* the library itself
(`import urllib3`, `import idna`, ...) — returns that cached copy. So you can't
just `pip install` both versions and hope.

The trick:

1. Install each version into its **own directory** (not site-packages):

   ```bash
   ./setup_libs.sh
   # which is just:
   #   pip install --target ./libs/requests_v2_28 "requests==2.28.2"
   #   pip install --target ./libs/requests_v2_31 "requests==2.31.0"
   ```

   (Two separate `pip install` commands — you can't ask one `pip` invocation
   for two versions of the same package; the resolver refuses.)

2. To load a version: stash the current `sys.modules` and `sys.path`, **evict**
   `requests` and all of its dependency packages from `sys.modules`, prepend the
   target directory to `sys.path`, `import requests`, then **snapshot** the
   freshly-imported module objects and **restore** the original `sys.modules` /
   `sys.path`.

   Because we restored `sys.modules`, the next load of the *other* version
   starts from a clean slate and pulls in *its* bundled `urllib3` / `idna` /
   `certifi`, not the other version's.

3. Hold onto the returned module object. It (and its submodules) keep working
   even though they're no longer in `sys.modules`.

See `dual_loader.py` for the mechanism and `demo.py` for it in action.

## Caveats (read these before doing this for real)

- This works cleanly only for **pure-Python** packages. A C-extension module
  (`foo._speedups`) can usually only be loaded **once** per process — the second
  load will either fail or silently return the first. `requests`' deps are
  pure-Python so we're fine; `numpy`/`pandas` would not be.
- Two `requests` modules means two of *everything*: two `Session` classes, two
  `requests.exceptions.HTTPError` types. `except v2_31.exceptions.HTTPError`
  will **not** catch an error raised by `v2_20`. Don't pass objects between the
  two worlds.
- This is genuinely a last resort. Real fixes, in order of preference:
  pin to one version → vendor the conflicting dep → run the second version in a
  subprocess → *then* consider this.

## Run it

```bash
./setup_libs.sh     # one-time: populates ./libs/
python demo.py
```

Expected output: `requests` 2.28.2 (bundled urllib3 1.26.x) and 2.31.0 (bundled
urllib3 2.x) reporting different `__version__`, different `Session` classes,
different `HTTPError` types — and a demonstration that
`except v2_31.exceptions.HTTPError` does *not* catch an error raised by the
v2.28 module.

## Files

| file             | what it is                                                        |
|------------------|-------------------------------------------------------------------|
| `setup_libs.sh`  | installs the two `requests` versions under `./libs/`               |
| `dual_loader.py` | `load_package(name, dir)` — the isolated-import mechanism          |
| `demo.py`        | loads both versions and prints proof they're independent          |
| `libs/`          | the two installed versions (generated; safe to delete & recreate) |
