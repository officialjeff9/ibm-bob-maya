import time, os, socket

payload_path = "/Users/jeffreyreinoso/Library/Preferences/Autodesk/maya/scripts/v2m_payload.py"
last_mtime = 0

def send_to_maya(command):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("localhost", 9006))
        s.sendall(command.encode('utf-8'))
        s.close()
    except: pass 

print(">>> Watcher active and listening for Bob's updates...")
while True:
    if os.path.exists(payload_path):
        current_mtime = os.path.getmtime(payload_path)
        if current_mtime != last_mtime:
            send_to_maya("exec(open('" + payload_path + "').read())")
            last_mtime = current_mtime
    time.sleep(1)