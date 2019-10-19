#!/usr/bin/env python3
# GitHub: karabin1
import sys
import numpy as np
import cv2

def draw():
    print('dimensions of the pallet 800x1200 [mm]')
    # dimensions of the pallet
    l_pal = 1200
    w_pal = 800
    
    # initialization window and drawing parameters
    color = (255, 0, 0) 
    thickness = 2   
    img = np.zeros((w_pal, l_pal, 3), dtype = "uint8")

    # get box dimensions from the user
    l, w = input("box length and width [mm]: \n").split()
    l = int(l)
    w = int(w)

    # the total number of boxes in a given dimension
    l_0deg  = int(l_pal/l)
    w_0deg  = int(w_pal/w)
    l_90deg = int(l_pal/w)
    w_90deg = int(w_pal/l) 

    print('Number of items for 0deg  =', (l_0deg*w_0deg), '\nNumber of items for 90deg =', (l_90deg*w_90deg))
    print("coordinate: x, y , rotation angle: ")

    # calculation of the optimal place for the angle of rotation of a boxes equal to 0 or 90 degrees
    if (l_0deg*w_0deg) > (l_90deg*w_90deg) or (l_0deg*w_0deg) == (l_90deg*w_90deg):         # 0 deg
        l_offset = int((l_pal-l_0deg*l)/2)                                                  # offset for width pallet 
        w_offset = int((w_pal-w_0deg*w)/2)                                                  # offset for length pallet  

        for j in range(w_0deg):                                                             # loop for width pallet 
            for i in range(l_0deg):                                                         # loop for length pallet 
                cv2.rectangle(img, (l*i+l_offset, w*j+w_offset), (l*(i+1)+l_offset, w*(j+1)+w_offset), color, thickness)    # rysowanie kartonu
                coordinate = (l*(i+1)+l_offset-l/2, w*(j+1)+w_offset-w/2, 0)                                                # obliczanie wspolrzednych (srodka kartonu i kata obrotu)
                cv2.circle(img,(int(coordinate[0]),int(coordinate[1])), 2, (0,255,0), -1)                                   # rysowanie punktu we wspolrzednych 
                print(coordinate)                                                                                           # wyswietlanie wpolrzednych 
    else:                                                                                   # 90 deg 
        l_offset = int((l_pal-l_90deg*w)/2)
        w_offset = int((w_pal-w_90deg*l)/2)
        
        for j in range(w_90deg):
            for i in range(l_90deg):
                cv2.rectangle(img, (w*i+l_offset, l*j+w_offset), (w*(i+1)+l_offset, l*(j+1)+w_offset), color, thickness)
                coordinate = (w*(i+1)+l_offset-w/2, l*(j+1)+w_offset-l/2, 90)
                cv2.circle(img,(int(coordinate[0]),int(coordinate[1])), 2, (0,255,0), -1)
                print(coordinate)

    cv2.imshow('Window', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    try:
        draw()
    except KeyboardInterrupt:
        print("Stop")
        