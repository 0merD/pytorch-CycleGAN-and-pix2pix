This is a fork of the original CycleGan repo as part of a final project in a Computer Vision course at the Holon Institute of Technology. 

Working Hypothesis
Using a large diverse premade dataset in domain A that is made for the purpose of generalizing natural/natural like images of human faces instead of a costume dataset I collected myself (hance the lack of a data collection script) whilst using a relatively comparable in scale dataset in domain B (the one I want to generate from A) in cycleGAN . Repository is a clone of the https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix repository

Exploration of the datasets
ArcaneFaces
A handcrafted high-quality dataset of over 3400 faces from the first season of the Arcane TV show. This is my domain B, the domain i want to transfer natural faces to.

https://www.kaggle.com/datasets/artermiloff/arcanefaces

This dataset contains 3414 images hand captured from the first season of Arcane and the music video Enemy by Imagine Dragons.

Important notes:
This dataset contains lots of characters, however, it is obviously heavily imbalanced towards the main characters, that make up an overwhelming majority of the images.
Lots of neighboring images in this dataset are extremely similar, since they were captured from neighboring frames.

Human Faces
A web scraped dataset of human faces suggested for image processing models.

https://www.kaggle.com/datasets/ashwingupta3012/human-faces

Context
A collection of 7.2k+ images useful for multiple use cases such image identifiers, classifier algorithms etc.

Content
A thorough mix of all common creeds, races, age groups and profiles in an attempt to create a unbiased dataset with a few GAN generated images as well to aid the functionality of differentiating between real and generated faces.

I used this dataset as domain A as it is a generalizer of natural/natural-like human images. And in practice it lead to better results than using images of myself

SETUP.
download the datasets from kaggle (linked above)

put the Human-Faces dataset in my_dataset/trainA
put the Arcane dataset in my_dataset/trainB
(test folders exist only for structural reasons as the actuall test was subjective (seeing how wel the model handles real time input))

usage.

scripts for training , generation of examples, and real time inference along with a general explanation of the project are in myCGANhumantoarcane.ipynb 

if you want to use the weights i trained you can download them here:

https://mega.nz/file/sAkA0DSY#YBWx-sqouVttsogniUo7JSkwhQVsDTQDIYYmrrMMWl4

(you might need to modify paths for inference accordingly. or you could just place them inside checkpoints/human2arcane and they should work)

inferenc_experimental.ipynb contains multipull versions of the inference scripts (full frame, different sizes of guasian gradients around head...) and also includes versions that be used as a virtual OBS camera so you could use the filter as a custom real time filter for video calls. 

some flashy products so you could see how good are the weights:

<img width="794" height="275" alt="download" src="https://github.com/user-attachments/assets/742291cb-a4fa-4e5e-9c82-f99b8179ef04" />
<img width="794" height="216" alt="download" src="https://github.com/user-attachments/assets/ea96b4a6-a8cd-4968-94a0-6b3d8fcdaf3b" />
<img width="794" height="216" alt="download" src="https://github.com/user-attachments/assets/dd56af53-af79-4cad-bdc4-8accc5a16c9b" />
<img width="772" height="425" alt="download" src="https://github.com/user-attachments/assets/5250503c-e88c-4e9c-871a-30152d260dde" />
<img width="794" height="216" alt="download" src="https://github.com/user-attachments/assets/bf9e2361-3050-420a-b3cf-8b073414ef18" />
<img width="794" height="216" alt="download" src="https://github.com/user-attachments/assets/ffce3b55-b39f-43ba-8b77-f7266b8a28da" />
<img width="794" height="392" alt="download" src="https://github.com/user-attachments/assets/05b5230f-2b78-450e-9aba-67112bc377f9" />
<img width="699" height="425" alt="download" src="https://github.com/user-attachments/assets/c9e6d220-d3e4-40e1-af26-66166dda00fc" />
<img width="699" height="425" alt="download" src="https://github.com/user-attachments/assets/d4f27580-1938-4ce9-85d3-84fafa4b1017" />


