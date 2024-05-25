import math
import re
import os
from glob import glob
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

SELF_DIR = os.path.dirname(__file__)
FONT_PATH = os.path.join(SELF_DIR, 'source-han-serif-cn-light.ttf')
FONT_BOLD_PATH = os.path.join(SELF_DIR, 'source-han-serif-cn-bold.ttf')
FONT_SIZE = 14
FONT_NAME = 'SourceCn'
FONT_BOLD_NAME = f'{FONT_NAME}Bd'
TITLE_SIZE = 16
POS_INIT = 20
PAGE_SIZE = A4
PAGE_WIDTH = PAGE_SIZE[0]
PAGE_HEIGHT = PAGE_SIZE[1]

pdfmetrics.registerFont(TTFont(FONT_NAME, FONT_PATH))
pdfmetrics.registerFont(TTFont(FONT_BOLD_NAME, FONT_BOLD_PATH))
pdfmetrics.registerFontFamily(FONT_NAME, normal=FONT_NAME, bold=FONT_BOLD_NAME, italic=F'{FONT_NAME}It', boldItalic=f'{FONT_NAME}BI')

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
        self.page_count = 0

    def pos_add(self, v):
        self.pos += v
        if self.pos > PAGE_HEIGHT or (v == TITLE_SIZE):
            self.page_count += 1
            print(f'新页 {self.page_count}')
            self.canvas.showPage()
            self.pos = POS_INIT
        self.canvas.setFont(FONT_BOLD_NAME if v == TITLE_SIZE else FONT_NAME, v)
    
    def save(self):
        self.canvas.save()
    
    def draw_line(self, txt_line):
        if is_title(txt_line):
            self.pos_add(TITLE_SIZE)
            bookmark = f'{self.page_count}-{self.pos}'
            self.canvas.drawString(10, self.pos, txt_line)
            self.canvas.bookmarkPage(bookmark)
            self.canvas.addOutlineEntry(txt_line, bookmark)
            self.pos_add(FONT_SIZE)
            return
        
        self.canvas.setFontSize(FONT_SIZE)
        sw = self.canvas.stringWidth(txt_line, fontSize=FONT_SIZE)
        if sw > PAGE_WIDTH:
            txt_len = len(txt_line)
            txt_scale = sw / PAGE_WIDTH
            row_len = math.floor(txt_len / txt_scale) - 4
            # print(txt_line)
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
        maker.draw_line(txt_line.strip('\r\n'))
    
    maker.save()
        

for txt_path in list_txt_paths():
    make_pdf_from_txt(txt_path)

