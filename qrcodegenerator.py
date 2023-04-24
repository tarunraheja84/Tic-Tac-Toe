import qrcode

# Create a QR code instance
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Set the data to be encoded in the QR code
data = "https://soft-dodol-fcd732.netlify.app/"

# Add the data to the QR code instance
qr.add_data(data)

# Make the QR code
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qrcode.png")
