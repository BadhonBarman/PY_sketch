# import cv2

# img_location = 'C:/Users/Badhon Barman/Desktop'
# filename = 'my3.jpg'

# img = cv2.imread(img_location+filename)

# cv2.imshow('Original Image', img)
# cv2.waitKey(0)


import cv2

image=cv2.imread("C:/Users/Badhon Barman/Desktop/import.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
inverted= 255-gray_image
blurred=cv2.GaussianBlur(inverted,(21,21),0)
invertedblur=255-blurred
pencilsketch = cv2.divide(gray_image, invertedblur, scale = 245.0)

cv2.imwrite("C:/Users/Badhon Barman/Desktop/save.jpg", pencilsketch)

