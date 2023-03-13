# skin-lesion-classifiers

This repo includes a few most popular pre trained CNN models to classify dermatoscopic images of common pigmented skin lesions from [HAM10000](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000) dataset and data processing operations to balance images from different classes. Vision Transformers (ViT) and accuracy results will be uploaded soon!

## Project initialization
 
- Create a folder with a name of `ham_data/splitted_ham10000` in this directory.
- Split the data with [data_util_split.py](https://github.com/robuno/skin-disease-classifiers/blob/master/data_util_split.py) to get `train` and `test` folder. Each folder has subfolders related to the labels.

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

## Results

### EfficientNet, 20 epochs, Dropout: 0.1

![eff_b0_acc_loss_20epochs_d10](https://github.com/robuno/skin-disease-classifiers/blob/master/results/eff_b0_drop_10_epoch_20/output.png)

![eff_b0_confmat_20epochs_d10](https://github.com/robuno/skin-disease-classifiers/blob/master/results/eff_b0_drop_10_epoch_20/output2.png)

### EfficientNet, 20 epochs, Dropout: 0.2

![eff_b0_acc_loss_20epochs_d20](https://github.com/robuno/skin-disease-classifiers/blob/master/results/eff_b0_drop_20_epoch_20/output.png)

![eff_b0_confmat_20epochs_d20](https://github.com/robuno/skin-disease-classifiers/blob/master/results/eff_b0_drop_20_epoch_20/output2.png)

### EfficientNet, 20 epochs, Dropout: 0.32

![eff_b0_acc_loss_20epochs_d32](https://github.com/robuno/skin-disease-classifiers/blob/master/results/eff_b0_drop_32_epoch_20/output.png)

![eff_b0_confmat_20epochs_d32](https://github.com/robuno/skin-disease-classifiers/blob/master/results/eff_b0_drop_32_epoch_20/output-2.png)
  
