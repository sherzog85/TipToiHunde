

import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('dogs_3.pdf', 'rb'))
pdfOverlayReader = PyPDF2.PdfFileReader(open('overlay.pdf', 'rb'))
pdfWriter = PyPDF2.PdfFileWriter()
for i in range(2):
    minutesFirstPage = pdfReader.getPage(i)
    minutesFirstPage.mergePage(pdfOverlayReader.getPage(0))
    pdfWriter.addPage(minutesFirstPage)
resultPdfFile = open('dogs_box.pdf', 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()