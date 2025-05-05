import streamlit as st
import qrcode
from PIL import Image
import io

# ---- Page Configuration ----
st.set_page_config(page_title="Raiden QR Generator", page_icon="⚡", layout="centered")

# ---- Title and Subtitle ----
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>⚡ Raiden QR Code Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Convert any URL into a QR Code instantly.</p>", unsafe_allow_html=True)

st.markdown("---")

# ---- Input Section ----
url = st.text_input("🔗 Enter a URL to generate a QR code:")

col1, col2 = st.columns(2)
with col1:
    box_size = 20 #st.slider("📦 QR Box Size", min_value=5, max_value=20, value=10)
    
with col2:
    use_color = st.toggle("🌈 Colored QR Code")
    

# ---- QR Generation ----
if url:
    # Build QR Code
    qr = qrcode.QRCode(box_size=box_size, border=4)
    qr.add_data(url)
    qr.make(fit=True)

    fill = "black"
    back = "white"

    if use_color:
        fill = "#4CAF50"  # Raiden green
        back = "#E8F5E9"  # light greenish background

    img = qr.make_image(fill_color=fill, back_color=back)

    # Convert to BytesIO for Streamlit
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)

    # ---- Display Section ----
    st.markdown("### 🖼️ Your QR Code")
    st.image(buf, caption="Scan Me!", use_container_width=True)  # Updated here

    # ---- Download Button ----
    st.download_button(
        label="⬇️ Download QR Code",
        data=buf.getvalue(),
        file_name="raiden_qr_code.png",
        mime="image/png"
    )

    st.success("✅ QR Code generated successfully!")

else:
    st.info("Please enter a URL to generate your QR code.")
