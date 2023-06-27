from pymem import Pymem
import subprocess
import os

# 使用此句加载后就可以 Pymem('notepad.exe') 定位到
notepad = subprocess.Popen(['notepad.exe'])

pm = Pymem('notepad.exe')
pm.inject_python_interpreter()
modules = list(pm.list_modules())
for module in modules:
    print(module.name)

# 很奇怪，这段代码一开始执行不通过。报错是：Could not allocate memory for shellcode
# 执行数次后就通过了，时好时坏。
filepath = os.path.join(os.path.abspath('.'), 'pymem_injection.txt')
filepath = filepath.replace("\\", "\\\\")
shellcode = """
f = open("{}", "w+")
f.write("pymem_injection")
f.close()
""".format(filepath)
pm.inject_python_shellcode(shellcode)
notepad.kill()