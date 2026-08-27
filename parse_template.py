import docx
import sys

sys.stdout.reconfigure(encoding='utf-8')
doc = docx.Document('coach 領導人公開課磨課教學設計_周尚枚1130919.docx')

for i, table in enumerate(doc.tables):
    print(f"\n==================== TABLE {i+1} ====================")
    for r_idx, row in enumerate(table.rows):
        cells = [c.text.strip().replace('\n', ' | ') for c in row.cells]
        print(f"[R{r_idx}] {cells}")
