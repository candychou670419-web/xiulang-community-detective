---
name: escape-room-generator
description: >-
  國文閱讀理解密室逃脫網頁產生器 Skill。當使用者提到「建立密室逃脫網頁」、「將課文做成密室逃脫」、「國文密室逃脫」時觸發。
  自動將課文或題庫轉為雙關卡（5關/10關）、隨機抽題、等長防猜、漢字碎片收集、即時證書及 GitHub Pages 自動部署的線上解謎網頁。
---

# Skill 指南：國文閱讀理解密室逃脫網頁產生器

本檔案是一份 AI 執行指南（Skill File）。當使用者指示要建立「密室逃脫」網頁時，AI 必須讀取此指南並嚴格執行以下步驟。

---

## 觸發條件
當使用者提到「建立密室逃脫網頁」、「將課文做成密室逃脫」或「國文密室逃脫」時，啟動本 Skill。

---

## 執行流程

### 階段一：教材分析、風格建議與命名 (與使用者互動)
1. **分析教材**：
   * **情況 A**（已有題庫）：若教材檔案已包含題目、選項與解析，直接提取使用。
   * **情況 B**（僅有課文）：若教材檔案僅為課文，AI 必須根據課文內容，自動出題：
     * **Beginner 庫（16 題）**：著重課文大意、修辭、基本理解。
     * **Expert 庫（16 題）**：著重層次剖析、寫作架構、深層邏輯。
     * **注意**：每題提供 4 個選項（第 0 個固定為正確答案，寫網頁時隨機打亂），**必須增加錯誤選項的文字長度，使四個選項長度相當或錯誤選項更長**，防止學生以長度猜出答案。
2. **建議視覺風格與人物**：
   * 根據課文主旨，建議網頁主題色調（如黃金溫暖、翠綠竹林、黃昏夕陽等）與 CSS 天空漸層色值。
   * 建議適合放在右下角緩慢擺動的代表人物（如：〈謝天〉配愛因斯坦，請說明原因）。
3. **提供 GitHub 專案英文名稱**：
   * 依據課文英文意象，提供 3 個簡短、適合用作網址的英文 GitHub 專案名稱供使用者挑選（例如 `thanks-to-heaven-escape-room`）。
4. **回覆使用者**：將題目清單（如果是自動生成）、視覺與人物建議、以及 GitHub 專案名稱選項列出，**等待使用者確認專案名稱與上傳去背頭像圖片**。

---

### 階段二：等待使用者回覆與素材準備
1. 收到使用者挑選的專案名稱後，記錄為 `REPO_NAME`。
2. 收到使用者提供的人物圖片後，儲存至專案目錄的 `網頁/assets/img/character.png`。

---

### 階段三：建立網頁原始碼與資源配置
1. **建立專案結構**：在當前教材資料夾下，建立 `網頁/` 資料夾，並在其下建立以下檔案：
   * `網頁/index.html`（底下的網頁代碼模板）
   * `網頁/README.md`
   * `網頁/.gitignore`
   * `網頁/assets/img/`
   * `網頁/assets/audio/`
2. **複製音效範本**：
   * 從資源路徑複製 `Awards.m4a` 和 `Music_Trap_Drama.mp3` 到專案目錄的 `網頁/assets/audio/` 下。
3. **客製化 `index.html` 模板**：
   * 替換 CSS 變數（`--sky-top`, `--sky-mid`, `--sky-bot` 等）為建議的色系。
   * 修改首頁標題、課文簡介與浮動頭像圖片路徑（指向 `assets/img/character.png`）。
   * 移除 CSS 中的 `mix-blend-mode`，保存在所有瀏覽器上正確呈現去背人物。
   * 置入 `QDB` 題庫（Beginner + Expert 各 16 題）。
   * 自訂解鎖漢字碎片 `FRAGMENTS` 與通關密語 `PHRASES`。
   * 修改證書上的圓形印章字樣為「老師認證」（或依據課文自訂）。
   * 五關與十關的說明分別設定為「約 3 分鐘，輕鬆體驗」與「約 5 分鐘，完整挑戰」。

---

### 階段四：初始化 Git 與 GitHub Pages 自動部署
1. **初始化與提交**：
   在 `網頁/` 資料夾下，執行以下 Git 命令：
   ```powershell
   git init
   git branch -M main
   git config user.name "teacher"
   git config user.email "teacher@users.noreply.github.com"
   git add .
   git commit -m "Initialize <課文名稱> Escape Room Web Game"
   ```
2. **建立 GitHub 儲存庫**：
   使用 GitHub CLI 建立公開儲存庫並推上去：
   ```powershell
   gh repo create REPO_NAME --public --source=. --remote=origin --push
   ```
3. **啟用 GitHub Pages**：
   利用 API 指令一鍵啟用 Pages 網站服務：
   ```powershell
   @'
   {
     "source": {
       "branch": "main",
       "path": "/"
     }
   }
   '@ | gh api -X POST /repos/:owner/REPO_NAME/pages --input -
   ```
4. **輸出結果**：
   將 GitHub 專案網址與線上遊玩網址提供給使用者。
