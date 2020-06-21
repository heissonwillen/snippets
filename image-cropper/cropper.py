from PIL import Image

last_pos_x, last_pos_y = 0, 0
GRID_DIMENSION = 10

image = Image.open("image.jpg")

width, height = [int(dimension/GRID_DIMENSION) for dimension in list(image.size)]

for i in range(GRID_DIMENSION):
    for j in range(GRID_DIMENSION):
        cropped_image = image.crop((last_pos_x, last_pos_y, last_pos_x+width, last_pos_y+height))
        cropped_image.save(f"cropped_images/image-{i}-{j}.jpg")

        last_pos_x += width

    last_pos_x = 0
    last_pos_y += height

print('done :)')
