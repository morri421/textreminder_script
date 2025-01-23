import getpass
import os
USER_NAME = getpass.getuser()
current_file_path = __file__

def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.realpath(current_file_path)
    # r' stands for raw string - use it when you need to use a backlash
    # %s stands for placeholder for string
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" "%s"' % file_path)