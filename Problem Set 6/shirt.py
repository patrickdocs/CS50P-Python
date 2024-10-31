import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        file_inp = sys.argv[1]
        file_outp = sys.argv[2]
        check(file_inp, file_outp)
        process_image(file_inp, file_outp)

def check(file_inp, file_outp):
    valid_exts = [".jpg", ".jpeg", ".png"]
    input_ext = os.path.splitext(file_inp)[1].lower()
    output_ext = os.path.splitext(file_outp)[1].lower()

    if not os.path.isfile(file_inp):
        sys.exit("Input does not exist")
    if input_ext not in valid_exts or output_ext not in valid_exts:
        sys.exit("Invalid extension of input/output")
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

def process_image(file_inp, file_outp):
    photo = Image.open(file_inp)
    shirt = Image.open("shirt.png")
    new_photo = ImageOps.fit(photo, shirt.size)
    new_photo.paste(shirt, shirt)
    new_photo.save(file_outp)

if __name__ == "__main__":
    main()


