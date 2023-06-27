import pymem

# 这个路径可以找到 python.exe 却不能找到 Path 里其他自定义的命令
pm = pymem.Pymem('python.exe')
# pm = pymem.Pymem('notepad.exe') # 找不到

modules = list(pm.list_modules())
for module in modules:
    print(module.name)

print('-=====================================')
pm.inject_python_interpreter() # 注入后会多出很多 dll
modules = list(pm.list_modules())
for module in modules:
    print(module.name)