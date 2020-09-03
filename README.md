This is a Python application that reads a `images.csv` file in the format of:
| image1 | image2 |
| ------ | ------ |
| image1 | image2 |

It then reads the files from the `images/` folder to find the images corresponding to the `images.csv` file. 

After some research I found that Python has a library that compares images using 2 different algorithims. One is MSE (Mean Squared Error) and SSIM(Structural Similarity Index). SSIM was the one I went with because it was more accurate and had a more easy to understand scoring scale. In order to write/read a csv the `csv` library in python is a powerful library that allows you to easily read/write to a csv, by even using arrays. 

Some improvements can be made to the program such as more robust error checking incase the files in the `images/` folder are not available or if they arent proper image files. Also more error checking when reading the csv file, in case it is improper format. 

In order to use this program be sure to:
1. Store image files in `images/` folder
2. install the `scikit-image` library using:
    `pip3 install scikit-image opencv-python imutils`

