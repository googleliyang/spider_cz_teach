#coding:utf-8
# pip install pillow
from PIL import Image
import pytesseract

im = Image.open('getimage.jpg')

result = pytesseract.image_to_string(im)
print(result)

# pytesseract绝大多数时间用于解析图片数据，很少有时间处理验证码，原因是没有训练过的引擎处理效率低下