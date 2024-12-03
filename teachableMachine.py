import cv2
import numpy as np
import tensorflow as tf
import serial
import time

# Load TFLite model and allocate tensors
interpreter = tf.lite.Interpreter(model_path="model_new.tflite")
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Setup Serial Communication
arduino = serial.Serial('/dev/tty.usbmodem14101', 9600)  # Updated with your macOS Arduino port
time.sleep(2)  # Allow time for Arduino to initialize

# Setup Webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess frame to fit model input
    input_image = cv2.resize(frame, (224, 224))  # Adjust size as per your model
    input_image = np.expand_dims(input_image, axis=0)
    input_image = input_image.astype(np.float32) / 255.0

    # Run inference
    interpreter.set_tensor(input_details[0]['index'], input_image)
    interpreter.invoke()
    predictions = interpreter.get_tensor(output_details[0]['index'])

    # Determine which class has the highest confidence
    predicted_class = np.argmax(predictions)
    confidence = np.max(predictions)

    if confidence > 0.7:  # Ensure confidence is high enough
        if predicted_class == 0:
            print("Hydrangea")
            arduino.write(b"Hydrangea\n")
        elif predicted_class == 1:
            print("Strelizia Reginae")
            arduino.write(b"Strelizia Reginae\n")
        elif predicted_class == 2:
            print("Sunflower")
            arduino.write(b"Sunflower\n")
        elif predicted_class == 3:
            print("Fern")
            arduino.write(b"Fern\n")
        elif predicted_class == 4:
            print("Orchid")
            arduino.write(b"Orchid\n")

    # Display the frame
    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
arduino.close()
