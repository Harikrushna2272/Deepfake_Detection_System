# Deepfake Detection System

A Python-based system for detecting deepfake videos by comparing them with original videos using face recognition techniques.

## Overview
This project analyzes pairs of real and fake videos to identify deepfakes by extracting frames, detecting faces, and comparing facial features. It leverages the `face_recognition` library for face detection and comparison, with configurable parameters for flexibility and performance optimization.

## Features

- **Frame Extraction**: Extracts frames from videos at user-defined intervals to optimize processing.
- **Face Detection**: Identifies faces in frames using the `face_recognition` library.
- **Deepfake Detection**: Compares faces between real and fake videos to compute a difference score for classification.
- **Configurable Parameters**: Supports command-line arguments for video paths, frame sampling interval, and detection threshold.
- **Logging**: Detailed logging for debugging and tracking the detection process.
- **Chart Data Output**: Generates data for visualizing deepfake scores (compatible with Chart.js for visualization).

## Prerequisites

- **Python**: Version 3.6 or higher
- **Video Files**: MP4 videos with clear, frontal faces for reliable detection.
- **Dependencies**: `opencv-python`, `numpy`, `face_recognition`
- **Optional**: `cmake` and a C++ compiler for installing `face_recognition`.

## Installation

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/Harikrushna2272/Deepfake_Detection_System.git
    cd Deepfake_Detection_System
    ```

2.  **Create and Activate a Virtual Environment**:
    ```bash
    # Create virtual environment
    python -m venv venv

    # Activate virtual environment
    # Windows
    venv\Scripts\activate
    # Unix/macOS
    source venv/bin/activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install opencv-python numpy face_recognition
    ```
    **Note**: Installing `face_recognition` requires `dlib`. Ensure the following:
    - **Windows**: Install [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) with C++ workload.
    - **macOS**: Install `cmake` and `libpng`:
        ```bash
        brew install cmake libpng
        ```
    - **Linux**: Install `cmake`, `libpng`, and `build-essential`:
        ```bash
        sudo apt-get install cmake libpng-dev build-essential
        ```

4.  **Set Up Project Structure**:
    Ensure the following directory structure:
    ```
    deepfake-detection/
    ├── main.py
    ├── src/
    │   ├── __init__.py
    │   ├── video_processor.py
    │   ├── face_detector.py
    │   ├── comparator.py
    ├── data/
    │   ├── real_videos/
    │   │   ├── real_video.mp4
    │   ├── fake_videos/
    │   │   ├── fake_video.mp4
    │   ├── extracted_frames/
    │   │   ├── real/
    │   │   ├── fake/
    ```
    Create the necessary directories:
    ```bash
    mkdir -p data/real_videos data/fake_videos data/extracted_frames/real data/extracted_frames/fake
    touch src/__init__.py
    ```
    Place your `real_video.mp4` and `fake_video.mp4` in `data/real_videos/` and `data/fake_videos/`, respectively.

## Usage

### Run with Default Settings

Uses default paths (`data/real_videos/real_video.mp4`, `data/fake_videos/fake_video.mp4`), a frame interval of 5, and a threshold of 0.6.

```bash
python main.py
```

### Run with Custom Settings

Specify custom video paths, frame interval, and threshold:

```bash
python main.py --real-video data/real_videos/your_real_video.mp4 --fake-video data/fake_videos/your_fake_video.mp4 --frame-interval 10 --threshold 0.7
```

### Output

- Logs frame extraction, face detection, and comparison results.
- Reports the average difference score and classifies the video as `DEEPFAKE` (score > threshold) or `REAL`.
- Generates chart data for visualization (for use with Chart.js).
- Saves extracted frames in `data/extracted_frames/real/` and `data/extracted_frames/fake/`.

#### Example Output

```log
2025-09-30 13:11:00,123 - INFO - Extracting frames from real video...
2025-09-30 13:11:01,456 - INFO - Extracted 50 frames from data/real_videos/real_video.mp4
2025-09-30 13:11:01,789 - INFO - Extracting frames from fake video...
2025-09-30 13:11:02,123 - INFO - Extracted 50 frames from data/fake_videos/fake_video.mp4
2025-09-30 13:11:02,456 - INFO - Extracted 50 real frames and 50 fake frames
2025-09-30 13:11:02,789 - INFO - Frame 0: Deepfake (Score: 0.65)
2025-09-30 13:11:03,012 - INFO - Frame 1: Real (Score: 0.45)
...
2025-09-30 13:11:05,678 - INFO - Final Analysis:
2025-09-30 13:11:05,679 - INFO - Average Difference Score: 0.62
2025-09-30 13:11:05,680 - INFO - Video is likely DEEPFAKE
2025-09-30 13:11:05,681 - INFO - Chart data generated (visualize separately)
```

## Troubleshooting

- **ModuleNotFoundError**:
  - Ensure dependencies are installed in the active virtual environment (`pip list`).
  - Reinstall if necessary: `pip install opencv-python numpy face_recognition`.

- **Video File Errors**:
  - Verify that video files exist at the specified paths and are in a format supported by OpenCV (e.g., MP4).

- **No Faces Detected**:
  - Use videos with clear, frontal faces.
  - Alternatively, use MTCNN for more robust face detection: `pip install mtcnn`.
  - Update `src/face_detector.py` (see code comments for MTCNN implementation details).

- **Performance Issues**:
  - For long videos, increase the frame interval to process fewer frames (e.g., `--frame-interval 20`).

- **dlib Installation Issues**:
  - Ensure `cmake` and a C++ compiler are installed *before* installing `face_recognition`.

## Development

- **IDE Support**: Tested with Visual Studio Code and Cursor IDE.
- **Visualization**: Use the generated chart data with Chart.js for score visualization.
- **Customization**: Adjust the `--threshold` (e.g., 0.5–0.8) based on your dataset's characteristics.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue on GitHub.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.