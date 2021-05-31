import pyqrcode
string="https://web.whatsapp.com/"
url=pyqrcode.create(string)
url.png("qrcode2.png",scale=8)