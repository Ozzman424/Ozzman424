from PIL import Image, ImageOps
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

allowed_extensions = ["png", "jpg", "jpeg"]

input_file_parts = sys.argv[1].split(".")
input_extension = input_file_parts[1]

output_file_parts = sys.argv[2].split(".")
output_extension = output_file_parts[1]

if (
    input_extension not in allowed_extensions
    or output_extension not in allowed_extensions
):
    sys.exit("Invalid input")

if input_extension != output_extension:
    sys.exit("Input and output have different extensions")


def process_image():
    try:
        input_image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt_image = Image.open("shirt.png")
    shirt_size = shirt_image.size
    fitted_image = ImageOps.fit(input_image, shirt_size)
    fitted_image.paste(shirt_image, shirt_image)
    fitted_image.save(sys.argv[2])


if __name__ == "__main__":
    process_image()
