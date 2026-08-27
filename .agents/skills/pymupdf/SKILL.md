---
name: pymupdf
description: >-
  PyMuPDF (fitz) PDF processing skill. Extract text, tables, images, metadata,
  render PDF pages to PNG/JPEG images, split/merge PDFs, search text, and analyze PDF layout.
---

# PyMuPDF (fitz) PDF Processing Skill

This skill enables the agent to process, extract, render, merge, split, and analyze PDF documents using the high-performance Python package `pymupdf` (`import fitz`).

---

## 1. Extracting Text from PDF Files

To extract text page-by-page or save it to Markdown / TXT:

```python
import fitz # PyMuPDF

doc = fitz.open("input.pdf")
full_text = []

for page_num in range(len(doc)):
    page = doc[page_num]
    text = page.get_text("text") # Options: "text", "blocks", "words", "html", "json"
    full_text.append(f"--- Page {page_num + 1} ---\n{text}")

output_text = "\n\n".join(full_text)
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(output_text)
```

---

## 2. Rendering PDF Pages to Images (PNG/JPEG)

Convert PDF pages into high-quality images (useful for previewing worksheets, teaching slides, or embedded graphics):

```python
import fitz

doc = fitz.open("input.pdf")
zoom = 2.0 # 2.0x zoom = ~150-200 DPI for high quality
mat = fitz.Matrix(zoom, zoom)

for page_num in range(len(doc)):
    page = doc[page_num]
    pix = page.get_pixmap(matrix=mat, alpha=False)
    pix.save(f"page_{page_num + 1}.png")
```

---

## 3. Extracting Embedded Images from PDF

Extract all raw images embedded inside a PDF:

```python
import fitz, os

doc = fitz.open("input.pdf")
os.makedirs("extracted_images", exist_ok=True)

image_count = 0
for page_num in range(len(doc)):
    page = doc[page_num]
    image_list = page.get_images(full=True)
    for img_index, img in enumerate(image_list):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        image_filename = f"extracted_images/page{page_num + 1}_img{img_index + 1}.{image_ext}"
        with open(image_filename, "wb") as f:
            f.write(image_bytes)
        image_count += 1

print(f"Extracted {image_count} images.")
```

---

## 4. Merging Multiple PDFs or Splitting PDF Pages

Merge multiple PDF files into a single PDF:

```python
import fitz

merged_doc = fitz.open()

pdf_files = ["doc1.pdf", "doc2.pdf"]
for pdf_file in pdf_files:
    sub_doc = fitz.open(pdf_file)
    merged_doc.insert_pdf(sub_doc)
    sub_doc.close()

merged_doc.save("merged_output.pdf")
merged_doc.close()
```

Split specific page range (e.g. pages 1 to 5):

```python
import fitz

doc = fitz.open("input.pdf")
new_doc = fitz.open()
new_doc.insert_pdf(doc, from_page=0, to_page=4) # 0-indexed (pages 1-5)
new_doc.save("split_pages_1_to_5.pdf")
new_doc.close()
```

---

## 5. Searching Text & Extracting Bounding Boxes

Locate specific keywords or text snippets in a PDF:

```python
import fitz

doc = fitz.open("input.pdf")
search_term = "學習單"

for page_num in range(len(doc)):
    page = doc[page_num]
    text_instances = page.search_for(search_term)
    if text_instances:
        print(f"Found '{search_term}' on Page {page_num + 1} at rects: {text_instances}")
```
