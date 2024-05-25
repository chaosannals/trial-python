import math
import re
import os
from glob import glob
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4

FONT_SIZE = 14
TITLE_SIZE = 16
POS_INIT = 10
PAGE_SIZE = A4
PAGE_WIDTH = PAGE_SIZE[0]
PAGE_HEIGHT = PAGE_SIZE[1]

def list_txt_paths():
    txt_paths = glob('*.txt')
    return [p for p in filter(lambda p: not p.endswith('index.txt'), txt_paths)]

def read_txt_lines(txt_path):
    with open(txt_path, 'r') as reader:
        return reader.readlines()
    
def is_title(txt_line):
    m = re.match(r'第.+[章卷节][： :]', txt_line)
    return m is not None

class PdfMaker:
    def __init__(self, pdf_path):
        self.canvas = Canvas(
            pdf_path,
            pagesize=PAGE_SIZE,
            # bottomup=1,
            bottomup=0,
            pageCompression=0,
            encrypt=None,
        )
        self.pos = POS_INIT

    def pos_add(self, v):
        self.pos += v
        if self.pos > PAGE_HEIGHT:
            print('new page')
            self.canvas.showPage()
            self.pos = POS_INIT
    
    def save(self):
        self.canvas.save()
    
    def draw_line(self, txt_line):
        if is_title(txt_line):
            self.canvas.setFontSize(TITLE_SIZE)
            self.pos_add(TITLE_SIZE)
            self.canvas.drawString(10, self.pos, txt_line)
            return
        
        self.canvas.setFontSize(FONT_SIZE)
        sw = self.canvas.stringWidth(txt_line, fontSize=FONT_SIZE)
        if sw > PAGE_WIDTH:
            txt_len = len(txt_line)
            txt_scale = sw / PAGE_WIDTH
            row_len = math.floor(txt_len / txt_scale) - 4
            print(txt_line)
            rows = re.findall(f'.{{1,{row_len}}}', txt_line)
            for row in rows:
                self.pos_add(FONT_SIZE)
                self.canvas.drawString(10, self.pos, row)
        else:
            self.pos_add(FONT_SIZE)
            self.canvas.drawString(10, self.pos, txt_line)

def make_pdf_from_txt(txt_path):
    dirname = os.path.dirname(txt_path)
    filename = os.path.basename(txt_path)
    [name, _] = os.path.splitext(filename)
    pdf_path = os.path.join(dirname, f'{name}.pdf')
    maker = PdfMaker(pdf_path)
    print(f'{txt_path} => {pdf_path}')
    txt_lines = read_txt_lines(txt_path)
    txt_lines_count = len(txt_lines)
    print(f'总计: {txt_lines_count} 行')

    for txt_line in txt_lines:
        maker.draw_line(txt_line)
    
    maker.save()
        

for txt_path in list_txt_paths():
    make_pdf_from_txt(txt_path)

