import pyautogui as p
import pandas as pd
import win32clipboard as clip


from tools import open_file_on_desktop
from tools import get__spreadsheet_data
from tools import windows_email
from tools import goto_cell, goto_sheet, create_sheet, delete_cols, goto_term, read_cell
from tools import log, repeated_press
from typing import List, Any
import datetime
from dateutil import parser
import pandas as pd
import pyautogui
import logging

NAME_OF_FILE_TO_OPEN = 'ex_1.xlsx'
NAME_OF_LOG_FILE = 'bot.log'