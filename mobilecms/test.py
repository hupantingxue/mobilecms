import os
from conf import *

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

gettext = lambda s: s
PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

print PROJECT_PATH
