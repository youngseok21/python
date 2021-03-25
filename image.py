# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 22:50:01 2021

@author: dudtj
"""

import cv2
import glob
output = glob.glob('dir/*.jpg')
    print(output)

def res_all_img():
    h_new = 300
    w_new = 300
    
def check():
    fname_new1 = "galaxy_resized_g.jpg"
    fname_new2 = "galaxy_resized_c.jpg"
    
if fname == 'galaxy'
    
main():
    img_gray = cv2.imread(fname, 0)
    img_color = cv2.imread(fname, 1)

    img_gnew = cv2.resize(img_gray, (w_new, h_new))
    img_cnew = cv2.resize(img_color, (w_new, h_new))
    
    cv2.imshow('Gray', img_gnew)
    cv2.imshow('Color', img_cnew)
    
    cv2.imwrite(fname_new1, img_gnew)
    cv2.imwrite(fname_new2, img_cnew)
    
    cv2.waitKey(2000)
    cv2.destroyAllWindows()