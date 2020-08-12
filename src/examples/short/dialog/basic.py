"""
Demonstration program for pythondialog.

This is a simple program demonstrating the possibilities offered by
the pythondialog module (which is itself a Python interface to the
well-known dialog utility, or any other program compatible with
dialog).

Please have a look at the documentation for the `handle_exit_code'
function in order to understand the somewhat relaxed error checking
policy for pythondialog calls in this demo.

References:
- http://pythondialog.sourceforge.net/doc/#main-contents
- https://pypi.python.org/pypi/pythondialog/3.4.0

Installing:
via apt:
    python 2: python-dialog
    python 3: python3-dialog
via pip:
    $ pip install pythondialog
"""

import os
import os.path
import sys
import time

import dialog

FAST_DEMO = True


def handle_exit_code(d, code):
    if code in (d.DIALOG_CANCEL, d.DIALOG_ESC):
        if code == d.DIALOG_CANCEL:
            msg = 'You chose CANCEL in the last dialog box. Do you want to exit this demo?'
        else:
            msg = 'You pressed ESC in the last dialog box. Do you want to exit this demo?'
        if d.yesno(msg) == d.DIALOG_OK:
            sys.exit(0)
        else:
            return 0
    else:
        return 1


def show_and_exit(collected):
    for k, v in collected.items():
        print('{k} is [{v}]'.format(k=k, v=v))
    sys.exit(0)


def demo_inputbox(d):
    while True:
        (code, answer) = d.inputbox('Whats your name?', init='Snow White')
        if handle_exit_code(d, code):
            break
    return answer


def demo_menu(d):
    while True:
        (code, tag) = d.menu(
            'Whats your favorite day of the week?',
            width=60,
            choices=[('Monday', 'Being the first day of the week...'),
                     ('Tuesday', 'Comes after Monday'),
                     ('Wednesday', 'Before Thursday day'),
                     ('Thursday', 'Itself after Wednesday'),
                     ('Friday', 'The best day of all'),
                     ('Saturday', 'Well, Ive had enough, thanks'),
                     ('Sunday', 'Lets rest a little bit')])
        if handle_exit_code(d, code):
            break
    return tag


def demo_infobox(d):
    d.infobox(
        'One moment, please. Just wasting some time here to show you the infobox...')
    if FAST_DEMO:
        time.sleep(0.5)
    else:
        time.sleep(3)


def demo_gauge(d):
    d.gauge_start('Progress: 0%', title='Still testing your patience...')
    for i in range(1, 101):
        if i < 50:
            d.gauge_update(i, 'Progress: %d%%' % i, update_text=1)
        elif i == 50:
            d.gauge_update(i, 'Over %d%%. Good.' % i, update_text=1)
        elif i == 80:
            d.gauge_update(
                i, 'Yeah, this boring crap will be over Really Soon Now.', update_text=1)
        else:
            d.gauge_update(i)
        if FAST_DEMO:
            time.sleep(0.01)
        else:
            time.sleep(0.1)
    d.gauge_stop()


def demo_yesno(d):
    answer = d.yesno('Do you like this demo?')
    if answer == d.DIALOG_OK:
        d.msgbox('Excellent! Press OK to see the source code.')
    else:
        d.msgbox('Well, feel free to send your complaints to /dev/null!')
    return answer


def demo_textbox(d):
    d.textbox(sys.argv[0], width=76)


def demo_checklist(d):
    while True:
        (code, tag) = d.checklist(text='What sandwich toppings do you like?',
                                  height=15, width=54, list_height=7,
                                  choices=[('Catsup', '', 0),
                                           ('Mustard', '', 0),
                                           ('Pesto', '', 0),
                                           ('Mayonaise', '', 1),
                                           ('Horse radish', '', 1),
                                           ('Sun-dried tomatoes', '', 1)],
                                  title='Do you prefer ham or spam?',
                                  backtitle='And now, for something '
                                            'completely different...')
        if handle_exit_code(d, code):
            break
    return tag


def demo_radiolist(d):
    while True:
        (code, tag) = d.radiolist(
            'Whats your favorite kind of sandwich?',
            width=65,
            choices=[('Hamburger', '2 slices of bread, a steak...', 0),
                     ('Hotdog', 'doesnt bite any more', 0),
                     ('Burrito', 'no se lo que es', 0),
                     ('Doener', 'Huh?', 0),
                     ('Falafel', 'Erm...', 0),
                     ('Bagel', 'Of course!', 0),
                     ('Big Mac', 'Ah, thats easy!', 1),
                     ('Whopper', 'Erm, sorry', 0),
                     ('Quarter Pounder',
                      'called \'le Big Mac\' in France', 0),
                     ('Peanut Butter and Jelly', 'Well, thats your own '
                                                 'business...', 0),
                     ('Grilled cheese', 'And nothing more?', 0)])
        if handle_exit_code(d, code):
            break
    return tag


def demo_calendar(d):
    while True:
        (code, date) = d.calendar(
            'When do you think Debian sarge will be released?', year=0)
        if handle_exit_code(d, code):
            break
    return date


def demo_passwordbox(d):
    while True:
        (code, password) = d.passwordbox(
            'What is your root password, so that I can crack your system right now?')
        if handle_exit_code(d, code):
            break
    return password


def demo_fselect(d):
    homedir = os.getenv('HOME') + os.sep
    while True:
        (code, path) = d.fselect(homedir, 10, 50,
                                 title='Cute little file to show as in a [tail -f]')
        if handle_exit_code(d, code):
            if not os.path.isfile(path):
                d.scrollbox(
                    'Hmm. Didnt I ask you to select a *file*?', width=50, height=10)
            else:
                break
    return path


def demo_tailbox(d, file):
    d.tailbox(
        file, 20, 60, title='You are brave. You deserve the right to rest, now.')


def demo_scrollbox(d, collected):
    msg = 'Here are your choice...\n'
    for k, v in collected.items():
        msg += '{k} is [{v}]\n'.format(k=k, v=v)
    d.scrollbox(msg, height=20, width=75, title='Great Report of the Year')


def demo():
    collected = {}
    d = dialog.Dialog(dialog='dialog')
    d.add_persistent_args(['--backtitle', 'pythondialog demo'])

    collected['name'] = demo_inputbox(d)
    collected['favourite_day'] = demo_menu(d)
    demo_infobox(d)
    demo_gauge(d)
    collected['yesno'] = demo_yesno(d)
    demo_textbox(d)
    collected['toppings'] = demo_checklist(d)
    collected['sandwich'] = demo_radiolist(d)
    collected['date'] = demo_calendar(d)
    collected['password'] = demo_passwordbox(d)
    collected['file'] = demo_fselect(d)
    demo_tailbox(d, collected['file'])
    demo_scrollbox(d, collected)
    # show_and_exit(collected)


def main():
    demo()


if __name__ == '__main__':
    main()
