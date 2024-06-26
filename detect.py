import sys
import time
import cv2
import control
from tflite_support.task import core
from tflite_support.task import processor
from tflite_support.task import vision
from box import drawBoxAndGetCenter


def detectHumans(vehicle, model: str, enable_edgetpu: bool):
 
  # Variables to calculate FPS
  counter, fps = 0, 0
  start_time = time.time()

  # Start capturing video input from the camera
  cap = cv2.VideoCapture(0)
  cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

  # Visualization parameters
  row_size = 20  # pixels
  left_margin = 24  # pixels
  text_color = (0, 0, 255)  # red
  font_size = 1
  font_thickness = 1
  fps_avg_frame_count = 10

  # Initialize the object detection model
  base_options = core.BaseOptions(
      file_name=model, use_coral=enable_edgetpu, num_threads=3)
  detection_options = processor.DetectionOptions(
      max_results=3, score_threshold=0.3)
  options = vision.ObjectDetectorOptions(
      base_options=base_options, detection_options=detection_options)
  detector = vision.ObjectDetector.create_from_options(options)

  # Continuously capture images from the camera and run inference
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      sys.exit(
          'ERROR: Unable to read from webcam. Please verify your webcam settings.'
      )

    counter += 1

    # Convert the image from BGR to RGB as required by the TFLite model.
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Create a TensorImage object from the RGB image.
    input_tensor = vision.TensorImage.create_from_array(rgb_image)

    # Run object detection estimation using the model.
    detection_result = detector.detect(input_tensor)

    tolerance = 80

    direction = "None"

    start_point = int(640/2 - tolerance), int(480/2 - tolerance)
    end_point =  int(640/2 + tolerance), int(480/2 + tolerance)

    cv2.rectangle(image, start_point, end_point, (255,0,0), 3)
    # Draw keypoints and edges on input image
    image, center = drawBoxAndGetCenter(image, detection_result)

    if center[0]<start_point[0]:
      direction = "Right"
      control.condition_yaw(vehicle,0)
    elif center[0]>end_point[0]:
      direction = "Left"
      control.condition_yaw(vehicle,-40)
    elif center[1]<start_point[1]:
      direction = "Up"
      control.send_ned_velocity(vehicle,1,0,0)
    elif center[1]>end_point[1]:
      direction = "Down"
      control.send_ned_velocity(vehicle,-1,0,0)
    else:
      direction = "None"
      control.send_ned_velocity(vehicle,0,0,0)
      return 

    # Calculate the FPS
    if counter % fps_avg_frame_count == 0:
      end_time = time.time()
      fps = fps_avg_frame_count / (end_time - start_time)
      start_time = time.time()

    # Show the FPS
    fps_val = 'FPS = {:.1f}'.format(fps)
    
    fps_text = direction + ' ' + fps_val
    
    text_location = (left_margin, row_size)
    cv2.putText(image, fps_text, text_location, cv2.FONT_HERSHEY_PLAIN,
                font_size, text_color, font_thickness)

    # Stop the program if the ESC key is pressed.
    if cv2.waitKey(1) == 27:
      break
    cv2.imshow('object_detector', image)

  cap.release()
  cv2.destroyAllWindows()





