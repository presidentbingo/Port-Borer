#!/usr/bin/env python

"""App description goes here."""

import logging
import traceback

from os.path import abspath, dirname

from appJar import gui

import i18n
from i18n import t

import re
import configparser
import urllib.request

# import sshtunnel

logging.basicConfig(format='[%(name)-6s] [%(levelname)-8s] %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger('main')

APP = gui()
config = configparser.ConfigParser()

I18N_PATH = dirname(abspath(__file__)) + '/locale'
i18n.load_path.append(I18N_PATH)

DEFAULTS = {
    "relay": "67328286-288b-4d7d-b637-3fe2ae63abf2.pub.cloud.scaleway.com:22",
    "password": "borer",
    "username": "port",
    "localconnection": "localhost:25565 / 25565",
}


def reloadrelays():
    config.read('options.ini')
    logger.debug('Downloading Relay List...')
    return(urllib.request.urlopen('https://raw.githubusercontent.com/FlaggedBrad/Port-Borer/master/servers.txt').read().decode('utf-8').splitlines())
    

    if 'GENERAL' not in config:
        config['GENERAL'] = {}

    if 'CUSTOMSERVERLIST' not in config:
        config['CUSTOMSERVERLIST'] = {}

    if 'NEWSERVERSACTIVE' not in config:
        config['GENERAL']['NEWSERVERSACTIVE'] = 'True'

    
    saveconfig()


def saveconfig():
    with open('options.ini', 'w') as configfile:
        config.write(configfile)

def launch():
    webrelaylist = reloadrelays()
    print(webrelaylist)
    """Build the GUI and start the app."""

    logger.debug('Setting up...')
    APP.setTitle(t('label.title'))
    APP.setIcon("icon.ico")



    APP.startLabelFrame(t('label.remoteconn'), 10, 1)
    # this sticky option only applies to the label frame.
    APP.setSticky("w")

    relaylist = '{'
    for webrelay in webrelaylist:
        relaylist = relaylist+'"'+webrelay+'":False, '
    relaylist = relaylist[:-2]+'}'
    print(relaylist)


    APP.addProperties(t('label.relays'), )

    APP.stopLabelFrame()




    APP.startLabelFrame(t('label.localconn'), 10, 2)
    # this sticky option only applies to the label frame.
    APP.setSticky("e")

    APP.addEntry(t('label.localconnection'), 1, 1, 1)
    APP.addButton(t('label.bindlocal'), press, 1, 2, 1)
    APP.setEntryDefault(t('label.localconnection'), DEFAULTS["localconnection"])

    APP.stopLabelFrame()




    APP.go()

    


def press(button):
    """Handle button presses."""
    if button == t('label.bindlocal'):
        APP.stop()


def loginpress(_):
    """Save login credentials for clicked relay."""
    APP.hide()

    relay = APP.getEntry(t('label.relay'))
    username = APP.getEntry(t('label.username'))
    password = APP.getEntry(t('label.password'))
    remember = APP.getCheckBox(t('label.rememberme'))
    logger.debug(f"Relay: {relay} ({type(relay)})")
    # logger.debug(f"User: {username} ({type(username)})")
    # logger.debug(f"Pass: {password} ({type(password)})")
    logger.debug(f"Remember: {remember} ({type(remember)})")

    APP.removeAllWidgets()
    APP.disableEnter()
    APP.setResizable(canResize=True)

    regexsearch = re.search('^(.*):(\d*)$', relay)
    




    APP.show()



def loginscreen():
    logger.debug('Opening the Login screen')
    APP.addLabelEntry(t('label.username'), 1, 1, 2)
    APP.addLabelSecretEntry(t('label.password'), 2, 1, 2)
    APP.addCheckBox(t('label.rememberme'), 3, 1)
    APP.setCheckBox(t('label.rememberme', ticked=True))
    APP.addButtons([t('label.login')], loginpress, 3, 2, 2)
    APP.enableEnter(loginpress)
    APP.setResizable(canResize=False)

    APP.setEntryDefault(t('label.relay'), DEFAULTS["relay"])


if __name__ == '__main__':
    try:
        launch()
    except Exception as exc:
        logger.exception("A problem has occurred:")
