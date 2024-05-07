import qrcode
import qrcode.image.svg


# img = qrcode.make("Hello, my name is Denis!")
# img.save("mycode.png")

# qr = qrcode.QRCode(version=1,
#                    error_correction=qrcode.constants.ERROR_CORRECT_L,
#                    box_size=50,
#                    border=1)
#
# qr.add_data("https://www.youtube.com/watch?v=l4ugfcj7qrI&list=PL7yh-TELLS1EgOLIPo1sVuf_rDPEp33S8&index=5")
# qr.make(fit=True)
#
# img = qr.make_image(fill_color="black", back_color="white")
# img.save("youtube.png")

factory = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make('Hello World', image_factory=factory)
svg_img.save('hello_world.svg')



