import os
import glob
import cv2
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

def single_pair(path, count, split):
    img = cv2.imread(path + '.jpg')
    mask = cv2.imread(path + '.png', cv2.IMREAD_GRAYSCALE)
    mask[mask!=0] = 1
    
    # cv2.imwrite(os.path.join('./data/ade/ADEChallengeData2016/images/', split, str(count)+'.jpg'), img)
    # cv2.imwrite(os.path.join('./data/ade/ADEChallengeData2016/annotations/', split, str(count)+'.png'), mask)
    return np.sum(mask)

if __name__ == '__main__':
    os.makedirs("./data/ade/ADEChallengeData2016/images/training", exist_ok = True) 
    os.makedirs("./data/ade/ADEChallengeData2016/annotations/training", exist_ok = True) 
    os.makedirs("./data/ade/ADEChallengeData2016/images/validation", exist_ok = True) 
    os.makedirs("./data/ade/ADEChallengeData2016/annotations/validation", exist_ok = True) 
    file_list = (glob.glob(r"/home/u/woody8657/projs/dataset/public/S1/**/*.jpg") + 
                glob.glob(r"/home/u/woody8657/projs/dataset/public/S2/**/*.jpg") + 
                glob.glob(r"/home/u/woody8657/projs/dataset/public/S3/**/*.jpg") + 
                glob.glob(r"/home/u/woody8657/projs/dataset/public/S4/**/*.jpg"))
    file_list = [file[:-4] for file in file_list]
    train, val = train_test_split(file_list, random_state=777, train_size=0.8)
    num_pulpil_list = []
    for count, path in enumerate(val):
        print(f"processing {count}th image...")
        num_pulpil = single_pair(path, count, 'validation')
        num_pulpil_list.append(num_pulpil)
    for count, path in enumerate(train):
        print(f"processing {count}th image...")
        num_pulpil = single_pair(path, count, 'training')
        num_pulpil_list.append(num_pulpil)
        
    num_pulpil_list = [i  for i in num_pulpil_list if i!=0] 
    n, bins, patches=plt.hist(num_pulpil_list)
    print(f"Number of pixels that are labeled as pupil per image")
    np.array(num_pulpil_list)
    plt.xlabel("number of pixels")
    plt.ylabel("#")
    plt.title('')
    plt.savefig(f"Histogram")
    np.array(num_pulpil_list)
    
   
    
   