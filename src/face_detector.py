import face_recognition
import cv2
import numpy as np

class FaceDetector:
    def __init__(self):
        pass
        
    def detect_faces(self, image_path):
        """Detect faces in an image"""
        try:
            # Load image
            image = cv2.imread(image_path)
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            # Detect faces
            face_locations = face_recognition.face_locations(rgb_image)
            
            if len(face_locations) == 0:
                return None
                
            # Return the first face found
            top, right, bottom, left = face_locations[0]
            face_image = image[top:bottom, left:right]
            return face_image
            
        except Exception as e:
            print(f"Error detecting face in {image_path}: {str(e)}")
            return None
