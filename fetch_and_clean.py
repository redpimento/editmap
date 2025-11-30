import requests
import os

# -----------------------------
# 원본 URL → GitHub 업로드 파일명 매핑
# -----------------------------
files = {
    # happisoop
    "happisoop_cafe24sitemap.xml": "https://happisoop.cafe24.com/sitemap.xml",
    "happisoop_cafe24rss.xml": "https://happisoop.cafe24.com/rss.xml",
    
    # felicewald
    "felicewald_cafe24sitemap.xml": "https://felicewald.cafe24.com/sitemap.xml",
    "felicewald_cafe24rss.xml": "https://felicewald.cafe24.com/rss.xml",
    
    # boldogles
    "boldogles_cafe24sitemap.xml": "https://boldogles.cafe24.com/sitemap.xml",
    "boldogles_cafe24rss.xml": "https://boldogles.cafe24.com/rss.xml"
}

# -----------------------------
# 다운로드 + <script/> 제거 + 저장
# -----------------------------
for local_filename, url in files.items():
    try:
        print(f"Fetching {url} ...")
        r = requests.get(url)
        r.raise_for_status()  # HTTP 오류 시 예외 발생

        # <script/> 제거
        clean_text = r.text.replace("<script/>", "")

        # GitHub Pages 업로드용 로컬 저장 (editmap 폴더)
        folder = "editmap"
        os.makedirs(folder, exist_ok=True)
        filepath = os.path.join(folder, local_filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(clean_text)

        print(f"{filepath} saved successfully.")

    except Exception as e:
        print(f"Error fetching {url}: {e}")

print("All files processed successfully.")
