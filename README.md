# 葉如凡｜企業溝通治理顧問

這是 [fanfanyeh.net](https://www.fanfanyeh.net/) 的 GitHub Pages 靜態備份專案。

## 網站內容

- 首頁
- CCOS 企業溝通營運系統
- 預防霸凌與溝通治理
- 洞察文章
- 關於如凡
- Email 洽詢頁面

原本依賴 Weebly 的聯絡表單已改為 `mailto:` Email 聯絡，不會蒐集或儲存訪客資料。

## 本機預覽

```bash
python3 -m http.server 8000 --directory docs
```

開啟 <http://localhost:8000/> 即可檢視。

## 部署

推送到 GitHub 的 `main` 分支後，GitHub Actions 會自動將 `docs/` 發佈到 GitHub Pages。

## 費用

本專案預定從私人儲存庫使用 GitHub Pages。GitHub Free 僅支援從公開儲存庫發佈 Pages；私人儲存庫需要 GitHub Pro、Team 或 Enterprise 等適用方案。若儲存庫屬於組織，應確認組織的 Team／Enterprise 方案及 Pages 發佈政策。自訂網域若沿用既有網域，另需負擔原網域註冊／續約費用。

私人儲存庫不代表網站本身是私人網站；一般 GitHub Pages 網站仍會公開。組織若要限制 Pages 網站的存取權限，需要 GitHub Enterprise Cloud 的私人發佈功能。
