import os
from IPython import display
from tqdm.notebook import tqdm
from ultralytics import YOLO
from supervision.video.dataclasses import VideoInfo
from supervision.video.source import get_video_frames_generator
from detection_utils import detections2boxes
from tracking_utils import tracks2boxes, match_detections_with_tracks
from congestion_utils import create_video_sink, annotate_frame

HOME = os.getcwd()
SOURCE_VIDEO_PATH = f"{HOME}/test1.mp4"
TARGET_VIDEO_PATH = f"{HOME}/results.mp4"

# Load YOLO model
MODEL = "/content/last.pt"
model = YOLO(MODEL)
model.fuse()
CLASS_NAMES_DICT = model.model.names
CLASS_NAMES = ['large', 'medium', 'small']

# Constants for vehicle per square meter thresholds
SMALL_THRESHOLD = 1.8
MEDIUM_THRESHOLD = 2.4
LARGE_THRESHOLD = 2.8

# ... (define other constants and configurations)

# Create BYTETracker instance
byte_tracker = BYTETracker(BYTETrackerArgs())

# Create VideoInfo instance
video_info = VideoInfo.from_video_path(SOURCE_VIDEO_PATH)

# Create frame generator
generator = get_video_frames_generator(SOURCE_VIDEO_PATH)

# Initialize video sink
video_sink = create_video_sink(TARGET_VIDEO_PATH, video_info)

# Initialize other variables
frame_counter = 0
prev_positions = {}

# Main processing loop
for frame in tqdm(generator, total=video_info.total_frames):
    print(f"Frame --- {frame_counter}")
    
    # Detection using YOLO model
    results = model(frame)
    detections = Detections(
        xyxy=results[0].boxes.xyxy.cpu().numpy(),
        confidence=results[0].boxes.conf.cpu().numpy(),
        class_id=results[0].boxes.cls.cpu().numpy().astype(int)
    )

    # Tracking detections
    tracks = byte_tracker.update(
        output_results=detections2boxes(detections=detections),
        img_info=frame.shape,
        img_size=frame.shape
    )

    # Match detections with tracks
    detections = match_detections_with_tracks(detections=detections, tracks=tracks)

    # Apply additional filtering or processing if needed

    # Annotate frame with bounding boxes and congestion information
    frame = annotate_frame(frame=frame, detections=detections, frame_counter=frame_counter, frame_vehicle_density=frame_vehicle_densities[-1])

    # Write annotated frame to the output video
    video_sink.write_frame(frame)

    # Update frame counter
    frame_counter += 1

# Close video sink after processing all frames
video_sink.close()
