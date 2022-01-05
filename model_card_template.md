# Model Card



## Model Details
Brian K created the model. It is logistic regression using the default hyperparameters in scikit-learn. This model can predict whether income exceeds $50K/yr based on census data. Also known as "Adult" dataset.



## Intended Use

This model should be used to predict the acceptability of a car based off a handful of attributes. The users are prospective car buyers.

Predict whether income exceeds $50K/yr based on census data. Also known as "Adult" dataset.



## Data

The data was obtained from the UCI Machine Learning Repository (https://archive.ics.uci.edu/ml/datasets/census+income). The target class was modified from four categories down to two: "unacc" and "acc", where "good" and "vgood" were mapped to "acc".

The original data set has 1728 rows, and a 75-25 split was used to break this into a train and test set. No stratification was done. To use the data for training a One Hot Encoder was used on the features and a label binarizer was used on the labels.

## Metrics

The model was evaluated using F1 score. The value is 0.8960.
