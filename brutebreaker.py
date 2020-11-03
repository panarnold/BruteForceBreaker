#! brutebreaker.py - script responsible for breaking simple passwords of encrypted PDF made of simple word
# from english dictionary. It searches .pdf files only from cwd and its subdirectories.
# USAGE: cmd: python brutebreaker.py [pdfnamewithextension.pdf]
# X 2020 Arnold Cytrowski

import PyPDF2, os, sys

pdf_files = {}

for folder_name, subfolders, filenames in os.walk(os.path.abspath('.')):
    for filename in filenames:
        if filename.endswith('.pdf'):
            pdf_files[filename] = os.path.join(folder_name, filename)


if len(sys.argv) !=2 and sys.argv[1] not in pdf_files.keys():
    print('ok, here is the usage, once again, dummy: python brutebreaker.py [pdfnamewithcorrectextension.pdf]')
    exit(0)

with open('dictionary.txt') as dictionary:
    words = dictionary.readlines()

    pdf_reader = PyPDF2.PdfFileReader(open(sys.argv[1], 'rb'))

    if not pdf_reader.isEncrypted:
        print(f'Don\'t you worry: {sys.argv[1]} is\'nt really encrypted')
        exit(0)

    else:
        for word in words:
            word = word.strip()
            lower = word.lower()
            upper = word.upper()

            if pdf_reader.decrypt(lower) == 1:
                print(f'current password is "{lower}"')
                exit(0)
            if pdf_reader.decrypt(upper) == 1:
                print(f'current password is "{upper}"')
                exit(0)

    