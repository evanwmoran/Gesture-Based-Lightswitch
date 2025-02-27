# 🚀 Gesture-Based Light Switcher (Arduino + TensorFlow Lite + Google Teachable Machine)

A smart light switch system that detects hand gestures using a camera and controls a **physical light switch** using an **Arduino-controlled servo motor**. 

## 🎯 **Project Overview**
This project uses **TensorFlow Lite and Google Teachable Machine** for gesture recognition and an **Arduino** to flip a light switch with a **TowerPro MicroServo 9g**. The system consists of:
- **Camera (Laptop Camera works)** for gesture detection.
- **TensorFlow Lite Model** trained to recognize "ON" and "OFF" hand gestures.
- **Arduino + Servo Motor** to physically flip a wall switch.


---

## 🔧 **Project Steps**
### **1. Train the Gesture Recognition Model**
To detect gestures, we use **TensorFlow Lite and Google Teachable Machine** to train a **deep learning model**.

#### **Steps:**
1. **Collect Gesture Data**: Capture images of your **ON, OFF, and NEUTRAL** gestures.
2. **Use **Google Teachable Machine** to Train Model
3. **Convert to TensorFlow Lite**: Optimize the model for **Keras**.
5. **Save Model Files**:
   - `keras_model.h5` (Full model)
   - `labels.txt` (Class labels)

---

### **2. Create the Python code**

---
### **3. Create the Arduino Code**
---
### **4. Build the Arduino and Servo circuit**
**Connect the Servo Motor Correctly:**
 1.Brown → GND
 2.Red → 5V
 3.Orange → D9 (Signal)

---
### **Test the project**
 1. Run the Arduino Code on the board.

 2. Run the Python Script on your computer.

 3. Show a gesture to the camera:

    -Open hand should turn the switch ON.
    -Closed hand should turn the switch OFF.
    -Neutral Expression will keep the servo at it's current position.






