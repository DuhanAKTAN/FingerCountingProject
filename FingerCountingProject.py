import cv2 as cv
import os 
import handTrackingModule as htm
import serial
import time

#arduino için haberleşme başlatilmasi
ser = serial.Serial("COM5",9600,timeout=1)

wCam,hCam = 1000,1000

#video başlatma
cap = cv.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

#video başladiktan sonra sol üstte parmak sayisina göre değişecek resimlerin yolu
folderPath = "Images"
myList = os.listdir(folderPath)
print(myList)
overlaylist = list()
for im in myList:
    image = cv.imread(f'{folderPath}/{im}')
    overlaylist.append(image)

#yazdiğimiz module den bir obje oluşturma
detector = htm.handDetector(detectionCon=0.75)

ids = [8,12,16,20]
while True:
    success,img = cap.read()

    img = detector.findHands(img,draw=True)
    lmlist = detector.findPosition(img)

    #parmak sayma
    count=0
    if len(lmlist) != 0:
        if lmlist[4][1]>lmlist[3][1]:
                count+=1
        for id in ids:
            
            if lmlist[id][2]<lmlist[id-2][2]:
                count+=1
        
    print(count)

    #arduino ya parmak sayisini gönderme
    ser.write(f'{count}\n'.encode())
    time.sleep(0.1)

    #sol üstteki resmi parmak sayisina göre değiştirme
    img[:200,:200] = overlaylist[count]

    #sol altta parmak sayisini yazdirma
    cv.rectangle(img,(20,225),(170,425),(0,255,0),cv.FILLED)
    cv.putText(img,str(count),(45,375),cv.FONT_HERSHEY_PLAIN,10,(255,255,255),25)

    cv.imshow("Image",img)
    c=cv.waitKey(1)
    if c==27:
        break

cap.release()
cv.destroyAllWindows()
ser.close()