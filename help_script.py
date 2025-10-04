import sys

def help_script():
    print("--help script feature is under development. To be released soon!")
    
if "--help" in sys.argv:
    help_script();
else:
    print("--help flag is missing")    