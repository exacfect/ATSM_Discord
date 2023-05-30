import requests
import time
import os
# Thay thế các giá trị sau bằng thông tin của bạn
try:
    with open('settings.txt', 'r') as settings_file:
        settings = settings_file.read().splitlines()
        token = settings[0].strip()
        channel_id = settings[1].strip()
        delay = int(settings[2].strip())
except FileNotFoundError:
    # Nếu tệp tin settings.txt không tồn tại, yêu cầu người dùng nhập thông tin
    token = input('Nhập mã token Discord: ')
    channel_id = input('Nhập ID của kênh: ')
    delay = int(input('Nhập thời gian delay (giây): '))

    # Lưu thông tin vào tệp tin settings.txt
    with open('settings.txt', 'w') as settings_file:
        settings_file.write(f'{token}\n{channel_id}\n{delay}')
if not os.path.isfile("message.txt"):
    # Create message.txt if it doesn't exist
    with open("message.txt", "w"):
        pass
message_file = 'message.txt'
with open(message_file, encoding='utf-8') as file:
    message_content = file.read().strip()
if message_content == "":
    print("Nội dung tin nhắn không được để trống, chỉnh sửa ở message.txt!")
    os.system('message.txt')
    exit()
print("Lưu ý: mục đích của tool không phải để spam,raid,attack, chúng tôi sẽ không chịu trách nhiệm về HẬU QUẢ bạn gây ra!")
print(time.ctime())
while True:

    # Tạo header chứa mã token
    headers = {
        'authorization': token
    }

    # Tạo payload chứa nội dung tin nhắn
    payload = {
        'content': message_content
    }

    # Tạo URL endpoint
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'

    # Gửi POST request
    response = requests.post(url, headers=headers, data=payload)

    # Kiểm tra phản hồi từ API
    if response.status_code == 200:
        print('Tin nhắn đã được gửi thành công với nội dung:\n'+message_content)
    else:
        print('Có lỗi xảy ra khi gửi tin nhắn.')
        print('Phản hồi từ API:', response.json())
    seconds = delay+2
    time.sleep(seconds)
    print(time.ctime())