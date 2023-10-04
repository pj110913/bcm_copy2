# BCM_TCH_Cardiomyopathy_F23

Objectives:


Team Members:


## Folder Structure
```
├── README.md
├── cardio_modules                              <- modularized code
│   ├── ImageTypes.py
│   ├── PreProcess.py
│   ├── ....
├── tasks                                       <- Demo ipynb or py, import cardio_modules
│   ├── task1_image_count.ipynb
│   ├── task2_crop_raw_img.ipynb
│   ├── pre_process.ipynb
│   ├── ....
├── raw_data                                    <- raw data folder, share on Box, change folder name to "raw_data"
│   ├── D2K - no DICOM
│   │   ├── DDCM-001
|   |   |   ├── xxx.jpg
|   |   |   ├── ....
│   │   ├── ....
│   │   ├── DDCM-119
│   ├── d2k_key.csv
├── processed_data                              <- processed data folder, share on Box
├── output                                      <- output folder, store output files
├── models                                      <- model folder, store trained models
├── ....
```

## Data
We standardize the naming of raw images. The information is stored in `cardio_modules/ImageTypes.py`, and shown below:

<table>
    <tr>
        <th>Image Group</th>
        <th>Image Name</th>
        <th>Image Description</th>
    </tr>
    <tr>
        <td rowspan="6">SPECTROGRAM_IMAGES</td>
        <td>bullet</td>
        <td></td>
    </tr>
    <tr>
        <td>mv</td>
        <td></td>
    </tr>
    <tr>
        <td>pulmvein</td>
        <td></td>
    </tr>
    <tr>
        <td>trjet</td>
        <td></td>
    </tr>
    <tr>
        <td>tdilat</td>
        <td></td>
    </tr>
    <tr>
        <td>tdimed</td>
        <td></td>
    </tr>
    <tr>
        <td rowspan="5">STRAIN_TRACING</td>
        <td>lasa2</td>
        <td>known as lasa2c</td>
    </tr>
    <tr>
        <td>lasa4</td>
        <td>known as lasa4c or lasap4</td>
    </tr>
    <tr>
        <td>vstrain2</td>
        <td>known as vstrain2c or vstraina2c or vstrainap2</td>
    </tr>
    <tr>
        <td>vstrain3</td>
        <td>known as vstrainap3</td>
    </tr>
    <tr>
        <td>vstrain4</td>
        <td>known as vstraina4c or vstrainap4 or vstrain4c</td>
    </tr>
</table>