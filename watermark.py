import pypdf
import sys
from os.path import splitext

watermark = sys.argv[1]
targetpdf = sys.argv[2:]

def imprint(water_mark , target_list):
    mark = pypdf.PdfReader(f"{watermark}").pages[0]
    counter = 1
    for pdfs in target_list:
        writer = pypdf.PdfWriter(clone_from= pdfs )
        for page in writer.pages:
            page.merge_page(mark, over = False)
        name = splitext(pdfs)[0]
        writer.write(f"{name}{counter}.pdf")
        counter += 1

imprint(watermark, targetpdf)

