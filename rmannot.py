#!/usr/bin/env python
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import TextStringObject  # Import the text string PdfObject
import argparse

parser = argparse.ArgumentParser(
    prog='rmannot.py',
    description='removes annotations (comments) from a PDF file',
    epilog="No need to buy license of Adobe Acrobat Pro for doing that :).\nGenerated by Masoud Ghaderi Zefreh for personal use",
    formatter_class=argparse.RawDescriptionHelpFormatter
)
parser.add_argument('-i','--input', help="input file")
parser.add_argument('-o','--output', help="output file (can be empty for default naming)", default=None)
args = parser.parse_args()
if args.output is None:
    args.output = str.split(args.input,'.')[-2]+'_anonymised.pdf'
input_pdf = args.input
output_pdf = args.output
reader = PdfReader(input_pdf)
writer = PdfWriter()

for page in reader.pages:
    # Check for annotations on the page.
    if "/Annots" in page:
        annots = page["/Annots"]
        for annot in annots:
            # Resolve the annotation reference, if necessary.
            annot_obj = annot.get_object()
            if "/T" in annot_obj:
                # Replace the author field with "Anonymous" (or blank)
                annot_obj.update({"/T": TextStringObject("Anonymous")})
    writer.add_page(page)

with open(output_pdf, "wb") as fp:
    writer.write(fp)