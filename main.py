#!/usr/bin/env python3

import settings
import subprocess as sp
import os


for directory in settings.repositories:
	if os.path.isdir(f"{directory}/.git") and directory:
		print(f"\nChecking: {directory}")

		cmd = f"cd '{directory}'; "
		cmd += f"{settings.git_path} pull origin main; "
		cmd += f"{settings.git_path} add .; "
		cmd += f"{settings.git_path} commit -m '{settings.message}'"
		cmd += f"{settings.git_path} push origin main"

		sp.run(cmd, shell=True)
		print()

 