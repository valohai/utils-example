import os
from PIL import Image

import valohai
from valohai.parameters import get_parameter
from valohai.inputs import get_input_file_paths
from valohai.outputs import get_output_path

parameters = {
    "width": 640,
    "height": 480,
}
inputs = {
    "images": [
        "https://upload.wikimedia.org/wikipedia/en/a/a9/Example.jpg",
        "https://homepages.cae.wisc.edu/~ece533/images/airplane.png",
    ]
}
valohai.prepare(step="resize", parameters=parameters, inputs=inputs)


def resize_image(in_path, out_path, width, height):
    image = Image.open(in_path)
    print(f"Resizing {in_path} ({image.size[0]}x{image.size[1]}) to {out_path} ({width}x{height})")
    new_image = image.resize((width, height))
    new_image.save(out_path)


if __name__ == '__main__':
    for image_path in valohai.inputs.get_input_file_paths("images"):
        filename = os.path.basename(image_path)
        resize_image(
            in_path=image_path,
            out_path=get_output_path(filename),
            width=get_parameter("width"),
            height=get_parameter("height"),
        )
