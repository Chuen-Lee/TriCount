import cv2
import numpy as np
import cvlib as cv
import sys
import argparse
from numpy.lib.polynomial import poly

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="Input File")
parser.add_argument("-o", "--output", help="Output File")
args = parser.parse_args()

img = cv2.imread(args.input,1)
img = cv2.resize(img,(500,500),interpolation = cv2.INTER_AREA)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_blur=cv2.GaussianBlur(gray,(15,15),0)

thresh = cv2.adaptiveThreshold(gray_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,5,4)
kernel=np.ones((1,1),np.uint8)
closing=cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel,iterations=10)
result_img=closing.copy()
# cv2.imshow("Binary",result_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

contours,hierachy=cv2.findContours(result_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
counter=0
for cnt in contours:
    area = cv2.contourArea(cnt)
    if  area <  5  :
    #if area<  300 :
        continue
    counter+=1
    ellipse = cv2.fitEllipse(cnt)
    cv2.ellipse(img,ellipse,(0,255,0),1)

#counter=len(contours)
#cv2.drawContours(img, contours, -1, (0,255,0), 3)
cv2.putText(img,"Beetles="+str(counter),(100,70),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1,cv2.LINE_AA)
output = args.output
cv2.imwrite(output,img)

print('Number of Beetles = '+ str(counter))
