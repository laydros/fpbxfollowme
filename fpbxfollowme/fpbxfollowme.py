#!/usr/bin/env python
"""fpbxfollowme: module to update follow me field to add or remove my
extension from support queue. requires python-xdg
"""
import mechanize
import sys
import os
import ConfigParser

from xdg.BaseDirectory import xdg_config_home

CONTROL_N = "grplist"
FORM_N = "editGRP"
BOTH_EXT = "368\n369"
D_EXT_ONLY = "368"


def update_grplist(br, ext):
    control = get_grplist(br)
    br[control.name] = ext
    br.submit()
    return br.response()


def get_grplist(br):
    br.select_form(FORM_N)
    control = br.form.find_control(CONTROL_N)
    print("grplist set to: \n" + br[control.name])
    return control


def get_arg():
    arglist = sys.argv
    helptext = ("Utility to add or remove extension from FreePBX.\n"
                "use " + arglist[0] + " a to add\n"
                "use " + arglist[0] + " r to remove\n")

    if len(sys.argv) < 2:
        print(helptext)
        sys.exit()

    if arglist[1] == 'a':
        ext_text = BOTH_EXT
    elif arglist[1] == 'r':
        ext_text = D_EXT_ONLY
    else:
        print(helptext)
        exit()

    return ext_text


def main():
    '''going to do something here'''

    config = ConfigParser.ConfigParser()
    config_f = os.path.join(xdg_config_home, "fpbxfollowme.conf")
    config.read(config_f)
    ext_text = get_arg()
    user = config.get('Authentication', 'user')
    pwd = config.get('Authentication', 'pwd')

    login = config.get('Address', 'login_page')
    action_p = config.get('Address', 'action_page')
    br = mechanize.Browser()

    # br.set_debug_http(True)
    # br.set_debug_redirects(True)
    # br.set_debug_responses(True)

    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    br.add_password(login, user, pwd)
    r = br.open(login)
    r.read()
    r = br.open(action_p)
    r.read()

    update_grplist(br, ext_text)
    r = br.open(action_p)
    r.read()
    print(">> after submit <<")
    get_grplist(br)

main()
