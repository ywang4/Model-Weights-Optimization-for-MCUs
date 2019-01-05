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
  
## Tasks
### 1. Input file
* Read the weights and model structure respectively from a HDF5 file (1/18)
### 2. Modify weights
* Modify weights using quantization (2/1)
* Save the new weights in a HDF5 file which is readable by keras and tensorflow (2/15)
### 3. Test
* Test the performance of the new model (3/1)