# C# PDFPatcher    MuPDF
# Python   ReportLab  https://docs.reportlab.com/

from reportlab.pdfgen import canvas
c = canvas.Canvas("hello.pdf")
c.drawString(100,100,"Hello World")
c.showPage()
c.save()

