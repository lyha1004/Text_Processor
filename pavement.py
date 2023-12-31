#!/usr/bin/python

from paver.easy import *
import paver
import os
import glob
import shutil
import sys
import subprocess

sys.path.append(os.path.dirname(__file__))

@task
def setup():
    sh('python -m pip install -U coverage parameterized radon')

@task
def test():
    sh('python -m coverage run --source src --omit src/console_UI.py -m unittest discover -s test')
    sh('python -m coverage html')
    sh('python -m coverage report --show-missing')

@task
def run():
    file_name = "sample.txt"
    command = f"echo {file_name}| python src/console_UI.py"
    sh(command)


@task
def clean():
    for pycfile in glob.glob("*/*/*.pyc"): os.remove(pycfile)
    for pycache in glob.glob("*/__pycache__"): os.removedirs(pycache)
    for pycache in glob.glob("*/__pycache__"): shutil.rmtree(pycache)
    try:
        shutil.rmtree(os.getcwd() + "/cover")
    except:
        pass

@task
def radon():
    sh('radon cc src -a -nb')
    sh('radon cc src -a -nb > radon.report')
    if os.stat("radon.report").st_size != 0:
        raise Exception('radon found complex code')

@task
@needs(['setup', 'clean', 'test', 'radon'])
def default():
    pass
