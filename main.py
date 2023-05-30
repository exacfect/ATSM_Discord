# Import thư viện.
import requests
import time
import os
try:
    with open('settings.txt', 'r') as settings_file:
        settings = settings_file.read().splitlines()
        token = settings[0].strip()
        channel_id = settings[1].strip()
        delay = int(settings[2].strip())
    print("Your token: {}\nChannel ID: {}\nDelay: {}".format(token, channel_id, delay))
    print("Bạn có thể nhấn Enter để xác nhận hoặc nhấn 'n' để chỉnh sửa lại.")
    confirmation = input()
    if confirmation.lower() == 'n':
        update_token = input('Bạn muốn cập nhật token (nhập "y" để đồng ý, nếu không thì chỉ cập nhật ID Kênh và Delay): ')
        if update_token.lower() == 'y':
            token = input('Nhập mã token Discord: ')
            with open('settings.txt', 'w') as settings_file:
                settings_file.write(f'{token}')
            print("Token đã được cập nhật.")
            print("Your token: {}\nChannel ID: {}\nDelay: {}".format(token, channel_id, delay))
        channel_id = input('Nhập ID của kênh: ')
        delay = int(input('Nhập thời gian delay (giây): '))
        with open('settings.txt', 'w') as settings_file:
            settings_file.write(f'{token}\n{channel_id}\n{delay}')
        print("Token, Channel ID và Delay đã được cập nhật.")
except FileNotFoundError:
    token = input('Nhập mã token Discord: ')
    channel_id = input('Nhập ID của kênh: ')
    delay = int(input('Nhập thời gian delay (giây): '))

    # Lưu thông tin vào tệp tin settings.txt
    with open('settings.txt', 'w') as settings_file:
        settings_file.write(f'{token}\n{channel_id}\n{delay}')
if not os.path.isfile("message.txt"):
    # Tạo file message.txt nếu nó không có.
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
    api = f'https://discord.com/api/v9/channels/{channel_id}/messages'

    # Gửi POST request
    response = requests.post(api, headers=headers, data=payload)

    # Kiểm tra phản hồi từ API
    if response.status_code == 200:
        print('[{}] Tin nhắn đã được gửi thành công với nội dung:\n'.format(time.ctime())+message_content)
    else:
        print('[{}] Có lỗi xảy ra khi gửi tin nhắn.'.format(time.ctime()))
        print('[{}] Phản hồi từ API:'.format(time.ctime()), response.json())
    seconds = delay+2
    time.sleep(seconds)