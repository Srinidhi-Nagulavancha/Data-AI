import shutil
from datetime import date
import os
source = "c:/Users/Admin/Desktop/data.txt"
backup = f"c:/Users/Admin/Desktop/backup_{date.today()}.txt"
try:
    if not os.path.exists(source):
        raise FileNotFoundError(f"Source file '{source}' does not exist.")
    shutil.copy(source, backup)
    print(f"Backup of {source} created at {backup}")
    if os.path.exists(backup):
        print("Backup file exists.")
except FileNotFoundError as e:
    print(e)
except PermissionError:
    print("Permission denied. Please check your file permissions.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")