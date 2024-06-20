import qrcode

img = qrcode.make('https://www.youtube.com')
img.save("some_file.png")