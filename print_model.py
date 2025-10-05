import torch
from models.networks import define_G, define_D

# Default parameters for CycleGAN generator (based on repository defaults)
input_nc = 3   # Number of input channels (e.g., RGB images)
output_nc = 3  # Number of output channels
ngf = 64       # Number of generator filters in the last conv layer
netG = 'resnet_9blocks' # Generator architecture type
norm = 'instance' # Normalization type
use_dropout = False # Whether to use dropout
gpu_ids = [0]

# Instantiate the generator
netG_A = define_G(input_nc, output_nc, ngf, netG, norm, use_dropout, gpu_ids=gpu_ids)
netG_B = define_G(input_nc, output_nc, ngf, netG, norm, use_dropout, gpu_ids=gpu_ids)

# Default parameters for CycleGAN discriminator
ndf = 64       # Number of discriminator filters in the first conv layer
netD = 'basic' # Discriminator architecture type
n_layers_D = 3 # Number of layers in the discriminator
norm_D = 'instance' # Normalization type for discriminator

# Instantiate the discriminator
netD_A = define_D(input_nc, ndf, netD, n_layers_D, norm_D, gpu_ids=gpu_ids)
netD_B = define_D(input_nc, ndf, netD, n_layers_D, norm_D, gpu_ids=gpu_ids)

# Print the architectures
print("Generator A:")
print(netG_A)
print("\nGenerator B:")
print(netG_B)
print("\nDiscriminator A:")
print(netD_A)
print("\nDiscriminator B:")
print(netD_B)