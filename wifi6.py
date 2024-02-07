import subprocess
import re

def get_nearby_wifi_networks():
    try:
        result = subprocess.check_output(["netsh", "wlan", "show", "networks"]).decode()
        networks = re.findall(r"(?<=SSID\s*:\s*)([\w\s]+)(?=\r\n)", result)
        return networks
    except Exception as e:
        print(f"Error: {e}")
        return []

def get_wifi_info(network):
    try:
        result = subprocess.check_output(["netsh", "wlan", "show", "profile", network, "key=clear"]).decode()
        ssid = [line.split(":")[-1].strip() for line in result.split("\n") if "SSID name" in line][0]
        security_type = [line.split(":")[-1].strip() for line in result.split("\n") if "Security key" in line][0]
        password = [line.split(":")[-1].strip() for line in result.split("\n") if "Key Content" in line][0]
        return ssid, security_type, password
    except Exception as e:
        print(f"Error: {e}")
        return "", "", ""

nearby_wifi_networks = get_nearby_wifi_networks()

if nearby_wifi_networks:
    for network in nearby_wifi_networks:
        ssid, security_type, password = get_wifi_info(network)
        if ssid:
            print(f"SSID: {ssid}, Password: {password}")
            break
else:
    print("No nearby Wi-Fi networks found.")