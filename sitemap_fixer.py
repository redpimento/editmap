import requests
import os

# 원본 URL과 저장할 GitHub 파일 이름 매핑
file_map = {
    "https://happisoop.cafe24.com/sitemap.xml": "happisoop_cafe24sitemap.xml",
    "https://felicewald.cafe24.com/sitemap.xml": "felicewald_cafe24sitemap.xml",
    "https://boldogles.cafe24.com/sitemap.xml": "boldogles_cafe24sitemap.xml",
    "https://happisoop.cafe24.com/rss.xml": "happisoop_cafe24rss.xml",
    "https://felicewald.cafe24.com/rss.xml": "felicewald_cafe24rss.xml",
    "https://boldogles.cafe24.com/rss.xml": "boldogles_cafe24rss.xml"
}

def fetch_and_fix_file():
    """각 URL에서 파일을 가져와 <script/> 태그를 제거하고 로컬에 저장합니다."""
    
    for original_url, target_filename in file_map.items():
        print(f"--- 처리 시작: {original_url} -> {target_filename} ---")
        
        try:
            # 1. 원본 파일 가져오기
            response = requests.get(original_url, timeout=10)
            response.raise_for_status() # HTTP 오류 발생 시 예외 발생
            
            content = response.text
            
            # 2. 내용 수정: <script/> 태그 제거
            fixed_content = content.replace('<script/>', '')
            
            # 3. 로컬 파일 저장
            # target_filename은 GitHub Repository의 루트 경로에 저장됩니다.
            with open(target_filename, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
                
            print(f"성공적으로 파일을 가져와 수정 후 저장했습니다.")
            
        except requests.exceptions.RequestException as e:
            print(f"파일 처리 중 오류 발생: {e}")
            
if __name__ == "__main__":
    fetch_and_fix_file()