**Rice Leaf Image Classification Project**

This project aims to classify rice leaf images using a deep learning model to detect the state of the crop, 
thereby helping provide expertise and eliminating the need for manual supervision of the crop.
The model was trained on the dataset (https://www.kaggle.com/competitions/paddy-disease-classification), 
which consists of over 10,000 color images in 10 distinct classes.
This project is accompanied with a react application, which users can use to take a picture of the leaf.
For model deployment, i used a fastapi backend to handle calls and requests, i used docker images to test sub application deployment on a server.
Lastly, i used an amazon web service virtual server to host my application, the server also uses Nginx for reverse proxy operations.
The model was test on images similar to this:

![image](https://user-images.githubusercontent.com/66518563/214966450-bd2e49f6-ac36-48f9-bc0b-b8b97506c495.png)

**Prerequisites**

Python 3.6 or higher
TensorFlow 2.x
NumPy
Matplotlib
Jupyter Notebook (optional, for running the notebooks)


**Installation**

Clone the repository:
git clone https://github.com/ugorjiizu/rice-paddy.git

To train the model:

I suggest following the notebook and going from there or you can use the already made model in the api folder.
For more information check the api and frontend folders

**Notebooks**

The project includes Jupyter notebooks with step-by-step explanations and visualizations of the model training, evaluation, and prediction process.

**Results**

The model achieved an accuracy of about 90% on the test dataset.

![image](https://user-images.githubusercontent.com/66518563/214966510-c6174877-26f1-4a52-9262-1096eda821a1.png)
![image](https://user-images.githubusercontent.com/66518563/214966622-87e65a9d-6ad9-472d-9f1f-c28bc69a01ac.png)
![image](https://user-images.githubusercontent.com/66518563/214965977-93afd086-328f-4e24-a919-65c7e4b58bd5.png)


