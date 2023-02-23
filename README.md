# skin-lesion-classifiers

This repo includes a few most popular pre trained CNN models to classify dermatoscopic images of common pigmented skin lesions from [HAM10000](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000) dataset and data processing operations to balance images from different classes. Vision Transformers (ViT) and accuracy results will be uploaded soon!

## Project initialization
 
- Create a folder with a name of `ham_data/splitted_ham10000` in this directory.
- Split the data with [data_util_split.py](https://github.com/robuno/skin-disease-classifiers/blob/master/data_util_split.py) to get `train` and `test` folder. Each folder has subfolders related to the labels.

  cc_data
    ├── train ## training image diretories.
    └── val ## validation image directories.
  cc
    ├── Train_GCC-training_output.csv ## training data list
    └── Validation_GCC-1.1.0-Validation_output.csv ## validation data list

```bash
  ham_data/splitted_ham10000
  ├── train
  └───── akiec
  └───── bcc
  └───── bkl
  └───── df
  └───── mel
  └───── nv
  └───── vasc
  ├── test
  └───── akiec
  └───── bcc
  └───── bkl
  └───── df
  └───── mel
  └───── nv
  └───── vasc
```
  
