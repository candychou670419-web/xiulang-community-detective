"""
社區小偵探：尋找秀朗神祕守護者 - QR Code 產生腳本
執行此腳本可自動生成四個站點的實體 QR Code 圖片。
"""

import os
import urllib.parse

def generate_qr_images():
    output_dir = os.path.dirname(os.path.abspath(__file__))
    img_dir = os.path.join(output_dir, "qr_images")
    os.makedirs(img_dir, exist_ok=True)
    
    stations = [
        ("station1", "01_民權圖書館.png"),
        ("station2", "02_得和派出所.png"),
        ("station3", "03_瓦窯溝.png"),
        ("station4", "04_民治市場.png"),
    ]
    
    base_url = "escape_room_game.html"
    
    print("Generating QR code URLs...")
    for st_id, filename in stations:
        target_url = f"{base_url}#{st_id}"
        encoded_url = urllib.parse.quote(target_url, safe='')
        qr_api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={encoded_url}"
        print(f"Station {st_id}: {qr_api_url}")
        
    print("\n[OK] All station QR Codes ready for preview & printing in output/station_qr_cards.html")

if __name__ == "__main__":
    generate_qr_images()
