# **Background Subtraction**

This project focuses on the removal of cars from roadway videos, an essential topic in the fields of **image processing** and **computer vision**. Removing moving objects like cars from video sequences has wide-ranging applications, including **road safety analysis**, **autonomous driving**, and **special effects in the film industry**.

The aim of this project is to explore different methods for removing cars from videos and demonstrate the impact of **morphological transformations** as preprocessing steps to enhance the effectiveness of car removal techniques.

---

## **Features**

- **Foreground Detection**: Recognizes moving objects in video sequences.
- **Background Subtraction**: Extracts the foreground for further processing using OpenCV methods.
- **Morphological Transformations**: Improves the accuracy of object removal.
- **Algorithm Comparison**: Demonstrates the effectiveness of two popular methods:
  - Mixture of Gaussians (MOG)
  - K-Nearest Neighbors (KNN)

---

## **Technologies Used**

- **Programming Language**: Python
- **Libraries**: OpenCV for image processing and morphological operations.

---

## **Description**

In the field of image processing and computer vision, **foreground detection** is used to recognize and isolate moving objects in video frames. The **background subtraction** method is one of the simplest yet effective techniques for this purpose. After extracting the foreground, **morphological transformations** (e.g., dilation, erosion) are applied to improve the results and refine the removal of moving objects.

This project implements:
1. **Mixture of Gaussians (MOG)** algorithm: Models the background using Gaussian distributions.
2. **K-Nearest Neighbors (KNN)** algorithm: Classifies pixels into foreground or background using spatial and temporal information.

---

## **Screenshots**

### **Original Traffic Video**
A frame from the original video showing traffic with moving cars.

<img src="https://github.com/MateoTokic/Background_subtraction/assets/73400469/8a87bfc7-2af5-4d6f-932c-b0e45b5440d4" alt="Original Traffic Video" width="800"/>

---

### **Background Obtained by MOG Algorithm**
The background extracted using the **Mixture of Gaussians (MOG)** algorithm.

<img src="https://github.com/MateoTokic/Background_subtraction/assets/73400469/b90bd62a-da14-4c95-8104-3454333fedae" alt="Background by MOG Algorithm" width="800"/>

---

### **Background Obtained by KNN Algorithm**
The background extracted using the **K-Nearest Neighbors (KNN)** algorithm.

<img src="https://github.com/MateoTokic/Background_subtraction/assets/73400469/aca0bf33-5e2c-46fb-8767-60f8c0c49b9b" alt="Background by KNN Algorithm" width="800"/>

---

### **Result of Car Removal by MOG Algorithm**
The processed video frame showing the removal of cars using the **MOG algorithm**.

<img src="https://github.com/MateoTokic/Background_subtraction/assets/73400469/2c3d25ef-12b1-4d86-ab4a-b389b0a4140b" alt="Car Removal by MOG Algorithm" width="800"/>

---

### **Result of Car Removal by KNN Algorithm**
The processed video frame showing the removal of cars using the **KNN algorithm**.

<img src="https://github.com/MateoTokic/Background_subtraction/assets/73400469/d0b11709-ce79-4af5-a3e6-39d48d4768c6" alt="Car Removal by KNN Algorithm" width="800"/>

---
