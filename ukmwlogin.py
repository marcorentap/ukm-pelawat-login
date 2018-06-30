import requests
import random


def main():
    header = """
                              ,      \    /      ,
                             / \     )\__/(     / \\
                            /   \   (_\  /_)   /   \\
    _______________________/_____\___\@  @/___/_____\\____________________
   |                                 |\../|                              |
   |                                  \VV/                               |
   |   _______ _______  ______ _______  _____  _  _  _ _______ __   _    |
   |   |  |  | |_____| |_____/ |       |     | |  |  | |______ | \  |    |
   |   |  |  | |     | |    \_ |_____  |_____| |__|__| |______ |  \_|    |
   |_____________________________________________________________________|
     || ||               |    /\ /     \\\\     \ /\    |
     || ||               |  /   V       ))     V   \  |
     || ||               |/     `      //      '     \|
     || ||               `             V              '"""

    # Create random email to be used in the packet
    f = open("useragents.txt", "r")
    useragents = [line.rstrip("\n") for line in f]
    f.close()

    # Use random useragent
    useragent = useragents[random.randrange(0, len(useragents))]

    parameters = {
        'user': 'p68128',
		'password' : '71003068',
        'cmd': 'authenticate',
        'Login': 'Log In',
        'user-agent': useragent
    }

    # Display information used to terminal
    url = "http://10.23.0.3/cgi-bin/login?cmd=login"
    print(header)
    print("""    _||_||_____________
   |                   |
   | UKM-Warga Login |
   |___________________|""")
    print("Useragent: {0}".format(parameters['user-agent']))
    print("User : {0}\nPassword: {1}\ncmd : {2}\nLogin: {3}\n".format(
        parameters['user'], parameters['password'], parameters['cmd'], parameters['Login']))
    print("Connecting to {0}".format(url))

    # Don't allow redirects because we will get too many redirects when URL doesn't accept bots(?)
    r = requests.post(url, data=parameters, allow_redirects=False)

    status = r.status_code
    print("Reply from {0}\n{1}".format(url, r.headers))
    print("Status\t\t: {0}".format(status))
    if status == 200:
        print("Successfully logged in\n")
    elif status == 302:
        print("Already logged in\n")
    else:
        print("Error\n")

    # Some validation so Windows update the WiFi icon
    validateURL = "http://httpbin.org/get"
    print("Validating. Test connection to {0}".format(validateURL))
    validator = requests.get(validateURL)
    validateStatus = str(validator.status_code)
    print("Status\t\t: {0}".format(validateStatus))
    if validateStatus.startswith("2"):
        print("Success")
    elif validateStatus.startswith("3"):
        print("Redirected")
    elif validateStatus.startswith("4"):
        print("Client Error")
    elif validateStatus.startswith("5"):
        print("Server Error")
    else:
        print("Error")
        print("Error")

    print("\nPress Enter to close this window")
    input()


if __name__ == "__main__":
    main()
