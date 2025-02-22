import cv2
import numpy as np
import face_recognition

class DeepfakeComparator:
    def __init__(self):
        pass
        
    def compare_faces(self, real_face, fake_face):
        """Compare two face images for deepfake detection"""
        try:
            if real_face is None or fake_face is None:
                return False, 0
                
            # Get face encodings
            real_encoding = face_recognition.face_encodings(real_face)[0]
            fake_encoding = face_recognition.face_encodings(fake_face)[0]
            
            # Calculate difference
            difference = np.linalg.norm(real_encoding - fake_encoding)
            
            # Define threshold for deepfake detection
            threshold = 0.6
            is_deepfake = difference > threshold
            
            return is_deepfake, difference
            
        except Exception as e:
            print(f"Error comparing faces: {str(e)}")
            return False, 0
