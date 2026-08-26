""" mymod.py """

import importlib.resources
import os.path
import pkgutil

# "__package__" is typed as "str | None" and is empty when this file is run as
# a plain script instead of being imported as part of the package. Fall back to
# the directory name so all three methods below work either way.
package = __package__ or os.path.basename(os.path.dirname(os.path.abspath(__file__)))

static_file_content = (
    importlib.resources.files(package)
    .joinpath("static_file.html")
    .read_text(encoding="utf-8")
)
print(f"static_file_content is [{static_file_content}]")


def get_real_filename(filename):
    return os.path.join(os.path.dirname(__file__), filename)


def get_data(filename):
    return open(get_real_filename(filename), "rb").read()


static_file_content2 = get_data("static_file.html").decode()
print(f"static_file_content2 is [{static_file_content2}]")

static_file_content3_bytes = pkgutil.get_data(package, "static_file.html")
assert isinstance(static_file_content3_bytes, bytes)
static_file_content3 = static_file_content3_bytes.decode()
print(f"static_file_content3 is [{static_file_content3}]")
