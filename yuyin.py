from aip import AipSpeech
import os
""" 你的 APPID AK SK """
APP_ID = '11281953'
API_KEY = 'DXrAftkcRz82MNIMXC7zltuX'
SECRET_KEY = 'nefvKfjv85wD5lz7Evlr6Zf4O9YN4VYS'

soundAI = AipSpeech(APP_ID, API_KEY, SECRET_KEY)



if __name__ == '__main__':
    result  = soundAI.synthesis('真的呀，比珍珠还真', 'zh', 1, {
        'vol': 5,
    })

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('zhende.mp3', 'wb') as f:
            f.write(result)
        os.system('zhende.mp3')
