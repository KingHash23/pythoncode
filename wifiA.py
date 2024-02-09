import subprocess

def connect_to_wifi_network(ssid, password, config_file="wpa_supplicant.conf"):
    try:
        with open(config_file, "w") as f:
            f.write(f"network={{\n\tssid=\"{ssid}\"\n\tpsk=\"{password}\"\n}}")
        result = subprocess.run(["wpa_supplicant", "-i", "wlan0", "-c", config_file], capture_output=True, text=True).stdout
        if f"CTRL-EVENT-CONNECTED - Connection to {ssid} completed" in result:
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
