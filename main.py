from PIL import Image

width = 101
height = 101
scale = 8

img = Image.new("RGB", (width*scale, height*scale))

pix = []

green = (0,255,0)
for y in range(height * scale):
    for x in range(width * scale):
        white = (255, 255, 255)
        black = (0, 0, 0)
        col = white if (y//scale) % 2 != 0 and (x//scale) % 2 != 0 else black
        if x // scale == 1 and y // scale == 1:
            col = green

        pix.append(col)

# print(type(upscale))
img.putdata(pix)

img.show()