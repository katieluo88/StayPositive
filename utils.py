import torch
import numpy as np


def change_range(img, max_val, min_val=0.):
    """ Rescales image value to [0, max_val].
    """
    rescaled = np.array(img) * (max_val - min_val) / 255. + min_val
    return np.rint(rescaled).astype(int)


def basic_normalization(img):
    # img: (B, channel, H, W)
    minimum = np.amin(img,axis=(0, 1))
    maximum = np.amax(img,axis=(0, 1))
    out = (img - minimum) / (maximum - minimum + 1e-6)  # between [0, 1]
    return out


def change_range_tensor(img, max_val, min_val):
    return img * (max_val - min_val) + min_val


def norm_tensor(x):
    h, w = x.size(0), x.size(1)
    x_min = x.view(-1, 3).min(dim=0, keepdim=True).values.view(1, 1, -1)
    x_max = x.view(-1, 3).max(dim=0, keepdim=True).values.view(1, 1, -1)
    return (x - x_min) / (x_max - x_min)


def norm_numpy(x):
    img_max = 1
    if x.max() > img_max:
        img_max = 255
    x /= float(img_max)
    x_min = x.min(axis=(0, 1), keepdims=True)
    x_max = x.max(axis=(0, 1), keepdims=True)
    out = (x - x_min) / (x_max - x_min)
    x *= float(img_max)
    return x
