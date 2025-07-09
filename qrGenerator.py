import streamlit as st
import qrcode
from PIL import Image
import io
import base64

# Function to generate a QR code and return the image
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    return img

# Convert image to bytes
def image_to_bytes(img):
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer.getvalue()

# Convert image to base64
def image_to_base64(img):
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    img_bytes = buffer.getvalue()
    return base64.b64encode(img_bytes).decode()

# Streamlit app
st.image("header.png", use_container_width=True)

# Input for QR code data
data = st.text_input("Enter the data or URL to encode in the QR code:")

if st.button("Generate QR Code"):
    if data:
        # Generate QR code
        img = generate_qr_code(data)
        
        # Convert image to bytes
        img_bytes = image_to_bytes(img)
        
        # Display QR code image
        st.image(img_bytes, caption="Generated QR Code", width=300)
        
        # Convert image to base64 for download and copy options
        img_base64 = image_to_base64(img)
        
        # Download button
        st.download_button(
            label="Download QR Code",
            data=img_bytes,
            file_name="qr_Code_Generator.png",
            mime="image/png"
        )
        
    else:
        st.error("Please enter some data to generate a QR code.")
