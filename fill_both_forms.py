import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ALIGN_VERTICAL, WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import qn, nsdecls
import os

os.makedirs('output', exist_ok=True)

# ==========================================
# PART 1: 114教學省思心得紀錄表.docx
# ==========================================
doc1 = docx.Document('114教學省思心得紀錄表.docx')

# Paragraphs setup
doc1.paragraphs[1].text = "教學班級：五年11班              教   師：周尚枚"
doc1.paragraphs[2].text = "教學日期：113年6月4日         任教科目：國語／閱讀理解"
doc1.paragraphs[3].text = "教學單元：《511閱讀：言外之意與文本深層理解》"

for p in doc1.paragraphs[1:4]:
    for run in p.runs:
        run.font.name = '標楷體'
        run._element.rPr.rFonts.set(qn('w:eastAsia'), '標楷體')
        run.font.size = Pt(12)
        run.font.bold = True

t1 = doc1.tables[0]

# Ensure row 1..18 have '○' in column 2 (優良)
for r in range(1, 19):
    cells = t1.rows[r].cells
    cells[2].text = '○'
    p = cells[2].paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in p.runs:
        run.font.name = '微軟正黑體'
        run._element.rPr.rFonts.set(qn('w:eastAsia'), '微軟正黑體')
        run.font.size = Pt(12)

# Row 19: Reflection Text
reflection_text = """◎自我教學省思：

一、 課堂約定與常規建立 (Classroom Culture & Norms)
本節公開課成功建立「很會聽」、「勇於求助 (Help-seeking)」、「樂於教人」與「全班默契」四大約定。透過 4 人小組分工，學生能在安心的學習氛圍中開口，不再害怕面對閱讀或理解上的困難。當學生在閱讀文本遇到瓶頸時，能習慣拿起彩色筆劃記標註，並在組內向夥伴尋求支援，落實學習共同體互幫互學的核心精神。

二、 閱讀策略應用與深層理解 (Reading Strategies & Deep Comprehension)
課堂中推動「細細地讀三次」策略：第一遍掌握輪廓，第二遍摘要關鍵，第三遍圈畫重點訊息並編號 (1, 2, 3, 4)。在文字意象與言外之意探究活動中，學生能從「字面直譯」提升至對「弦外之音」與隱含心理的推論（如：推敲角色選擇留在原地的背後情感與時空倒敘寫作法）。透過 A3 學習單的多重選項討論，引導學生提出證據支撐觀點。

三、 學習共同體組內共學與組間對話 (SLC Group Learning & Discourse)
組內共學時，看見同儕間熱烈的討論與觀點撞擊。適時行間巡視並給予引導式提問，不直接給予標準答案，而是反問：「這句話是針對前面的表情，還是後面的動作？」促進學生自我修正與深度思考。組間發表時，各組能清楚說出選擇特定選項的理由與對其他選項的迷思辨析。

四、 未來教學調整與精進方向 (Future Teaching Enhancements)
1. 差異化適性支援：針對理解較慢或表達較內向的學生，可進一步設計提示卡 (Prompt Cards) 或組內角色輪替機制，確保每位孩子在組內都能獲得充分發言與思考的時間。
2. 文本表徵圖像化：未來可結合 AI 繪圖或視覺心像 (Mental Imagery) 工具，幫助學生將抽象的言外之意轉化為具體圖像，提升閱讀素養與跨領域學習遷移能力。

                                                                                     簽名：周尚枚"""

cell_r19 = t1.rows[19].cells[0]
cell_r19.text = reflection_text
p_r19 = cell_r19.paragraphs[0]
p_r19.alignment = WD_ALIGN_PARAGRAPH.LEFT
for run in p_r19.runs:
    run.font.name = '微軟正黑體'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '微軟正黑體')
    run.font.size = Pt(10.5)

doc1.save('output/114教學省思心得紀錄表.docx')
doc1.save('114教學省思心得紀錄表.docx')
print("Successfully updated 114教學省思心得紀錄表.docx")


# ==========================================
# PART 2: 114觀課紀錄表.docx
# ==========================================
doc2 = docx.Document('114觀課紀錄表.docx')

# Paragraph setup
if len(doc2.paragraphs) > 1:
    doc2.paragraphs[1].text = "觀課班級：五年11班    授課教師：周尚枚老師    觀課日期：113年6月4日    觀察者(簽名)：陳亮穎 老師"
    doc2.paragraphs[1].alignment = WD_ALIGN_PARAGRAPH.RIGHT
    for run in doc2.paragraphs[1].runs:
        run.font.name = '標楷體'
        run._element.rPr.rFonts.set(qn('w:eastAsia'), '標楷體')
        run.font.size = Pt(11)

t2 = doc2.tables[0]

