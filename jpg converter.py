import os
from PIL import Image

# Folder with PNG images
source_folder = r'G:\Exam'

# Destination folder for renamed JPGs
destination_folder = r'G:\Exam\Exam2'
os.makedirs(destination_folder, exist_ok=True)  # Create folder if it doesn't exist

# Get list of .png files
png_files = sorted([f for f in os.listdir(source_folder) if f.lower().endswith('.jpg')])

# Loop through each .png file
for i, file in enumerate(png_files, start=1):
    png_path = os.path.join(source_folder, file)
    jpg_filename = f"{i}.jpg"
    jpg_path = os.path.join(destination_folder, jpg_filename)

    try:
        # Open PNG and convert to RGB (JPG doesn't support alpha)
        with Image.open(png_path) as img:
            rgb_img = img.convert('RGB')
            rgb_img.save(jpg_path, 'JPEG')
        print(f"Converted and renamed: {file} → {jpg_filename}")
    except Exception as e:
        print(f"Error processing {file}: {e}")