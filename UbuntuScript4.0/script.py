# Modules that are going to be used
import os
import time


# Colors for text
class bcolors:
    RED = '\033[91m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    NORMAL = '\033[0m'
    BOLD = '\033[1m'
    FLASH = '\033[5m'


# Banner
print(bcolors.FLASH + bcolors.RED + bcolors.BLUE + """

/***
 *              _____                    _____                   _______                   _____                    _____                    _____          
 *             /\    \                  /\    \                 /::\    \                 /\    \                  /\    \                  /\    \         
 *            /::\    \                /::\    \               /::::\    \               /::\____\                /::\____\                /::\    \        
 *           /::::\    \              /::::\    \             /::::::\    \             /:::/    /               /::::|   |               /::::\    \       
 *          /::::::\    \            /::::::\    \           /::::::::\    \           /:::/    /               /:::::|   |              /::::::\    \      
 *         /:::/\:::\    \          /:::/\:::\    \         /:::/~~\:::\    \         /:::/    /               /::::::|   |             /:::/\:::\    \     
 *        /:::/  \:::\    \        /:::/__\:::\    \       /:::/    \:::\    \       /:::/    /               /:::/|::|   |            /:::/  \:::\    \    
 *       /:::/    \:::\    \      /::::\   \:::\    \     /:::/    / \:::\    \     /:::/    /               /:::/ |::|   |           /:::/    \:::\    \   
 *      /:::/    / \:::\    \    /::::::\   \:::\    \   /:::/____/   \:::\____\   /:::/    /      _____    /:::/  |::|   | _____    /:::/    / \:::\    \  
 *     /:::/    /   \:::\ ___\  /:::/\:::\   \:::\____\ |:::|    |     |:::|    | /:::/____/      /\    \  /:::/   |::|   |/\    \  /:::/    /   \:::\ ___\ 
 *    /:::/____/  ___\:::|    |/:::/  \:::\   \:::|    ||:::|____|     |:::|    ||:::|    /      /::\____\/:: /    |::|   /::\____\/:::/____/     \:::|    |
 *    \:::\    \ /\  /:::|____|\::/   |::::\  /:::|____| \:::\    \   /:::/    / |:::|____\     /:::/    /\::/    /|::|  /:::/    /\:::\    \     /:::|____|
 *     \:::\    /::\ \::/    /  \/____|:::::\/:::/    /   \:::\    \ /:::/    /   \:::\    \   /:::/    /  \/____/ |::| /:::/    /  \:::\    \   /:::/    / 
 *      \:::\   \:::\ \/____/         |:::::::::/    /     \:::\    /:::/    /     \:::\    \ /:::/    /           |::|/:::/    /    \:::\    \ /:::/    /  
 *       \:::\   \:::\____\           |::|\::::/    /       \:::\__/:::/    /       \:::\    /:::/    /            |::::::/    /      \:::\    /:::/    /   
 *        \:::\  /:::/    /           |::| \::/____/         \::::::::/    /         \:::\__/:::/    /             |:::::/    /        \:::\  /:::/    /    
 *         \:::\/:::/    /            |::|  ~|                \::::::/    /           \::::::::/    /              |::::/    /          \:::\/:::/    /     
 *          \::::::/    /             |::|   |                 \::::/    /             \::::::/    /               /:::/    /            \::::::/    /      
 *           \::::/    /              \::|   |                  \::/____/               \::::/    /               /:::/    /              \::::/    /       
 *            \::/____/                \:|   |                   ~~                      \::/____/                \::/    /                \::/____/        
 *                                      \|___|                                            ~~                       \/____/                  ~~              
 *                                                                                                                                                          
 *              _____                    _____                    _____                   _______                                                           
 *             /\    \                  /\    \                  /\    \                 /::\    \                                                          
 *            /::\    \                /::\    \                /::\    \               /::::\    \                                                         
 *            \:::\    \              /::::\    \              /::::\    \             /::::::\    \                                                        
 *             \:::\    \            /::::::\    \            /::::::\    \           /::::::::\    \                                                       
 *              \:::\    \          /:::/\:::\    \          /:::/\:::\    \         /:::/~~\:::\    \                                                      
 *               \:::\    \        /:::/__\:::\    \        /:::/__\:::\    \       /:::/    \:::\    \                                                     
 *                \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \     /:::/    / \:::\    \                                                    
 *                 \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \   /:::/____/   \:::\____\                                                   
 *                  \:::\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\ |:::|    |     |:::|    |                                                  
 *    _______________\:::\____\/:::/__\:::\   \:::\____\/:::/  \:::\   \:::|    ||:::|____|     |:::|    |                                                  
 *    \::::::::::::::::::/    /\:::\   \:::\   \::/    /\::/   |::::\  /:::|____| \:::\    \   /:::/    /                                                   
 *     \::::::::::::::::/____/  \:::\   \:::\   \/____/  \/____|:::::\/:::/    /   \:::\    \ /:::/    /                                                    
 *      \:::\~~~~\~~~~~~         \:::\   \:::\    \            |:::::::::/    /     \:::\    /:::/    /                                                     
 *       \:::\    \               \:::\   \:::\____\           |::|\::::/    /       \:::\__/:::/    /                                                      
 *        \:::\    \               \:::\   \::/    /           |::| \::/____/         \::::::::/    /                                                       
 *         \:::\    \               \:::\   \/____/            |::|  ~|                \::::::/    /                                                        
 *          \:::\    \               \:::\    \                |::|   |                 \::::/    /                                                         
 *           \:::\____\               \:::\____\               \::|   |                  \::/____/                                                          
 *            \::/    /                \::/    /                \:|   |                   ~~                                                                
 *             \/____/                  \/____/                  \|___|                                                                                     
 *                                                                                                                                                          
 */
""" + bcolors.NORMAL)

time.sleep(7)

os.system("clear")

# Firefox settings, warning, apt fix, GUI updates, 
print(bcolors.RED + bcolors.FLASH + "Ensure you ran this as root. I.E (sudo python3 script.py) " + bcolors.NORMAL)
print(bcolors.GREEN + "Ensure you did things like: fix apt and got the GUI software update settings " + bcolors.NORMAL)
print('')
print(bcolors.GREEN + "Ensure you go to firefox > privacy and security settings > enable delete cookies > disable ask to save logins" + bcolors.NORMAL)
print(bcolors.GREEN + "enable block pop ups > Block deceptive content" + bcolors.NORMAL)
print("")
print(bcolors.RED + bcolors.FLASH + "Screenshot all logins! this will do PAM and LightDM!!!" + bcolors.NORMAL)
time.sleep(15)

# Fixing package manager, any broken dependencies will be fixed
os.system("sudo dpkg --configure -a")
os.system("sudo apt clean")

# Updates and installing nessesary tools

os.system("sudo apt install net-tools -y")
os.system("sudo apt update -y && sudo apt upgrade -y")
os.system("sudo apt install clamav -y")
os.system("sudo apt install synaptic -y")
os.system("sudo apt install ufw -y")
os.system("sudo apt install gufw -y")
os.system("sudo apt install rkhunter -y")
os.system("sudo apt install gedit -y")
os.system("sudo apt install terminator -y")
# Bum may not work, hit or miss
os.system("sudo apt install bum")

os.system("clear")
os.system("sudo apt install libpam-cracklib -y")

cracklib = input(bcolors.YELLOW + "*Was cracklib installed correctly? If no tyne 'n' and go fix it! y/n * " + bcolors.NORMAL)

# Check if cracklib was installed correctly

if cracklib == str("n"):
	print("Ok, fix it and come back!")
	quit()
elif cracklib == str("y"):
	print("Proceeding...")

# Tool Removal
print("Going through services and hacking tools commonly used (refer to the readme to see what you do and dont need)... ")
time.sleep(2)

# Apache2 removal
os.system("clear")
apache2 = input("Is apache2 a critical service or do you need it? y/n ")
if apache2 == str("y"):
	print("Leaving apache2 installed!")
elif apache2 == str("n"):
	print("Removing apache2 and all dependencies completley... ")
	os.system("sudo apt purge apache2 -y")

# Wireshark removal
os.system("clear")
wireshark = input("Is wireshark a critical service or do you need it? y/n ")
if wireshark == str("y"):
        print("Leaving wireshark installed!")
elif wireshark == str("n"):
        print("Removing wireshark and all dependencies completley... ")
        os.system("sudo apt purge wireshark -y")

# Ophcrack removal
os.system("clear")
ophcrack = input("Is ophcrack a critical service or do you need it? y/n ")
if ophcrack == str("y"):
        print("Leaving ophcrack installed!")
elif ophcrack == str("n"):
        print("Removing ophcrack and all dependencies completley... ")
        os.system("sudo apt purge ophcrack -y")

# Nmap removal
os.system("clear")
nmap = input("Is nmap a critical service or do you need it? y/n ")
if nmap == str("y"):
        print("Leaving nmap installed!")
elif nmap == str("n"):
        print("Removing nmap and all dependencies completley... ")
        os.system("sudo apt purge nmap -y")

# Zenmap removal
os.system("clear")
zenmap = input("Is zenmap a critical service or do you need it? y/n ")
if zenmap == str("y"):
        print("Leaving zenmap installed!")
elif zenmap == str("n"):
        print("Removing zenmap and all dependencies completley... ")
        os.system("sudo apt purge zenmap -y")

# Kismet removal
os.system("clear")
kismet = input("Is kismet a critical service or do you need it? y/n ")
if kismet == str("y"):
        print("Leaving kismet installed!")
elif kismet == str("n"):
        print("Removing kismet and all dependencies completley... ")
        os.system("sudo apt purge kismet -y")

# Hashcat removal
os.system("clear")
hashcat = input("Is hashcat a critical service or do you need it? y/n ")
if hashcat == str("y"):
        print("Leaving hashcat installed!")
elif hashcat == str("n"):
        print("Removing hashcat and all dependencies completley... ")
        os.system("sudo apt purge hashcat -y")

# Nikto removal
os.system("clear")
nikto = input("Is nikto a critical service or do you need it? y/n ")
if nikto == str("y"):
        print("Leaving nikto installed!")
elif nikto == str("n"):
        print("Removing nikto and all dependencies completley... ")
        os.system("sudo apt purge nikto -y")

# Hydra removal
os.system("clear")
hydra = input("Is hydra a critical service or do you need it? y/n ")
if hydra == str("y"):
        print("Leaving hydra installed!")
elif hydra == str("n"):
        print("Removing hydra and all dependencies completley... ")
        os.system("sudo apt purge hydra -y")

# Netcat removal
os.system("clear")
netcat = input("Is netcat a critical service or do you need it? y/n ")
if netcat == str("y"):
        print("Leaving netcat installed!")
elif netcat == str("n"):
        print("Removing netcat and all dependencies completley... ")
        os.system("sudo apt purge netcat -y")


# Going through packages manually
print(bcolors.GREEN + """Synaptic is going to open, click the button that says 'status' then click installed and check all those packages
You're looking for hacking tools and other random stuff, when you find stuff mark it and when done apply it
When you're done, make sure to exit synaptic for the script to continue. DOCUMENT WHAT YOU DELETE SOMEWHERE""" + bcolors.NORMAL)
time.sleep(7)
os.system("sudo synaptic")
time.sleep(3)

os.system("clear")

# Firewall settings
os.system("sudo ufw enable")
print(bcolors.YELLOW + "Set it to office environment and make sure to set incoming to reject it not deny" + bcolors.NORMAL)
time.sleep(3)
os.system("sudo gufw")
os.system("clear")

# Runs a clamscan
os.system("clear")
print("Running AV scan")
time.sleep(1)
os.system("sudo clamscan")
time.sleep(4)
os.system("clear")

# rkhunter thing
print("This is going to go through and check for rootkits/bootkits")
time.sleep(2)
rkhunter = input("Rkhunter scan if this is the first time you run this script type y if it isnt type n")

if rkhunter == str("y"):
	os.system("sudo rkhunter --check")
elif rkhunter == str("n"):
	print("Skipping rkhunter scan")
	time.sleep(1)
	os.system("clear")

# PAM Auth Setup

# Doing PAM Password settings
pamq = input(bcolors.GREEN + "Do you need to do pam? y/n" + bcolors.NORMAL)
if pamq	== str("y"):
	print(bcolors.RED + "This is going to do PAM Password Complexity" + bcolors.NORMAL)
	os.system("sudo cat common-password > /etc/pam.d/common-password")
	print("Finished doing PAM Auth... doing pam password complexity...")
	os.system("clear")
	time.sleep(3)
	print(bcolors.YELLOW + "Doing PAM remember AUTH PASSWORD settings" + bcolors.NORMAL)
	os.system("sudo echo 'auth required pam_tally2.so deny=5 onerr=fail unlock_time=1800' >> /etc/pam.d/common-auth")
	os.system("clear")
	print(bcolors.YELLOW + "Done with PAM" + bcolors.NORMAL)
elif pamq == str("n"):
	print("Skipping PAM settings...")

# Doing file permissions on files
print(bcolors.GREEN + "Doing file permissions for: /etc/passwd /etc/shadow" + bcolors.NORMAL)
os.system("sudo chmod 600 /etc/shadow")
os.system("sudo chmod 644 /etc/passwd")
os.system("clear")

# Check for crontabs
print(bcolors.GREEN + "Go check all these located in /var/spool, comment or delete anything that isnt supposed to be startup!" + bcolors.NORMAL)
os.system("sudo ls /var/spool")
time.sleep(7)
os.system("clear")

# Sodoers check

print(bcolors.GREEN + "Check these files in the following directory using another terminal: /etc/sudoers.d" + bcolors.NORMAL)
time.sleep(4)
os.system("sudo ls /etc/sudoers.d")
time.sleep(4)
os.system("clear")

# Visudo
print(bcolors.YELLOW + "Make sure only root is the only one unless specified" + bcolors.NORMAL)
time.sleep(5)
os.system("sudo visudo")
os.system("clear")

# Disable ipv6
os.system("clear")
print(bcolors.GREEN + "Disabling IPv6... " + bcolors.NORMAL)
os.system("sudo sysctl -w net.ipv6.conf.all.disable_ipv6=1")
os.system("sudo sysctl -w net.ipv6.conf.default.disable_ipv6=1")
os.system("sudo sysctl -w net.ipv6.conf.lo.disable_ipv6=1")
print("")
os.system("ip a")
print("")
print("Ensure there is no ipv6")
print("")
time.sleep(5)
os.system("ifconfig")
print("")
print("Same thing here")
time.sleep(5)
os.system("clear")

# Check for DNS spoofing
print(bcolors.YELLOW + "Checking for DNS re-routes/spoofing..." + bcolors.NORMAL)
print(bcolors.RED + "Make sure nothing is routing to anything stupid in /etc/hosts" + bcolors.NORMAL)
time.sleep(3)
os.system("sudo gedit /etc/hosts")
time.sleep(2)
os.system("clear")

# LightDM

os.system("clear")
lightdm = input(bcolors.YELLOW + "Do you need lightDM done? y/n" + bcolors.NORMAL)
if lightdm == str("y"):
	print("OK")
	os.system("sudo echo 'allow-guest=false' >> /usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf")
elif lightdm == str("n"):
	print("Skipping LightDM!")

# Account removal

os.system("clear")
print(bcolors.YELLOW + "Pull up the readme, this is going to do account removals and additions. Make sure forensics are done and ensure you've checked all accounts for misc stuff." + bcolors.NORMAL)
time.sleep(8)

print("")

account_misc = input("Do you need to remove an account? y/n ")
while account_misc == str("y"):
	account_name = input(bcolors.GREEN + "What is the account name (case sensitive)? If there are no more accounts type: There are no accounts" + bcolors.NORMAL)
	print("Removing: " + account_name)
	os.system("sudo deluser " + account_name)
	if account_name == str("There are no accounts"):
		break

# Account age policies

os.system("clear")
print(""" 
Change these settings:

PASS_MIN_DAYS 7
PASS_MAX_DAYS 90
PASS_WARN_AGE 14

""")

time.sleep(5)
os.system("sudo nano /etc/login.defs")

# IPv4 security settings
print(bcolors.GREEN + "changing ipv4 settings in /etc/sysctl.conf" + bcolors.NORMAL)
os.system("sudo cat sysctl.conf > /etc/sysctl.conf")

# Checking for other shells

os.system("clear")
print("Searching for other shells that may be on the system... ")
os.system("sudo ps -p $$")
time.sleep(6)

# Check ports

os.system("clear")
print(bcolors.RED + "Check for all and any uneeded ports that are open." + bcolors.NORMAL)
os.system("sudo netstat -tulpn")
time.sleep(7)




# END SEQUENCE print("Finished! A list of what this tool has completed will be sent to a folder")

