# Program for TUI.
import os
# To change the font colour to red.
os.system("tput setaf 1")
# To print the statement with 3 tab.
print("\t\t\tWelcome to TUI")
# To change the font colour to white.
os.system("tput setaf 7")
print("\t\t\t==============")

os.system("tput setaf 1")

print("""press 1 : TO see the date
press 2 : To see the calander
press 3 : To see the history
press 4 : To see the list of files and directories
press 5 : To see the details of files and directories
""")

os.system("tput setaf 7")

choice=input("Enter your choice : ")

if int(choice) == 1:
	os.system("date")
else:
	print("Option not supported , try for the next option")
	
