import os.path
import pkgutil

import pkg_resources

static_file_content = pkg_resources.resource_string(
    'my_pack', 'static_file.html').decode()
print(f"static_file_content is [{static_file_content}]")


def get_real_filename(filename):
    return os.path.join(os.path.dirname(__file__), filename)


def get_data(filename):
    return open(get_real_filename(filename), 'rb').read()


static_file_content2 = get_data('static_file.html').decode()
print(f"static_file_content2 is [{static_file_content2}]")

static_file_content3 = pkgutil.get_data('my_pack', 'static_file.html').decode()
print(f"static_file_content3 is [{static_file_content3}]")
