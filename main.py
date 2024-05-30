import cv2 as cv

img = cv.imread("assets/stock.jpg",-1)
#modes:-1,0,1 for color,grayscale,unchanged resp.

img=cv.resize(img,(500,500))
#we use this function to resize our media by 500*500 in this case

cv.imshow("display",img)
#to display the image with a name in the window written inside quotes

cv.waitKey(0)
#to wait for infinite time for user to press any key
#if we put in there 10 then the window closes automatically after 10seconds

cv.destroyAllWindows()
#after clicking any the window gets closed

