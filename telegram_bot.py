import os
import requests
import testflight_watcher
import sys

# Lấy giá trị từ biến môi trường
CHAT_ID = os.getenv('CHAT_ID')
BOT_TOKEN = os.getenv('BOT_TOKEN')

BOT_URL = "https://api.telegram.org/bot{}/sendMessage".format(BOT_TOKEN)
MSG_NO_FULL = "TestFlight slots for <b>{}</b> slot còn trống cài đặt ngay! \
<a href='{}'>Download now</a>"
MSG_FULL = "<b>{}</b> Trạng thái slot app beta đã FULL"

def send_notification(tf_id, free_slots, title): ...

with open('id.txt', 'r') as file:
    ids = file.read().splitlines()

while True:
    testflight_watcher.watch(ids, send_notification)
    time.sleep(10)  # Chờ 10 giây trước khi kiểm tra lại