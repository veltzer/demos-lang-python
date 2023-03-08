from gi.repository import Gio

all_apps = Gio.AppInfo.get_all()  # Returns a list of DesktopAppInfo objects (see docs)

# For example, print display name and description of all apps
for app in all_apps:
    print(app.get_display_name())
    print(f"\t{app.get_filename()}")  # type: ignore[attr-defined]
    print(f"\t{app.get_description()}")
