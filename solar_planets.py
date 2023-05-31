import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Mercury",
            (100,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Venus",
            (290,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Earth",
            (410,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Mars",
            (590,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Jupiter",
            (710,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Saturn",
            (900,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Uranus",
            (1000,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Neptune",
            (1070,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.imshow("output", img)
cv2.waitKey(0)

cv2.imwrite("Solar-systemwithname.jpg",img)
