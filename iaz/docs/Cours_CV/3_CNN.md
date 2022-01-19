# Convolutional Neural Network

## Introduction
The first time that computer vision task was solved by using Artificial Neural Network was back in 1979 with the introduction of Neocognitron by Kunihiko Fukushima[[1]](#1). It was used for Japanese handwritten character recognition. It was inspired by the work of Hubel & Wiesel in 1959, where two type of cells were present in cats visual primary cortex which are simple cell and complex cell[[2]](#2). The simple cells called S-cells were responsible for extracting local features, and the complex cells called C-cells were responsible for the features' deformation, local shifts. The Convolutional Neural Network was introduced by Yann LeCun in 1989[[3]](#3) for the task of handwritten digital recognition. The trend after the 1990s was to use optimization algorithms for computer vision tasks, at 1998 Convolutional Neural Network was optmized using gradient descent based algorithm with backpropagation[[4]](#4).

## 0. Contents
1. Convolution operation on images
2. Features Maps and kernels
3. Padding and stride
4. Pooling
5. LeNet-5


## 1. Convolution operation on images
The convolution operation formula applied to 2D tensors is:

<!-- $f\circledast g(i,j) = \sum_{a}\sum_{b}f(a,b)g(i-a,j-b)$ --> <img style="transform: translateY(0.1em); background: white;" src="../../svg/JQEBTWc5ke.svg">

Where $(a,b)$ are the indexes for function $f$ and $(i,j)$ are the indexes for function $g$. 
Now if we use matrix notation for hidden representation layers $[H]_{i,j}$, the input image $[X]_{i,j}$ and the kernel $[K]_{a,b}$ the formula becomes:

<!-- $[H]_{i,j} = \sum_{a=-delta}^{delta}\sum_{b=-delta}^{delta}[X]_{i+a,j+b}[K]_{a,b}$ --> <img style="transform: translateY(0.1em); background: white;" src="../../svg/eJaBCGlAPc.svg">

Note here we have changed the difference $(i-a,j-b)$ to $(i+a,j+b)$, this function now will produce a convolution operation for a given index $(i,j)$ for the input image $[X]_{i,j}$ and kernel $[K]_{a,b}$. Where the $delta$ can be interpreted as the kernel size.


Now when we have multiple channel such as RGB images, we will have one 2D array for each channel. So the input image will be a 3D array with the shape of $(C,H,W)$, where $C$ is the number of channels, $H$ is the height of the image, and $W$ is the width of the image. So the image convolution formula becomes:  

<!-- $[H]_{i,j,d} = \sum_{a=-delta}^{delta}\sum_{b=-delta}^{delta}\sum_{c}[X]_{i+a,j+b,c}[K]_{a,b,c,d}$ --> <img style="transform: translateY(0.1em); background: white;" src="../../svg/5DpPa28MoD.svg">

Where <!-- $d$ --> <img style="transform: translateY(0.1em); background: white;" src="../../svg/hf6DCWcSPa.svg"> is the number of receptive fields, or feature maps in the hidden representation, which can be interpreted as the number of kernels that we have defined for the output of this layer, and each kernel applied the convolution operation on each of the 3 channel RGB, we then sum these channels to produce a single receptive field (Note that there has been studies that applied average function to fuse the differents channels).    



## 2. Features Maps and Kernels


## 3. Padding and Stride


## 4. Pooling




## 5. LeNet-5














# References

<a id="1">[1]</a>
Fukushima, K. and Miyake, S., 1982. Neocognitron: A self-organizing neural network model for a mechanism of visual pattern recognition. In Competition and cooperation in neural nets (pp. 267-285). Springer, Berlin, Heidelberg.


<a  id="2">[2]</a>
Hubel, D.H. and Wiesel, T.N., 1959. Receptive fields of single neurones in the cat's striate cortex. The Journal of physiology, 148(3), pp.574-591.


<a  id="3">[3]</a>
LeCun, Y., Boser, B., Denker, J.S., Henderson, D., Howard, R.E., Hubbard, W. and Jackel, L.D., 1989. Backpropagation applied to handwritten zip code recognition. Neural computation, 1(4), pp.541-551.


<a  id="4">[4]</a>
LeCun, Y., Bottou, L., Bengio, Y. and Haffner, P., 1998. Gradient-based learning applied to document recognition. Proceedings of the IEEE, 86(11), pp.2278-2324.