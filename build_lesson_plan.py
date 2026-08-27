import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ALIGN_VERTICAL, WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import qn, nsdecls
import os

os.makedirs('output', exist_ok=True)
doc = docx.Document()

# Set margins to 0.75 inch
for section in doc.sections:
    section.top_margin = Inches(0.75)
    section.bottom_margin = Inches(0.75)
    section.left_margin = Inches(0.75)
    section.right_margin = Inches(0.75)

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=120, bottom=120, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_table_borders(table, color="B0C4DE", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'<w:tblBorders {nsdecls("w")}><w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/><w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/><w:left w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/><w:right w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/><w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/><w:insideV w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/></w:tblBorders>')
    tblPr.append(borders)

# Title 1
p1 = doc.add_paragraph()
p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
r1 = p1.add_run('新北市學習共同體 coach 領導人公開課磨課教學設計')
r1.font.name = '標楷體'
r1._element.rPr.rFonts.set(qn('w:eastAsia'), '標楷體')
r1.font.size = Pt(16)
r1.font.bold = True
r1.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)

# Title 2
p2 = doc.add_paragraph()
p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
r2 = p2.add_run('國小國語／閱讀理解——《511閱讀：言外之意與文本深層理解》')
r2.font.name = '微軟正黑體'
r2._element.rPr.rFonts.set(qn('w:eastAsia'), '微軟正黑體')
r2.font.size = Pt(13)
r2.font.bold = True
r2.font.color.rgb = RGBColor(0x2E, 0x75, 0xB6)
p2.paragraph_format.space_after = Pt(12)

# Table 1: Main Metadata Table
table1 = doc.add_table(rows=8, cols=4)
table1.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(table1)

data_rows = [
    ("單元\n學習目標", "文章觀念：理解文本中言語的「言外之意」與「弦外之音」，透過句子標點、段落關係釐清作者隱含意圖。\n文章思維：鼓勵學生自行細讀思考，再透過小組比較不同讀題觀點，引導發現文本寫作脈絡與邏輯。\n閱讀活動：\n1. 引導學生細細讀題三次，進行關鍵訊息圈畫與編號 (1, 2, 3, 4)。\n2. 進行 4 人小組組內共學與互幫互學 (Help-seeking)，找出文本中困難字詞與言外之意。\n3. 利用「字詞難關標記」與 A3 學習單進行組間對話與發表。\n4. 結合生活經驗與想像，將文字表徵轉化為具體心像。\n態度與責任：經歷自主探索閱讀，學習傾聽同儕意見、勇敢表達疑惑並協助解答，養成主動互學態度。"),
    ("核心素養", "國-E-A3 能觀察出日常生活問題與文本的關聯，並能嘗試擬定閱讀解題計畫，將閱讀理解應用於生活。\n國-E-C1 具備從證據討論事情，以及和他人有條理溝通的態度。\n國-E-C2 樂於與他人合作解決問題並尊重不同的問題解決想法。"),
    ("學習表現", "5-III-1 能運用不同的閱讀策略，擷取大意、摘要重點，並推論文本的隱含意義與言外之意。\n5-III-2 能在討論中傾聽他人發言，回應觀點並表達自己的理解。"),
    ("學習內容", "Ad-III-1 篇章大意、主旨與文章結構分析。\nBa-III-1 順敘、倒敘與回憶法之表達效果。\nCc-III-1 文本中各類修辭與文字意象（如譬喻、擬人、言外之意）之理解與轉化。"),
    ("學習目標", "1. 能覺察文本佈題情境，指出條件語句與核心問題，進行關係性理解，讀懂題意並進行文字轉譯。\n2. 透過與夥伴的對話（組內共學/組間互學），發現文本中字詞與意象的關聯，挑戰深層閱讀理解，成功解題並檢驗合理性。"),
    ("學習單元\n核心概念", "單元一 課堂約定與讀題轉譯：建立 4 人小組傾聽、求助 (Help-seeking) 與細讀三次標註策略。\n單元二 言外之意與詞句難關：標記文本困難字詞，辨析文字背後的隱含意圖與心理感受。\n單元三 結構推論與文本對話：分析文本順序（如倒敘/回憶法）與修辭法，完成併式/閱讀解題。"),
    ("教材來源", "115.05.21 國小五年級 511 閱讀公開課錄影（周尚枚老師觀課磨課教案設計）"),
    ("教學活動設計", "教學活動設計")
]

for r_idx, (label, val) in enumerate(data_rows):
    row_cells = table1.rows[r_idx].cells
    row_cells[0].text = label
    # Merge cells 1, 2, 3 for wide value column
    a = row_cells[1]
    b = row_cells[2]
    c = row_cells[3]
    a.merge(b).merge(c)
    a.text = val
    
    set_cell_background(row_cells[0], 'F2F2F2')
    set_cell_margins(row_cells[0], top=100, bottom=100, left=120, right=120)
    set_cell_margins(a, top=100, bottom=100, left=120, right=120)
    
    p0 = row_cells[0].paragraphs[0]
    p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in p0.runs:
        run.font.name = '微軟正黑體'
        run._element.rPr.rFonts.set(qn('w:eastAsia'), '微軟正黑體')
        run.font.bold = True
        run.font.size = Pt(10.5)
        
    p1 = a.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.LEFT
    for run in p1.runs:
        run.font.name = '微軟正黑體'
        run._element.rPr.rFonts.set(qn('w:eastAsia'), '微軟正黑體')
        run.font.size = Pt(10)

