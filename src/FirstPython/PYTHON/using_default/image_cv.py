import cv2
#이미지 파일을 읽어온다.

# 이미지 파일을 읽습니다
image = cv2.imread('image.jpg')

# 이미지를 흑백으로 변환합니다
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 변환된 이미지를 저장합니다
cv2.imwrite('gray_image.jpg', gray_image)

# 흑백 이미지 출력
cv2.imshow('Gray Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


