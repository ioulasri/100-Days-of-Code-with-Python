"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['Pomodoro_main.py']
DATA_FILES = ['icon.png']
OPTIONS = {
'iconfile': '/Users/imadoulasri/PycharmProjects/100day/Pomodoro/iconapp.png'}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)