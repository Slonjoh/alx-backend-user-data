#!/usr/bin/env python3

import subprocess
import os
import sys

def check_python_version():
    if sys.version_info[0] != 3 or sys.version_info[1] != 7:
        print("This script requires Python 3.7")
        sys.exit(1)

def install_requirements():
    subprocess.run(['pip3', 'install', '--upgrade', 'markupsafe'])
    subprocess.run(['pip3', 'install', '-r', 'requirements.txt'])

def start_server():
    os.environ['PYTHONPATH'] = '/alx-backend-user-data/0x01-Basic_authentication'
    os.environ['API_HOST'] = '0.0.0.0'
    os.environ['API_PORT'] = '5000'
    subprocess.run(['python3', '-m', 'api.v1.app'])

if __name__ == "__main__":
    check_python_version()
    install_requirements()
    start_server()
