import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["os", 'win32', 'win32com', 'win32comext'],
    "excludes": ["tkinter"]
}

setup(
    name = "cxfzsvc",
    version = "0.1",
    description = "My Service application!",
    options = {
        "build_exe": build_exe_options,
    },
    executables = [
        Executable(
            "winsvc.py"
        ),
    ]
)