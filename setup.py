import sys
from cx_Freeze import setup, Executable

base = None

if sys.platform == 'win32':
    base = 'win32GUI'

executables = [
    Executable(script='main.py', base=base, icon='imagens, icones/dinheiro-icone_1.ico', )
]

includeFiles = ['imagens, icones/', 'View/', 'easy_finances.db']
packages = ['PyQt5', 'datetime', 'sqlite3']

setup(
    name = 'EasyFinances',
    version = '1.0',
    description = "App Controle Financeiro",
    author = "Geovani Debastiani",
    options = {'build_exe': {'include_files':includeFiles}},
    executables = executables

)