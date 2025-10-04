import sys
import help_script_message

def help_script():
    print(help_script_message.help_message)
    
if "--help" in sys.argv:
    help_script();
else:
    print(help_script_message.help_invalid_message)    