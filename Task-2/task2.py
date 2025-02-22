import cv2
#
# #Aynı görüntüyü gri tonlamaya çevirip kaydet.
# img = cv2.imread('../Img/bus.jpg')
# resized = cv2.resize(img, (400, 400))
# greyimg = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
# # Save the grayscale image
# cv2.imwrite('grey_image.jpg', greyimg)
#
# cv2.imshow('Grayscale Image', greyimg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




#Görüntüyü yeniden boyutlandır ve döndür.
#Görüntüye bir dikdörtgen ve metin ekle.

# img = cv2.imread('../Img/bus.jpg')
# resized = cv2.resize(img, (400, 400))

# (h, w) = resized.shape[:2]
# center = (w // 2, h // 2)
# M = cv2.getRotationMatrix2D(center, 45, 1.0)
# rotated = cv2.warpAffine(resized, M, (w, h))
#
# # Draw a rectangle on the image
# cv2.rectangle(rotated, (50, 50), (300, 300), (0, 255, 0), 2)
#
# # Add text to the image
# cv2.putText(rotated, 'Sample Text', (60, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
#
# cv2.imshow('Transformed Image', rotated)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#Gaussian Blur uygula.
#Kenarları belirginleştir (cv2.Canny()).

# blurred = cv2.GaussianBlur(resized, (5, 5), 0)
# # Find the edges of the image
# edged = cv2.Canny(blurred, 50, 150)
# cv2.imshow('Edged Image', edged)
# cv2.waitKey(0)

#Renk bazlı maskeleme yap.
#Görseldeki konturları tespit et ve çiz.

img = cv2.imread('../Img/bus.jpg')
resized = cv2.resize(img, (400, 400))
hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (0, 50, 50), (10, 255, 255))
res = cv2.bitwise_and(resized, resized, mask=mask)
cv2.imshow('Result', res)
cv2.waitKey(0)


#OpenCV’nin hazır haarcascade_frontalface_default.xml modelini kullanarak yüzleri algıla.
#Algılanan yüzleri dikdörtgen içine al.
#LİNK https://github.com/Fase2507/Odak-analisti