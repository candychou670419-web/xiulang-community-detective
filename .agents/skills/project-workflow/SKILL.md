---
name: project-workflow
description: >-
  工作階段與專案收工自動化技能。當使用者說「開始工作」、「開工」、「開始」或「專案開始」時，檢查與初始化 Git、建立 output 資料夾及 .gitignore；
  當使用者說「結案」、「收工」、「專案結束」、「開發完成」、「結束」或「存檔並更新說明」時，自動更新 README.md 開發歷史並進行 Git Commit 存檔。
---

# 專案工作階段與收工自動化 Skill (Project Workflow Manager)

本 Skill 提供標準化的專案開始與收工流程自動化管理。

---

## 1. 觸發條件一：當使用者說「開始工作」、「開工」、「開始」或「專案開始」時

請依序執行以下步驟：

### 步驟 A：檢查並初始化 Git 版本控制
1. 執行 `git rev-parse --is-inside-work-tree` 檢查目前專案是否已建立 Git 倉庫。
2. 若尚未建立，執行 `git init` 初始化專案。

### 步驟 B：建立 `output` 資料夾
1. 檢查根目錄下是否有 `output` 資料夾，若無則建立。
2. 在 `output` 資料夾內建立 `.gitkeep` 檔案，確保 Git 能追蹤此資料夾。
3. **原則**：後續產生的報告、文件、圖片、資料表等產出物，優先存入 `output` 資料夾中。Git 版本控制必須涵蓋 `output` 資料夾。

### 步驟 C：檢查並建立 `.gitignore` 檔案
若專案根目錄缺乏 `.gitignore`，自動建立包含以下排除項目的 `.gitignore`：

```gitignore
# 敏感資訊與金鑰
.env
*.env.*
*.pem
*.key
secrets.json

# 系統與暫存檔
.DS_Store
Thumbs.db
desktop.ini
*.tmp
*.log

# Python
__pycache__/
*.py[cod]
*$py.class
.venv/
venv/
env/
.pytest_cache/
*.egg-info/

# Node.js
node_modules/
npm-debug.log*
yarn-error.log*
.next/
dist/

# IDE & 編輯器
.vscode/
.idea/
```

> **安全與規範提醒**：
> - 務必保留原始檔案，禁止直接覆寫或刪除原始資料。
> - 涉及刪除、移動、覆寫或執行外部破壞性指令時，請先說明影響並等待使用者明確確認。

---

## 2. 觸發條件二：當使用者說「結案」、「收工」、「專案結束」、「開發完成」、「結束」或「存檔並更新說明」時

請依序執行以下步驟：

### 步驟 A：檢查 Git 狀態
1. 執行 `git rev-parse --is-inside-work-tree`。若無 Git 倉庫，詢問使用者是否執行 `git init`。
2. 執行 `git status` 檢視未提交的變更與新增檔案。

### 步驟 B：自動建立 / 更新 `README.md`
1. 檢查專案根目錄是否有 `README.md`，若無則建立基礎結構。
2. 尋找 `## 開發歷史 / Changelog` 標題（若無則自動在檔尾建立）。
3. 追加當天日期（如：`### YYYY-MM-DD`）與今日工作成果條列摘要。

### 步驟 C：自動 Git Commit
1. 執行 `git add .` 將所有變更納入暫存區。
2. 執行 commit 指令：
   ```bash
   git commit -m "docs: 專案結束存檔，更新 README 說明文件"
   ```

### 步驟 D：回報存檔摘要
向使用者回報 Commit Hash、提交訊息內容以及 `README.md` 更新的摘要內容。