doc.add_paragraph().paragraph_format.space_after = Pt(10)

# Section 2: Detailed Learning Activities Table
p_act = doc.add_paragraph()
r_act = p_act.add_run('二、 學習共同體公開課教學活動歷程設計')
r_act.font.name = '微軟正黑體'
r_act._element.rPr.rFonts.set(qn('w:eastAsia'), '微軟正黑體')
r_act.font.size = Pt(13)
r_act.font.bold = True
r_act.font.color.rgb = RGBColor(0x2E, 0x75, 0xB6)

table2 = doc.add_table(rows=4, cols=4)
table2.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(table2)

# Table 2 Header
t2_headers = ['活動名稱與布題內容', '評量重點與活動類型', '學習共同體核心任務與引導歷程', '評量方式與重點']
hdr2_cells = table2.rows[0].cells
for i, h in enumerate(t2_headers):
    hdr2_cells[i].text = h
    set_cell_background(hdr2_cells[i], 'D9E1F2')
    set_cell_margins(hdr2_cells[i], top=120, bottom=120, left=100, right=100)
    p = hdr2_cells[i].paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in p.runs:
        run.font.name = '微軟正黑體'
        run._element.rPr.rFonts.set(qn('w:eastAsia'), '微軟正黑體')
        run.font.bold = True
        run.font.size = Pt(10.5)

activities_data = [
    (
        "活動一：課堂約定與讀題轉譯\n（時間：10分鐘）\n\n【布題情境】\n發下文本閱讀學習單，進行學習共同體 4 人小組編制（分 ABCD 角色）。\n\n【閱讀挑戰】\n1. 建立課堂四項約定：很會聽、勇於求助 (Help-seeking)、願意教人、全班展現默契。\n2. 執行「細細地讀三次」閱讀策略。",
        "課前破冰\n約定建立\n讀題轉譯",
        "核心任務：建立課堂默契，學會細讀與訊息劃記\n\n1. 師：說明課堂四大約定：(1) 很會聽夥伴說話；(2) 有問題勇於發問與求助；(3) 已經懂的人願意教同學；(4) 全班變成最有默契的學習共同體。\n2. 師：發下學習單，請同學「細細地讀三次」。遇到困難或不理解的地方，不要閃躲，直接用彩色筆劃線標記。\n3. 師：請同學在題目的重要訊息前圈選並標記編號 1、2、3、4...，用自己的話轉譯題目重點。\n4. 學生組內互學：檢查彼此劃記與理解是否一致。",
        "評量方式：\n學習單劃記\n口頭發表\n\n評量重點：\n檢視學生是否能落實細讀三次、圈劃關鍵訊息並與組員對話。"
    ),
    (
        "活動二：困難字詞與「言外之意」探究\n（時間：15分鐘）\n\n【布題情境】\n「文章中有些文字描寫不僅是字面意思，還藏著『言外之意』與『弦外之音』。請找出文中讓你覺得最困難或最有深意的句子。」\n\n【文本討論】\n例如：「好久好久以前發生的事...」這句話是針對前面的表情，還是後面的動作？",
        "文字意象\n言外之意\n組內共学",
        "核心任務：找出困難點與言外之意，進行深層推論\n\n1. 師：請同學在 4 人組內分享自己劃記的困難點。師：「困難的點不一定是你不會，而是容易忽略的言外之意。」\n2. 師：引導學生討論文本細節，例如討論描寫角色外貌或動作時隱含的心理狀態（如：為什麼角色會選擇留在原地？為什麼會朝向天空生長？）。\n3. 學生可能迷思：部分學生習慣停留在字面直譯，無法聯繫上下文的因果與心理脈絡。\n4. 互學機制：小組同學互相討論不同詮釋，修正自己的理解，並將小組 consensus 記錄在 A3 學習單上。",
        "評量方式：\nA3 小組學習單\n組內對話觀察\n\n評量重點：\n檢視學生是否能從字面深入推論「言外之意」，並與同儕溝通討論。"
    ),
    (
        "活動三：文章結構推論與組間互學發表\n（時間：18分鐘）\n\n【布題情境】\n「請找到文章第三段最後一句，並分析整篇文章的寫作順序（如倒敘法/回憶法）。主角的心境前後發生了什麼變化？」\n\n【綜合作答】\n完成 A3 學習單綜合挑戰題，準備組間發表。",
        "文章結構\n組間互學\n綜合發表",
        "核心任務：分析篇章結構，進行組間互學與分享\n\n1. 師：請各組找到第三段最後一句，討論：「這句話在說什麼？文章是順敘還是回憶以前的事？」\n2. 師發下 A3 選項學習單，請小組討論哪一個選項詮釋最正確，並說出正確理由與其他選項錯誤的理由。\n3. 組間發表與黑板紀錄：各組派代表展示 A3 學習單，分享對「主旨與言外之意」的理解。\n4. 師總結：肯定學生從同儕對話中修正想法，並連結生活經驗與閱讀素養。",
        "評量方式：\nA3 學習單\n組間發表\n黑板紀錄\n\n評量重點：\n檢視學生是否能運用併式與結構分析完整回答問題。"
    )
]

