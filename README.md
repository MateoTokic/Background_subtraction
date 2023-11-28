# Background_subtraction

This project is used for the removal of cars from road videos. Removing cars from roadway videos is an important topic in the field of image processing and computer vision. This technique is often used in the automotive industry, mainly in road safety, but also in the film industry for special effects. The aim of the project is to study different methods for removing cars from roadway videos and to show the influence of morphological transformations as pre-processing operations to improve the efficiency of the method.
In the field of image processing and computer vision, the foreground detection technique is used to recognize moving objects. Foreground detection is one of the main tasks aimed at detecting changes in image sequences.
One of the simplest approaches for foreground detection is the background subtraction method, which works on the principle of extracting the foreground of the image for further processing. After successfully extracting the foreground, it is possible to use morphological transformation methods to improve the results of removing objects from the video.
The programming language used to create the project is Python, and the background subtraction methods are taken from the OpenCV library, which also offers different operators for morphological transformation.

Original traffic video:
![image](https://github.com/MateoTokic/Background_subtraction/assets/73400469/8a87bfc7-2af5-4d6f-932c-b0e45b5440d4)

Background obtained by Mixture of Gaussians (MOG) algorithm:
![image](https://github.com/MateoTokic/Background_subtraction/assets/73400469/b90bd62a-da14-4c95-8104-3454333fedae)


Background obtained by K-nearest neighbors (KNN) algorithm:
![image](https://github.com/MateoTokic/Background_subtraction/assets/73400469/aca0bf33-5e2c-46fb-8767-60f8c0c49b9b)



Result of car removal by Mixture of Gaussians(MOG) algorithm:
![image](https://github.com/MateoTokic/Background_subtraction/assets/73400469/2c3d25ef-12b1-4d86-ab4a-b389b0a4140b)

Result of car removal by K-nearest neighbors(KNN) algorithm:
![image](https://github.com/MateoTokic/Background_subtraction/assets/73400469/d0b11709-ce79-4af5-a3e6-39d48d4768c6)
