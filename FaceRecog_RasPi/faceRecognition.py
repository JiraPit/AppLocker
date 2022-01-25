import cv2
import requests
idConfirm = ''
def drawBorder(img,feature):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    scale = []
    named = ['Jira']
    idToReturn = ''
    for (x,y,w,h) in feature:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),5)
        id,con = clf.predict(gray[y:y+h,x:x+w])
        con = round(100-con)+50
        if(con>100):
            con = 100
        if(con >= 50):
            cv2.putText(img,named[id-1]+' '+str(con)+' %',(int(x+w/2)-len(named[id-1]+str(con)+' %')*7,y-4),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,2)
            if(named[id-1] == 'Jira'):
                print('Welcome Jira!')
                requests.get('https://dt6fo9.deta.dev/setstatus/false')
                idConfirm = named[id-1]
        else:
            cv2.putText(img,'Unknown'+' '+str(con)+' %',(int(x+w/2)-len('Unknown'+str(con)+' %')*7,y-4),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,2,)
        scale = [x,y,w,h]
        
    return img,scale

def detect(img,faceCascade):
    grayed = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    feature = faceCascade.detectMultiScale(grayed,1.1,10)
    img,scale = drawBorder(img,feature);
    return img

cam = cv2.VideoCapture(0)
requests.get('https://dt6fo9.deta.dev/setstatus/true')
faceCascade = cv2.CascadeClassifier('/home/pi/Desktop/FaceDetect_Recognize/haarcascade_frontalface_alt2.xml')

clf = cv2.face.LBPHFaceRecognizer_create()
clf.read('/home/pi/Desktop/FaceDetect_Recognize/classifier.xml')
color = [255,0,0]

while(True):
    video = cam.read()
    if(video[0]):
        image = detect(img=video[1],faceCascade=faceCascade)
        cv2.imshow('camera',image)
        if idConfirm != '':
            break
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break
    else: break
cam.release()
cv2.destroyAllWindows()
