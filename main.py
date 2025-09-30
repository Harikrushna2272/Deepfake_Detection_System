import os
import argparse
import logging
from src.video_processor import VideoProcessor
from src.face_detector import FaceDetector
from src.comparator import DeepfakeComparator

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_videos(real_video_path, fake_video_path, frame_interval=5, threshold=0.6):
    """Process and compare real and fake videos"""
    try:
        # Initialize classes
        processor = VideoProcessor("data/extracted_frames")
        detector = FaceDetector()
        comparator = DeepfakeComparator(threshold=threshold)
        
        # Create output directories
        real_frames_dir = os.path.join("data", "extracted_frames", "real")
        fake_frames_dir = os.path.join("data", "extracted_frames", "fake")
        os.makedirs(real_frames_dir, exist_ok=True)
        os.makedirs(fake_frames_dir, exist_ok=True)
        
        # Extract frames
        logging.info("Extracting frames from real video...")
        real_frames = processor.extract_frames(real_video_path, real_frames_dir, frame_interval)
        logging.info("Extracting frames from fake video...")
        fake_frames = processor.extract_frames(fake_video_path, fake_frames_dir, frame_interval)
        
        logging.info(f"Extracted {real_frames} real frames and {fake_frames} fake frames")
        
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
                logging.info(f"Frame {i}: {'Deepfake' if is_deepfake else 'Real'} (Score: {score:.2f})")
            else:
                logging.warning(f"No faces detected in frame {i} for one or both videos")
        
        # Calculate final result
        if deepfake_scores:
            avg_score = sum(deepfake_scores) / len(deepfake_scores)
            logging.info("\nFinal Analysis:")
            logging.info(f"Average Difference Score: {avg_score:.2f}")
            logging.info(f"Video is likely {'DEEPFAKE' if avg_score > threshold else 'REAL'}")
            
            # Optional: Generate chart data (can be visualized separately)
            chart = {
                "type": "line",
                "data": {
                    "labels": list(range(len(deepfake_scores))),
                    "datasets": [{
                        "label": "Deepfake Score",
                        "data": deepfake_scores,
                        "borderColor": "#ff6384",
                        "backgroundColor": "rgba(255, 99, 132, 0.2)",
                        "fill": True
                    }]
                },
                "options": {
                    "scales": {
                        "y": {"beginAtZero": True, "title": {"display": True, "text": "Score"}},
                        "x": {"title": {"display": True, "text": "Frame"}}
                    }
                }
            }
            logging.info("Chart data generated (visualize separately)")
        else:
            logging.warning("No faces found for comparison")
            
    except Exception as e:
        logging.error(f"Error in main process: {str(e)}")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Deepfake detection")
    parser.add_argument("--real-video", default="data/real_videos/real_video.mp4", help="Path to real video")
    parser.add_argument("--fake-video", default="data/fake_videos/fake_video.mp4", help="Path to fake video")
    parser.add_argument("--frame-interval", type=int, default=5, help="Extract every nth frame")
    parser.add_argument("--threshold", type=float, default=0.6, help="Threshold for deepfake detection")
    args = parser.parse_args()

    # Create base directories
    os.makedirs("data/real_videos", exist_ok=True)
    os.makedirs("data/fake_videos", exist_ok=True)
    
    # Check if video files exist
    if not os.path.exists(args.real_video) or not os.path.exists(args.fake_video):
        logging.error("Please place videos in the appropriate directories:")
        logging.error(f"- Real video in: {os.path.dirname(args.real_video)}")
        logging.error(f"- Fake video in: {os.path.dirname(args.fake_video)}")
    else:
        process_videos(args.real_video, args.fake_video, args.frame_interval, args.threshold)
