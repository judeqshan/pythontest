import pytesseract
from PIL import Image


if __name__ == '__main__':
    #text = pytesseract.image_to_string(Image.open("/Users/jshan/Documents/test/automation/pic/digital.png"),lang="eng")
    text = pytesseract.image_to_string(Image.open("/Users/jshan/Documents/python/tv_info.jpeg"),lang="eng")
    print(text)