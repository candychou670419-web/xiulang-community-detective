import os
import base64
from PIL import Image

src_path = r'C:/Users/Chou Shang Mei/.gemini/antigravity/brain/10d52de2-2797-44f4-85b4-46b4127f4d28/.user_uploaded/media_1789885128728.png'
img = Image.open(src_path).convert('RGBA')

width, height = img.size
new_img = Image.new('RGBA', (width, height), (0, 0, 0, 0))

# Targeted pink color for "秀": Bright elegant pink #ec4899 / #f43f5e
# Target RGB for Pink: (244, 63, 94) or (236, 72, 153)
target_pink = (244, 63, 94) # Beautiful warm vibrant pink

pixels = img.load()
new_pixels = new_img.load()

for x in range(width):
    for y in range(height):
        r, g, b, a = pixels[x, y]
        
        # Determine background (navy blue: r < 40, g < 40, b < 70)
        # Background distance check
        if r < 50 and g < 50 and b < 80:
            new_pixels[x, y] = (0, 0, 0, 0) # Transparent
        elif r > 200 and g > 200 and b > 200:
            # White sun/ball dot
            new_pixels[x, y] = (255, 255, 255, 255)
        else:
            # Magenta "秀" glyph -> recolor to pink, keeping original brightness/alpha transition
            # Calculate intensity relative to magenta
            # Original magenta is around (192, 38, 211) or (160, 30, 120)
            brightness = (r * 0.3 + g * 0.29 + b * 0.41) / 255.0
            # Blend smoothly towards pink
            alpha_val = int(min(255, max(0, (r + b - g) * 1.5)))
            
            # Recolor glyph to pink (244, 63, 94) or (236, 72, 153)
            p_r = int(244 * (r / 190.0))
            p_g = int(75 * (r / 190.0) + g * 0.5)
            p_b = int(145 * (b / 190.0))
            
            p_r = min(255, max(0, p_r))
            p_g = min(255, max(0, p_g))
            p_b = min(255, max(0, p_b))
            
            new_pixels[x, y] = (p_r, p_g, p_b, 255 if r > 70 or b > 70 else alpha_val)

out_dir = r'g:/我的雲端硬碟/antigravity/123/output'
out_path1 = os.path.join(out_dir, 'xiulang_logo_pink.png')
out_path2 = r'g:/我的雲端硬碟/antigravity/123/xiulang_logo_pink.png'

new_img.save(out_path1, 'PNG')
new_img.save(out_path2, 'PNG')

with open(out_path1, 'rb') as f:
    b64_str = base64.b64encode(f.read()).decode('utf-8')
    data_url = f"data:image/png;base64,{b64_str}"

with open(os.path.join(out_dir, 'logo_base64.txt'), 'w', encoding='utf-8') as f:
    f.write(data_url)

print(f"Processed logo saved to {out_path1} and {out_path2}")
print(f"Base64 length: {len(data_url)}")
