import os

def get_apps():
    apps = []
    for file in os.listdir("/usr/share/applications"):
        if file.split(".")[-1] == "desktop":
            details = {}
            open_file = open("/usr/share/applications/"+file, "r")
            text = open_file.read()
            for line in text.split("\n"):
                if "[" not in line and line != "" and "#" not in line:
                    variables = line.split("=")
                    details[variables[0]] = variables[1]
            apps.append(details)
    return apps