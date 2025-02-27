# 🚀 Gesture-Based Light Switcher (Arduino + TensorFlow Lite)

A smart light switch system that detects hand gestures using a camera and controls a **physical light switch** using an **Arduino-controlled servo motor**. The system operates even in the dark using **infrared (IR) sensors**.

## 🎯 **Project Overview**
This project uses **TensorFlow Lite** for gesture recognition and an **Arduino** to flip a light switch with a **TowerPro MicroServo 9g**. The system consists of:
- **Camera (ESP32-CAM or USB webcam)** for gesture detection.
- **TensorFlow Lite Model** trained to recognize "ON" and "OFF" hand gestures.
- **Arduino + Servo Motor** to physically flip a wall switch.
- **Infrared (IR) sensors** to allow operation in low-light conditions.

---

## 🔧 **Project Steps**
### **1. Train the Gesture Recognition Model**
To detect gestures, we use **TensorFlow and Keras** to train a **deep learning model**.

#### **Steps:**
1. **Collect Gesture Data**: Capture images of your **ON, OFF, and NEUTRAL** gestures.
2. **Preprocess Images**: Resize images to **224x224 pixels**.
3. **Train a CNN Model**: Use `DepthwiseConv2D` for lightweight processing.
4. **Convert to TensorFlow Lite**: Optimize the model for **microcontrollers**.
5. **Save Model Files**:
   - `keras_model.h5` (Full model)
   - `labels.txt` (Class labels)

---

### **2. Upload the Gesture Model**
Once trained, the model is uploaded to the project directory:
```bash
# Convert model to TensorFlow Lite
tflite_convert --saved_model_dir=saved_model --output_file=model.tflite
