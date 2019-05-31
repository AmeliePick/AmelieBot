from cx_Freeze import setup, Executable
import sys

exe = Executable(script="Amelie.py", icon = "../logo.ico")

buildOptions = dict(includes =["idna.idnadata", 'atexit', 'numpy.core._methods', 'numpy.lib.format', 'scipy',
                                'scipy.integrate', 'scipy.signal',  'scipy.sparse.linalg', 'scipy.sparse.csgraph',
                                'scipy.sparse.csgraph._validation', 'pyglet.resource', 'pyglet.clock'], optimize=1)

setup(name = "AmelieBot",version = "2.5.3.1", description = "Chat bot with the ability to perform some functions", executables = [exe], options = dict(build_exe = buildOptions))
