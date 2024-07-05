from PIL import Image

# Open an image file
img = Image.open('D:\\workspace\\pythontest\\road.jpg')

gray_img = img.convert('L')

gray_img.save('example_gray.jpg')

# Display the image
img.show()

gray_img.show()


# Split the image into red, green, and blue channels
r, g, b = img.split()

# Create a new image using the red channel
red_img = Image.merge('RGB', (r, g.point(lambda i: i*0), b.point(lambda i: i*0)))

# Display the red image
red_img.show()


r, g, b = img.split()

# Create a new image using the blue channel with reduced intensity
pale_blue_img = Image.merge('RGB', (r.point(lambda i: i*0.5), g.point(lambda i: i*0.5), b))

# Display the pale blue image
pale_blue_img.show()