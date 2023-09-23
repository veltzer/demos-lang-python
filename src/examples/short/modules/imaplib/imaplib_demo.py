"""
This example shows how to use the imaplib module.
In this case I use it to access my gmail account, upload messages, download messages
and more.

To see the documentation of the API use: pydoc imaplib
This thing started from me wanting to import my old mail to gmail and seeing
this blog post: http://scott.yang.id.au/2009/01/migrate-emails-maildir-gmail.html
"""

import imaplib
import os.path

import configparser

config = configparser.ConfigParser()
config.read(os.path.expanduser("~/.passwords.ini"))
opt_username = config.get("imap", "username")
opt_password = config.get("imap", "password")
opt_hostname: str = config.get("imap", "hostname")
opt_port: int = int(config.get("imap", "port"))


def imap_have_mailbox(imap, name):
    (res, l) = imap.list(name)
    if res != "OK":
        raise ValueError("could not list", name)
    if len(l) == 1 and l[0] is None:
        return False
    return True


def imap_create(imap, name):
    (res, _) = imap.create(name)
    if res != "OK":
        raise ValueError("could not create", name)


def imap_delete(imap, name):
    (res, _) = imap.delete(name)
    if res != "OK":
        raise ValueError("could not delete", name)


def imap_logout(imap):
    (res, l) = imap.logout()
    if res != "BYE":
        raise ValueError("could not logout", res, l)


def imap_login(imap, username, password):
    (res, _) = imap.login(username, password)
    if res != "OK":
        raise ValueError("could not login")


def main():
    """
    imap = imaplib.IMAP4(
        host=opt_hostname,
        port=opt_port,
    )
    """
    imap = imaplib.IMAP4_SSL(host=opt_hostname, port=opt_port)
    imap_login(imap, opt_username, opt_password)
    print(imap.capability())
    print(imap.list())
    if imap_have_mailbox(imap, "foo"):
        raise ValueError("have mailbox foo")
    if not imap_have_mailbox(imap, "business"):
        raise ValueError("do not have mailbox business")
    imap_create(imap, "foo")
    imap_delete(imap, "foo")
    imap_logout(imap)


main()
