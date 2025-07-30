import qrcode

# Ask the user for input to encode
data = input("Enter the text or URL to generate a QR code: ")

# Create a QR Code object with some basic settings
qr = qrcode.QRCode(
    version=1,  # size of the QR code (1–40), higher means bigger
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # error correction level
    box_size=10,  # size of each box in pixels
    border=4,  # border in boxes
)

# Add the input data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create the image of the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
filename = "my_qrcode.png"
img.save(filename)

print(f"✅ QR Code generated and saved as '{filename}'")
