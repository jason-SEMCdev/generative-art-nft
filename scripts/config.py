# This file MUST be configured in order for the code to run properly

# Make sure you put all your input images into an 'assets' folder. 
# Each layer (or category) of images must be put in a folder of its own.

# CONFIG is an array of objects where each object represents a layer
# THESE LAYERS MUST BE ORDERED.

# Each layer needs to specify the following
# 1. id: A number representing a particular layer
# 2. name: The name of the layer. Does not necessarily have to be the same as the directory name containing the layer
# images.
# 2a. linked: Optional, designate name of layer to try to match image to. Images match names excluding layer name
# 3. directory: The folder inside assets that contain traits for the particular layer
# 4. required: If the particular layer is required (True) or optional (False). The first layer must always be set to
# true.
# 5. rarity_weights: Denotes the rarity distribution of traits. It can take on three types of values.
#       - None: This makes all the traits defined in the layer equally rare (or common)
#       - "random": Assigns rarity weights at random.
#       - array: An array of numbers where each number represents a weight.
#                If required is True, this array must be equal to the number of images in the layer directory. The
#                first number is  the weight of the first image (in alphabetical order) and so on...
#                If required is False, this array must be equal to one plus the number of images in the layer
#                directory. The first number is the weight of having no image at all for this layer. The second number
#                is the weight of the first image and so on...

# Be sure to check out the tutorial in the README for more details.                

CONFIG = [
    {
        'id': 1,
        'name': 'Background',
        'directory': 'background',
        'required': True,
        'rarity_weights': [10, 5, 5, 10, 60],
    },
    {
        'id': 2,
        'name': 'Hair Back',
        'directory': 'hair-back',
        'required': True,
        'rarity_weights': [30, 5, 5, 5, 20, 5, 15, 5, 10, 5],
    },
    {
        'id': 3,
        'name': 'Weapon',
        'directory': 'weapon',
        'required': False,
        'rarity_weights': [40, 15, 5, 15, 5, 15, 5],
    },
    {
        'id': 4,
        'name': 'Face',
        'directory': 'face',
        'required': True,
        'rarity_weights': [10, 5, 10, 25, 5, 2, 2, 1, 10, 5, 3, 2, 10, 5, 3, 2],
    },
    {
        'id': 5,
        'name': 'Armor',
        'directory': 'armor',
        'required': True,
        'rarity_weights': [40, 10, 10, 10, 7, 3, 7, 3, 7, 3],
    },
    {
        'id': 6,
        'name': 'Hair Front',
        'linked': 'Hair Back',
        'directory': 'hair-front',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 7,
        'name': 'Mask',
        'directory': 'mask',
        'required': False,
        'rarity_weights': [99, 5],
    },
    {
        'id': 8,
        'name': 'VFX',
        'directory': 'vfx',
        'required': False,
        'rarity_weights': [60, 30, 10, 10, 1, 20, 10, 10, 5, 4],
    },
]
