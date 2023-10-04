"""
Use this file to store data types and other global variables.
"""

# all image types
IMAGE_TYPES = ['bullet', 'mv', 'pulmvein', 'trjet', 'tdilat', 'tdimed',
               'lasa2', 'lasa4', 'vstrain2', 'vstrain3', 'vstrain4']


IMAGE_TYPES_MAP = {
    'mv': ['mv'], 
    'pulmvein': ['pulmvein'], 
    'tdilat': ['tdilat'],
    'tdimed': ['tdimed'],
    'trjet': ['trjet'],
    'lasa2': ['lasa2c'], 
    'lasa4': ['lasa4c', 'lasap4'], 
    'vstrain2': ['vstrain2c', 'vstraina2c', 'vstrainap2'],
    'vstrain3': ['vstrainap3'],
    'vstrain4': ['vstraina4c', 'vstrainap4', 'vstrain4c'],
    'bullet': ['bullet']
}


# 2 groups + bullet
DOPPLER_SPECTROGRAM = ['mv', 'pulmvein', 'trjet', 'tdilat', 'tdimed']
STRAIN_MAPPING = ['lasa2', 'lasa4', 'vstrain2', 'vstrain3', 'vstrain4']
BULLET = ['bullet']


# crop size for raw images, HOW SHOULD I NAME THESE?
DOPPLER_SPEC_PULSE_SIZE = (49, 200, 910, 650)
DOPPLER_SPEC_ECG_SIZE = (49, 600, 910, 708)
STRAIN_MAPPING_PULSE_SIZE = (386, 53, 998, 617)
STRAIN_MAPPING_ECG_SIZE = (370, 620, 1010, 700)