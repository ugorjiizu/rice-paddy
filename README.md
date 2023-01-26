#Rice Leaf Image Classification Project#

This project aims to classify rice leaf images using a deep learning model to detect the state of the crop, 
thereby eliminating the need for constant present expertise and manual supervision of the crop.
The model was trained on the dataset (https://www.kaggle.com/competitions/paddy-disease-classification), 
which consists of over 10,000 color images in 10 distinct classes.
This project is accompanied with a react application, which users can use to take a picture of the leaf.
For model deployment, i used a fastapi backend to handle calls and requests, i used docker images to test sub application deployment on a server.
Lastly, i used an amazon web service virtual server to host my application, the server also uses Nginx for reverse proxy operations.
The model was test on images similar to this:
https://pbs.twimg.com/media/FcncYxhWQAMFl49?format=jpg&name=small

#Prerequisites#

Python 3.6 or higher
TensorFlow 2.x
NumPy
Matplotlib
Jupyter Notebook (optional, for running the notebooks)

#Notebooks#

The project includes Jupyter notebooks with step-by-step explanations and visualizations of the model training, evaluation, and prediction process.

#Results#
The model achieved an accuracy of about 90% on the test dataset.

https://pbs.twimg.com/media/Fc9ewK_WIAAQXf5?format=jpg&name=small
![image](https://user-images.githubusercontent.com/66518563/214965977-93afd086-328f-4e24-a919-65c7e4b58bd5.png)
https://pbs.twimg.com/media/FcrtNnFWYAIL4Xt?format=jpg&name=large

