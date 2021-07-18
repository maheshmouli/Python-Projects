import cv2
import numpy as np
import img2pdf
from PIL import Image
import os

img = cv2.imread("sample-1.jpg")

alpha = 2.1
beta = -160

new = alpha * img + beta
new = np.clip(new, 0, 255).astype(np.uint8)

cv2.imwrite("cleaned.jpg", new)
  
# storing image path
img_path = "C:/Users/s megha shyam/Desktop/temp/Python-Remove-Watermark/cleaned.jpg"
  
# storing pdf path
pdf_path = "C:/Users/s megha shyam/Desktop/temp/Python-Remove-Watermark/cleaned.pdf"
  
# opening image
image = Image.open(img_path)
  
# converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.filename)
  
# opening or creating pdf file
file = open(pdf_path, "wb")
  
# writing pdf files with chunks
file.write(pdf_bytes)
  
# closing image file
image.close()
  
# closing pdf file
file.close()
  
# output
print("Successfully made pdf file")