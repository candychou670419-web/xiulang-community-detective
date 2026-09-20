import os

out_dir = r'g:/我的雲端硬碟/antigravity/123/output'
with open(os.path.join(out_dir, 'logo_base64.txt'), 'r', encoding='utf-8') as f:
    b64_logo = f.read().strip()

target_files = [
    os.path.join(out_dir, 'escape_room_game.html'),
    r'g:/我的雲端硬碟/antigravity/123/index.html'
]

old_pattern = '<img src="" style="height: 65px; width: auto; object-fit: contain;" alt="秀朗校徽秀字">'
new_pattern = f'<img src="{b64_logo}" style="height: 65px; width: auto; object-fit: contain; vertical-align: middle;" alt="秀朗校徽秀字">'

for file_path in target_files:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if old_pattern in content:
            content = content.replace(old_pattern, new_pattern)
            print(f"Replaced empty src in {os.path.basename(file_path)}")
        elif 'alt="秀朗校徽秀字"' in content:
            import re
            content = re.sub(
                r'<img src="[^"]*" style="height:\s*65px;[^"]*" alt="秀朗校徽秀字">',
                new_pattern,
                content
            )
            print(f"Replaced pattern in {os.path.basename(file_path)}")
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

print("All files updated successfully.")
