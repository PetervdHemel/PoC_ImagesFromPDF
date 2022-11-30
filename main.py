from io import BytesIO
from pikepdf import Pdf, PdfError, PdfImage
from PIL import Image
import logging
from base64 import b64encode
import json


def save_images(bytes_list: list[bytes]):
    if bytes_list:
        print("Encoding bytes and dumping to json file...")
        for count, bytes in enumerate(bytes_list):
            _obj = b64encode(bytes)
            data = [_obj.decode('utf-8')]
            
            with open(f".\data\myfile-{count}.json", "w") as f:
                json.dump(data, f)
                


def convert_images(images: list[PdfImage]) -> list[bytes]:
    if images:
        images_as_bytes = []
        img_bytes_io = BytesIO()

        print("Converting image(s) to bytes...")
        for image in images:

            image = image.as_pil_image()
            image.save(img_bytes_io, format="PNG")

            images_as_bytes.append(img_bytes_io.getvalue())

        return images_as_bytes

    else:
        print("Pdf contains no images.")


def extract_images(pdf: Pdf) -> list[PdfImage]:
    images = []
    print("Extracting image(s)...")
    for page in pdf.pages:
        for image_key in page.images.keys():
            raw_img = page.images[image_key]
            pdf_img = PdfImage(raw_img)
            images.append(pdf_img)

    return images


def open_pdf(path: str) -> list[bytes]:
    print("Opening Pdf...")
    try:
        with Pdf.open(path) as pdf:
            images: list = extract_images(pdf)
            images_as_bytes: list = convert_images(images)
            return images_as_bytes

    except FileNotFoundError as e:
        logging.warning(f"File not found:\n{e}")
    except PdfError as e:
        logging.warning(f"File of incorrect type or corrupted:\n{e}")


def main():
    path_to_pdf = r".\pdfs\msi-kombustor-technical-guide.pdf"

    bytes_list = open_pdf(path_to_pdf)

    save_images(bytes_list)


if __name__ == main():
    main()
