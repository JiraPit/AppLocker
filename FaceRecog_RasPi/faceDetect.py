import cv2

def drawBorder(img,feature):
    scale = []
    for (x,y,w,h) in feature:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)
        scale = [x,y,w,h]
    return img,scale

def detect(img,faceCascade,pic_no):
    grayed = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    feature = faceCascade.detectMultiScale(grayed,1.1,10)
    img,scale = drawBorder(img,feature);
    if(len(scale)==4):
        id = 1
        result = img[scale[1]:scale[1]+scale[3],scale[0]:scale[0]+scale[2]]
        create_dataset(result,id,pic_no)
    return img

def create_dataset(img,id,pic_no):
    cv2.imwrite('FaceDetect_Recognize/DataSet/pic.'+str(id)+'.'+str(pic_no)+'.jpg',img)

cam = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('Models/haarcascade_frontalface_alt2.xml')
pic_no = 1
while(True):
    video = cam.read()
    if(video[0] and pic_no<=200):
        finalImage = detect(img=video[1],faceCascade=faceCascade,pic_no=pic_no)
        cv2.imshow('camera',finalImage)
        pic_no +=1
        if(cv2.waitKey(1) & 0xFF == ord('q')) : break
    else : break 

cam.release() ; cv2.destroyAllWindows()
