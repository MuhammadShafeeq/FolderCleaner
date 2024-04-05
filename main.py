import os
import shutil
from tkinter import filedialog

target_path = filedialog.askdirectory(title="Select Folder to be cleared")
cleared_path = filedialog.askdirectory(title="Select Folder to be Moved to")


files = []
filetypes = []
os.chdir(target_path)
for i in os.listdir():
    if os.path.isfile(i):
        print(i)
        file_details = i.split('.')
        file_name = i.replace(f'.{file_details[-1]}', '')
        file = {"Filetype": file_details[-1].lower(), "Filename": file_name, "File": i}
        files.append(file)
        if file_details[-1] not in filetypes:
            filetypes.append(file_details[-1].lower())

print(files, filetypes)
os.chdir(cleared_path)
for i in filetypes:
    if i not in os.listdir():
        try:
            os.mkdir(i)
        except Exception as e:
            print(e)

os.chdir(target_path)
for file in files:
    shutil.move(file["File"], f'{cleared_path}/{file["Filetype"]}//{file["File"]}')
