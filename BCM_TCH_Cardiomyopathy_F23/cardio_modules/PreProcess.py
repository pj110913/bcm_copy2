import os
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
from scipy.interpolate import interp1d
from cardio_modules.ImageTypes import IMAGE_TYPES_MAP

class PreProcessing:
    def __init__(self):
        """
        """


    def get_patient_data(self, file_path, patient_id):
        """
        Get the raw images for a given patient.

        Input:
            - patient_id: eg 'DDCM-003'

        Output: 
            - a dictionary of images for the patient {image_name: image}
            - make sure image names are consistent with IMAGE_TYPES_MAP
        """        
        patient_path = os.path.join(file_path, patient_id)
        raw_image_names = os.listdir(patient_path)
        raw_image_names = [image[:-4] for image in raw_image_names if image.lower().endswith('.jpg')]
        # print('Patient {} has images: {}'.format(patient_id, raw_image_names))

        def get_mapped_name(image_name):
            for key, values in IMAGE_TYPES_MAP.items():
                if image_name in values:
                    return key
            raise ValueError('image {} not found in IMAGE_TYPES_MAP'.format(image_name))

        patient_data = {}
        for image_name in raw_image_names:
            image_path = os.path.join(patient_path, image_name + '.jpg')
            image_key = get_mapped_name(image_name)
            image = Image.open(image_path)
            patient_data[image_key] = image

        return patient_data


    @staticmethod
    def crop_image(image, crop_size):
        """
        Crop image.

        Input:
            - crop_size: (x_0, y_0, x_1, y_1)
            - define crop size in ImageTypes.py

        return the cropped image
        """
        cropped_image = image.crop(crop_size)

        return cropped_image


    def calculate_horizontal_intensity(self, image):
        """
        Sum intensity of x for each y, only for spectrogram image.
        """
        pass

    def plot_horizontal_intensity(self, image):
        """
        Plot above
        """
        pass

    def crop_image_by_intensity(self, image, lower_percentile, upper_percentile):
        """
        Calculate the 5th and 95th percentile of the horizontal intensity distribution,
        crop the spectrogram image (on y-axis/height)
        """
        pass

    def interpolate_height(self, image, standard_height):
        """
        Set a standard height, interpolate all spectrogram images to this same height
        """
        pass

    def extract_waves(self, image):
        """
        Extract the waves from the image based on color
        """
        pass

    def segment_ecg(self, image):
        """
        Segment the ECG from the image. Do not know how to do this yet.
        """
        pass
