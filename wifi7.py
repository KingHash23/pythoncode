import subprocess
import re

def get_nearby_wifi_networks():
    try:
        result = subprocess.run(["netsh", "wlan", "show", "networks"], capture_output=True).stdout.decode()
        networks = re.findall(r"(?<=SSID\s*:\s*)([\w\s]+)(?=\r\n)", result)
        return networks
    except Exception as e:
        print(f"Error: {e}")
        return []

def get_wifi_info(network):
    try:
        result = subprocess.run(["netsh", "wlan", "show", "profile", network, "key=clear"], capture_output=True).stdout.decode()
        if "Profile does not exist" in result:
            print(f"Error: The profile '{network}' does not exist.")
            return "", "", ""
        ssid = [line.split(":")[-1].strip() for line in result.split("\n") if "SSID name" in line][0]
        security_type = [line.split(":")[-1].strip() for line in result.split("\n") if "Security key" in line][0]
        if "Hidden" in security_type or "Closed" in security_type:
            print(f"Error: The Wi-Fi network '{ssid}' is hidden or closed.")
            return "", "", ""
        if "Enterprise" in security_type or "802.1X" in security_type:
            print(f"Error: The Wi-Fi network '{ssid}' is secured with Enterprise or 802.1X security, which does not allow password retrieval.")
            return "", "", ""
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
            print(f"SSID: {ssid}, Security Type: {security_type}, Password: {password}")
            break
else:
    print("No nearby Wi-Fi networks found.")