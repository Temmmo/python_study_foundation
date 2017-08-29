#! python
import PyPDF2
pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())

pdfReader1 = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
print(pdfReader1.isEncrypted)
#pdfReader1.getPage(0)

pdfReader1.decrypt('rosebud')
pageObj1 =pdfReader1.getPage(0)

pdf1File = open('meetingminutes.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('combinedminutes.pdf','wb')
pdfWriter.write(pdfOutputFile)
pdf1File.close()
pdf2File.close()
pdfOutputFile.close()

minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader3 = PyPDF2.PdfFileReader(minutesFile)
page = pdfReader3.getPage(0)
page.rotateClockwise(90)
pdfWriter1 =PyPDF2.PdfFileWriter()
pdfWriter1.addPage(page)
resultPdfFile = open('rotatedPage.pdf', 'wb')
pdfWriter1.write(resultPdfFile)
resultPdfFile.close()
minutesFile.close()

minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader3 = PyPDF2.PdfFileReader(minutesFile)
minutesFirstPage = pdfReader3.getPage(0)
pdfWatermakeReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
minutesFirstPage.mergePage(pdfWatermakeReader.getPage(0))
pdfWriter2 = PyPDF2.PdfFileWriter()
pdfWriter2.addPage(minutesFirstPage)
for pageNum in range(1,pdfReader3.numPages):
    minutesPage = pdfReader3.getPage(0)
    pdfWriter2.addPage(minutesPage)
resultPdfFile1 = open('watermarkedCover.pdf', 'wb')
pdfWriter1.write(resultPdfFile1)
resultPdfFile1.close()
minutesFile.close()


