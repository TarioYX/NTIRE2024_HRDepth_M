import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

image_path = 'data/Booster-test'
mask_path = 'data/mask'
save_path = 'data/Booster'

#读取文件夹中的图片文件名
folder_list = os.listdir(image_path)
second_list = ['camera_00']


for folder in folder_list:

    mask = cv2.imread(os.path.join(mask_path, folder + '.png'))
    mask_gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    _, mask_binary = cv2.threshold(mask_gray, 127, 255, cv2.THRESH_BINARY)
    image_list = os.listdir(os.path.join(image_path, folder, 'camera_00'))
    for image_name in image_list:
        image = cv2.imread(os.path.join(image_path, folder, 'camera_00', image_name))

        gaussian_blurred = cv2.GaussianBlur(image, (0,0), sigmaX=100, sigmaY=100)
        gaus_final_image = np.where(mask_binary[:, :, None] == 255, gaussian_blurred, image)
        save_folder_path = os.path.join(save_path, folder, 'camera_00')
        if not os.path.exists(save_folder_path):
            os.makedirs(save_folder_path)
        cv2.imwrite(os.path.join(save_folder_path, image_name), gaus_final_image)
    print(f'Folder {folder} has been processed and saved to {save_folder_path}')




