import subprocess

def run_http_server():
    cmd = [
        "http-server",
        "-S",
        "-C", "localhost.pem",
        "-K", "localhost-key.pem",
        "-p", "8000",
    ]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Server failed to start: {e}")

if __name__ == "__main__":
    run_http_server()