import argparse
import http.server
import os
import socketserver
import threading
import time
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()


class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


def run_server(port: int, open_browser: bool = True) -> None:
    with ReusableTCPServer(("127.0.0.1", port), NoCacheHandler) as httpd:
        httpd.timeout = 1
        url = f"http://127.0.0.1:{port}/"
        print("AI자력이탈감지 서버 시작")
        print(f"경로: {ROOT}")
        print(f"접속: {url}")
        print("종료: Ctrl+C")

        if open_browser:
            def _open() -> None:
                time.sleep(0.5)
                webbrowser.open(url)

            threading.Thread(target=_open, daemon=True).start()

        try:
            while True:
                httpd.handle_request()
        except KeyboardInterrupt:
            print("\n서버를 종료합니다.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="AI자력이탈감지 로컬 실행기")
    parser.add_argument("--port", type=int, default=8080, help="서버 포트 (기본값: 8080)")
    parser.add_argument("--no-browser", action="store_true", help="브라우저 자동 열기 비활성화")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    os.chdir(ROOT)
    run_server(port=args.port, open_browser=not args.no_browser)


if __name__ == "__main__":
    main()
