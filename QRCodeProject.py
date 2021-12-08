import cv2
import numpy as np
from pyzbar.pyzbar import decode
#from PCA9685 import PCA9685


#pwm = PCA9685(0x40, debug=False)
#pwm.setPWMFreq(50)
#pwm.setServoPosition(0, 90)
#img = cv2.imread('1.png')
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

#_, img = cap.read()
#rows, cols, _ = img.shape

#x_medium = int(cols / 2)
#center = int(cols / 2)
#position = 90 # degrees

with open('mydatabase.txt') as f:
    mydatabase = f.read().splitlines()

while True:

    success, img = cap.read()

    for barcode in decode(img):
      #(x, y, w, h) = cv2.boundingRect(barcode)

      #x_medium = int((x + x + w) / 2)
      #break
    # cv2.line(img, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)
      #print(barcode.data)
      myData = barcode.data.decode('utf-8')
      print(myData)

      if myData in mydatabase:
            myOutput = 'Authorized'
            print('move servo')
        # Move servo motor
        # if x_medium < center - 30:
        #    position += 1
        # elif x_medium > center + 30:
        #    position -= 1
        # pwm.setServoPosition(0, position)
      else:
            myOutput = 'Unauthorized'

      pts = np.array([barcode.polygon], np.int32)
      pts = pts.reshape((-1, 1, 2))
      cv2.polylines(img,[pts],True,(255,0,255),5)
      pts2 = barcode.rect
      cv2.putText(img,myOutput,(pts2[0], pts2[1]),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.9,(255,0,255),2)

    #  cv2.line(img, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)

    #cv2.imshow("Frame", img)
    #key = cv2.waitKey(1)

    #if key == 27:
     #   break

    cv2.imshow('Result', img)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()