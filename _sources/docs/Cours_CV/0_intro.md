# Computer Vision
As human we perceive the world using our eyes, by processing those signal in our brain to understand the world. Computer Vision is that task to percieve the world by a machine.
Today computer vision has evolved trememdously and it is used in several different industires. Back in the earlier days of 1970 it was believed that Computer Vision was the beginning to the Artificial General Intelligence. It was mainly dominated by hand crafted mathematical models. Fast forward to the present days, Computer Vision has outperformed the humans in many visual tasks. 

This is an introduction to the field of computer vision. We will cover the basics of computer vision, some of the milestones computer vision algorithms, and some of their applications.

## Contents
The following sections will cover the following topics:
1. Image processing techniques
2. Machine Learning based Computer Vision
3. Convolutional Neural Networks
4. Modern Convolutional Neural Networks
5. Modern Computer Vision tasks

## Some tasks in Computer Vision
This is not an exhaustive list of tasks.
- **Image classification**: the task to classify an image into one of the classes.
- **Object detection**: detection and/or localization of objects in an image.
- **Image segmentation**: the task to segment an image into different regions, based on the content of the image.
- **Image generation**: Such as generating images from texts, transfer the style of an image to another image, etc
- **Key points detection**: the task to detect the key points in an image.
- **3D Computer Vision**: Converting a set of 2D images into a 3D model, etc

## A brief history of computer vision
<figure>
  <img
  src=timeline_intro.jpeg
  alt="Timeline history">
  <figcaption>Figure 1. Few milestones in computer vision</figcaption>
</figure>




**1970s**. The field of computer vision was mainly digital image processing techniques such as improving the image qualities, enhancing the contrast, enhancing the resolution, enhancing the sharpness, enhancing the color, etc[[1]](#1). At the same time the topic of edge and contours detections became an active area of research[[2]](#2). 

**1980s**. One noticeble milestone from our present day view was the introduction of Neocognition[[3]](#3). It was the first time that a Neural Network was used to solve a computer vision problem. Few years later, Convolutional Neural Network was introduced by Yan LeCun[[4]](#4).

**1990s**. Although Neural Network based computer visions models were a step toward Artificial Intelligence, the hardware limitations could not produce satifactory results compared to other techniques. Statistical learnings techniques became a research direction such as eigenfaces for face recognition[[5]](#5). It was an improvement of the previous hand-crafted models. Later on, optimization algorithms became an active area of research to solve computer vision problems. Then gradient based Convolutional Neural Networks LeNet-5 was introduced by Yann LeCun[[6]](#6).

**2000s**. Machine Learning based techniques were introduced to solve computer vision problems. Around 2004 a paper was introduced that implements Neural Networks using GPU[[7]](#7). With the growing number of online images, a dataset called ImageNet was introduced[[8]](#8), which later became a benchmark for computer vision task at that time.

**2010s**. The era of solving computer vision tasks using Neural Networks became popular after the introduction of AlexNet in 2012[[9]](#9). Later on many other Neural Network architecture were introduced that modernized the computer vision field, outperforming any human experts. Unprecedented improvements were made, more than ~10k research paper was written during that time outmatching any of the previous computer vision research era. The field also began to specialize by task, such as object detection, image segmentation, image classification, each having his own subset of tasks. 


This module will only cover some of the milestones work, a detailed study in each of the tasks and sub-tasks will require a full-time study and research. Such as the task of image classification have the sub task of image retrieval.

<figure>
  <img
  src=arvix.png
  alt="submission">
  <figcaption>Figure 2. number of submission where CV stands for computer vision[10]</figcaption>
</figure>


## References
<a id="1">[1]</a> 
Rosenfeld, A. and Pfaltz, J.L., 1966. Sequential operations in digital picture processing. Journal of the ACM (JACM), 13(4), pp.471-494.

<a id="2">[2]</a> 
Davis, L.S., 1975. A survey of edge detection techniques. Computer graphics and image processing, 4(3), pp.248-270.

<a id="3">[3]</a> 
Fukushima, K. and Miyake, S., 1982. Neocognitron: A self-organizing neural network model for a mechanism of visual pattern recognition. In Competition and cooperation in neural nets (pp. 267-285). Springer, Berlin, Heidelberg.

<a id="4">[4]</a>
LeCun, Y., Boser, B., Denker, J.S., Henderson, D., Howard, R.E., Hubbard, W. and Jackel, L.D., 1989. Backpropagation applied to handwritten zip code recognition. Neural computation, 1(4), pp.541-551.

<a id="5">[5]</a>
Turk, M. and Pentland, A., 1991. Eigenfaces for recognition. Journal of cognitive neuroscience, 3(1), pp.71-86.


<a id="6">[6]</a>
LeCun, Y., Bottou, L., Bengio, Y. and Haffner, P., 1998. Gradient-based learning applied to document recognition. Proceedings of the IEEE, 86(11), pp.2278-2324.


<a id="7">[7]</a>
Oh, K.S. and Jung, K., 2004. GPU implementation of neural networks. Pattern Recognition, 37(6), pp.1311-1314.


<a id="8">[8]</a>
Deng, J., Dong, W., Socher, R., Li, L.J., Li, K. and Fei-Fei, L., 2009, June. Imagenet: A large-scale hierarchical image database. In 2009 IEEE conference on computer vision and pattern recognition (pp. 248-255). Ieee.


<a id="9">[9]</a>
Krizhevsky, A., Sutskever, I. and Hinton, G.E., 2012. Imagenet classification with deep convolutional neural networks. Advances in neural information processing systems, 25, pp.1097-1105.


<a id="10">[10]</a>
https://arxiv.org/help/stats/2020_by_area/index