# import the necessary packages
import imutils
import cv2

# load the input image and show its dimensions, keeping in mind that images are represented as multi-dimensional Numpy array with
# shape no. rows (height), no. columns (width), no. channels (depth)

# Reading an image
image = cv2.imread("jp.png")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

#Displaying an image
# display the image to our screen -- we will need to click the window
# open by opencv and press a key on our keyboard to continue execution
cv2.imshow("Image", image)
cv2.waitKey(0)

# Accessing the pixel values of an image
# access the RGB pixel located at x=50, y=100, keep in mind that
# OpenCV stores images in BGR order rather than RGB
(B, G, R) = image[100, 50]
print("R={}, G={}, B={}".format(R, G, B))

#Extracting ROI from image
# extract a 100x100 pixel square ROI (Region of Interest) from the
# input image starting at x=320, y=60 and ending at x=420, y=160
roi = image[60:160, 320:420]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

# Resiging images
# resize the images to 200x200 pixels ignoring the aspect ratio
resized = cv2.resize(image, (200, 200))
cv2.imshow("Resized", resized)
cv2.waitKey(0)
#fixed resizing and distorted aspect ratio so lets resize the width
# to be 300px but compute the new height based on aspect ratio
r = 300.0/w
dim = (300, int(h*r))
resized = cv2.resize(image, dim)
cv2.imshow("Aspect Ratio Resized", resized)
cv2.waitKey(0)
# manually computing the aspect ratio can be apin so let us use the imutils library instead
resized = imutils.resize(image, width=300)
cv2.imshow("Imutils Resized", resized)
cv2.waitKey(0)

# Rotating and image
# Lets rotate an image 45 degrees clockwise using OpenCV by first
# computing the image center, then constructing the rotation matrix
# and then finally applying the affine warp
center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("OpenCV Rotation", rotated)
cv2.waitKey(0)
# rotation can also be easily accomplished via imutils using less code
rotated = imutils.rotate(image, -45)
cv2.imshow("Imutils Rotation", rotated)
cv2.waitKey(0)
# OpenCV dosent "care" if our rotated image is clipped after rotation
# so we can instead use another imutils convienience function to help us out
rotated = imutils.rotate_bound(image, 45)
cv2.imshow("Imutils Bound Rotation", rotated)
cv2.waitKey(0)

# Smoothening an image
# apply a gausian blur with a 11x11 kernel to the image to smooth it,
# useful when reducing high frequency noise
blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)

# Drawing on a image
# draw a 2px thick rectangle sourounding the face
output = image.copy()
cv2.rectangle(output, (320, 60), (420, 160), (0, 0, 255), 2)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)
# draw a blue 20px (filled in) circle on the image centered at
# x=300, y=150
output = image.copy()
cv2.circle(output, (300, 150), 20, (255, 0, 0), -1)
cv2.imshow("Circle", output)
cv2.waitKey(0)
#draw a 5px thick red line from x=60, y=20 to x=400, y=200
output = image.copy()
cv2.line(output, (60, 20), (400, 200), (0, 0, 255), 5)
cv2.imshow("Line", output)
cv2.waitKey(0)
# draw green text on the image
output = image.copy()
cv2.putText(output, "OpenCV + Jurasic Park!!!", (10, 20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)