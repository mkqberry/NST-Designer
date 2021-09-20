import tensorflow as tf
import numpy as np
import PIL.Image
import os

class StyleTransfer:
    def __init__(self, fpathContent:str, fpathStyle:str):
        self.Content = fpathContent
        self.Style = fpathStyle

    def tensor_to_image(self, tensor):
        tensor = tensor*255
        tensor = np.array(tensor, dtype=np.uint8)
        if np.ndim(tensor)>3:
            assert tensor.shape[0] == 1
            tensor = tensor[0]
        return PIL.Image.fromarray(tensor)
    
    def load_img(self, path_to_img):
        max_dim = 512
        img = tf.io.read_file(path_to_img)
        img = tf.image.decode_image(img, channels=3)
        img = tf.image.convert_image_dtype(img, tf.float32)
        shape = tf.cast(tf.shape(img)[:-1], tf.float32)
        long_dim = max(shape)
        scale = max_dim / long_dim
        new_shape = tf.cast(shape * scale, tf.int32)
        img = tf.image.resize(img, new_shape)
        img = img[tf.newaxis, :]
        return img
    
    def transfer(self, i:int):
        path = os.getcwd()
        fpath = os.path.join(path, "magenta_arbitrary-image-stylization-v1-256_2")
        hub_model = tf.saved_model.load(fpath)
        content_image = self.load_img(self.Content)
        style_image = self.load_img(self.Style)
        stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
        PIL.Image.Image.show(self.tensor_to_image(stylized_image))
        im = self.tensor_to_image(stylized_image)
        ipath = os.path.join(path, "saved_images")
        im.save(os.path.join(ipath, f"image{i}.png"))
