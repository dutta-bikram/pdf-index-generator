# filename: pdf_with_index_bookmarks.py

from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import io

input_pdf = "input.pdf"
output_pdf = "output_with_index.pdf"

chapter_map = [
    ("Data Structures & Algorithms", 1),
    ("Mathematics for IT-I", 2),
    ("Database Management Systems ", 2),
    ("Object Oriented Programming", 3),
    ("Computer Organization and Architecture", 3),
    ("Object Oriented Systems ", 6),
    ("Mathematics for IT-II ", 7),
    (" Software Engineering ", 8),
    ("Graph Theory and Combinatorics ", 8),
    ("Computer Networks ", 9),
    ("Graphics and Geometric Modeling ", 10),
    ("------------3RD YEAR-----------------------", 11),
    ("Cloud Computing ", 11),
    ("Sensor Networks ", 12),
    ("Artificial Intelligence ", 13),
    ("Wireless and Mobile Networks ", 13),
    ("Web Technologies – I ", 13),
    ("Automata and  Compiler ", 14),
    ("Operating Systems ", 15),
    ("Design & Analysis of Algorithms ", 17),
    ("Information Security", 18),
    ("Web Technologies – II", 18),
    ("Multimedia Coding and Communications", 19),
    ("Soft Computing ", 19),
    ("Big Data ", 20),
    ("Mobile Applications Development ", 21),
    ("-----------4TH YEAR------------------------", 23),
    ("Machine Learning ", 23),
    ("Data Warehousing and Data Mining ", 24),
    ("IoT and Next Generation Networks", 25),
    ("Bio-Informatics", 25),
    ("Distributed Computing ", 26),
    ("Network Security ", 26),
    ("Data Science ", 28),
    ("Management ", 29),
    ("Pattern Recognition and Applications ", 29),
    ("NLP and Text Mining", 30),
    ("Cyber Forensics and Security", 31),
    ("Digital Image Processing", 32),
    ("Comprehensive Viva Voce", 32)
]

# Step 1: Create an index page (simple, no internal hyperlinks)
packet = io.BytesIO()
c = canvas.Canvas(packet, pagesize=A4)
c.setFont("Helvetica-Bold", 16)
c.drawString(200, 800, "Index / Table of Contents")

c.setFont("Helvetica", 12)
y = 760
lines_per_page = 35
line_count = 0

index_pages = (len(chapter_map) // lines_per_page) + 1

for chapter, page in chapter_map:
    adjusted_page = page + index_pages
    c.drawString(50, y, f"{chapter} ........ {adjusted_page}")
    y -= 20
    line_count += 1
    if line_count >= lines_per_page:
        c.showPage()
        c.setFont("Helvetica", 12)
        y = 800
        line_count = 0

c.save()
packet.seek(0)

# Step 2: Merge with the original PDF
index_pdf = PdfReader(packet)
reader = PdfReader(input_pdf)
writer = PdfWriter()

# Add index pages first
for p in index_pdf.pages:
    writer.add_page(p)

# Add all pages from the original
for page in reader.pages:
    writer.add_page(page)

# Step 3: Add bookmarks (visible in sidebar)
for chapter, page in chapter_map:
    adjusted_page = page + index_pages - 1  # zero-based
    writer.add_outline_item(chapter, adjusted_page)

# Step 4: Write new PDF
with open(output_pdf, "wb") as f:
    writer.write(f)

print(f"✅ New PDF with index and sidebar bookmarks created: {output_pdf}")
