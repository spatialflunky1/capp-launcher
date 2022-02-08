import parse_files

apps = parse_files.get_apps()

for app in apps:
    print(app["Type"])