import sys
import os
from cx_Freeze import setup, Executable

# Add Files
files = ['Interface.py', 'sold_icon.ico', 'img/']

# TARGET
target = Executable(
    script= 'main.py',
    base="Win32GUI",
    icon='sold_icon.ico'
)

# SETUP
setup(
    name = 'AMS',
    version = '0.1',
    description = 'Additive Manufacturing Software developed by students at LNTSOLD lab, UFRJ, Rio de Janeiro Brazil',
    options =  {'build_exe' : {'include_files' : files}},
    executables = [target]
)