# Program for TUI.
import os
import getpass
# To change the font colour to red.
os.system("tput setaf 1")
# To print the statement with 3 tab.
print("\t\t\tWelcome to TUI")
# To change the font colour to white.
os.system("tput setaf 7")
print("\t\t\t==============")

password = getpass.getpass("Enter your password : ")
passwd = "redhat"
if password != passwd:
    print("authentication failed")
    exit()

location = input("Where would you like to perform your job (local/remote): ")
if location == "remote":
    hostname = input("Enter IP-Adderss : ")

os.system("tput setaf 1")
while True :

    print("""
    press 1 : TO see the date
    press 2 : To see the calander
    press 3 : To see the IPAdderss
    press 4 : To see the list of files and directories
    press 5 : To see the details of files and directories
    press 6 : To see the current user
    press 7 : To add user and assign password
    press 8 : To create a directory
    press 9 : To create an empty file
    press 10 : To update the system
    press 11 : To see the version of operating system and kernal
    press 12 : To see the process running inside docker
    press 13 : To see the images in local repository
    press 14 : To see all the process either running or stopped in docker
    press 15 : To exit
    """)

    os.system("tput setaf 7")

    choice=input("Enter your choice : ")

    if location == "local":

        if int(choice) == 1:
            os.system("cal")	
        elif int(choice) == 2:
    	    os.system("cal")
        elif int(choice) == 3:
            print("IP Adderss of the system is : ")
            os.system("hostname -I")
        elif int(choice) == 4:
            os.system("ls")
        elif int(choice) == 5:
            os.system("ls -al")
        elif int(choice) == 6:
            os.system("whoami")
        elif int(choice) == 7:
            useradd = input("Inter username : ")
            os.system("sudo useradd {}".format(useradd))
            os.system("sudo passwd {}".format(useradd))
        elif int(choice) == 8:
            directoryname = input("Inter directory name : ")
            os.system("mkdir {}".format(directoryname))
        elif int(choice) == 9:
            filename = input("Inter file name : ")
            os.system("touch {}".format(filename))
        elif int(choice) == 10:
            os.system("sudo apt update -y")
        elif int(choice) == 11:
            os.system("hostnamectl")
        elif int(choice) == 12:
            os.system("docker ps")
        elif int(choice) == 13:
            os.system("docker images")
        elif int(choice) == 14:
            os.system("docker ps -a")
        else:
             print("Option not supported , try for the next option")


    elif location == "remote":

        if int(choice) == 1:
            os.system("cal")
        elif int(choice) == 2:
            os.system("cal")
        elif int(choice) == 3:
            print("IP Adderss of the system is : ")
            os.system("hostname -I")
        elif int(choice) == 4:
            os.system("ls")
        elif int(choice) == 5:
            os.system("ls -al")
        elif int(choice) == 6:
            os.system("whoami")
        elif int(choice) == 7:
            useradd = input("Inter username : ")
            os.system("sudo useradd {}".format(useradd))
            os.system("sudo passwd {}".format(useradd))
        elif int(choice) == 8:
            directoryname = input("Inter directory name : ")
            os.system("mkdir {}".format(directoryname))
        elif int(choice) == 9:
            filename = input("Inter file name : ")
            os.system("touch {}".format(filename))
        elif int(choice) == 10:
            os.system("sudo apt update -y")
        elif int(choice) == 11:
            os.system("hostnamectl")
        elif int(choice) == 12:
            os.system("docker ps")
        elif int(choice) == 13:
            os.system("docker images")
        elif int(choice) == 14:
            os.system("docker ps -a")
        else:
            print("Option not supported , try for the next option")
