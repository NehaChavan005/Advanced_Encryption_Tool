# Advanced_Encryption_Tool


📝 Project Description: AES-256 File Encryption Tool
This project is a secure file encryption and decryption tool built in Python using the AES-256-GCM encryption algorithm. It provides both a desktop GUI (Tkinter) and a web interface (Streamlit), making it easy for anyone to securely protect sensitive files.

🔐 What It Does
Encrypts any file using a password-based AES-256 key.

Decrypts encrypted files back to their original form using the same password.

Ensures confidentiality, integrity, and authenticity using AES-GCM.

Supports file upload/download directly in the browser (via Streamlit).

🛠️ Tech Used
Python 3

Cryptography library (AES-GCM, PBKDF2-HMAC-SHA256)

Tkinter for desktop interface

Streamlit for web-based interface

🧠 How Security Works
Passwords are converted to encryption keys using PBKDF2 with SHA-256 and a random salt.

Files are encrypted using AES-256 in GCM mode, which also verifies integrity.

The encrypted file format contains:

css
Copy
Edit
[salt (16 bytes)] + [nonce (12 bytes)] + [ciphertext + tag]
💡 Use Cases
Encrypt and email sensitive documents

Protect local backups or cloud-stored files

Educational tool for learning AES encryption

## ✨ Features

- ✅ AES-256 encryption with GCM (ensures confidentiality & integrity)
- ✅ Password-based key derivation (PBKDF2 + SHA-256)
- ✅ Streamlit web GUI for easy use in browser
- ✅ Desktop GUI via Tkinter
- ✅ Supports encryption and decryption of any file type

---

## 📦 Project Structure

aes_app/
├── logic.py # Core AES encryption/decryption logic
├── gui.py # Desktop GUI using Tkinter
└── gui_streamlit.py # Web GUI using Streamlit


---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/aes-encryption-tool.git
cd aes-encryption-tool

🔒 How It Works
Key Derivation: Uses PBKDF2 with SHA-256, 100,000 iterations, and random salt
Encryption: AES-GCM (AES-256 with authentication tag and random nonce)
Output Format: [salt + nonce + ciphertext] in a single binary file
Security Note: Password strength is critical! Use strong passphrases.

📁 File Types
File	Description
file.ext	Original file
file.ext.enc	Encrypted file (downloadable)
file.ext.dec	Decrypted file (after decoding)

🧪 Example
Upload any file
Enter a password
Click Encrypt → download .enc file
Use the same password to decrypt .enc → get original file

📜 License
MIT License © [Your Name or GitHub Username]

🤝 Contributions
Feel free to fork and submit pull requests for improvements, bug fixes, or features!


