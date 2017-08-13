#!/usr/bin/env python

"""App description goes here."""

from os.path import abspath, dirname

from appJar import gui

import i18n
from i18n import t

import sshtunnel

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
    print("Server:", server, "Pass:", password, "Remember:", remember)

    APP.removeAllWidgets()
    APP.disableEnter()
    APP.setResizable(canResize=True)
    APP.show()


def main():
    """Build the GUI and start the app."""
    APP.setTitle(t('label.title'))
    APP.addLabelEntry(t('label.server'), 1, 1, 2)
    APP.setEntryDefault(t('label.server'), DEFAULTS["server"])
    APP.addLabelSecretEntry(t('label.password'), 2, 1, 2)
    APP.addCheckBox(t('label.rememberme'), 3, 1)
    APP.addButtons([t('label.login')], loginpress, 3, 2)
    APP.enableEnter(loginpress)
    APP.setResizable(canResize=False)

    APP.go()


if __name__ == '__main__':
    main()
