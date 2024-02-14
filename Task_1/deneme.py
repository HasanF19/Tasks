# -*- coding: utf-8 -*-
import cv2 
resim = cv2.imread("indir.jpeg")
cv2.imshow("deneme",resim)
cv2.waitKey(0)
siyahbeyazresim = cv2.imread("indir.jpeg", 0 )
cv2.imshow("siyahbeyazdeneme",siyahbeyazresim)
cv2.waitKey(0)
