import subprocess
import re

def get_wifi_interface():
    try:
        result = subprocess.run(["iwconfig"], capture_output=True).stdout.decode()
        interfaces = re.findall(r"^\w+", result, re.MULTILINE)
        return [interface for interface in interfaces if "ESSID" in subprocess.run([f"iwconfig", interface], capture_output=True).stdout.decode()]
    except Exception as e:
        print(f"Error: {e}")
        return []

def connect_to_wifi_network(ssid, password):
    interface = get_wifi_interface()[0] if get_wifi_interface() else "wlan0"
    try:
        result = subprocess.run(["wpa_supplicant", "-i", interface, "-c", "-"], input=f"network={\n\tssid=\"{ssid}\"\n\tpsk=\"{password}\"\n}", capture_output=True).stdout.decode()
        if "CTRL-EVENT-CONNECTED - Connection to {ssid} completed" in result:
            print(f"Connected to Wi-Fi network '{ssid}'")
            return True
        else:
            print(f"Failed to connect to Wi-Fi network '{ssid}'")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

ssid = "My Wi-Fi Network"
password = "My Wi-Fi Password"
connect_to_wifi_network(ssid, password)