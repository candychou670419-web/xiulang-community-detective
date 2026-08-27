import fitz
import sys
import zipfile
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')

print("=== Reading PDF Pages 5 to 13 ===")
pdf_doc = fitz.open('學生主體性彰顯的學共課堂_內觀人員的課例研究_周尚枚.pdf')
for i in range(4, len(pdf_doc)):
    print(f"\n--- Page {i+1} ---")
    print(pdf_doc[i].get_text("text"))

print("\n=== Trying raw docx extract for 學習共同體公開課的實踐歷程-周尚枚.docx ===")
try:
    with zipfile.ZipFile('學習共同體公開課的實踐歷程-周尚枚.docx', 'r') as z:
        xml_content = z.read('word/document.xml')
        tree = ET.fromstring(xml_content)
        texts = [node.text for node in tree.iter() if node.text]
        full_text = "".join(texts)
        print(f"Extracted length: {len(full_text)}")
        print(full_text[:1000])
except Exception as e:
    print(f"Docx zip extract error: {e}")
