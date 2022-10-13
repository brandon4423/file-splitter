from PyPDF2 import PdfFileReader, PdfFileWriter
import os

user = os.getlogin()

os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads")

def pageone():
    os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads")
    pages = [0]

    with open("Design.pdf", "rb") as f:
        reader = PdfFileReader(f)
        writer = PdfFileWriter()

        os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads\\Split")
        
        for page in range(len(reader.pages)):
            if page in pages:
                writer.addPage(reader.getPage(page))
            else:
                pass

            with open("page_one.pdf", "wb") as f2:
                writer.write(f2)

def pagetwo():
    os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads")
    pages = [1]

    with open("Design.pdf", "rb") as f:
        reader = PdfFileReader(f)
        writer = PdfFileWriter()

        os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads\\Split")

        for page in range(len(reader.pages)):
            if page in pages:
                writer.addPage(reader.getPage(page))
            else:
                pass

            with open("page_two.pdf", "wb") as f2:
                writer.write(f2)

def pagethree():
    os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads")
    pages = [2]

    with open("Design.pdf", "rb") as f:
        reader = PdfFileReader(f)
        writer = PdfFileWriter()

        os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads\\Split")

        for page in range(len(reader.pages)):
            if page in pages:
                writer.addPage(reader.getPage(page))
            else:
                pass

            with open("page_three.pdf", "wb") as f2:
                writer.write(f2)

def pagefour():
    os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads")
    pages = [3]

    with open("Design.pdf", "rb") as f:
        reader = PdfFileReader(f)
        writer = PdfFileWriter()

        os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads\\Split")

        for page in range(len(reader.pages)):
            if page in pages:
                writer.addPage(reader.getPage(page))
            else:
                pass

            with open("page_four.pdf", "wb") as f2:
                writer.write(f2)

def pagefive():
    os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads")
    pages = [4]

    with open("Design.pdf", "rb") as f:
        reader = PdfFileReader(f)
        writer = PdfFileWriter()

        os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads\\Split")

        for page in range(len(reader.pages)):
            if page in pages:
                writer.addPage(reader.getPage(page))
            else:
                pass

            with open("One Line.pdf", "wb") as f2:
                writer.write(f2)

def pagesix():
    os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads")
    pages = [5]

    with open("Design.pdf", "rb") as f:
        reader = PdfFileReader(f)
        writer = PdfFileWriter()

        os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads\\Split")

        for page in range(len(reader.pages)):
            if page in pages:
                writer.addPage(reader.getPage(page))
            else:
                pass

            with open("page_six.pdf", "wb") as f2:
                writer.write(f2)

def pageseven():
    os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads")
    pages = [6]

    with open("Design.pdf", "rb") as f:
        reader = PdfFileReader(f)
        writer = PdfFileWriter()

        os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads\\Split")

        for page in range(len(reader.pages)):
            if page in pages:
                writer.addPage(reader.getPage(page))
            else:
                pass

            with open("page_seven.pdf", "wb") as f2:
                writer.write(f2)

def pageeight():
    os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads")
    pages = [7]

    with open("Design.pdf", "rb") as f:
        reader = PdfFileReader(f)
        writer = PdfFileWriter()

        os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads\\Split")

        for page in range(len(reader.pages)):
            if page in pages:
                writer.addPage(reader.getPage(page))
            else:
                pass

            with open("page_eight.pdf", "wb") as f2:
                writer.write(f2)

def pagenine():
    os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads")
    pages = [8]

    with open("Design.pdf", "rb") as f:
        reader = PdfFileReader(f)
        writer = PdfFileWriter()

        os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads\\Split")

        for page in range(len(reader.pages)):
            if page in pages:
                writer.addPage(reader.getPage(page))
            else:
                pass

            with open("page_nine.pdf", "wb") as f2:
                writer.write(f2)

def pageten():
    os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads")
    pages = [9]

    with open("Design.pdf", "rb") as f:
        reader = PdfFileReader(f)
        writer = PdfFileWriter()

        os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads\\Split")

        for page in range(len(reader.pages)):
            if page in pages:
                writer.addPage(reader.getPage(page))
            else:
                pass

            with open("Specsheet.pdf", "wb") as f2:
                writer.write(f2)

