import subprocess
import pyfiglet

def print_banner():
    ascii_banner_auto_smb = pyfiglet.figlet_format("AUTO SMB")
    print(ascii_banner_auto_smb)
    print("Developed by cod0xb0")

def main():
    print_banner()

    country_code = input("Enter the country code (2 letters format): ")

    shodan_command = f'shodan search "Authentication: disabled" --fields ip_str,port country:"{country_code}"'
    result = subprocess.run(shodan_command, shell=True, capture_output=True, text=True)

    num_hosts = result.stdout.count('\n') if result.stdout else 0
    print(f"Number of hosts found: {num_hosts}")

    print("\nShodan Search Results:")
    print(result.stdout)

    with open("SMB-Hosts.log", "w") as log_file:
        log_file.write(result.stdout)

    user_choice = input("Do you want to enumerate shares (Y/N)? ")

    if user_choice.lower() == "y":
        ascii_art_happy_hunting = pyfiglet.figlet_format("HAPPY HUNTING")
        print(ascii_art_happy_hunting)

        with open("SMB-Hosts.log", "r") as hosts_file:
            for line in hosts_file:
                ip, port = line.strip().split()
                enum_command = f"smbclient -L {ip} -p {port} -U '' --password=''"
                enum_result = subprocess.run(enum_command, shell=True, capture_output=True, text=True)
                
                # Print the enumeration result on the terminal
                print(f"Result for IP: {ip}, Port: {port}")
                print(enum_result.stdout)

                # Save the enumeration result to log file (Enum_Shared.log)
                with open("Enum_Shared.log", "a") as enum_log_file:
                    enum_log_file.write(f"Result for IP: {ip}, Port: {port}\n")
                    enum_log_file.write(enum_result.stdout)
                    enum_log_file.write("\n" + "="*30 + "\n")

        print("Enumeration completed. Check Enum_Shared.log for results.")

    else:
        ascii_art_bye_bye = pyfiglet.figlet_format("BYE BYE")
        print(ascii_art_bye_bye)

    print("\nLogs saved at:")
    print("SMB-Hosts.log")
    print("Enum_Shared.log")

if __name__ == "__main__":
    main()
