import sys
import os
from cx_Freeze import setup, Executable

# Add Files
build_options = {'packages': [], "excludes": []}
# TARGET
target = Executable(
    script= 'main.py',
    base="Win32GUI",    
    icon='img/sold_icon.ico'
)


# SETUP
setup(
    name = 'AMS',
    version = '0.1',
    description = 'Additive Manufacturing Software developed by students at LNTSOLD lab, UFRJ, Rio de Janeiro Brazil',
    options =  {'build_exe' : build_options},
    executables = [Executable("main.py", base="Win32GUI", icon='img/sold_icon.ico')]
)