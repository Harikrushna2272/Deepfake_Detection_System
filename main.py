import os
from src.video_processor import VideoProcessor
from src.face_detector import FaceDetector
from src.comparator import DeepfakeComparator

def process_videos(real_video_path, fake_video_path):
    """Process and compare real and fake videos"""
    try:
        # Initialize classes
        processor = VideoProcessor("data/extracted_frames")
        detector = FaceDetector()
        comparator = DeepfakeComparator()
        
        # Create output directories
        real_frames_dir = "data/extracted_frames/real"
        fake_frames_dir = "data/extracted_frames/fake"
        os.makedirs(real_frames_dir, exist_ok=True)
        os.makedirs(fake_frames_dir, exist_ok=True)
        
        # Extract frames
        print("Extracting frames from real video...")
        real_frames = processor.extract_frames(real_video_path, real_frames_dir)
        print("Extracting frames from fake video...")
        fake_frames = processor.extract_frames(fake_video_path, fake_frames_dir)
        
        print(f"Extracted {real_frames} real frames and {fake_frames} fake frames")
        
        # Process each pair of frames
        deepfake_scores = []
        for i in range(min(real_frames, fake_frames)):
            real_frame_path = os.path.join(real_frames_dir, f'frame_{i}.jpg')
            fake_frame_path = os.path.join(fake_frames_dir, f'frame_{i}.jpg')
            
            # Detect faces
            real_face = detector.detect_faces(real_frame_path)
            fake_face = detector.detect_faces(fake_frame_path)
            
            # Compare faces
            if real_face is not None and fake_face is not None:
                is_deepfake, score = comparator.compare_faces(real_face, fake_face)
                deepfake_scores.append(score)
                print(f"Frame {i}: {'Deepfake' if is_deepfake else 'Real'} (Score: {score:.2f})")
        
        # Calculate final result
        if deepfake_scores:
            avg_score = sum(deepfake_scores) / len(deepfake_scores)
            print(f"\nFinal Analysis:")
            print(f"Average Difference Score: {avg_score:.2f}")
            print(f"Video is likely {'DEEPFAKE' if avg_score > 0.6 else 'REAL'}")
        else:
            print("No faces found for comparison")
            
    except Exception as e:
        print(f"Error in main process: {str(e)}")

if __name__ == "__main__":
    # Example usage
    real_video = "data/real_videos/real_video.mp4"
    fake_video = "data/fake_videos/fake_video.mp4"
    
    if not os.path.exists(real_video) or not os.path.exists(fake_video):
        print("Please place videos in the appropriate directories:")
        print("- Real video in: data/real_videos/")
        print("- Fake video in: data/fake_videos/")
    else:
        process_videos(real_video, fake_video)
