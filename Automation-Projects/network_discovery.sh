#!/bin/bash

# Host Discovery

echo -e "\n[*] Hosts Found in $1\n"
hosts=$(nmap -sn $1 | grep -v "host down"  | grep -o "[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}" | sort | uniq)
for i in $hosts; do echo -e "    $i" ; done
echo -e "\n[+] Machine to pwn: \n"
pwnable=$(echo $hosts | tr " " "\n" |  tail -1 )
echo -e "    $pwnable"
echo -e "\n[*] Starting nmap and storing result in $2.nmap\n"
mkdir -p Vulnhub/$2
#nmap $pwnable
portscan=$(nmap -sC -sV -p-  -oN /home/alkis/Vulnhub/$2/$2 $pwnable | grep -o  "[0-9]\{1,5\}/tcp" )

echo -e "[+] Done! \n"

echo -e "[*] Available tcp ports: \n"
for port in $portscan ; do echo "    $port" ; done

if [ $(echo $portscan | grep -o "80/tcp" | wc -c) -gt 0 ]
then
	echo -e "\n[*] Port 80 is open so I will start gobuster and store result to go.txt. Check again in 5 minutes!"
	gobuster dir -q -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://$pwnable/ -t 30 -x php,asp,txt,dat,sh,js,exe -o /home/alkis/Vulnhub/$2/go.txt 
	echo -e "\n[+] Medium done.\n"
	gobuster dir -q -w /usr/share/wordlists/dirb/big.txt -u http://$pwnable/ -t 30 -x php,asp,txt,dat,sh,js,exe  
	echo -e "[+] Big done. \n"
	gobuster dir -q -w /usr/share/wordlists/dirb/common.txt -u http://$pwnable/ -t 30 -x php,asp,txt,dat,sh,js,exe 
	echo -e "[+] common done.\n"
	echo -e "\n[+] Done!\n"
fi




