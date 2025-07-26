# **DriveSafe Vision**

A real-time computer vision-based system to detect driver drowsiness by monitoring eye closure and yawning using webcam feed. This project leverages facial landmark detection via dlib and OpenCV, integrated into a user-friendly Streamlit web interface.

## Author
Priyanka Rawat

## Technologies Used

- Python
- OpenCV – Real-time video processing
- dlib – Facial landmark detection
- imutils – Eye aspect ratio (EAR) computation
- Streamlit – Frontend web interface
- NumPy, SciPy – Mathematical operations
- Threading – For smooth camera frame handling

## Features

- Real-time eye blink detection using EAR (Eye Aspect Ratio)
- Yawning detection based on lip distance
- Audio alarm system when drowsiness is detected
- Clean and interactive Streamlit UI
- Modular structure with separate backend and frontend components

## How It Works

1. Face Detection: Uses dlib’s HOG-based detector to identify face.
2. Landmark Detection: Detects 68 facial landmarks using shape_predictor_68_face_landmarks.dat.
3. Drowsiness Logic:
   - Eye Aspect Ratio (EAR): Calculates eye openness. If eyes remain closed for a threshold number of frames, alarm is triggered.
   - Lip Distance: Measures mouth opening. If beyond threshold, yawning is detected.
4. Alarm Trigger: Audio alert using playsound or pyttsx3.

## Installation and Setup

### 1. Clone the Repository

git clone https://github.com/Priyankarawat30/DriveSafe-Vision.git
cd DriverDrowsinessDetection

### 2. Create a Virtual Environment (optional but recommended)

python -m venv venv
venv\Scripts\activate  # On Windows

### 3. Install Requirements
pip install -r requirements.txt

### 4. Install dlib Manually (if needed)
Download the .whl file compatible with your Python version and install it:

pip install path\to\dlib‑19.24.2‑cp311‑cp311‑win_amd64.whl
Make sure your Python version matches the .whl file (e.g., Python 3.11).

### 5. Run the Streamlit App

streamlit run streamlit_app.py
Ensure shape_predictor_68_face_landmarks.dat is in the same directory or update its path in the code.


## Future Improvements
Add face recognition to identify driver

Track head position to detect nodding off

Deploy to cloud platforms with webcam support

Integrate night vision camera compatibility

## License
This project is licensed under the MIT License.

## Contact
GitHub: @Priyankarawat30


