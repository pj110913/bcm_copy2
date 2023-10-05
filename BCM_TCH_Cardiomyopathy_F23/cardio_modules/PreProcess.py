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
        image_spec = image.convert('L')
        
        image_spec_arr = np.array(image_spec)
        
        image_spec_dist = image_spec_arr.sum(axis=1)
        
        return image_spec_dist

    def plot_horizontal_intensity(self, image):
        """
        Plot above
        """
        plt.figure(figsize=(6,10))
        plt.barh(range(len(image_spec_dist)), image_spec_dist, height=1)
        plt.gca().invert_yaxis()
        plt.title('intensity_distribution')
        plt.ylabel('y axis same as image height')
        plt.xlabel('Sum of pixel values of x axis')
        plt.grid(False)
        
        return plt.show()

    def crop_image_by_intensity(self, image, image_path, lower_percentile, upper_percentile):
        """
        Calculate the 2th and 98th percentile of the horizontal intensity distribution,
        crop the spectrogram image (on y-axis/height)
        """
        image_intensity = np.cumsum(image_spec_dist)
        image_height = image_intensity[-1]
        top = np.searchsorted(image_intensity, image_height*upper_percentile)
        bottom = np.searchsorted(image_intensity, image_height*lower_percentile)
        
        image_cropped_byint = image.convert('L').crop((0,bottom, image.convert('L').width, top))
        """
        save image
        """
        return image_cropped_byint.save(image_path[:-4] + "_cropped" + image_path[-4:])

   def interpolate_height(self, image, standard_height):
        """
        Set a standard height, interpolate all spectrogram images to this same height
        """
        image_cropped_byint_arr = np.array(image)
        width, height = image.size
        # height_standard = 500
        
        y=np.linspace(0, height-1, height)
        y_new = np.linspace(0, height-1, standard_height)
        
        image_cropped_interpolated_arr = np.zeros((standard_height, width), dtype=np.unit8)
        
        for w in range(width):
            f = interp1d(y, image_cropped_byint_arr[:,w], kind='linear', fill_value="extrapolate")
            image_cropped_interpolated_arr[:,w] = f(y_new)
        
        image_cropped_interpolated_image = Image.fromarry(image_cropped_interpolated_arr)
        
        return plt.show()

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
