import socket
import os
from colorama import init, Fore, Style

# Inisialisasi colorama
init(autoreset=True)

def clear_screen():
    # Bersihkan layar tergantung sistem operasi
    if os.name == 'nt':  # Untuk Windows
        os.system('cls')
    else:  # Untuk macOS dan Linux
        os.system('clear')

def display_title():
    title = f"""{Fore.RED}{Style.BRIGHT}
______  ___{Fore.WHITE}{Style.BRIGHT}Tools By JavaXploiter{Fore.RED}{Style.BRIGHT}______________
___   |/  /_____ __________________  _/__  __ \.v1
__  /|_/ /_  __ `/_  ___/_  ___/__  / __  /_/ /
_  /  / / / /_/ /_(__  )_(__  )__/ /  _  ____/
/_/  /_/  \__,_/ /____/ /____/ /___/  /_/
{Fore.YELLOW}{Style.BRIGHT}FAST SCAN MASS IP & SAME IP CHECKER TOOL 
{Fore.CYAN}{Style.BRIGHT}[+]==================================[+]
{Fore.WHITE}{Style.BRIGHT}"""
    print(title)

def get_ip_address(url):
    try:
        ip_address = socket.gethostbyname(url)
        return ip_address
    except socket.gaierror:
        return "Unable To Resolve IP"

def check_ips_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            websites = file.readlines()

        results = {}
        for website in websites:
            website = website.strip()  # Menghapus spasi atau newline
            if website:
                ip_address = get_ip_address(website)
                results[website] = ip_address

        return results

    except FileNotFoundError:
        return None

def display_thank_you():
    thank_you_text = f"{Fore.RED}T{Fore.YELLOW}e{Fore.GREEN}r{Fore.CYAN}i{Fore.BLUE}m{Fore.MAGENTA}a {Fore.RED}k{Fore.YELLOW}a{Fore.GREEN}s{Fore.CYAN}i{Fore.BLUE}h!"
    print(f"\n{thank_you_text}\n")

def collect_websites_by_ip(ip, results):
    matching_websites = [website for website, address in results.items() if address == ip]
    if matching_websites:
        print(f"\nWebsites With IP {Fore.CYAN}{ip}{Fore.RESET}:\n")
        for website in matching_websites:
            print(f"{Fore.GREEN}{website}")
    else:
        print(f"{Fore.RED}No Websites Found With The IP Address: {ip}")

# Contoh penggunaan
if __name__ == "__main__":
    clear_screen()
    display_title()
    
    file_path = input("Enter Your List.txt File: ")
    results = check_ips_from_file(file_path)

    if results is None:
        print(f"{Fore.RED}File Not Found Dek. Please Check The File Path.")
    else:
        # Tampilkan hasilnya
        print("\nResults:\n")
        for website, ip in results.items():
            print(f"{Fore.GREEN}{website}: {Fore.CYAN}{ip}")
        
        # Tampilkan pesan terima kasih
        display_thank_you()
        
        # Tanya apakah ingin mengumpulkan website dengan IP yang sama
        user_input = input("\nWould You Like To Gather Websites With The Same IP? (yes/no): ").strip().lower()
        
        if user_input == 'yes':
            ip_to_check = input("Enter The IP Address You Want To Check: ").strip()
            collect_websites_by_ip(ip_to_check, results)
