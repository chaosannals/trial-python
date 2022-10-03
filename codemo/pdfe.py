from PyPDF2 import PdfReader

reader = PdfReader(".\mypdf.pdf")
number_of_pages = len(reader.pages)
print(number_of_pages)
page = reader.pages[0]
image_count = len(page.images)
print(image_count)
print(page.images[0].name)
with open(page.images[0].name, 'wb') as fp:
    fp.write(page.images[0].data)