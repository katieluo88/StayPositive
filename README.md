# Stay Positive: Non-Negative Image Synthesis for Augmented Reality

This repository contains a PyTorch implementation of the paper:

[Stay Positive: Non-Negative Image Synthesis for Augmented Reality](https://openaccess.thecvf.com/content/CVPR2021/papers/Luo_Stay_Positive_Non-Negative_Image_Synthesis_for_Augmented_Reality_CVPR_2021_paper.pdf) \[[Project Page](https://katieluo88.github.io/StayPositive/)\] \[[Video](https://youtu.be/wYEbZWtQ-T4)\]

[Katie Luo*](https://www.cs.cornell.edu/~katieluo/),
[Guandao Yang*](http://www.guandaoyang.com), 
[Wenqi Xian](https://www.cs.cornell.edu/~wenqixian/),
[Harald Haraldsson](http://haraldharaldsson.com/),
[Bharath Hariharan](http://home.bharathh.info/),
[Serge Belongie](http://blogs.cornell.edu/techfaculty/serge-belongie/)

(* Equal contribution)
CVPR 2021 (**Oral**)

<p float="left">
    <img src="images/banner.gif"/>
</p>

## Abstract

In applications such as optical see-through and projector augmented reality, producing images amounts to solving non-negative image generation, where one can only add light to an existing image. Most image generation methods, however, are ill-suited to this problem setting, as they make the assumption that one can assign arbitrary color to each pixel. In fact, naive application of existing methods fails even in simple domains such as MNIST digits, since one cannot create darker pixels by adding light. We know, however, that the human visual system can be fooled by optical illusions involving certain spatial configurations of brightness and contrast. Our key insight is that one can leverage this behavior to produce high quality images with negligible artifacts. For example, we can create the illusion of darker patches by brightening surrounding pixels. We propose a novel optimization procedure to produce images that satisfy both semantic and non-negativity constraints. Our approach can incorporate existing state-of-the-art methods, and exhibits strong performance in a variety of tasks including image-to-image translation and style transfer. 

## Installation

This demo has been tested on the following package versions:
* Conda (4.8.5)
* Pytorch (1.7.0)
* Matplotlib (3.3.2)
* Numpy (1.19.2)
* tqdm (4.51.0)
* Jupyter notebook (1.0.0)

Following is a simple way to install the required dependencies.

```bash
conda env create -f environment.yml
conda activate staypositive
```

## Demo

This is a small demo for the CVPR submission _Stay Positive: Non-Negative Image Synthesis for Augmented Reality_.
The demo requires a simple installation process (presented in the previous section).
It takes an input image (e.g. `demoA.png`) and a proposed target image (e.g. `demoB.png`), and run the optimization process proposed in Section 3 of the paper to produce an output image that tries to be perceptually similar to the propose target while fulfilling the non-negative constraints.
The demo will be in `Demo.ipynb`:

```bash
conda activate staypositive
jupyter notebook
```

## Cite
Please cite our work if you find it useful:
```latex
@InProceedings{StayPositive_2021,
    author    = {Luo, Katie and Yang, Guandao and Xian, Wenqi and Haraldsson, Harald and Hariharan, Bharath and Belongie, Serge},
    title     = {Stay Positive: Non-Negative Image Synthesis for Augmented Reality},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
    month     = {June},
    year      = {2021},
    pages     = {10050-10060}
}
```
