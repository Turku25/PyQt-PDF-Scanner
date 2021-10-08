# PyQt-PDF-Scanner
Python Qt application for scanning pages into a PDF on Linux
This was a project built in one week in order to learn Python and Qt. It's far from perfect, however it was a usefull learning tool. 

Dependencies:
  PyQt5 https://pypi.org/project/PyQt5/
  Sane https://github.com/python-pillow/Sane
  FPDF https://github.com/reingart/pyfpdf  (compile and install locally, the pip version has issues)
  PIL https://pypi.org/project/Pillow/

Areas for improvement:
  Add ability to rotate pages once they have already been scanned
  Add "maximize" feature to inspect single pages in as much detail as necessary
  Add OS abstractions for operating systems other than Linux
  Don't render any pages that are not within the bounds of the screen
