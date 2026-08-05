from pathlib import Path
import qrcode

folder = Path("Qr codes")

while True:
    content = input().strip() 
    if content.upper().strip() == "XXX":
        print("See you soon, Take care :)")
        break
    else:
        file_name = Path(f"{str(content.title())}.png")
        file_path = folder / file_name
        qr = qrcode.make(content)
        qr.save(file_path)
        print("Process text-to-QRcode is succesfully completed :)")
