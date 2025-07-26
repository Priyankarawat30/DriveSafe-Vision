import dlib
import cv2
from imutils import face_utils
from backend.utils import eye_aspect_ratio, mouth_aspect_ratio

predictor = dlib.shape_predictor("backend/shape_predictor_68_face_landmarks.dat")
detector = dlib.get_frontal_face_detector()

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
(mStart, mEnd) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]

EAR_THRESHOLD = 0.25
MAR_THRESHOLD = 0.75

def process_image(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)
    response = {"drowsy": False, "ear": None, "yawning": False, "mar": None}

    for rect in rects:
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        mouth = shape[mStart:mEnd]

        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        mar = mouth_aspect_ratio(mouth)
        ear = (leftEAR + rightEAR) / 2.0

        response["ear"] = round(ear, 2)
        response["mar"] = round(mar, 2)

        if ear < EAR_THRESHOLD:
            response["drowsy"] = True
        if mar > MAR_THRESHOLD:
            response["yawning"] = True

    return response