for row_idx, data in enumerate(activities_data):
    row_cells = table2.rows[row_idx + 1].cells
    for col_idx in range(4):
        row_cells[col_idx].text = data[col_idx]
        set_cell_margins(row_cells[col_idx], top=100, bottom=100, left=100, right=100)
        p = row_cells[col_idx].paragraphs[0]
        if col_idx in [0, 1, 3]:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        else:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        for run in p.runs:
            run.font.name = '微軟正黑體'
            run._element.rPr.rFonts.set(qn('w:eastAsia'), '微軟正黑體')
            run.font.size = Pt(9.5)

doc.add_paragraph().paragraph_format.space_after = Pt(10)

# Section 3: Comprehension Strategies & Partner Relationships
p_strat = doc.add_paragraph()
r_strat = p_strat.add_run('三、 融入之閱讀理解策略與學習共同體夥伴關係')
r_strat.font.name = '微軟正黑體'
r_strat._element.rPr.rFonts.set(qn('w:eastAsia'), '微軟正黑體')
r_strat.font.size = Pt(13)
r_strat.font.bold = True
r_strat.font.color.rgb = RGBColor(0x2E, 0x75, 0xB6)

table3 = doc.add_table(rows=4, cols=3)
table3.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(table3)

table3_data = [
    (
        "融入的理解策略",
        "1. 讀題轉譯：讀題三遍確認背景語句、條件語句與核心問題，並用自己的話說出來轉譯為解題結構。\n2. 背景知識：運用已有知識確認文本中的文法、修辭與背景脈絡。\n3. 關係性理解：透過比較與對照，處理條件語句間的關係與隱含意義。\n4. 說明順序：確認文章結構順序（順敘、倒敘、回憶法）與時空轉換關係。",
        "理解策略索引：\n1. 背景知識\n2. 轉譯\n3. 表徵\n4. 舉例理解\n5. 推論\n6. 摘要\n7. 順序 (sequence)\n8. 關係性理解\n9. 主旨\n10. 改寫 (paragraphing)"
    ),
    (
        "如何建立夥伴關係？",
        "1. 編碼學習：4 人小組分編 ABCD 角色，強調學習張力與互幫互學。\n2. 強調 Help-seeking：遇有不懂隨時向夥伴求助，被求助者樂意協助。\n3. 強調傾聽與紀錄：不強求個人主張，傾聽並記錄夥伴發言進行深度對話。",
        "對話引導語：\n引導語 1：請和小組夥伴分享自己的看法...\n引導語 2：你覺得這句話的言外之意是什麼？\n引導語 3：我和你的看法不太一樣，因為...\n引導語 4：我們可以怎麼修正這個答案？\n引導語 5：請試著幫同學說明這個難題..."
    ),
    (
        "評量方式說明",
        "1. 學習單與對話紀錄：能與夥伴轉譯並意義化文本句子的關係。\n2. 組內共學與組間互學：藉由同儕對題意與言外之意的詮釋，提高個人閱讀理解力與答對率。",
        "對應核心概念：\n每一個核心概念對應一個以上核心問題與閱讀任務。"
    ),
    (
        "備註",
        "本教學設計改編自周尚枚老師學習共同體 coach 領導人公開課觀課磨課架構，兼顧 108 課綱核心素養與 SLC 課例研究精神。",
        ""
    )
]

for row_idx, (c0, c1, c2) in enumerate(table3_data):
    row_cells = table3.rows[row_idx].cells
    row_cells[0].text = c0
    row_cells[1].text = c1
    row_cells[2].text = c2
    set_cell_background(row_cells[0], 'F2F2F2')
    for col_idx in range(3):
        set_cell_margins(row_cells[col_idx], top=100, bottom=100, left=100, right=100)
        p = row_cells[col_idx].paragraphs[0]
        if col_idx == 0:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        else:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        for run in p.runs:
            run.font.name = '微軟正黑體'
            run._element.rPr.rFonts.set(qn('w:eastAsia'), '微軟正黑體')
            if col_idx == 0:
                run.font.bold = True
                run.font.size = Pt(10)
            else:
                run.font.size = Pt(9.5)

output_path1 = 'output/511閱讀_尚枚老師公開課磨課教學設計.docx'
output_path2 = '511閱讀_尚枚老師公開課磨課教學設計.docx'
doc.save(output_path1)
doc.save(output_path2)
print(f"Successfully generated lesson plan docx: {output_path1} and {output_path2}")
