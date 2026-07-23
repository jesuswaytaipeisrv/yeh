# 專案開發紀錄

## 2026-07-23

- 建立 GitHub Pages 靜態網站專案。
- 以 `https://www.fanfanyeh.net/` 為來源，保存首頁、服務頁、洞察文章、關於頁與原站公開圖片素材。
- 修正頁首背景圖片路徑，使網站能從 GitHub 專案子路徑載入。
- 將原 Weebly 洽詢表單與 reCAPTCHA 替換成 Email 聯絡卡片。
- 將 Cloudflare 電子郵件保護連結改為 `mailto:eltha0122@gmail.com`。
- 加入 `.nojekyll` 與 GitHub Pages 自動部署工作流程。
- 保留準備腳本 `work/prepare-static-site.sh`，方便日後重新擷取與整理來源內容。
- 本機 HTTP 驗證通過：首頁、CCOS、霸凌預防、洽詢、洞察、關於頁、主要樣式與抽樣圖片皆回應 HTTP 200。
- 發佈前檢查發現目前環境未安裝 GitHub CLI (`gh`)；GitHub 儲存庫建立與推送待安裝並登入後續作業。
- 建立 `outputs/CODEX_CLI_HANDOFF.md`，完整記錄 Codex CLI 接手所需的專案背景、完成項目、阻塞狀態、GitHub 發佈流程、驗證要求與注意事項。
- Codex CLI 已重新讀取移交文件並核對專案內容；確認 `docs/` 靜態網站、GitHub Pages workflow 與交付 ZIP 均存在。
- 再次檢查仍顯示系統找不到 `gh`，因此尚未執行 Git 初始化、建立公開儲存庫、提交、推送或啟用 GitHub Pages，避免在未確認登入帳號前誤發佈。
- 使用者改為指定既有私人儲存庫 `https://github.com/jesuswaytaipeisrv/yeh` 作為推送目標；在 `gh` 安裝並完成登入前，尚無法驗證遠端內容、寫入權限與 GitHub Pages 方案資格。
- 成本注意：GitHub 官方目前僅在 GitHub Pro、Team 或 Enterprise 等付費方案支援私人儲存庫的 GitHub Pages；若 `jesuswaytaipeisrv` 是組織且使用 Free 方案，需改為公開儲存庫或升級組織方案後才能用 Pages 發佈。
- 使用標準 `git ls-remote` 成功確認指定遠端目前沒有任何 branch 或 commit，可安全建立首個版本，不需要依賴 GitHub CLI。
- 發佈前安全掃描發現 1 個課程洽詢表單及 21 個重複的電子報訂閱表單仍會向舊 Weebly 端點送出訪客資料；已改成靜態提示與 Email 聯絡方式，並同步更新 `work/prepare-static-site.sh`，避免重建時恢復外部表單。
- 調整 `.gitignore`：繼續忽略 `work/reference/` 原站擷取資料，但允許提交可重現整理流程的 `work/prepare-static-site.sh`。
- 靜態檢查通過：Weebly 表單送出端點、multipart 表單、GitHub Pages 不相容的網域根路徑及私鑰特徵均為 0 筆；重建腳本通過 `bash -n` 語法檢查。
- 更新後的本機 HTTP smoke test 通過：首頁、CCOS、霸凌預防、洽詢、洞察、關於頁、頁首背景圖、帶 `%3F` 檔名的 CSS 與圖片皆回應 HTTP 200；課程洽詢、電子報停用及 Email 洽詢提示均可讀取。

### 已知相依項目

- 版型的共用字型、CSS 與部分 JavaScript 仍由 Weebly 共用 CDN 載入；原站空間停用後，這些 Weebly 平台共用資源通常仍可使用。
- Facebook、LinkedIn、Instagram 等外部連結需連線至各自平台。
