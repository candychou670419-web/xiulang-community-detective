import fitz  # PyMuPDF
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== Reading 台灣教育雙月刊2021年12月第732期-吳淑芳校長.pdf ===")
try:
    pdf_doc = fitz.open('台灣教育雙月刊2021年12月第732期-吳淑芳校長.pdf')
    print(f"Total PDF Pages: {len(pdf_doc)}")
    for i in range(len(pdf_doc)):
        print(f"\n--- Page {i+1} ---")
        print(pdf_doc[i].get_text("text"))
except Exception as e:
    print(f"PDF error: {e}")
