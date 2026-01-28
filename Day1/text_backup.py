import shutil
from datetime import date
import os
source = "c:/Users/Admin/Desktop/data.txt"
backup = f"c:/Users/Admin/Desktop/backup_{date.today()}.txt"

shutil.copy(source, backup)
print(f"Backup of {source} created at {backup}")
