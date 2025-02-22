import cv2
import os

class VideoProcessor:
    def __init__(self, output_path):
        self.output_path = output_path
        
    def extract_frames(self, video_path, output_folder):
        """Extract frames from a video file"""
        try:
            # Create output directory if it doesn't exist
            os.makedirs(output_folder, exist_ok=True)
            
            # Read the video
            video = cv2.VideoCapture(video_path)
            frame_count = 0
            success = True
            
            while success:
                # Read a frame
                success, frame = video.read()
                if success:
                    # Save frame as image
                    frame_path = os.path.join(output_folder, f'frame_{frame_count}.jpg')
                    cv2.imwrite(frame_path, frame)
                    frame_count += 1
            
            video.release()
            return frame_count
            
        except Exception as e:
            print(f"Error processing video {video_path}: {str(e)}")
            return 0
