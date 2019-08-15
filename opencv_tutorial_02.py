# importing the necessary package
import argparse
import imutils
import cv2

# constructing the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help = "path to input image")
args = vars(ap.parse_args())

# Converting an image to a grayscale
# load the input image whose path was provided via command line
# argument) and display the image to our screen
image = cv2.imread(args['image'])
cv2.imshow("Image", image)
cv2.waitKey(0)
# convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)

# Edge Detection
# applying edge detection we can find the outlines of an object in images
edged = cv2.Canny(gray, 30, 150)
cv2.imshow("Edged", edged)
cv2.waitKey(0)

# Thresholding
# threshold the image by setting all pixel values less than 255
# to 255 (white; foreground) and all pixel values >= 255 to 255
# (black; background), thereby segmenting the image
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)

# Detecting and drawing contours
# find contours (i.e outlines) of the foreground objects in the threshold image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = image.copy()
# loop over the countours
for c in cnts:
    # draw each contour on the output with a 3px thick purple line
    # outline, then display output contours at one time
    cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
    cv2.imshow("Contours", output)
    cv2.waitKey(0)

# draw the total number of contours found in purple
text = "I found {} objects!".format(len(cnts))
cv2.putText(output, text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
            (240, 0, 159), 2)
cv2.imshow("Contours", output)
cv2.waitKey(0)

# we apply erosions to reduce the size of foreground objects
mask = thresh.copy()
mask = cv2.erode(mask, None, iterations=5)
cv2.imshow("Eroded", mask)
cv2.waitKey(0)

# masking and bitwise operations
# a typical operation we may 
