# Stay Positive: Non-Negative Image Synthesis for Augmented Reality

This repository contains a PyTorch implementation of the paper:

[Stay Positive: Non-Negative Image Synthesis for Augmented Reality](). 
<br>
[Katie Luo*](),
[Guandao Yang*](http://www.guandaoyang.com), 
[Wenqi Xian](https://www.cs.cornell.edu/~wenqixian/),
[Harald Haraldsson](http://haraldharaldsson.com/),
[Bharath Hariharan](http://home.bharathh.info/),
[Serge Belongie](http://blogs.cornell.edu/techfaculty/serge-belongie/)
<br>
(* Equal contribution)
<br>
CVPR 2021 (**Oral**)

# Abstract

In applications such as optical see-through and projector augmented reality, producing images amounts to solving non-negative image generation, where one can only add light to an existing image. Most image generation methods, however, are ill-suited to this problem setting, as they make the assumption that one can assign arbitrary color to each pixel. In fact, naive application of existing methods fails even in simple domains such as MNIST digits, since one cannot create darker pixels by adding light. We know, however, that the human visual system can be fooled by optical illusions involving certain spatial configurations of brightness and contrast. Our key insight is that one can leverage this behavior to produce high quality images with negligible artifacts. For example, we can create the illusion of darker patches by brightening surrounding pixels. We propose a novel optimization procedure to produce images that satisfy both semantic and non-negativity constraints. Our approach can incorporate existing state-of-the-art methods, and exhibits strong performance in a variety of tasks including image-to-image translation and style transfer. 

# Installation

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

# Demo

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
@article{staypositive,
 title={Stay Positive: Non-Negative Image Synthesis for Augmented Reality},
 author={Luo, Katie and Yang, Guandao and Haraldsson, Harald and Xian, Wenqi and Hariharan, Bharath and Belongie, Serge},
 journal={CVPR},
 year={2021}
}
```
