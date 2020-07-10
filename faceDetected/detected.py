# encoding:utf-8
import requests
import base64
import os
import time


# 图片转换为base64后的编码
def pictures2base64(pictures_path):
    with open(pictures_path, 'rb') as f:
        picture_base64 = base64.b64encode(f.read())
        f.close()
    return picture_base64.decode()


# client_id 为官网获取的AK， client_secret 为官网获取的SK
def getToken():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s' % (
        'Uwi1i09p4wYY4LAQpEleB7CV', 'wjGmaGmhyGkhhPafGdo4GQspoEBDa6ko')
    response = requests.get(host)
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
    return response, request_url


base_path = r'C:\Users\zhoulong2.LENOVO\Desktop\zl\pictures'
path_list = os.listdir(base_path)
for path in path_list:
    pciture_name = path
    pictures_path = r'C:\Users\zhoulong2.LENOVO\Desktop\zl\pictures\%s' % (pciture_name)
    picture_base64 = pictures2base64(pictures_path)
    params = "{\"image\":\"%s\",\"image_type\":\"BASE64\",\"face_field\":\"beauty,spoofing\",\"max_face_num\":\"1\"}" % (
        picture_base64)
    response, request_url = getToken()
    access_token = response.json()['access_token']
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        # beauty表示漂亮度：0-100，spoofing表示图片合成度：0.00048以下为轻度，以上为重度
        beauty = response.json()['result']['face_list'][0]['beauty']
        spoofing = response.json()['result']['face_list'][0]['spoofing']
        print(pciture_name + ' \tbeauty:' + str(beauty) + ' \tspoofing:' + str(spoofing))
    # 发起请求太快，会导致百度API连接失效，按每秒处理2条速度
    time.sleep(0.5)
