import os
import subprocess

os.system("echo hello world")
print("Parte 1")
# variavel = subprocess.call(["py", "list-operations.py"])
# variavel = subprocess.check_output(["py", "list-operations.py"])
variavel = subprocess.check_output(["python3", "list-operations.py"])
print("Parte 2")
print(variavel)
