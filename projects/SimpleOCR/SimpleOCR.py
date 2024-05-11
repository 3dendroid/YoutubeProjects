import easyocr


def is_text_present(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path)

    return len(result) > 0


def text_from_image(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path)

    for (bbox, text, prob) in result:
        print(text)


# print(is_text_present('images\image_4.jpg'))
text_from_image('images\image_2.jpg')