# 📘 PDF Index Generator

A Python tool to automatically generate an **Index / Table of Contents (TOC)** page for any existing PDF.  
It inserts a new first page listing **chapter names and page numbers**, and also creates **clickable sidebar bookmarks** in the output PDF.

---

## 🚀 Features

- 🧾 Adds an **Index page** at the beginning of your PDF  
- 🔖 Creates **sidebar bookmarks** (clickable in any PDF viewer)  
- 📄 Automatically adjusts page numbering  
- ⚙️ Simple configuration with a single `chapter_map` array  
- ✅ Works with any existing PDF (reports, books, notes, etc.)

---

## 📂 Project Structure

pdf-index-generator/
│
├── pdf_with_index_bookmarks.py # Main Python script
├── input.pdf # Your source PDF file
├── output_with_index.pdf # Generated output file (after running script)
└── README.md # This documentation


---

## 🧰 Requirements

### 🐍 Python Version
- Python **3.8 or higher**

### 📦 Install Dependencies
Run the following command in your terminal:

```bash
pip install PyPDF2 reportlab
```

These libraries are required for:

PyPDF2: Reading, merging, and bookmarking PDFs

reportlab: Generating the Index (TOC) page

⚙️ How to Use
1️⃣ Place Your Input PDF

Copy your source file into the same folder and rename it to:

input.pdf


(You can change this name in the script if needed.)

2️⃣ Edit Chapter–Page Mapping

Open pdf_with_index_bookmarks.py and edit this section:

chapter_map = [
    ("Introduction", 1),
    ("Getting Started", 5),
    ("Variables and Data Types", 12),
    ("Control Flow", 25),
    ("Functions", 38),
    ("OOP Concepts", 50),
    ("Modules and Packages", 65),
    ("File Handling", 78),
    ("Error Handling", 90),
    ("Conclusion", 100)
]


Each tuple is (Chapter Name, Page Number in Original PDF).

✅ Example:
If your PDF’s chapter “Functions” starts on page 38, you just write:

("Functions", 38)

3️⃣ Run the Script
python pdf_with_index_bookmarks.py

4️⃣ Output

After running, a new file will appear:

output_with_index.pdf


This PDF will have:

A first page with a formatted Table of Contents

All original pages preserved

A sidebar panel (bookmarks) with clickable chapters