import socket
from datetime import datetime

# ------------------------------
# Mini Port Scanner (Simple Version)
# ------------------------------
# Scans a given host for open ports in a specified range.
# Great for understanding basic network principles, like how services run on specific ports.

def scan_ports(host, start_port=1, end_port=1024):
    print(f"\n🔍 Starting scan on host: {host}")
    print(f"📅 Time started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📦 Scanning ports {start_port} to {end_port}...\n")

    # Try to resolve host (e.g., "google.com" to IP)
    try:
        target_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("❌ Could not resolve host. Are you sure it's correct?")
        return

    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Wait max 0.5 seconds per port (speed vs accuracy)

        result = sock.connect_ex((target_ip, port))  # Returns 0 if port is open
        if result == 0:
            print(f"✅ Port {port} is OPEN")
            open_ports.append(port)
        sock.close()

    print("\n🔚 Scan complete.")
    if open_ports:
        print(f"🟢 Open ports: {open_ports}")
    else:
        print("🔒 No open ports found in that range.")

# ------------------------------
# Example usage
# ------------------------------
if __name__ == "__main__":
    # You can change 'localhost' to any domain/IP you *own or have permission to test*
    target_host = "localhost"  # Try 'scanme.nmap.org' for testing (public scan target by Nmap)
    scan_ports(target_host, 20, 100)  # You can adjust the range as needed
