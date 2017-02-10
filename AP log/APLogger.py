import shelve
import datetime
import requests
import json
import atexit


# Ensures logout of API
def logout(session,logout_url):
    session.get(logout_url, verify=False)


# Returns number of items in the "devices" dict that's filtered for aps
def get_ap_number(user,pwd):
    login_url = '' #sanitized for your protection
    logout_url = '' #sanitized for your protection
    devices_url = '' #seriously, wear protection, kids

    login = {
        '': user, #payload information, login request requirements may differ
        '': pwd
    }

    with requests.Session() as session:
        ap_number = None

        # let me log in and ignore ssl fails, then makes sure session logs out at exit
        session.post(login_url, data=login, verify=False)
        atexit.register(logout, session, logout_url)

        try:
            # get a dict of all devices that fit the "AP" category, then counts devices
            aps = session.get(devices_url, verify=False)
            aps = aps.json()
            ap_number = aps['queryResponse']['@count'] # specific to Cisco Prime, may differ
        except:
            print('Could not get AP count')
            pass

    return ap_number


# Updates the shelf-based log (python-accessible dictionary)
def update_list(ap_number):
    with shelve.open('AP History') as log:
        log[str(datetime.date.today())] = int(ap_number)


# Main method: gets the number of ap's, then stores it
def main(user, pwd):
    ap_number = get_ap_number(user,pwd)

    update_list(ap_number)


# Inits main. Change these credentials to something that can actually see VH devices
user = '' #username sanitized
pwd = '' #password sanitized
main(user,pwd)