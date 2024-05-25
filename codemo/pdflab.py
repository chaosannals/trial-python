# C# PDFPatcher    MuPDF
# Python   ReportLab  https://docs.reportlab.com/
import math
import re
import os
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

SELF_DIR = os.path.dirname(__file__)
TTF_NAME = 'SourceCn'

font_path = os.path.join(SELF_DIR, 'source-han-serif-cn-light.ttf')
pdfmetrics.registerFont(TTFont(TTF_NAME, font_path))

# c = Canvas("hello.pdf")

font_size = 14
page_size = A4

print(f'pagesize: {page_size}')
c = Canvas(
    'hello.pdf',
    pagesize=page_size,
    # bottomup=1,
    bottomup=0,
    pageCompression=0,
    encrypt=None,
)
# c.drawString(100,100,"Hello World")
pos = 0
for i in range(100):
    c.setFont(TTF_NAME, font_size)
    line = "Hello World 中文" * 10
    sw = c.stringWidth(line, fontSize=font_size)

    if sw > page_size[0]:
        ll = len(line) 
        lm = sw / page_size[0]
        lc = math.ceil(lm)
        rcc = math.floor(ll / lm) - 4
        rows = re.findall(f'.{{1,{rcc}}}', line)
        print(f'row char count: {rcc} | line count: {lc} line multi: {lm} line len: {ll}')
        for row in rows:
            print(f'row len: {len(row)}')
            pos += 20
            c.drawString(10, pos,row)
    else:
        pos += 20
        c.drawString(10,pos ,line)
    
    if pos > page_size[1]:
        print('new page')
        c.showPage()
        pos = 0
c.save()

