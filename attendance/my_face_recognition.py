import face_recognition
import cv2

# Load a sample image and learn how to recognize it
sample_image = face_recognition.load_image_file("sample.jpg")
sample_encoding = face_recognition.face_encodings(sample_image)[0]

# Capture video from webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Find all face locations in the frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare the detected face encoding with the sample
        match = face_recognition.compare_faces([sample_encoding], face_encoding)
        
        if match[0]:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        else:
            cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)

    cv2.imshow('Face Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
