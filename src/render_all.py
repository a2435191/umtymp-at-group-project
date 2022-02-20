import os
import glob

for filename in glob.glob("src/manim/**/*.py", recursive=True):
    os.system(f"manim -qk --write_all {filename}")