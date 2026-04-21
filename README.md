Image Utility Scripts
Two lightweight Python scripts for batch renaming and converting image files.

Scripts Overview
ScriptWhat it doesScript 1 — Rename & MoveRenames .png files to sequentially numbered .jpg filenames and moves them to a new folderScript 2 — Convert & RenameOpens .jpg images, converts them properly using Pillow, and saves them as sequentially numbered .jpg files in a new folder

Script 1 — Batch Rename & Move
What it does
Scans a folder for .png files, renames them as .jpg with sequential numbers starting from 301, and moves them to a destination folder.

⚠️ This script only renames the files — it does not convert the image format. The file content stays the same; only the filename and extension change.

Requirements
No external packages needed — uses Python's built-in os module only.
bash# No installation required
Configuration
Open the script and update these variables:
pythonfolder = r'F:\download\IOT'           # Folder containing your .png files
folder_path = r'F:\download\Coverted' # Destination folder for renamed files
file_extension = ".png"               # Source file extension to look for
file_extension2 = ".jpg"              # New file extension for renamed files
To change the starting number, update the start value in the enumerate call:
pythonfor i, file in enumerate(files, start=301):   # Change 301 to any number
Usage
bashpython rename_move.py
Example Output
Changed successfully
Changed successfully
Changed successfully
...
Example Result
Before → F:\download\IOT\photo.png
After  → F:\download\Coverted\301.jpg

Script 2 — Convert & Rename
What it does
Scans a folder for .jpg files, properly re-encodes them as JPEG images using Pillow (handling color mode conversion), and saves them as sequentially numbered .jpg files in a destination subfolder.

✅ This script actually converts the image data using Pillow, which ensures compatibility and strips any unsupported color modes (like RGBA or transparency).

Requirements
Requires the Pillow library:
bashpip install pillow
Configuration
Open the script and update these variables:
pythonsource_folder = r'G:\Exam'             # Folder containing your source .jpg files
destination_folder = r'G:\Exam\Exam2'  # Output folder (created automatically if missing)
To change the starting number, update the start value:
pythonfor i, file in enumerate(png_files, start=1):  # Change 1 to any number
Usage
bashpython convert_rename.py
Example Output
Converted and renamed: photo1.jpg → 1.jpg
Converted and renamed: photo2.jpg → 2.jpg
Error processing badfile.jpg: cannot identify image file
...
Example Result
Before → G:\Exam\photo1.jpg
After  → G:\Exam\Exam2\1.jpg

Key Differences Between the Two Scripts
Feature                   manin.py j       pg_converter

Actual image conversion      ❌ No          ✅ Yes (via Pillow)

Handles RGBA / transparency  ❌ No          ✅ Yes (converts to RGB)

External dependency          None              pillow

Source format                .png              .jpg

Output format               .jpg (rename only)  .jpg (re-encoded)

Starting number              301                1

Error handling              ❌ No           ✅ Yes (try/except)

Project Structure
your-folder/
│
├── rename_move.py       # Script 1 — rename & move
├── convert_rename.py    # Script 2 — convert & rename
└── README.md            # This file

Troubleshooting
ModuleNotFoundError: No module named 'PIL'
→ Run pip install pillow to install the Pillow library.
FileNotFoundError on the destination folder (Script 1)
→ Make sure the destination folder (F:\download\Coverted) already exists. Script 1 does not create it automatically — unlike Script 2.
No files are being processed
→ Double-check that the file extensions in the script exactly match your files. Extensions are case-sensitive on some systems (e.g. .PNG vs .png). Script 2 uses .lower() to handle this automatically; Script 1 does not.
Files are renamed but images don't open correctly (Script 1)
→ Script 1 only renames — it doesn't convert the format. If you need the files to be valid JPEGs, use Script 2 instead.

License
Free to use and modify for personal or educational purposes.
