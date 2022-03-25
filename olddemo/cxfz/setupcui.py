import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["os"],
    "excludes": ["tkinter"]
}

setup(
    name = "cuifoo",
    version = "0.1",
    description = "My CUI application!",
    options = {"build_exe": build_exe_options},
    executables = [Executable("cuifoo.py")]
)