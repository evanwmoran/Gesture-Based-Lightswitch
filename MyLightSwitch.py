import cv2
import serial
import time
import atexit
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
from tensorflow.keras.layers import DepthwiseConv2D

global last_command_time

class CustomDepthwiseConv2D(DepthwiseConv2D):
    def __init__(self, *args, **kwargs):
        kwargs.pop("groups", None)  
        super().__init__(*args, **kwargs)

# Setup Arduino communication
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)
time.sleep(2)  # Allow Arduino to initialize

def send_command(command):
    """Send a command to the Arduino and wait for servo completion."""
    print(f"Sending command: {command}")
    arduino.write(f"{command}\n".encode())  
    time.sleep(2.5)  # Wait 2.5 seconds to allow full servo movement
    response = arduino.readline().decode().strip()  
    print(f"Arduino Response: {response}")  
    return response

# Cleanup function
def cleanup():
    """Cleanup function to close Arduino connection."""
    print("Sending EXIT command to Arduino...")
    send_command("EXIT")  
    arduino.close()
    print("Arduino connection closed.")

atexit.register(cleanup)

# Load the gesture recognition model
model_gesture = load_model(
    r"C:\Users\evanm\keras\keras_model.h5",
    compile=False,
    custom_objects={"DepthwiseConv2D": CustomDepthwiseConv2D}
)

# Load gesture labels
with open(r"C:\Users\evanm\keras\labels.txt", "r") as f:
    class_names_gesture = [line.strip() for line in f.readlines()]

# Add a cooldown timer
last_command_time = 0
command_cooldown = 3  # 3-second cooldown between commands

def process_frame(frame, model, class_names):
    """Process the frame for gesture recognition."""
    size = (224, 224)
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # Normalize image
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Prepare input data
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array

    # Predict gesture
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]  
    confidence_score = prediction[0][index]
    return class_name, confidence_score

try:
    camera = cv2.VideoCapture(0)

    while True:
        ret, frame = camera.read()
        if not ret:
            print("Failed to capture frame. Exiting...")
            break

        cv2.imshow("Camera Feed", frame)

        class_name_gesture, confidence_gesture = process_frame(frame, model_gesture, class_names_gesture)

        # Debugging print statements
        print(f"Gesture: {class_name_gesture}, Confidence: {confidence_gesture:.2f}")

        # Apply cooldown before sending a new command
        
        if time.time() - last_command_time >= command_cooldown:  # Ensure at least 3 seconds between commands
            if class_name_gesture == "0 ON" and confidence_gesture > 0.8:
                print("Turning ON the light...")
                send_command("ON")
                last_command_time = time.time()  # Update last command time

            elif class_name_gesture == "1 OFF" and confidence_gesture > 0.8:
                print("Turning OFF the light...")
                send_command("OFF")
                last_command_time = time.time()  # Update last command time

            elif class_name_gesture == "2 NEUTRAL" and confidence_gesture > 0.8:
                print("Neutral gesture detected, no action.")

        # Exit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except Exception as e:
    print(f"Error: {e}")

finally:
    camera.release()
    cv2.destroyAllWindows()
