import os
folder_path = r"C:\Users\Admin\Desktop\Python\day4"
prefix="new_1_"
for filename in os.listdir(folder_path):
    old_path=os.path.join(folder_path,filename)
    if os.path.isfile(old_path):
        new_name=prefix+filename
        new_path=os.path.join(folder_path,new_name)
        os.rename(old_path,new_path)
print("Files renamed successfully!")