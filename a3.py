import cv2
import easyocr
import re
import os
def startextracting(img):
    bus_no = ''
    reader = easyocr.Reader(['en'])
    result = reader.readtext(img, detail = 0)
    print(result)
    for line in result:
        match = re.search(r'[ob\d][ob\d][ob\d]', line.lower())
        if str(type(match)) != '<class \'NoneType\'>':
            bus_no = list(match.group())
            if bus_no[0]=='0':
                bus_no[0]='8'
            for i in range(0,3):
                if bus_no[i]=='b':
                    bus_no[i]='8'
                if bus_no[i]=='o':
                    bus_no[i]='0'
            break
    return str(''.join(bus_no))


def main():
    final = []
    for e in os.listdir():
        im = cv2.imread(e)
        bus_n = startextracting(im)
        final.append(f"{e} {bus_n}")
        print(e, bus_n)
    for e in final:
        print(e)
    return None

# def main():
#      for i in range(1, 9):
#         im = cv2.imread('i'+ str(i) +'.jpeg')
#         bus_n = startextracting(im)
#         print(i, bus_n)
main()
