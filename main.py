#!/usr/bin/env python3

import settings
import subprocess as sp
import os


for directory in settings.repositories:
	if os.path.isdir(f"{directory}/.git") and directory:
		print(f"\nChecking: {directory}")

		cmd = f"cd '{directory}'; "
		cmd += f"git pull origin main; "
		cmd += f"git add .; "
		cmd += f"git commit -m '{settings.message}'; "
		cmd += f"git push origin main"

		sp.run(cmd, shell=True)
		print()

 