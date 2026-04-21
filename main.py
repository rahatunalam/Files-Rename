import os

folder = r'F:\download\IOT'

folder_path = r'F:\download\Coverted'

file_extension = ".png"
file_extension2 = ".jpg"

files = sorted([f for f in os.listdir(folder) if f.endswith(file_extension)])

for i,file in enumerate(files , start=301):
    old_path = os.path.join(folder,file)
    new_filename = f"{i}{file_extension2}"
    new_path = os.path.join(folder_path , new_filename)
    os.rename(old_path , new_path)
    print('Changed successfully')
