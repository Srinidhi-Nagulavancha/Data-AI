import shutil
import os
from datetime import date
source_dir = "c:/Users/Admin/Desktop/source_images"
backup_dir = f"c:/Users/Admin/Desktop/backup_{date.today()}"
os.makedirs(backup_dir, exist_ok=True)
for file_name in os.listdir(source_dir):
    if file_name.lower().endswith(".jpeg"): 
        source_file = os.path.join(source_dir, file_name)
        backup_file = os.path.join(backup_dir, file_name)
        shutil.copy(source_file, backup_file)
        print(f"Copied {source_file} to {backup_file}")
print(f"Backup completed. JPEG images are saved in {backup_dir}")