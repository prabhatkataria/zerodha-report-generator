from PIL import Image
import os
import argparse


def createPdf(folder, pdfFileName):
    files = os.listdir(folder)
    firstImage = None
    imageList = []
    for index, filePath in enumerate(files):
        if "png" not in filePath.lower():
            continue

        filePath = r'{}\{}'.format(folder, filePath)
        if index == 0:
            rgba = Image.open(filePath)
            firstImage = Image.new('RGB', rgba.size, (255, 255, 255))
            firstImage.paste(rgba, mask=rgba.split()[3])
        else:
            rgba = Image.open(filePath)
            image = Image.new('RGB', rgba.size, (255, 255, 255))
            image.paste(rgba, mask=rgba.split()[3])
            imageList.append(image)

    firstImage.save(r'{}\{}'.format(folder, pdfFileName), 'PDF',
                    save_all=True, append_images=imageList, resolution=100.0)
    print("pdf created")
