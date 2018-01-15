import os
import scipy.misc
import numpy as np

def read_images(path):
    imlist = []
    count = 1
    for filename in os.listdir(path):
        imlist.append(scipy.misc.imread(os.path.join(path, filename)))
        count += 1
        if count > 4000:
            break
    array = np.array(imlist).astype('float32')/255.0
    #array = (array-np.mean(array))/np.var(array)
    return array

def aug_images(path,aug_path,save=False):
    data_images = read_images(path)

    ata_min = np.min(data_images)
    aug_data_images = data_images-data_min
    data_max = np.max(aug_data_images)
    aug_data_images = aug_data_images/data_max
    aug_data_images = (aug_data_images-0.5)*2

    if save:
        for i in range(aug_data_images.shape[0]):
            sio.savemat(aug_path + '\%0.3d.mat' % i, {'img_raw':aug_data_images[i]})
    else:
        return aug_data_images