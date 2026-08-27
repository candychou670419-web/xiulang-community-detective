import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')
doc = docx.Document('coach 領導人公開課磨課教學設計_周尚枚1130919.docx')

table2 = doc.tables[1]
for r_idx in range(8):
    row = table2.rows[r_idx]
    cells = [c.text.strip().replace('\r', '') for c in row.cells]
    print(f"Row {r_idx}: {cells}")
