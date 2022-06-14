import argparse
import os
import cv2
import numpy as np
import tqdm
import glob

def post(folder_list):
    for folder in tqdm.tqdm(folder_list):
        conf_list = []
        for i in range(10000000):
         
            # try:
            if folder == './challenge/HM/':
                m = cv2.imread(folder+"{:0>2d}".format(i+1)+'.png', cv2.IMREAD_GRAYSCALE)
            elif folder == './challenge/KL/':
                m = cv2.imread(folder+"{:0>4d}".format(i)+'.png', cv2.IMREAD_GRAYSCALE)
            else:
                m = cv2.imread(folder+str(i)+'.png', cv2.IMREAD_GRAYSCALE)
    
            tmp = np.zeros((m.shape[0], m.shape[1], 3))
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
            params.filterByArea = True
            params.minArea = 500
            # params.maxArea = 25000
            
            # Set Circularity filtering parameters
            params.filterByCircularity = True
            params.minCircularity = 0.7
            
            
            # # Set Convexity filtering parameters
            params.filterByConvexity = False
            params.minConvexity = 0.9
                
            # Set inertia filtering parameters
            params.filterByInertia = False
            # params.minInertiaRatio = 0.01
            
            # Create a detector with the parameters
            detector = cv2.SimpleBlobDetector_create(params)
                
            # Detect blobs
            keypoints = detector.detect((1-m)*255)
            
            # Draw blobs on our image as red circles
            text = "Number of Circular Blobs: " + str(len(keypoints))
            blank = np.zeros((1, 1))
            m = cv2.drawKeypoints((1-m)*255, keypoints, blank, (0, 0, 255),
                                    cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            
            if len(keypoints)>0:
                print(keypoints[0].size)
            cv2.putText(m, text, (20, 550),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)
            number_of_blobs = len(keypoints)
        
            print(folder+str(i)+'.png')
            print(text)
                
            if number_of_blobs>=1:
                conf_list.append(1)
                cv2.imwrite(folder+str(i)+'.png', m)
            else:            
                conf_list.append(0)
                cv2.imwrite(folder+str(i)+'.png', np.zeros((m.shape[0], m.shape[1], 3)))
            
            # except:
            #     break
        
        conf_list = [str(conf) for conf in conf_list]
        path = folder + 'conf.txt'
        f = open(path, 'w')
        f.writelines('\n'.join(conf_list))
        f.close()
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--dataset', help='S5, hidden, challenge')
    opt = parser.parse_args()
    
    print(opt.dataset)
    if opt.dataset == 'hidden':
        folder_list = glob.glob('./hidden_mask/**/**/')
    elif opt.dataset == 'S5':
        folder_list = glob.glob('./S5/**/')
    elif opt.dataset == 'challenge':
        folder_list = glob.glob('./challenge/**/')
    else:
        pass
    print(folder_list)
    
    post(folder_list)
    
    