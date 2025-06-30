# gui_streamlit.py

import streamlit as st
from logic import encrypt_data, decrypt_data

st.set_page_config(page_title="AES-256 File Encryption", layout="centered")
st.title("🔐 AES-256 File Encryption Tool")

st.markdown("""
This tool lets you **securely encrypt and decrypt files** using **AES-256-GCM**.
""")

action = st.radio("Select Action", ["Encrypt", "Decrypt"], horizontal=True)

uploaded_file = st.file_uploader("Upload a file", type=None)

password = st.text_input("Enter password", type="password")

if uploaded_file and password:
    file_bytes = uploaded_file.read()

    if action == "Encrypt":
        if st.button("🔒 Encrypt"):
            try:
                encrypted = encrypt_data(file_bytes, password)
                st.success("✅ File encrypted successfully!")
                st.download_button(
                    label="📥 Download Encrypted File",
                    data=encrypted,
                    file_name=uploaded_file.name + ".enc",
                    mime="application/octet-stream"
                )
            except Exception as e:
                st.error(f"❌ Error: {e}")

    elif action == "Decrypt":
        if st.button("🔓 Decrypt"):
            try:
                decrypted = decrypt_data(file_bytes, password)
                st.success("✅ File decrypted successfully!")
                st.download_button(
                    label="📥 Download Decrypted File",
                    data=decrypted,
                    file_name=uploaded_file.name.replace(".enc", ".dec"),
                    mime="application/octet-stream"
                )
            except Exception as e:
                st.error(f"❌ Decryption failed: {e}")
else:
    st.info("Upload a file and enter a password to proceed.")