def pageeleven():
    os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads")
    pages = [10]

    with open("Design.pdf", "rb") as f:
        reader = PdfFileReader(f)
        writer = PdfFileWriter()

        os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads\\Split")

        for page in range(len(reader.pages)):
            if page in pages:
                writer.addPage(reader.getPage(page))
            else:
                pass

            with open("page_eleven.pdf", "wb") as f2:
                writer.write(f2)

def pagetwelve():
    os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads")
    pages = [11]

    with open("Design.pdf", "rb") as f:
        reader = PdfFileReader(f)
        writer = PdfFileWriter()

        os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads\\Split")

        for page in range(len(reader.pages)):
            if page in pages:
                writer.addPage(reader.getPage(page))
            else:
                pass

            with open("page_twelve.pdf", "wb") as f2:
                writer.write(f2)

def pagethirteen():
    os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads")
    pages = [12]

    with open("Design.pdf", "rb") as f:
        reader = PdfFileReader(f)
        writer = PdfFileWriter()

        os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads\\Split")

        for page in range(len(reader.pages)):
            if page in pages:
                writer.addPage(reader.getPage(page))
            else:
                pass

            with open("page_thirteen.pdf", "wb") as f2:
                writer.write(f2)

def pagefourteen():
    os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads")
    pages = [13]

    with open("Design.pdf", "rb") as f:
        reader = PdfFileReader(f)
        writer = PdfFileWriter()

        os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads\\Split")

        for page in range(len(reader.pages)):
            if page in pages:
                writer.addPage(reader.getPage(page))
            else:
                pass

            with open("page_fourteen.pdf", "wb") as f2:
                writer.write(f2)

def pagefifteen():
    os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads")
    pages = [14]

    with open("Design.pdf", "rb") as f:
        reader = PdfFileReader(f)
        writer = PdfFileWriter()

        os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads\\Split")

        for page in range(len(reader.pages)):
            if page in pages:
                writer.addPage(reader.getPage(page))
            else:
                pass

            with open("page_fifteen.pdf", "wb") as f2:
                writer.write(f2)

def pagesixteen():
    os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads")
    pages = [15]
    
    with open("Design.pdf", "rb") as f:
        reader = PdfFileReader(f)
        writer = PdfFileWriter()

        os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads\\Split")

        for page in range(len(reader.pages)):
            if page in pages:
                writer.addPage(reader.getPage(page))
            else:
                pass

            with open("page_sixteen.pdf", "wb") as f2:
                writer.write(f2)

def pageseventeen():
    os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads")
    pages = [16]

    with open("Design.pdf", "rb") as f:
        reader = PdfFileReader(f)
        writer = PdfFileWriter()

        os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads\\Split")

        for page in range(len(reader.pages)):
            if page in pages:
                writer.addPage(reader.getPage(page))
            else:
                pass

            with open("page_seventeen.pdf", "wb") as f2:
                writer.write(f2)

def pageeightteen():
    os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads")
    pages = [17]

    with open("Design.pdf", "rb") as f:
        reader = PdfFileReader(f)
        writer = PdfFileWriter()

        os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads\\Split")

        for page in range(len(reader.pages)):
            if page in pages:
                writer.addPage(reader.getPage(page))
            else:
                pass

            with open("page_eightteen.pdf", "wb") as f2:
                writer.write(f2)

def pagenineteen():
    os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads")
    pages = [18]

    with open("Design.pdf", "rb") as f:
        reader = PdfFileReader(f)
        writer = PdfFileWriter()

        os.chdir(f"C:\\Users" + "\\" + user + "\\Downloads\\Split")

        for page in range(len(reader.pages)):
            if page in pages:
                writer.addPage(reader.getPage(page))
            else:
                pass

            with open("page_nineteen.pdf", "wb") as f2:
                writer.write(f2)

def main():
    pageone()
    pagetwo()
    pagethree()
    pagefour()
    pagefive()
    pagesix()
    pageseven()
    pageeight()
    pagenine()
    pageten()
    pageeleven()
    pagetwelve()
    pagethirteen()
    pagefourteen()
    pagefifteen()
    pagesixteen()
    pageseventeen()
    pageeightteen()
    pagenineteen()

if __name__ == '__main__':
    main()