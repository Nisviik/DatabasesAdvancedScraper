# DatabasesAdvancedScraper
A scraper for my databases advanced course

Created an Ubuntu virtual machine.

Updated the machine and installed python 3.

- sudo apt update
- sudo apt-get update
- sudo apt install python3

(There were some errors during my installations followed this guide: https://unix.stackexchange.com/questions/374748/ubuntu-update-error-waiting-for-unattended-upgr-to-exit)
// These were the commands I executed 
- sudo dpkg-reconfigure -plow unattended-upgrades
- sudo dpkg --configure -a
- sudo apt update && sudo apt -f install && sudo apt full-upgrade
- sudo dpkg-reconfigure -plow unattended-upgrades
 
Finishing installing python3 and beautifulsoup4

- sudo apt install python3 (worked)
- sudo apt install python3-pip
- sudo pip install beautifulsoup4 

The Scraper is only printing the transaction with the highest value of each minute for now, in the upcoming weeks that will change 
