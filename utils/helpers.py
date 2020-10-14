import numpy as np
import torch
import glob

IMG_SCALE = 1.0 / 255
IMG_MEAN = np.array([0.435, 0.390, 0.383]).reshape((1, 1, 3))
IMG_STD = np.array([0.318,  0.294, 0.3]).reshape((1, 1, 3))


def maybe_download(model_name, model_url, model_dir=None, map_location=None):
    import os
    import sys
    from six.moves import urllib

    if model_dir is None:
        torch_home = os.path.expanduser(os.getenv("TORCH_HOME", "~/.torch"))
        model_dir = os.getenv("TORCH_MODEL_ZOO", os.path.join(torch_home, "models"))
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
    filename = "{}.pth.tar".format(model_name)
    cached_file = os.path.join(model_dir, filename)
    if not os.path.exists(cached_file):
        url = model_url
        sys.stderr.write('Downloading: "{}" to {}\n'.format(url, cached_file))
        urllib.request.urlretrieve(url, cached_file)
    print("ok: ", cached_file, map_location)
    print(glob.glob('/root/.torch/models/'))
    return torch.load(cached_file, map_location=map_location)


def prepare_img(img):
    return (img * IMG_SCALE - IMG_MEAN) / IMG_STD
