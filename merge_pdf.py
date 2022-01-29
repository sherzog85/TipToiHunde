import PyPDF2

#load documents to merge
pdfReader = PyPDF2.PdfFileReader(open('dogs.pdf', 'rb'))
pdfOverlayReader = PyPDF2.PdfFileReader(open('overlay.pdf', 'rb'))
#open output stream
pdfWriter = PyPDF2.PdfFileWriter()
for i in range(2):
    OIDPage = pdfReader.getPage(i)
    OIDPage.mergePage(pdfOverlayReader.getPage(0))
    pdfWriter.addPage(OIDPage)
resultPdfFile = open('dogs_box.pdf', 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
