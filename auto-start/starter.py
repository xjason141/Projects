import os
import webbrowser
from time import sleep

# open excel files.
def excel():
    # set path for files that need opening.
    # add paths according to your needs
    tp_path = 'filepath'
    calc_path = 'filepath'
    addr_path = 'filepath'

    # open the files
    os.startfile(tp_path)
    os.startfile(calc_path)
    os.startfile(addr_path)


# runs default browser, and straight away go to google maps.
def browser():
    # if default browser is already running, a new instance will be created instead of opening a new tab.
    webbrowser.open_new_tab('https://www.google.com/')


# runs functions.
def runner():
    excel()
    sleep(10)
    browser()

# runner.
if __name__ == '__main__':
    runner()


