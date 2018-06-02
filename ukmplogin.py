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
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    providers = ['gmail.com', 'yahoo.com',
                 'outlook.com', 'hotmail.com', 'icloud.com']

    # Generate random character username, with maximum length of 10 characters
    username = ''
    for x in range(0, random.randrange(1, 7)):
        username += characters[random.randrange(0, len(characters))]

    provider = providers[random.randrange(0, 4)]
    useragent = useragents[random.randrange(0, len(useragents))]

    email = '{0}@{1}'.format(username, provider)
    parameters = {
        'email': email,
        'cmd': 'authenticate',
        'Login': 'Log In',
        'user-agent': useragent
    }

    # Display information used to terminal
    url = "http://10.23.0.3/cgi-bin/login?cmd=login"
    print(header)
    print("""    _||_||_____________
   |                   |
   | UKM-Pelawat Login |
   |___________________|""")
    print("Useragent: {0}".format(parameters['user-agent']))
    print("Email : {0}\ncmd : {1}\nLogin: {2}\n".format(
        parameters['email'], parameters['cmd'], parameters['Login']))
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
