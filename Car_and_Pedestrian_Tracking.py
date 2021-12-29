import cv2

##### Start with detecting cars #####

# car image
img_file = "car.jpeg"
video = cv2.VideoCapture("DashcamPedestrians.mp4")

# Our pre-trained car and pedestrian classfiers
car_classifier_file = "car_detector.xml"
pedestrian_classifier_file = "haarcascade_fullbody.xml"

# Create our car and pedestrian classifiers
car_tracker = cv2.CascadeClassifier(car_classifier_file)
pedestrian_tracker = cv2.CascadeClassifier(pedestrian_classifier_file)


while True:
    # Read the current frame
    read_successful, frame = video.read()

    # Safe coding
    if read_successful:
        # Convert to gray scale
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    # detect cars AND pedestrians
    cars = car_tracker.detectMultiScale(grayscaled_frame)
    pedestrians = pedestrian_tracker.detectMultiScale(grayscaled_frame)

    # Draw rectangles around the cars
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x + 5, y + 5), (x + w - 5, y + h - 5), (48, 200, 213), 5)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (200, 213, 48), 5)

    # Draw rectangles around the pedestrians
    for (x, y, w, h) in pedestrians:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (213, 48, 200), 5)

    # Display the image with the faces spotted
    cv2.imshow("Self Driving Car", frame)

    # Don't autoclose (Wait her in the code and listen for a key press)
    key = cv2.waitKey(1)

    # Stop if Q or q is pressed
    if key == 81 or key == 113:
        break


video.release()


"""

# create opencv image
img = cv2.imread(img_file)

# Create our car classifier
car_tracker = cv2.CascadeClassifier(classifier_file)

# convert to grayscale (needed for haar cascade)
grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# detect cars
cars = car_tracker.detectMultiScale(grayscale_img)
print(cars)

# Draw rectangles aroudn the cars
for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x + w, y + h), (43, 177, 219), 5)

# Display the image with the faces spotted
cv2.imshow("Clever Programmer Car Detector", img)

# Don't autoclose (Wait her in the code and listen for a key press)
cv2.waitKey()


"""


print("Code completed!")
