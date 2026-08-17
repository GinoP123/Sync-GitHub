#!/usr/bin/env python3
import subprocess as sp
import os, glob
import settings
import sys

script_dir = os.path.dirname(sys.argv[0])

with open(f"{script_dir}/{settings.folders_copy}") as infile:
    for folder in infile.read().strip().split('\n'):
        folder = os.path.expanduser(folder)
        assert sp.run(f"cp -r '{folder}' '{script_dir}/{settings.copied_folder_destination}'", shell=True).returncode == 0

