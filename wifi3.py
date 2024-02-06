import subprocess

def get_wifi_profiles():
    try:
        result = subprocess.check_output(["netsh", "wlan", "show", "profile"]).decode()
        profiles = [line.split(":")[-1].strip() for line in result.split("\n") if "All User Profile" in line]
        return profiles
    except Exception as e:
        print(f"Error: {e}")
        return []

def get_wifi_info(profile):
    try:
        result = subprocess.check_output(["netsh", "wlan", "show", "profile", profile, "key=clear"]).decode()
        ssid = [line.split(":")[-1].strip() for line in result.split("\n") if "SSID name" in line][0]
        security_type = [line.split(":")[-1].strip() for line in result.split("\n") if "Security key" in line][0]
        password = [line.split(":")[-1].strip() for line in result.split("\n") if "Key Content" in line][0]
        return ssid, security_type, password
    except Exception as e:
        print(f"Error: {e}")
        return "", "", ""

wifi_profiles = get_wifi_profiles()

if wifi_profiles:
    for profile in wifi_profiles:
        ssid, security_type, password = get_wifi_info(profile)
        print(f"SSID: {ssid}, Security Type: {security_type}, Password: {password}")
else:
    print("No Wi-Fi profiles found.")