"""Generates PDFs using a mail merge operation.

This program uses the data in output/data.xlsx to output PDFs and Word
documents based upon the Word template in template/Letter Template.docx
This can be modified to other needs.

  Prerequisites:

  A standard mail merge has to be set up in the Word template
  before running this program (https://www.youtube.com/watch?v=mFqCvTOpOL0)

  Typical usage example:

  pdf_generator = PDFGenerator()
  pdf_generator.start()

  Once started the template will open in Word and ask you
  to 'Select Table' click OK. There may be a slight delay
  during the first PDF but after that will output very fast

"""

from pdf_generator import PDFGenerator

if __name__ == '__main__':
    pdf_generator = PDFGenerator()
    pdf_generator.start()
