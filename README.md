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

舊文章的投影片圖片已保存於專案內，並改為可水平滑動的靜態圖庫；不再依賴 Weebly 投影片與留言服務。原 Weebly 文章網址也保留靜態轉址頁，避免既有外部連結立即失效。

## 本機預覽

```bash
python3 -m http.server 8000 --directory docs
```

開啟 <http://localhost:8000/> 即可檢視。

## 維護與檢查

重新整理原站備份後，可執行修復腳本下載文章圖片、移除 Weebly 留言與投影片依賴，並重建 SEO metadata、舊網址轉址及 sitemap：

```bash
python3 work/repair_static_site.py \
  --docs docs \
  --base-url https://jesuswaytaipeisrv.github.io/yeh/ \
  --download-images
```

提交前執行：

```bash
python3 work/check_static_site.py docs
bash -n work/prepare-static-site.sh
git diff --check
```

## 部署

推送到 GitHub 的 `main` 分支後，GitHub Actions 會自動將 `docs/` 發佈到 GitHub Pages。

- 正式網站：<https://jesuswaytaipeisrv.github.io/yeh/>
- GitHub 儲存庫：<https://github.com/jesuswaytaipeisrv/yeh>
- Sitemap：<https://jesuswaytaipeisrv.github.io/yeh/sitemap.xml>

## 費用

本專案使用公開 GitHub 儲存庫與 GitHub Pages，靜態網站託管費用為免費。自訂網域若沿用既有網域，另需負擔原網域註冊／續約費用。
