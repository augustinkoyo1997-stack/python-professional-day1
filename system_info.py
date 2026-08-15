import platform 
import sys
chemin =r'C:\Users\Augustin\python-professional-day1'

def show_system_info():
   return {
		"Computer": platform.node(),
		"Machine" : platform.machine(),
		"OS"      : platform.system(),
		"Python"  : sys.version.split()[0]
	  }


def display_system_info(info):
	"""Display system information in a readable format"""
	print("=" * 40)
	print("=" * 5)
	print("SYSTEM INFORMATION")
	print("=" * 5)
	for key,value in info.items():
	    print(f"{key}:{value}")
	    print("=" * 10)

def main():
	"""Application  entry point """
	system_info = show_system_info() 
	display_system_info(system_info)
	
	if __name__=="__main__":
	   main()

print("Git tranning--version 2")
print("version  developpée par le develeloppeur A et développée B")
