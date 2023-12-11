# TrafficFlowAnalyzer

TrafficFlowAnalyzer is a project that combines vehicle detection using YOLOX and tracking with BYTETracker to analyze traffic flow and congestion in a given video stream.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Configuration](#configuration)
6. [Trained Models](#trained-models)
7. [Training Configuration](#training-configuration)
8. [Result Video](#result-video)
9. [Contributing](#contributing)
10. [Acknowledgments](#acknowledgments)



## Introduction

TrafficFlowAnalyzer is designed to analyze traffic flow and congestion in a video stream. It integrates YOLOX for vehicle detection and BYTETracker for tracking, providing insights into vehicle movements and traffic density.

## Features

- Real-time vehicle detection and tracking
- Analysis of traffic density and congestion
- Integration of YOLOX and BYTETracker for comprehensive analysis

## Installation

### Prerequisites

Before installing TrafficFlowAnalyzer, make sure you have the following prerequisites installed:

- Python 3.6 or later
- Git
- Pip

### Installation Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/TrafficFlowAnalyzer.git
    cd TrafficFlowAnalyzer
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use TrafficFlowAnalyzer, follow these steps:

1. Run the main script:

    ```bash
    python main.py
    ```

2. Provide the path to the input video when prompted.

3. The program will process the video, detecting and tracking vehicles, and output the results.

### Additional Usage Notes

- Adjust configurations in `config.py` to customize the analysis parameters.
- Ensure your input video is in a supported format.

## Configuration

The `config.py` file contains configuration parameters for TrafficFlowAnalyzer. Adjust these parameters based on your specific requirements.

## Acknowledgments

- YOLOX: [GitHub Repository](https://github.com/Megvii-BaseDetection/YOLOX)
- BYTETracker: [GitHub Repository](https://github.com/ifzhang/ByteTrack)
- Ultralytics: [GitHub Repository](https://github.com/ultralytics/yolov5)

## Trained Models

The TrafficFlowAnalyzer project requires pre-trained models for vehicle detection and tracking. You can download the necessary models using the following steps:

1. **Vehicle Detection Model (YOLOX):**
   - Download the YOLOX model weights (`best.pt`).
   - Save the weights in the  directory

Make sure to download the correct version of the models that aligns with the project version.

## Training Configuration

If you are interested in training your own models, you can customize the training configuration using the `train.yaml` file. Modify the following parameters in the `train.yaml` file to suit your needs:

- `train`: Path to the directory containing training images.
- `val`: Path to the directory containing validation images.
- `nc`: Number of classes (large, medium, small).
- `names`: List of class names.
- `backup`: Directory to save the model checkpoints during training.
- `batch_size`: Training batch size.
- `subdivisions`: Number of subdivisions per batch (reduce if running out of GPU memory).
- `width`: Width of input images (should be a multiple of 32).
- `height`: Height of input images (should be a multiple of 32).

## Result Video

After running TrafficFlowAnalyzer, you can find the result video in the project's root directory with the name `results.mp4`. This video contains the analyzed output with annotated bounding boxes, congestion information, and other relevant details.

### Interpreting the Result Video

- **Annotated Bounding Boxes:** Each detected and tracked vehicle is annotated with a bounding box.

Feel free to watch the result video to gain insights into the traffic flow and congestion analysis performed by the TrafficFlowAnalyzer.

## Contributing

Contributions are welcome! If you find a bug or have an idea for an improvement, please [open an issue](https://github.com/your-username/TrafficFlowAnalyzer/issues) or submit a pull request.
