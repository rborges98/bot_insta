import sys
from cx_Freeze import Executable, setup

files = ['tela.py', 'db.py', 'chromedriver.exe']

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name = 'Instagram Bot',
    options = {'build_exe':{'packages':['sqlite3', 'selenium', 'webdriver_manager', 'PySimpleGUI'], 
               'includes':['tkinter'],
               'include_files': files}},
    executables = [Executable('bot_insta.py', base=base)]
)