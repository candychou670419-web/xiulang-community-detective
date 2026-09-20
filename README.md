# 社區小偵探：尋找秀朗神祕守護者｜國小二年級實境解謎互動課程

本專案專為**國小二年級學生**設計，結合情境故事、平板互動網頁與實體社區四個站點（民權圖書館、得和派出所、瓦窯溝、民治市場），讓學童透過掃描 QR Code 體驗互動式實境解謎遊戲。

---

## 🌐 部署與公開發布網址 (GitHub Pages)

- 🎮 **實境解謎互動遊戲主網頁**：[https://candychou670419-web.github.io/xiulang-community-detective/](https://candychou670419-web.github.io/xiulang-community-detective/)
- 🖨️ **實體站點 QR Code 任務海報卡**：[https://candychou670419-web.github.io/xiulang-community-detective/station_qr_cards.html](https://candychou670419-web.github.io/xiulang-community-detective/station_qr_cards.html)
- 📦 **GitHub 專案儲存庫**：[https://github.com/candychou670419-web/xiulang-community-detective](https://github.com/candychou670419-web/xiulang-community-detective)

---

## 🎮 遊戲與教材產出檔案

1. **實境解謎互動網頁**：[`output/escape_room_game.html`](file:///g:/%E6%88%91%E7%9A%84%E9%9B%B2%E7%AB%AF%E7%A1%AC%E7%A2%9F/antigravity/123/output/escape_room_game.html) （以及根目錄 [`index.html`](file:///g:/%E6%88%91%E7%9A%84%E9%9B%B2%E7%AB%AF%E7%A1%AC%E7%A2%9F/antigravity/123/index.html)）
   - 專為平板與手機觸控設計，支援雙體驗模式（QR Code 現場定點掃描 / 自由地圖切換）。
   - 內建語音朗讀（Web Speech API）、多感官音效、照片自動儲存及彩帶噴發動畫。
   - 包含【Show SMART】、【Show Better】、【立足本土】、【展望國際】四道關卡任務與數位榮譽證書。

2. **實體 QR Code 任務海報卡**：[`output/station_qr_cards.html`](file:///g:/%E6%88%91%E7%9A%84%E9%9B%B2%E7%AB%AF%E7%A1%AC%E7%A2%9F/antigravity/123/output/station_qr_cards.html) （以及根目錄 [`station_qr_cards.html`](file:///g:/%E6%88%91%E7%9A%84%E9%9B%B2%E7%AB%AF%E7%A1%AC%E7%A2%9F/antigravity/123/station_qr_cards.html)）
   - A4 雙欄列印格式，包含 4 站 QR Code、實地小偵探任務提示與教師安全常規提醒。
   - 支援線上與本機部署網址一鍵切換與列印。

3. **第一站照片備份資料夾**：[`output/station1_uploads/`](file:///g:/%E6%88%91%E7%9A%84%E9%9B%B2%E7%AB%AF%E7%A1%AC%E7%A2%9F/antigravity/123/output/station1_uploads/)

---

## 📚 四大站點遊戲設計對照表

| 節數 | 站點與主題 | 解謎任務與平板互動介面 | 學習目標與榮譽徽章 |
| --- | --- | --- | --- |
| **第一節** | **民權圖書館**<br>（好書閱讀） | **閱讀好書，拍照上傳**<br>挑選喜愛書籍安靜閱讀，由帶隊家長協助拍攝同學認真閱讀照片上傳，解鎖【Show SMART】徽章。照片自動下載備份至 `output`。 | **目標：** 養成閱讀習慣與自主學習。<br>**徽章：** 【Show SMART】 |
| **第二節** | **得和派出所**<br>（裝備配對） | **交通警察及刑警裝備配對**<br>辨識區分反光背心、測速照相機（交通警察）與採證箱、手銬（刑警），解鎖【Show Better】徽章。 | **目標：** 認識警察機關功能與警種分工。<br>**徽章：** 【Show Better】 |
| **第三節** | **瓦窯溝**<br>（生態探索） | **河畔生態 Bingo 卡**<br>3x3 九宮格觀察小白鷺、大公鵝、水質淨化設施等，點亮達成 2 條連線解鎖【立足本土】徽章。 | **目標：** 覺察社區生態與水資源保育。<br>**徽章：** 【立足本土】 |
| **第四節** | **民治市場**<br>（金錢運用） | **30元美食探險家**<br>買 15 元紅豆餅與 10 元冬瓜茶，於平板點選硬幣組合 5 元找零金額，解鎖【展望國際】徽章。 | **目標：** 體驗市場購物與面額加減算數。<br>**徽章：** 【展望國際】 |

---

## 📝 開發歷史 / Changelog

- **2026-08-27**
  - 完成專案初始化與 Git 版本控制建置。
  - 完成「社區小偵探：尋找秀朗神祕守護者」實境解謎互動網頁 (`escape_room_game.html`)。
  - 完成 4 站實體 QR Code 海報卡與 A4 列印排版系統 (`station_qr_cards.html`)。
- **2026-09-02**
  - 新增「國小低年級專屬可愛數字電子鐘 Desktop App」(`output/cute-lunch-clock/`)。
- **2026-09-20**
  - 獨立創建並發布專屬 GitHub Repository (`xiulang-community-detective`)，完全解決網址重疊問題。
  - 全面更新四大終極榮譽徽章名稱為：【Show SMART】、【Show Better】、【立足本土】、【展望國際】。
  - 更新第一站任務為「閱讀一本好書，拍照上傳」，支援照片自動下載儲存至 `output` 資料夾與匯出機制。
  - 更新第二站任務為「交通警察及刑警裝備配對大考驗」，提供動態配對卡牌。
  - 升級「數位榮譽證書」繪製與下載系統，支援實時圖像生成、長按儲存相簿、新分頁開啟全圖與 AirPrint 無線列印。
  - 精準去除秀朗校徽【秀】字暗藍背景，重構為粉紅色高畫質校徽圖樣，完美嵌入數位榮譽證書抬頭。
  - 全面修正為繁體中文正體標籤（如【已通關】）。
