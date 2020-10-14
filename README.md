# Ear_Detection
Ear Detection in videos via a light weights ResNet-based network (RefineNet)

# Usage

- Please set your demanded video path in "cap = cv2.VideoCapture('input1.mp4')"
- Please Consider that vertical head orientation has a huge impact on the results, therefore, rotate your video wit "framet = cv2.rotate(frames, cv2.ROTATE_90_CLOCKWISE)", if the head direction is horizontal in you video. If you utilize the rotation, you should change the original size axes, like this "out = cv2.VideoWriter('output.avi', fourcc, 5.0, (270, 360))".


# Reference Paper:
  - https://doi.org/10.1007/978-3-030-03000-1_14
# Reference Codes:
  - https://github.com/DrSleep/light-weight-refinenet.git
