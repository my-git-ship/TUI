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
press 3 : To see the IPAdderss
press 4 : To see the list of files and directories
press 5 : To see the details of files and directories
press 6 : To see the current user
press 7 : To add user and assign password
press 8 : To create a directory
press 9 : To create an empty file
press 10 : To update the system
""")

os.system("tput setaf 7")

choice=input("Enter your choice : ")

if int(choice) == 1:
	os.system("date")
elif int(choice) == 2:
	os.system("cal")
elif int(choice) == 3:
	os.system("hostname -I")
elif int(choice) == 4:
	os.system("ls")
elif int(choice) == 5:
	os.system("ls -al")
elif int(choice) == 6:
	os.system("whoami")
elif int(choice) == 7:
	useradd = input("Inter username : ")
	os.system("useradd {}".format(useradd))
	os.system("passwd {}".format(useradd))
elif int(choice) == 8:
	directoryname = input("Inter directory name : ")
	os.system("mkdir {}".format(directoryname))
elif int(choice) == 9:
	filename = input("Inter file name : ")
	os.system("touch {}".format(filename))
elif int(choice) == 10:
	os.system("sudo apt update -y")


else:
	print("Option not supported , try for the next option")
