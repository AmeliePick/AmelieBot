# -*- coding: utf-8 -*-
from cx_Freeze import setup, Executable
from configparser import ConfigParser
import sys

parser = ConfigParser()
parser.read("Version/AppSetup.ini")

mainScript = parser.get("Setup", "MainScript")
AppIco = parser.get("Setup", "AppIco")
AppName = parser.get("Setup", "Name")
AppVersion = parser.get("Setup", "Version")

exe = Executable(script = mainScript, icon = AppIco)

buildOptions = dict(includes =["idna.idnadata", 'atexit', 'numpy.core._methods', 'numpy.lib.format', 'scipy',
                                'scipy.integrate', 'scipy.signal',  'scipy.sparse.linalg', 'scipy.sparse.csgraph',
                                'scipy.sparse.csgraph._validation', 'pyglet.resource', 'pyglet.clock', 'multiprocessing', 
                                'joblib', 'ffmpeg', 'ffprobe', 'speech_recognition'], optimize=1)


setup(name = AppName, 
      version = AppVersion, 
      description = "Amelie Bot", 
      author = "AmeliePick",
      author_email = "ameliepickdev@gmail.com",
      executables = [exe], options = dict(build_exe = buildOptions))






''' Errors which can be while build
-----------------------------------------------------------------------------------------
'multiprocessing' module can be incorretly works.

SOLUTION: remove from 'lib\multiprocessing' copy sources files into that path.

multiprocessing GitHub: https://github.com/python/cpython/tree/3.8/Lib/multiprocessing/


-----------------------------------------------------------------------------------------
Scipy's lib has wrong paths with some modules.

SOLUTION: Just remove that bullshit and copy sources files into that path.

Scipy GitHub: https://github.com/scipy/scipy


'''
