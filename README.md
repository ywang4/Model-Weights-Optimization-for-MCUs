# Model-Weights-Optimization-for-MCUs

## Goal
To create a stand alone program that can input machine learning model and weight files and output the smallest weight 
file with highest performance for MCUs.

## Prerequisites & Constraints
 **Input file:** A HDF5 file with the saved keras model and its weights. The model and its weights should be saved using 
 the following command:
```python
keras.models.save_model(model, "model.h5")
```
  
## TODO LISTS
### 1. Visualization

### 2. Read&Save weight and model files

### 3. Manipulation and Optimization
