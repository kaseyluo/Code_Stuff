
from PIL import Image

# For recoloring.
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

white = (255, 255, 255)
black = (0,0,0)
light_grey = (64,64,64)
dark_grey = (32,32,32)

# Load the image and turn the image into a list of tuples.
my_image = Image.open("bunny.jpg")
image_list = my_image.getdata()
image_list = list(image_list)
# print(image_list)

#start with pseudocode

user_input = input("What color filter?: Obamicon or B&W ")

# Check the intensity of each pixel, determine how to recolor it, and save it in a new list.
recolored = []
for pixel in image_list:

    intensity = pixel[0] + pixel[1] + pixel[2]

    if intensity < 182:

        if user_input == "Obamicon":
        	recolored.append(darkBlue)
        elif user_input == "B&W":
        	recolored.append(black)
        else: 
        	print("error")

    elif intensity >= 182 and intensity < 364:

        if user_input == "Obamicon":
        	recolored.append(red)
        elif user_input == "B&W":
        	recolored.append(light_grey)
        else: 
        	print("error")

    elif intensity >= 364 and intensity < 546:
        if user_input == "Obamicon":
        	recolored.append(lightBlue)
        elif user_input == "B&W":
        	recolored.append(dark_grey)
        else: 
        	print("error")

    elif intensity >=546:
        if user_input == "Obamicon":
        	recolored.append(yellow)
        elif user_input == "B&W":
        	recolored.append(white)
        else: 
        	print("error")

# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size)
new_image.putdata(recolored)
new_image.show()
new_image.save("recolored.jpg", "jpeg")