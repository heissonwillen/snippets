from PIL import Image, ImageDraw
from math import pi, sin, cos

RADIUS = 1800
SIZE = (4000, 4000)
COLOR = (255, 255, 255, 255)
FILL = (0, 0, 0, 255)

NUMBER_OF_NAILS = 10

image = Image.new(
    mode='RGB',
    size=SIZE,
    color=COLOR
)

theta = pi/NUMBER_OF_NAILS
nails_coordinates = []

for n in range(-NUMBER_OF_NAILS, NUMBER_OF_NAILS):
    nails_coordinates.append((
        int(image.size[0]/2 + cos(n*theta)*RADIUS),
        int(image.size[1]/2 + sin(n*theta)*RADIUS)
    ))

ImageDraw.Draw(image).point(
    xy=nails_coordinates,
    fill=FILL
)

for i in range(-NUMBER_OF_NAILS, NUMBER_OF_NAILS):
    for j in range(-NUMBER_OF_NAILS, NUMBER_OF_NAILS):
        ImageDraw.Draw(image).line(
            xy=[nails_coordinates[i], nails_coordinates[j]],
            fill=FILL,
            width=1,
        )

image.show()
