import cv2
import os
import logging

class VideoProcessor:
    def __init__(self, output_path):
        self.output_path = output_path
        
    def extract_frames(self, video_path, output_folder, frame_interval=5):
        """Extract frames from a video file at specified intervals"""
        try:
            # Create output directory if it doesn't exist
            os.makedirs(output_folder, exist_ok=True)
            
            # Read the video
            video = cv2.VideoCapture(video_path)
            if not video.isOpened():
                logging.error(f"Could not open video {video_path}")
                return 0
            
            frame_count = 0
            saved_frame_count = 0
            while True:
                success, frame = video.read()
                if not success:
                    break
                if frame_count % frame_interval == 0:
                    frame_path = os.path.join(output_folder, f'frame_{saved_frame_count}.jpg')
                    cv2.imwrite(frame_path, frame)
                    saved_frame_count += 1
                frame_count += 1
            
            video.release()
            logging.info(f"Extracted {saved_frame_count} frames from {video_path}")
            return saved_frame_count
            
        except Exception as e:
            logging.error(f"Error processing video {video_path}: {str(e)}")
            return 0
