from pikepdf import Pdf, PdfError, PdfImage
import logging


def save_images(images: dict):
    if images:
        print("Saving image(s)...")
        for image_name, image in images.items():
            image.extract_to(fileprefix=image_name)
    else:
        print("Pdf contains no images.")


def extract_images(pdf: Pdf) -> dict({str: PdfImage}):
    images = {}
    print("Extracting image(s)...")
    for page_number, page in enumerate(pdf.pages):
        for image_number, image_key in enumerate(page.images.keys()):
            raw_img = page.images[image_key]
            pdf_img = PdfImage(raw_img)
            dict_key: str = f".\imgs\pg{page_number}_{image_number}"
            images.update({dict_key: pdf_img})

    return images


def open_pdf(path: str):
    try:
        with Pdf.open(path) as pdf:
            images: dict = extract_images(pdf)
            save_images(images)

    except FileNotFoundError as e:
        logging.warning(f"File not found:\n{e}")
    except PdfError as e:
        logging.warning(f"File of incorrect type or corrupted:\n{e}")


def main():
    path_to_pdf: str = r".\pdfs\msi-kombustor-technical-guide.pdf"

    print("Opening Pdf...")
    open_pdf(path_to_pdf)


if __name__ == main():
    main()
