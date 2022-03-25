import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["os"],
    "excludes": ["tkinter"]
}

setup(
    name="allfoo",
    version="0.1",
    description="My GUI and cui application!",
    options={"build_exe": build_exe_options},
    executables=[
        Executable(
            "guifoo.py",
            icon='app.ico',
            base="Win32GUI" if sys.platform == "win32" else None
        ),
        Executable("cuifoo.py", icon='app.ico')
    ]
)
