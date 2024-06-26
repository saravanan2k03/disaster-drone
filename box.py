# Utility functions to display the pose detection results.

import cv2
import numpy as np
from tflite_support.task import processor

_MARGIN = 10 
_ROW_SIZE = 10 
_FONT_SIZE = 1
_FONT_THICKNESS = 1
_TEXT_COLOR = (0, 0, 255) 


def drawBoxAndGetCenter(image: np.ndarray, detection_result: processor.DetectionResult):
 
  mid_point =  int(640/2), int(480/2)
  
  if len(detection_result.detections) > 0:
    
    for i in range(len(detection_result.detections)):
        
        detection = detection_result.detections[0]
        category = detection.categories[0]
        category_name = category.category_name
    
        if category_name!="person":
            continue
        else:
            # Draw bounding_box
            bbox = detection.bounding_box
            start_point = bbox.origin_x, bbox.origin_y
            end_point = bbox.origin_x + bbox.width, bbox.origin_y + bbox.height
            mid_point = int((start_point[0] + end_point[0]) / 2 ), int((start_point[1] + end_point[1]) / 2)
            cv2.rectangle(image, start_point, end_point, _TEXT_COLOR, 3)
            cv2.circle(image, mid_point, 2, (0,255,0), 2) 

            # Draw label and score

            probability = round(category.score, 2)
            result_text = category_name + ' (' + str(probability) + ')'
            text_location = (_MARGIN + bbox.origin_x,
                             _MARGIN + _ROW_SIZE + bbox.origin_y)
            cv2.putText(image, result_text, text_location, cv2.FONT_HERSHEY_PLAIN,
                        _FONT_SIZE, _TEXT_COLOR, _FONT_THICKNESS)
            break

  return image, mid_point
