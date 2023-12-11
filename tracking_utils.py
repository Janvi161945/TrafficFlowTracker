
import numpy as np
from supervision.tools.detections import Detections
from yolox.tracker.byte_tracker import STrack

def tracks2boxes(tracks: List[STrack]) -> np.ndarray:
 
    # Convert a list of STrack objects to a numpy array of bounding boxes.

    # Args:
    #     tracks (List[STrack]): List of STrack objects representing tracks.

    # Returns:
    #     np.ndarray: Numpy array of bounding boxes in the format [x_min, y_min, x_max, y_max, track_id].
    
    if not tracks:
        return np.empty((0,))

    return np.array([
        track.tlbr + [track.track_id]
        for track in tracks
    ], dtype=float)

def match_detections_with_tracks(detections: Detections, tracks: List[STrack]) -> Detections:
  
    # Match detections with existing tracks based on bounding box overlap.

    # Args:
    #     detections (Detections): Detections object containing bounding box information.
    #     tracks (List[STrack]): List of STrack objects representing existing tracks.

    # Returns:
    #     Detections: Updated Detections object with matched track IDs.
    
    if not np.any(detections.xyxy) or not tracks:
        return Detections(np.empty((0,)))

    tracks_boxes = tracks2boxes(tracks)
    iou = box_iou_batch(tracks_boxes[:, :4], detections.xyxy)
    track2detection = np.argmax(iou, axis=1)

    tracker_ids = [None] * len(detections)

    for tracker_index, detection_index in enumerate(track2detection):
        if iou[tracker_index, detection_index] != 0:
            tracker_ids[detection_index] = int(tracks[tracker_index].track_id)

    return Detections(
        xyxy=detections.xyxy,
        confidence=detections.confidence,
        class_id=detections.class_id,
        tracker_id=np.array(tracker_ids)
    )
