from io import BytesIO
from pikepdf import Pdf, PdfError, PdfImage
import logging
from base64 import b64encode
import json


def save_images(bytes_list: list[bytes]):
    print("Encoding bytes and dumping to json file...")
    for count, bytes in enumerate(bytes_list):
        _obj = b64encode(bytes)
        data = [_obj.decode("utf-8")]

        with open(f".\data\myfile-{count}.json", "w") as f:
            json.dump(data, f)


def convert_to_bytes(image: PdfImage) -> bytes:
    img_bytes_io = BytesIO()

    image = image.as_pil_image()
    image.save(img_bytes_io, format="BMP")

    return img_bytes_io.getvalue()


def convert_images(images: list[PdfImage]) -> list[bytes]:

    images_as_bytes = []

    print("Converting image(s) to bytes...")

    for image in images:
        images_as_bytes.append(convert_to_bytes(image))

    return images_as_bytes


def convert_page_to_images(page: Pdf.pages) -> list[PdfImage]:
    images = []
    for image_key in page.images.keys():
        raw_img = page.images[image_key]
        pdf_img = PdfImage(raw_img)
        images.append(pdf_img)

    return images


def extract_images(pdf: Pdf) -> list[PdfImage]:
    images = []
    print("Extracting image(s)...")
    for page in pdf.pages:
        images += convert_page_to_images(page)

    return images


def convert_pdf(path: str) -> list[bytes]:
    print("Opening Pdf...")
    try:
        with Pdf.open(path) as pdf:
            images: list = extract_images(pdf)
            if images:
                images_as_bytes: list[bytes] = convert_images(images)
            else:
                raise ValueError("Pdf contains no images.")

        return images_as_bytes

    except FileNotFoundError as e:
        logging.warning(f"File not found:\n{e}")
    except PdfError as e:
        logging.warning(f"File of incorrect type or corrupted:\n{e}")


def main():
    path_to_pdf = r".\pdfs\BURNING_TOWER_README.pdf"

    bytes_list = convert_pdf(path_to_pdf)

    if bytes_list:
        save_images(bytes_list)
    else:
        raise ValueError("No data could be extracted from images.")


if __name__ == "__main__":
    main()
