import cv2

#Load pre-trained data on frontal faces
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

"""
#Choose and image
img = cv2.imread("beelzebub.png")

#Convert image to grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

#Draw rectangles around faces
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)

cv2.imshow("Face Detector", img)
key = cv2.waitKey()
"""



#Capture from webcam
webcam = cv2.VideoCapture("leo_face.mov") #Use 0 for facecam

#Iterate forever over frames
while True:
    #Read the current frame
    successful_frame_read, frame = webcam.read()

    #Convert image to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    #Draw rectangles around faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow("Face Detector", frame)
    key = cv2.waitKey(1)

    #Stop if Q_KEY is pressed using ASCII
    if key == 81 or key == 113:
        break

#Release the VideoCapture object
webcam.release()






