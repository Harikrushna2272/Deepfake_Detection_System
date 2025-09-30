import cv2
import numpy as np
import face_recognition
import logging

class DeepfakeComparator:
    def __init__(self, threshold=0.6):
        self.threshold = threshold
        
    def compare_faces(self, real_face, fake_face):
        """Compare two face images for deepfake detection"""
        try:
            if real_face is None or fake_face is None:
                logging.warning("One or both face images are None")
                return False, 0
                
            # Get face encodings
            real_encodings = face_recognition.face_encodings(real_face)
            fake_encodings = face_recognition.face_encodings(fake_face)
            if not real_encodings or not fake_encodings:
                logging.warning("Could not generate face encodings")
                return False, 0
                
            real_encoding = real_encodings[0]
            fake_encoding = fake_encodings[0]
            
            # Calculate difference
            difference = np.linalg.norm(real_encoding - fake_encoding)
            
            # Determine if deepfake
            is_deepfake = difference > self.threshold
            
            return is_deepfake, difference
            
        except Exception as e:
            logging.error(f"Error comparing faces: {str(e)}")
            return False, 0