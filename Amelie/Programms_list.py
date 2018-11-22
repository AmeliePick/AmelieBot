# -*- coding: utf-8 -*-

'''
Module for viewing all installed applications in the system.

Not used in AmelieBot Alpha 2.0

'''

from winreg import *

UNINSTALL_PATH_LIST = [
    r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall',
    r"SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall",
]

programs_dict = dict()

for path in UNINSTALL_PATH_LIST:
    with OpenKey(HKEY_LOCAL_MACHINE, path) as key:
        for i in range(QueryInfoKey(key)[0]):
            keyname = EnumKey(key, i)
            subkey = OpenKey(key, keyname)

            try:
                subkey_dict = dict()
                for j in range(QueryInfoKey(subkey)[1]):
                    k, v = EnumValue(subkey, j)[:2]
                    subkey_dict[k] = v

                if 'DisplayName' not in subkey_dict:
                    continue

                name = subkey_dict['DisplayName'].strip()
                if not name:
                    continue

                programs_dict[name] = subkey_dict

            except WindowsError:
                pass


for number, name in enumerate(sorted(programs_dict.keys()), 1):
    subkey_dict = programs_dict[name]
    print(name)
    
