from PIL import Image, ImageDraw
from math import pi, sin, cos

RADIUS = 200
SIZE = (1000, 1000)
COLOR = (255, 255, 255, 255)
FILL = (255, 0, 0, 255)

NAILS = 1000

image = Image.new(
    mode='RGB',
    size=SIZE,
    color=COLOR
)

theta = pi/NAILS
coordinates = []

for n in range(-NAILS, NAILS):
    coordinates.append((
        int(image.size[0]/2 + cos(n*theta)*RADIUS),
        int(image.size[1]/2 + sin(n*theta)*RADIUS)
    ))

ImageDraw.Draw(image).point(
    xy=coordinates,
    fill=FILL
)

image.show()
