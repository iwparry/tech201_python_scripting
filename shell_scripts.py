import os
import subprocess

# Python doesn't actually run shell (terminal) commands
# Instead we can use Python to run shell script files

script_dir = os.path.dirname(__file__)   #  __file__ indicates current file

scripts_absolute_path = os.path.join(script_dir, "script.sh")

subprocess.call(['sh', scripts_absolute_path])

# Homework - Debug the above, need to call script.sh