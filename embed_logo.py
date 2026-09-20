import os

out_dir = r'g:/我的雲端硬碟/antigravity/123/output'
with open(os.path.join(out_dir, 'logo_base64.txt'), 'r', encoding='utf-8') as f:
    b64_logo = f.read().trim() if hasattr(f.read(), 'trim') else f.read().strip()

target_file = os.path.join(out_dir, 'escape_room_game.html')
with open(target_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace certificate header to include the pink 秀 logo
old_header = '<div style="font-size: 3rem; margin-bottom: 4px;">🦉✨</div>\n      <div class="cert-header">秀朗社區小偵探 榮譽證書</div>'

new_header = f'''<div style="display:flex; align-items:center; justify-content:center; gap:14px; margin-bottom:10px;">
        <img src="{b64_logo}" style="height: 65px; width: auto; object-fit: contain;" alt="秀朗校徽秀字">
        <div style="font-size: 2.8rem;">🦉✨</div>
      </div>
      <div class="cert-header">秀朗社區小偵探 榮譽證書</div>'''

if old_header in html:
    html = html.replace(old_header, new_header)
    print("Replaced header in escape_room_game.html")
else:
    # Try alternative matching
    import re
    html = re.sub(
        r'<div style="font-size:\s*3rem; margin-bottom:\s*4px;">🦉✨</div>\s*<div class="cert-header">秀朗社區小偵探 榮譽證書</div>',
        new_header,
        html
    )
    print("Replaced header via regex in escape_room_game.html")

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated escape_room_game.html successfully")
