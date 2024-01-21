import pytesseract
from Utils import image_cleanup, identify, panda_csv, parse
import os
output =  []
if __name__ == "__main__":
    io = parse.main()
    print(io)
    dir_list = os.listdir(io)
    for i in dir_list:
        im_file = io + "/" + i
        image = image_cleanup.cleanup(im_file)
        ocr = pytesseract.image_to_string(image, lang="eng")
        output.append(identify.iden(ocr, i))
        print(output)
        panda_csv.csv(output)
