import os
import webbrowser
from time import sleep
from dotenv import load_dotenv

# open excel files.
load_dotenv()
def excel():
    # set path for files that need opening.
    # add paths according to your needs
    tp_path = os.getenv('TP_PATH')
    calc_path = os.getenv('CALC_PATH')
    addr_path = os.getenv('ADDR_PATH')

    # open the files
    os.startfile(calc_path)
    sleep(5)
    os.startfile(tp_path)
    sleep(5)
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
runner()


