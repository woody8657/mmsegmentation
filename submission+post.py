import os
import cv2
import numpy as np
import tqdm
import glob

if __name__ == '__main__':

    folder_list = glob.glob('./hidden_mask/**/**/')

    for folder in tqdm.tqdm(folder_list):
        conf_list = []
        for i in range(10000000):
            tmp = np.zeros((480, 640, 3))
            try:
                m = cv2.imread(folder+str(i)+'.png', cv2.IMREAD_GRAYSCALE)
          
                m[m!=0] = 1
                idx = np.where(m!=0)
                tmp[idx[0],idx[1],:] = np.array([255, 0, 255])
                
                # conf = (m!=0).sum() / 1500
                # if conf>=1:
                #     conf_list.append(1)
                #     cv2.imwrite(folder+str(i)+'.png', tmp)
                # else:            
                #     conf_list.append(conf)
                #     cv2.imwrite(folder+str(i)+'.png', tmp)
                
                params = cv2.SimpleBlobDetector_Params()
                params.minRepeatability = 1
                params.minDistBetweenBlobs = 1
                # Set Area filtering parameters
                params.filterByArea = False
                # params.minArea = 200
                # params.maxArea = 25000
                
                # Set Circularity filtering parameters
                params.filterByCircularity = False
                # params.minCircularity = 0
               
                
                # # Set Convexity filtering parameters
                params.filterByConvexity = False
                # params.minConvexity = 0.02
                    
                # Set inertia filtering parameters
                params.filterByInertia = False
                # params.minInertiaRatio = 0.01
                
                # Create a detector with the parameters
                detector = cv2.SimpleBlobDetector_create(params)
                    
                # Detect blobs
                keypoints = detector.detect((1-m)*255)
                
                # Draw blobs on our image as red circles
                blank = np.zeros((1, 1))
                # blobs = cv2.drawKeypoints(tmp, keypoints, blank, (0, 0, 255),
                #                         cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                # cv2.imwrite(folder+str(i)+'.png', tmp)
                number_of_blobs = len(keypoints)
                text = "Number of Circular Blobs: " + str(len(keypoints))
                print(folder+str(i)+'.png')
                print(text)
                 
                if number_of_blobs>=1:
                    conf_list.append(1)
                    cv2.imwrite(folder+str(i)+'.png', tmp)
                else:            
                    conf_list.append(0)
                    cv2.imwrite(folder+str(i)+'.png', np.zeros((480, 640, 3)))
                
            except:
                break
        
        conf_list = [str(conf) for conf in conf_list]
        path = folder + 'conf.txt'
        f = open(path, 'w')
        f.writelines('\n'.join(conf_list))
        f.close()
        