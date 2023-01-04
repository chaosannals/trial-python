# codon

一个基于 LLVM 的 Python 编译器/解释器

注：目前只能在 Linux 和 macOs 是使用，Windows 要使用 wsl 或者虚拟机。

- [GitHub](https://github.com/exaloop/codon)
- [下载](https://github.com/exaloop/codon/releases)

```bash
# 解释执行
codon run fibdemo.py
codon run -release fibdemo.py

# 编译可执行文件
codon build -release -exe fibdemo.py
# 编译 LLVM IR
codon build -release -llvm fibdemo.py
```