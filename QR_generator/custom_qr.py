import qrcode
from PIL import Image

qr = qrcode.QRCode(version = 1,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=20, border=10,)
qr.add_data("https://l.facebook.com/l.php?u=https%3A%2F%2Fyoutu.be%2FJ9Qk0tRAg0Q%3Ffbclid%3DIwAR0OCsCn6jN64Gxp7M7R7GL_Kt1ekAuFF4vcKAui9fe4PNyAVQLGZWBR9iM&h=AT2ar1X7eQ-Byai8UHM1NaNRhztSePjSytCAs_BI1aR8rjcOZ__4Gkd-_jFrLiRtRJt7_IXIwLMXG8Ys1-nScxrvua9vew1P4LlK_eWF_d-hN7ODRBdSGUX9psTLsqUGw-niTry0lkXtxQ")
qr.make(fit = True)
pic=qr.make_image(fill_color="black",back_color = "white")
pic.save("sasto_mutu_slowed.png")