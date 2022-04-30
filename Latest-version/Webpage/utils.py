import base64
import re
from io import BytesIO
from django.core.files.base import ContentFile

#圖片內容轉化所得的Base64 String(data)是不帶有頭信息/html標籤（data:image/jpeg;base64,）
#https://www.twblogs.net/a/5b8ed7882b717718834828f8
def decode_base64(data, altchars=b'+/'):
    image_data = re.sub('^data:image/.+;base64,', '', data)
    return base64.b64decode(image_data)

#use BytesIO,to manipulate binary data
def prepare_image(image):
    return BytesIO(decode_base64(image))

#Decoding base64 string
#If you have an image in base64 string format and you want to save it to a models CharField,
def base64_file(data, name=None):
    _format, _img_str = data.split(';base64,')
    _name, ext = _format.split('/')
    if not name:
        name = _name.split(":")[-1]
    return ContentFile(base64.b64decode(_img_str), name='{}.{}'.format(name, ext))