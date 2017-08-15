#!/usr/bin/env python

"""App description goes here."""

import logging
import traceback

from os.path import abspath, dirname

from appJar import gui

import i18n
from i18n import t

# import sshtunnel

logging.basicConfig(format='[%(name)-6s] [%(levelname)-8s] %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger('main')

APP = gui()

I18N_PATH = dirname(abspath(__file__)) + '/locale'
i18n.load_path.append(I18N_PATH)

DEFAULTS = {
    "server": "67328286-288b-4d7d-b637-3fe2ae63abf2.pub.cloud.scaleway.com",
    "password": "pass",
}


def press(button):
    """Handle button presses."""
    if button == t('label.customport'):
        APP.stop()
    if button == t('label.localport'):
        APP.stop()
    if button == t('label.serveravailport'):
        APP.stop()


def loginpress(_):
    """Save login credentials."""
    APP.hide()

    server = APP.getEntry(t('label.server'))
    password = APP.getEntry(t('label.password'))
    remember = APP.getCheckBox(t('label.rememberme'))
    logger.debug(f"Server: {server} ({type(server)})")
    # logger.debug(f"Pass: {password} ({type(password)})")
    logger.debug(f"Remember: {remember} ({type(remember)})")

    APP.removeAllWidgets()
    APP.disableEnter()
    APP.setResizable(canResize=True)
    APP.show()


def main():
    """Build the GUI and start the app."""
    logger.debug('Setting up...')
    APP.setTitle(t('label.title'))
    APP.addLabelEntry(t('label.server'), 1, 1, 2)
    APP.setEntryDefault(t('label.server'), DEFAULTS["server"])
    APP.addLabelSecretEntry(t('label.password'), 2, 1, 2)
    APP.addCheckBox(t('label.rememberme'), 3, 1)
    APP.addButtons([t('label.login')], loginpress, 3, 2)
    APP.enableEnter(loginpress)
    APP.setResizable(canResize=False)

    logger.debug('Starting GUI')
    APP.go()


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        logger.exception("A problem has occurred:")
