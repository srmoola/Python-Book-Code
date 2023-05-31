import cv2
from matplotlib import pyplot as plt

# Load the classifier XML files for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Define the figure and axes for Matplotlib
fig, ax = plt.subplots(figsize=(10, 6))

# Define the minimum and maximum sizes for face detection
min_size = (50, 50)
max_size = (200, 200)

try:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=min_size, maxSize=max_size)

        # Draw a rectangle around each face and eyes in the frame
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        # Display the resulting frame with Matplotlib
        ax.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        plt.draw()
        plt.pause(0.001)
        ax.clear()

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) == ord('q'):
            break

except KeyboardInterrupt:
    print("Program closed by user.")

finally:
    # When everything is done, release the capture and close the window
    cap.release()
    cv2.destroyAllWindows()
