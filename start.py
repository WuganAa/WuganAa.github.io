import os
import shutil
from pathlib2 import Path
from datetime import datetime

cv_dir = Path("/Users/chenxg/Project/Homepage/my_cv/cv")
home_dir = Path(
    "/Users/chenxg/Project/Homepage/WuganAa.github.io")

cv_name = "xuganchen_cv.pdf"

cv_path = cv_dir / cv_name

if not cv_path.exists():
    raise FileNotFoundError(str(cv_path) + "not found")

print("\n" + "=" * 30 + "\n" + "=" * 30 + "\n" + "=" * 30)
print("copy " + cv_name)
print("=" * 30 + "\n" + "=" * 30 + "\n" + "=" * 30)
shutil.copy(cv_path, home_dir / 'content/download' / cv_name)

now = datetime.now().strftime("%Y%m%d %H:%M:%S")

print("\n" + "=" * 30 + "\n" + "=" * 30 + "\n" + "=" * 30)
print("make clean, generate, and github")
print("=" * 30 + "\n" + "=" * 30 + "\n" + "=" * 30)
os.system("make clean")
os.system("make html")
shutil.copy(home_dir / 'README.md', home_dir / 'output/README.md')
os.system("make github")

print("\n" + "=" * 30 + "\n" + "=" * 30 + "\n" + "=" * 30)
print("git add, commit, push, and pull")
print("=" * 30 + "\n" + "=" * 30 + "\n" + "=" * 30)
os.system("git add .")
os.system("git commit -m 'update at " + now + "'")
os.system("git push -u origin source")
os.system("git pull --all")

