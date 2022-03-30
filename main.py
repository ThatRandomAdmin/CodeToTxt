import shutil
import os
from tkinter import filedialog
from pathlib import Path

src_path = filedialog.askdirectory()
dst_path = "C:/CodeToText"

shutil.copytree(src_path, dst_path)
print('Copied')

import os

for subdir, dirs, files in os.walk(dst_path):
    for file in files:
        filepath = subdir + os.sep + file
        filename, file_extension = os.path.splitext(filepath)
        p = Path(filepath)
        p.rename(p.with_suffix(file_extension + '.txt'))
