# 🔐 VeraCrypt Controller

**VeraCrypt Controller** is a lightweight Python terminal utility that allows users to mount and dismount `.hc` encrypted volumes through an interactive and colorized interface.  
It simplifies working with VeraCrypt volumes in environments where portable usage or centralized control is needed.

---

## ✨ Features

- 🎨 Beautiful CLI interface with colorful prompts and menu
- 🔑 Password entry with file path confirmation
- 🔄 Ability to mount/dismount encrypted `.hc` files
- 🔁 Change mount drive letter dynamically
- 📂 Switch to a different `.hc` file at any time
- 🤫 Hidden option for program information and usage policy
- 📦 Fully compatible with **VeraCrypt Portable** – no installation needed

---

## 📸 Preview

![image](https://github.com/user-attachments/assets/85764345-ebe4-480b-8996-896ad0cd00c2)

## 🚀 Requirements

- Python 3.7+
- [VeraCrypt Portable](https://www.veracrypt.fr/en/Downloads.html)
- `colorama` module (`pip install colorama`)

---

## 🛠️ Setup

1. **Install Python** (if not already)
2. **Place VeraCrypt portable binary** in a known location or shared drive
3. **Clone this repository**:

   ```bash
   git clone https://github.com/raikoho/VeraControl.git
   cd VeraControl
   ```

4. Edit the script to set:

``veracrypt_path`` — full path to your VeraCrypt portable executable

``volume_path`` — default .hc volume file

## 💼 Usage
Run the script from terminal:

```bash
python veracontrol.py
```

## 🔒 Hidden Functionality
There's a secret menu option:

Typing 6 at the main menu reveals Program Info & Usage Policy

##🧠 Tips
You can add this script to your system tray or autorun task for faster access

For secure environments, consider using a password prompt with masking