# Fill qualitative narratives and ratings for indicators (Row 2 to Row 24)
qualitative_data = {
    "A-2-1": "能極精準掌握文本結構與段落脈絡，針對言外之意與修辭意象進行深層解析。",
    "A-2-2": "巧妙運用學生舊有的閱讀劃記技巧，延伸發展出「細細地讀三次」與訊息編號策略。",
    "A-2-3": "將閱讀理解連結學生生活體驗與AI視覺心像生成，讓文字意象變得具體生動。",
    "A-3-1": "開宗明義宣布課堂四大約定與學習目標，目標具體且非常符合五年級學童發展。",
    "A-3-2": "教學流程流暢，從課堂約定、個案細讀、組內共學到組間對話，結構極具條理。",
    "A-3-3": "對「言外之意」、「順敘與倒敘寫作法」等抽象語文概念講解極為清晰透徹。",
    "A-3-4": "設計高層次 A3 學習單與多重選項辨析任務，引導學生進行有意義的深度討論。",
    "A-4-1": "透過親切鼓勵與幽默對話，全程維持全班高度專注力與熱烈的探索動機。",
    "A-4-2": "靈活融合學習共同體 (SLC) 4人組內互學、組間分享與彩色筆標註等多重策略。",
    "A-4-3": "教學環節轉換自然順暢，時間掌握恰到好處，學習節奏明快。",
    "A-4-4": "口語極具親和力與渲染力，音量清晰，適時運用肢體語言與眼神進行眼神打招呼。",
    "A-4-5": "教師全程進行高品質行間巡視，精準掌握各組學習卡關點並給予對話引導。",
    "A-4-6": "善用彩色劃記標註、學習單與教具，創造視覺化與互動性極佳的學習環境。",
    "A-4-7": "發問具啟發性與層次感，常以「這句話是針對前面還是後面？」等反思問題引導學生思考。",
    "A-4-8": "時間掌控精準，各活動階段時間分配合理，流程推進明快緊湊。",
    "A-4-9": "課末統整要點，引導學生總結從同儕對話中所學到的閱讀理解法與言外之意解析。",
    "B-1-1": "班級常規優異，學生專注傾聽且能迅速切換個人細讀與小組討論模式。",
    "B-1-3": "善用口頭正向回饋與默契約定，有效建立榮譽感與同儕自律精神。",
    "B-1-4": "學生表現極為積極投入，無不當行為，展現極佳的學習自律。",
    "B-1-5": "能以平和且具智慧的態度回應學生的多元提問，迅速化解疑惑。",
    "B-2-2": "營造出高度安全、包容且充滿安全感的學習氣氛，學生樂於表達想法。",
    "B-2-3": "師生互動極為融洽，教師時常關心學生思考瓶頸，進行溫暖雙向溝通。",
    "B-2-4": "課堂空間與座位安排完全符合學習共同體 4 人小組互學之需求。"
}

# Row 2 to 24 mapping
for r in range(2, 25):
    cells = t2.rows[r].cells
    ref_code = cells[2].text.strip().split()[0] if cells[2].text.strip() else ""
    
    # Matching ref_code to qualitative_data
    text_to_fill = ""
    for code, narrative in qualitative_data.items():
        if code in cells[2].text:
            text_to_fill = narrative
            break
    if not text_to_fill:
        text_to_fill = "表現極佳，能有效落實教學目標與學習共同體互學精神。"

    # Set qualitative text in Col 3 (文字敘述)
    cells[3].text = text_to_fill
    p3 = cells[3].paragraphs[0]
    p3.alignment = WD_ALIGN_PARAGRAPH.LEFT
    for run in p3.runs:
        run.font.name = '微軟正黑體'
        run._element.rPr.rFonts.set(qn('w:eastAsia'), '微軟正黑體')
        run.font.size = Pt(9.5)

    # Set 'V' in Col 4 (優異)
    cells[4].text = "V"
    p4 = cells[4].paragraphs[0]
    p4.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in p4.runs:
        run.font.name = '微軟正黑體'
        run._element.rPr.rFonts.set(qn('w:eastAsia'), '微軟正黑體')
        run.font.size = Pt(11)
        run.font.bold = True

# Row 25: 觀課紀錄與綜合評語
obs_summary = """◎觀課綜合紀錄與建議：

【觀課整體亮點與優良事實】
1. 學習共同體靈魂落實：周尚枚老師在課堂開端即成功建立「傾聽、求助 (Help-seeking)、分享與默契」四大課堂約定。4 人小組互學機制極為成熟，學生遇到閱讀困難時能毫不猶豫向同儕發問，同儕亦能有耐心且具體地給予引導，真正達到「無一人落單 (No child left behind)」的學習共同體精神。
2. 高階閱讀策略實踐：透過「細細地讀三次」與「訊息畫線編號 1, 2, 3, 4」策略，成功引導學生從字面閱讀提升至「言外之意」與修辭意象的深層理解。課堂中學生能分析句子寫作順序（如倒敘法/回憶法）及隱含心理，表現出優異的文本對話力。
3. 高品質提問與行間巡視：授課教師行間巡視非常細緻，能精準捕捉各組卡關點，並以開放式引導提問（如：「你覺得這句話是針對前面還是後面？」）激發學生批判思考，而非直接告知答案。

【觀課建設性建議】
1. 延伸思考時間留白：在進行「言外之意」深度討論時，可適度延長小組組內沉思與個別紀錄的時間，讓較內向的學生有更充足的心智轉化空間。
2. 學習成果視覺化展示：在組間發表階段，若能運用數位載具或小白板將各組對言外之意的不同解構心像同時展示，將能創造更高層次的組間對話與觀點交鋒。

                                                                                     觀察者：陳亮穎 老師 (簽章)"""

cell_r25 = t2.rows[25].cells[0]
cell_r25.text = obs_summary
p_r25 = cell_r25.paragraphs[0]
p_r25.alignment = WD_ALIGN_PARAGRAPH.LEFT
for run in p_r25.runs:
    run.font.name = '微軟正黑體'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '微軟正黑體')
    run.font.size = Pt(10.5)

doc2.save('output/114觀課紀錄表.docx')
doc2.save('114觀課紀錄表.docx')
print("Successfully updated 114觀課紀錄表.docx")
