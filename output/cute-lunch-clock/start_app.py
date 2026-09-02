import os
import sys
import webbrowser
import http.server
import socketserver
import threading

PORT = 8520
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def start_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

if __name__ == "__main__":
    print(f"啟動可愛數字電子鐘伺服器: http://localhost:{PORT}")
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()

    url = f"http://localhost:{PORT}/index.html"
    try:
        # 嘗試使用 Edge/ChromeApp 模式無邊框視窗開啟
        os.system(f'start msedge --app="{url}"')
    except Exception:
        webbrowser.open(url)

    print("電子鐘正在運行中，按下 Ctrl+C 結束。")
    try:
        server_thread.join()
    except KeyboardInterrupt:
        sys.exit(0)
