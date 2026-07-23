# 專案開發紀錄

## 2026-07-23

### Codex 複核與靜態備份完整化

- 重新核對已部署版本 `afcff671cd51e81f7c01cfb498f7498a2fba22af` 與 Claude 待修建議，發現原檢查沒有涵蓋 Weebly 投影片 JavaScript 內的圖片引用。
- 確認 11 個頁面含 149 個投影片引用（70 張不同圖片），GitHub Pages 實際會請求錯誤的主機根目錄 `/uploads/...`，抽樣回應 HTTP 404。
- 趁原 Weebly 網站仍可存取，將缺少的 70 張投影片圖片下載至 `docs/uploads/1/0/2/8/102844230/`；下載檔案經 `file` 檢查均為 PNG 圖片。
- 將 Weebly JavaScript 投影片改成使用本地圖片的水平滑動靜態圖庫，新增 `docs/files/static-overrides.css`，降低外部服務失效造成的內容缺漏。
- 將 12 個含查詢字串的圖片檔名正規化為標準 `.png`／`.jpg`，避免靜態主機以 `application/octet-stream` 回傳而影響瀏覽器顯示。
- 修正 19 篇文章與第 2 頁文章列表共 20 個格式錯誤的頁首背景網址；根因是原準備腳本只處理 `docs/*.html`，未遞迴處理文章子目錄。
- 移除 19 個 Weebly 留言輸入 iframe，保留既有留言顯示區並改為靜態停用提示與 Email 聯絡方式。
- 將 26 個正式頁面的 `og:url`、`og:image` 與 canonical 統一為目前 GitHub Pages 正式網址；所有 OG 圖片均改成本地檔案。
- 更新 37 個 Facebook 與 37 個 Twitter 舊文章分享網址，並建立 18 個 `/2/post/YYYY/MM/` 舊路徑靜態轉址頁。
- 新增含 25 個正式網址的 `docs/sitemap.xml`，並將 `docs/robots.txt` 更新為目前 sitemap 網址。
- 新增可重複執行的 `work/repair_static_site.py` 與 `work/check_static_site.py`，並串接 `work/prepare-static-site.sh`，避免日後重建恢復同類問題。
- 靜態驗證通過：26 個正式頁面各有一組 canonical、`og:url` 與本地覆寫樣式；所有本地 `src`／`href` 引用存在；表單、Weebly 留言、Weebly 投影片及錯誤背景網址均為 0。
- Python 語法檢查、Shell 語法檢查與 `git diff --check` 通過。
- 本機 HTTP smoke test 通過：首頁、文章列表、新舊文章、本地圖片、覆寫樣式、sitemap、robots.txt 與舊路徑轉址頁均回應 HTTP 200，正規化後的圖片回應正確圖片 MIME 類型。
- 嘗試進行自動化桌面／手機瀏覽器檢查，但目前執行環境沒有可用的瀏覽器實例；正式部署後仍需人工抽查桌面與手機排版。
- 修復 commit `8338001`（`完整化靜態網站圖片與舊網址`）已直接推送至 `origin/main`。
- GitHub Actions `Deploy GitHub Pages` run `30015886088` 已成功完成；正式站首頁、文章列表、舊文章、本地圖片、sitemap 與舊路徑轉址頁抽查均回應 HTTP 200，新增圖片回應 `image/png`。

### 初始建置與部署

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
- 已初始化本機 Git 儲存庫並建立 `main`，遠端設為私人儲存庫 `https://github.com/jesuswaytaipeisrv/yeh`；首個 commit 為 `57b8f5772ef728195965caad2af0131c99196c88`（`建立葉如凡靜態網站`），已成功推送。
- GitHub Actions `Deploy GitHub Pages #1`（run `30011028291`）已自動觸發但失敗；確認原因是儲存庫尚未啟用 Pages，而目前帳號方案的設定頁僅提供「升級方案或將儲存庫改為公開」兩種啟用方式。
- 目前儲存庫維持 private，未擅自改為 public、未開始付費升級，也尚未產生 GitHub Pages 正式網址；等待使用者決定升級 GitHub Pro 或改為公開儲存庫後再繼續部署。
- 使用者後續明確確認此儲存庫用於葉如凡網站，並完成 GitHub sudo mode 身分驗證；`jesuswaytaipeisrv/yeh` 已由 private 改為 public。
- GitHub Pages 已啟用，Build and deployment source 設為 GitHub Actions；依使用者要求先停在此階段，尚未重新執行失敗的 workflow 或驗證正式網址。
- 推送 commit `55cb77f58a13f02c63099dac4913184b19d2ebec`（`記錄公開 Pages 設定`）後，自動觸發 `Deploy GitHub Pages #2`（run `30011932199`），已於 25 秒內成功完成部署。
- 正式網站為 `https://jesuswaytaipeisrv.github.io/yeh/`；首頁、CCOS、霸凌預防、洽詢、洞察、關於頁，以及實際引用的背景圖、帶 `%3F` 檔名 CSS 與圖片皆回應 HTTP 200。
- 正式環境內容檢查通過：首頁與洽詢頁顯示 `mailto:` 聯絡方式，抽樣頁面未出現舊 Weebly 表單送出端點或可提交表單。
- 正式環境瀏覽器 smoke test 通過：桌面版顯示六個主要導覽連結；390 x 844 手機版顯示 Menu，展開後可由「洽詢服務」進入正式洽詢頁，Email 洽詢區塊正常顯示。
- 公開儲存庫搭配 GitHub Pages 的靜態託管費用為免費；若日後設定自訂網域，仍需負擔網域註冊或續約費用。

### 已知相依項目

- 文章投影片、投影片圖片與留言輸入功能已不再依賴 Weebly；版型的共用字型、CSS 與部分 JavaScript 仍由 Weebly 共用 CDN 載入，後續可再評估本地化與第三方資源授權。
- Facebook、LinkedIn、Instagram 等外部連結需連線至各自平台。
