import platform 
import sys


def get_computer_name():
    return f"Computer:{ platform.node()}"

def get_os_version():
    return f"Machine:{platform.machine()}"

def get_operating_system():
    return f"OS:{platform.system()}"

def get_python_version():
    return f"Python:{sys.version.split()[0]}"


def show_system_info():
   print("SYSTEM INFORMATION")
   print("=" *40)
   print(get_computer_name())
   print(get_os_version())
   print(get_operating_system())
   print(get_python_version())
   print("=" *40)


show_system_info()
print("System information tool -version 2")
print("System information tool -version 3")










