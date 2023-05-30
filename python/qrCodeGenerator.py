import qrcode

message = input("Write your message: ")

qrCode = qrcode.make(message)

type(qrCode)

imageFileName = input("Name to be saved to the file: ")
qrCode.save(imageFileName + ".png")
