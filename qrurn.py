from urllib.parse import urlencode
import qrcode

params = {
   'label': 'バナナ会社',
   'message': '端末代',
}
params = urlencode(params)
uri = 'bitcoin:2NF969a1pYgeGfRMSoTMaaix8jEj4aadbaU?amount=0.1&'+params
print(uri)
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(uri)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('/home/pi/crypto-currency/qrcode_banana.png')
