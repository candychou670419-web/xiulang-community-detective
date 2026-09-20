import os

out_dir = r'g:/我的雲端硬碟/antigravity/123/output'
with open(os.path.join(out_dir, 'logo_base64.txt'), 'r', encoding='utf-8') as f:
    b64_logo = f.read().strip()

target_files = [
    os.path.join(out_dir, 'escape_room_game.html'),
    r'g:/我的雲端硬碟/antigravity/123/index.html'
]

# Set clean relative URL src="xiulang_logo_pink.png" with fallback onError to b64_logo
clean_img_tag = f'<img src="xiulang_logo_pink.png" style="height: 65px; width: auto; object-fit: contain; vertical-align: middle;" alt="秀朗校徽秀字" onerror="this.onerror=null;this.src=\'{b64_logo}\';">'

for file_path in target_files:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace any existing img tag with alt="秀朗校徽秀字"
        import re
        content = re.sub(
            r'<img src="[^"]*" style="height:\s*65px;[^"]*" alt="秀朗校徽秀字"[^>]*>',
            clean_img_tag,
            content
        )
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updated img src in HTML files with relative image file and Base64 fallback.")
