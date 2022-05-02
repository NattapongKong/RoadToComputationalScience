# from posixpath import split
# import PyPDF2
# import os

# pdfName = input("unsplit PDF file name/path (Example.pdf): ")

# try:
#     with open(pdfName, 'rb') as pdfFile:
#         print("วิชา math2 การบ้านครั้งที่ 0 กลุ่ม 99 ลำดับที่ 00 ส่งปี 60 เดือน 01 วันที่ 01")
#         newName = input("new file name/path (math2 hw00 b99 00 600101): ")
#         splitName = newName.split(' ')
#         pdfReader = PyPDF2.PdfFileReader(pdfFile)
        
#         for pageNum in range(pdfReader.numPages):
#             pdfWriter = PyPDF2.PdfFileWriter()
#             if(pageNum < 10):
#                 splitName.insert(2, "p0" + str(pageNum + 1))
#             else:
#                 splitName.insert(2, "p" + str(pageNum + 1))
#             finalName = ' '.join(splitName)
#             pdfWriter.addPage(pdfReader.getPage(pageNum))
#             with open(finalName + ".pdf", 'wb') as newFile:
#                 pdfWriter.write(newFile)
#             newFile.close()
#             print("file " + finalName + ".pdf created")
#             splitName.pop(2)
            
#         print("PDF file splited successfully")
    
# except FileNotFoundError as e:
#     print("File not found")
#     exit()
newName ="math2 hw00 b99 00 600101"
print(len(newName.split(' ')))

