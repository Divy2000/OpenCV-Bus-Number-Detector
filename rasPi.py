import cv2
import easyocr
import re

def startextracting(img):
    bus_no = ''
    reader = easyocr.Reader(['en'])
    result = reader.readtext(img, detail = 0)
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
    bus_n = str(''.join(bus_no))
    if bus_n == '':
        print('not found!')
    else:
        print(bus_n)
    img = cv2.putText(img,bus_n, (100,100),cv2.FONT_HERSHEY_SIMPLEX, 4, color=(0,0,255), thickness=2 )
    return img


cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()
    frame = startextracting(frame)
    frame = cv2.resize(frame, (640,480))
    cv2.imshow("Image", frame)
    key = cv2.waitKey(1)
    if  key == 103:
        cv2.imwrite('frame.jpg', frame)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()

