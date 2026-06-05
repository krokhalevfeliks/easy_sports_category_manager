from docx import Document

file = open(r"C:\Users\anaconda3\Predstavlenie_na_razryad_blank.docx", "r")
content = file.read()
file.close()

with open(r"C:\Users\anaconda3\Predstavlenie_na_razryad_blank.docx", "r") as f:
    result = Document.detect(f.read(10000))
    print(result['encoding'])  

#No module named 'docx'
