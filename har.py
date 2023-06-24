import cv2
cascade_face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap= cv2.VideoCapture(0)

while True:
     ret,img=cap.read()
     print(ret)
     g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
     f=cascade_face.detectMultiScale(g,1.3,5)

     for( X,Y,W,H)in f:
         cv2.rectangle(img,(X,Y),(X+W,Y+H),(0,0,255),5)



     cv2.imshow('img',img)
     k=cv2.waitKey(30) & 0xff
     if k==27:
         break
cap.realease()
cv2.destroyAllWindows()
