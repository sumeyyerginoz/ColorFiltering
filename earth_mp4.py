import cv2
import numpy as np 

video_capture = cv2.VideoCapture('world.mp4')

print("""Which color filter do you want to apply on World video?
       1 = blue regions of the Earth
       2 = stars in space
       3 = illuminated regions on the Earth
       Select one of these operations and let's filter our video.
       """)

filter_choice = int(input("Enter the number of the color filter you will choose: "))

if filter_choice == 1:
    while True:
        ret, frame = video_capture.read()  
        cv2.imshow("Original Video", frame)
    
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([90,80,80])
        upper_blue = np.array([140,255,255])
      
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
         
        result = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow("Blue Color Filter Result", result)
       
        key = cv2.waitKey(25)
        if key == 27:
            break
        
if filter_choice == 2:
    while True:
        ret, frame = video_capture.read()  
        cv2.imshow("Original Video", frame)
            
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_star = np.array([0, 0, 255])
        upper_star = np.array([180, 10, 255])
              
        mask = cv2.inRange(hsv, lower_star, upper_star)
               
        result = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow("Star Movement", result)
               
        key = cv2.waitKey(25)
        if key == 27:
            break

if filter_choice == 3:
    while True:
        ret, frame = video_capture.read()  
        cv2.imshow("Original Video", frame)
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_light = np.array([20, 0, 0])
        upper_light = np.array([30, 255, 255])    
        
        mask = cv2.inRange(hsv, lower_light, upper_light)
               
        result = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow("Illumination on Earth", result)
        
        key = cv2.waitKey(25)
        if key == 27:
            break

video_capture.release()
cv2.destroyAllWindows()
