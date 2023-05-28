# Face_Detection_through_webcam
It is a project to detect faces by drawing rectangle around each face by capturing video from webcam.



# How it works
* Face detection is a technique to find the location of the human faces in an image.The faces are detected through the webcam by creating rectangles around each face.

* It uses conversion to gray scale and hence detecting the faces.

* It works even when we move our face up,down,left and right.


* HOW TO STOP THE WEBCAM AFTER DETECTING THE FACES?-It stops when escape key is pressed.

# Algorithm used- “haarcascade”.
Steps involved in it:
* Haar-feature selection-A Haar-like feature consists of dark regions and light regions. It produces a single value by taking the difference of the sum of the intensities of the dark regions and the sum of the intensities of light regions. 
* Integral images-A given pixel in the integral image is the sum of all the pixels on the left and all the pixels above it. Since the process of extracting Haar-like features involves calculating the difference of dark and light rectangular regions, the introduction of Integral Images reduces the time needed to complete this task significantly.
* AdaBoost Training-This algorithm selects the best features from all features. It combines multiple “weak classifiers” (best features) into one “strong classifier”. The generated “strong classifier” is basically the linear combination of all “weak classifiers”.
* Cascade Classifier-It is a method for combining increasingly more complex classifiers like AdaBoost in a cascade which allows negative input (non-face) to be quickly discarded while spending more computation on promising or positive face-like regions. It significantly reduces the computation time and makes the process more efficient.

Haarcascade file can be download from here: [haarcascade file](https://drive.google.com/file/d/1PPO2MCttsmSqyB-vKh5C7SumwFKuhgyj/view)

# Tech-Stacks used

* Python
* OpenCV
