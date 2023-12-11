# detection_utils.py
import numpy as np
from supervision.tools.detections import Detections

def detections2boxes(detections: Detections) -> np.ndarray:

    # Convert Detections object to a numpy array of bounding boxes.

    # Args:
    #     detections (Detections): Detections object containing bounding box information.

    # Returns:
    #     np.ndarray: Numpy array of bounding boxes in the format [x_min, y_min, x_max, y_max, confidence].

    if not detections.xyxy.size:
        return np.empty((0,))

    return np.hstack((
        detections.xyxy,
        detections.confidence[:, np.newaxis]
    ))
