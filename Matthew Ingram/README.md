# Image Classification of Food Items

Name: Matthew Ingram

Date: November 3, 2025

My project for this semester is to create an image classification model which can be given an input of an image of a food item (of various types), and then attempt to classify that food item.

This project uses a modified version of the "Food Image Classification Dataset" available on Kaggle at the following link:
https://www.kaggle.com/datasets/harishkumardatalab/food-image-classification-dataset

The modifications of the dataset relate to renaming the topmost folder to "Food Dataset", and making all of the food folders/directories have uniform naming conventions, stripping out underscores and converting all names to lowercase. The exact names used for the folders can be found in the initial values of the "food_types" list.

This project is based on the "Digit_Recognition.ipynb" lab.

The final results of this project are that the model was only able to get an accuracy of 0.3750, and a val_accuracy of 0.4121. I would assume that due to the learning plateau experienced by the model, it is either suffering from overfitting, or underfitting. The model was able to correctly predict some of the food images that I got from other sources than the training data, but it also failed to correctly predict results quite often.
