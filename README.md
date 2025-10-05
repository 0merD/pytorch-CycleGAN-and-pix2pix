This is a fork of the original CycleGAN repository 


Working Hypothesis¶
Using a large diverse premade dataset in domain A that is made for the purpose of generalizing natural/natural like images of human faces instead of a costume dataset I collected myself (hance the lack of a data collection script) whilst using a relatively comparable in scale dataset in domain B (the one I want to generate from A) in cycleGAN 

My domain B is images of face from the animated League of Legends Animated Netflix show "Arcane"


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

I used this dataset as domain A as it is a generalizer of natural/natural-like human images. And in practice it lead to better results then using images of mysel¶

some visual products:
<img width="794" height="275" alt="download" src="https://github.com/user-attachments/assets/d16f9b13-d0fe-4233-8605-c7aa2deab7f1" />

<img width="794" height="238" alt="download" src="https://github.com/user-attachments/assets/a02535fa-a4f8-474b-b8a0-905a66e32c33" />
<img width="794" height="216" alt="download" src="https://github.com/user-attachments/assets/fcffda85-3f0d-47b4-b29a-6018b4a3920f" />
<img width="794" height="216" alt="download" src="https://github.com/user-attachments/assets/34d97dc9-04d1-4a41-8a97-ecc788041aa3" />
<img width="772" height="425" alt="download" src="https://github.com/user-attachments/assets/5f01b8cb-e869-44cd-97b6-99c2e637a6b1" <img width="794" height="216" alt="download" src="https://github.com/user-attachments/assets/51bfa260-aa8d-42c8-98a5-fc59d09c9628" />

<img width="699" height="425" alt="download" src="https://github.com/user-attachments/assets/83eb2d81-36f0-45fa-aac2-72ad398d3026" />

<img width="699" height="425" alt="download" src="https://github.com/user-attachments/assets/692fcdb0-2dfc-4782-9966-5fe6845f84ed" />

<img width="794" height="392" alt="download" src="https://github.com/user-attachments/assets/6f7dee5f-7126-4696-b776-2b6b036ffca8" />


<img width="794" height="216" alt="download" src="https://github.com/user-attachments/assets/1dd575de-0384-4fd9-8de0-5ade27c30dda" />

how to train and run:
download the datasets. put the photorealistic human generalizer dataset at /my_dataset/trainA
put the Arcane dataset at /my_dataset/trainB

run myCGANhumantoarcane.ipynb

it has a complete explanation of the project. the python code that is nessesery to train the network and the script for live inference i used in my live demonstration.

in inference_experimental.ipynb you will be able to find alot of different versions of inference scripts for real time use (entire frame, face only....) including versions where the output is a virtual OBS camera (meaning you could use it as a custom filter in a call).
