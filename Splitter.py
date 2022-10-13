import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
import os

user = os.getlogin()

path = os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads")
fname = "Design.pdf"

def split():
    file = open('Design.pdf', 'rb')
    readpdf = PyPDF2.PdfFileReader(file)
    totalpages = readpdf.numPages

    act_pdf_file = 'C:\\Users\\Brandon Neil\\Downloads\\Design.pdf'
    act_sub_pages_name = ['page_1.pdf', 'page_2.pdf', 'page_3.pdf',
    'page_4.pdf', 'page_5.pdf', 'page_6.pdf', 'page_7.pdf', 'page_8.pdf',
    'page_9.pdf', 'page_10.pdf', 'page_11.pdf', 'page_12.pdf', 'page_13.pdf',
    'page_14.pdf', 'page_15.pdf', 'page_16.pdf', 'page_17.pdf', 'page_18.pdf',
    'page_19.pdf', 'page_20.pdf', 'page_21.pdf', 'page_22.pdf', 'page_23.pdf']

    def pdf_splitter(index, src_file):
        with open(src_file, 'rb') as act_mls:
            reader = PdfFileReader(act_mls)
            writer = PdfFileWriter()
            writer.addPage(reader.getPage(index))
            out_file = os.path.join('C:\\Users\\Brandon Neil\\Downloads', act_sub_pages_name[index])
            with open(out_file, 'wb') as out_pdf: writer.write(out_pdf)

    for x in range(totalpages): pdf_splitter(x, act_pdf_file)

def main():
    split()

if __name__ == '__main__':
    main()