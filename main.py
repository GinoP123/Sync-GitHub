#!/usr/bin/env python3

import settings
import subprocess as sp
import os
import sys

os.chdir(os.path.dirname(sys.argv[0]))
with open(settings.repositories_path) as infile:
	repositories = infile.read().strip().split()

for directory in repositories:
	if os.path.isdir(f"{directory}/.git") and directory:
		print(f"\nChecking: {directory}")

		cmd = f"cd '{directory}'; "
		cmd += f"git pull origin main; "
		cmd += f"git add .; "
		cmd += f"git commit -m '{settings.message}'; "
		cmd += f"git push origin main"
		
		output = sp.run(cmd, shell=True, capture_output=True).stdout.decode()
		print(output)

 