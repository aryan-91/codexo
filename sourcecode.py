import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime
 
video_capture = cv2.VideoCapture(0)
 
aryan_image = face_recognition.load_image_file(r"C:\Users\hp\Downloads\1662573856622-aad6e318-41ee-4839-9927-d394f0908133.jpg")
aryan_encoding = face_recognition.face_encodings(aryan_image)[0]
 
kislay_image = face_recognition.load_image_file(r"C:\Users\hp\Downloads\Screenshot_2022-07-31-23-49-11-921_com.whatsapp.jpg")
kislay_encoding = face_recognition.face_encodings(kislay_image)[0]
 
anurag_image = face_recognition.load_image_file(r"C:\Users\hp\Downloads\20211120_195818.jpg")
anurag_encoding = face_recognition.face_encodings(anurag_image)[0]
 
hritik_image = face_recognition.load_image_file(r"C:\Users\hp\Downloads\hritik.png")
hritik_encoding = face_recognition.face_encodings(hritik_image)[0]
 
known_face_encoding = [
aryan_encoding,
kislay_encoding,
anurag_encoding,
hritik_encoding
]
 
known_faces_names = [
"aryan",
"kislay",
"anurag",
"hritik"
]
 
students = known_faces_names.copy()
 
face_locations = []
face_encodings = []
face_names = []
s=True
 
 
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
 
 
 
f = open(current_date+'.csv','w+',newline = '')
lnwriter = csv.writer(f)
 
while True:
    _,frame = video_capture.read()
    small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    if s:
        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(small_frame,face_locations)
        face_names = []
        
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
            name=""
            face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_faces_names[best_match_index]
 
            face_names.append(name)
            if name in known_faces_names:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10,100)
                fontScale              = 1.5
                fontColor              = (255,0,0)
                thickness              = 3
                lineType               = 2
 
                cv2.putText(frame,name+' Present', 
                    bottomLeftCornerOfText, 
                    font, 
                    fontScale,
                    fontColor,
                    thickness,
                    lineType)
 
                if name in students:
                    students.remove(name)
                    print(students)
                    current_time = now.strftime("%H-%M-%S")
                    lnwriter.writerow([name,current_time])
    cv2.imshow("attendence system",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
video_capture.release()
cv2.destroyAllWindows()
f.close()
