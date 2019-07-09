from pip._vendor.distlib.compat import raw_input

import sublist3r

from socket import gethostbyname
from socket import gaierror


def print_list(domain_list):
    for item in domain_list:
        print(item)


def main():
    print("This tool scans a given domain and lists an extensive list of subdomains")

    while True:
        domain_name = raw_input("enter base domain for subdomain scan: ")
        try:
            gethostbyname(domain_name)
            break

        except gaierror:
            print("can't verify " + domain_name + " please enter a valid domain")

    brute_input = raw_input("would you like to enable brute force searching? (y/N)")
    enable_brute = True if (brute_input == "y" or brute_input == "yes") else False

    print(f'Searching valid subdomains for "{domain_name}" with brute force {"enabled" if enable_brute else "disabled"} ...')

    # call to open source library that does the subdomain searching
    subdomains = sublist3r.main(
        domain_name,
        40,
        savefile=None,
        ports=None,
        silent=True,
        verbose=True,
        enable_bruteforce=enable_brute,
        engines=None
    )

    found_subdomains = open('found_subdomains.txt', 'w+')

    valid_subdomains = []
    invalid_subdomains = []

    for sub in subdomains:
        try:
            gethostbyname(sub)
            valid_subdomains.append(sub)
            # valid_file.write(sub + "\n")

        except:
            invalid_subdomains.append(sub)
            # invalid_file.write(sub + "\n")

    found_subdomains.write("Valid Subdomains\n\n")
    for valid in valid_subdomains:
        found_subdomains.write(valid + "\n")

    found_subdomains.write("\nInvalid Subdomains\n\n")
    for invalid in invalid_subdomains:
        found_subdomains.write(invalid + "\n")

    print(f'\n\033[96mFound {len(valid_subdomains)} valid subdomains\033[0m')
    print_list(valid_subdomains)

    print(f'\n\033[96mFound {len(invalid_subdomains)} invalid subdomains\033[0m')
    print_list(invalid_subdomains)


main()
