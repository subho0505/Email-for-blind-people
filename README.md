Here’s a professional **README.md** for your voice-controlled email sender project:

---

# 📧 Voice-Controlled Email Sender

## 📌 Overview

A Python-based voice-activated email automation system that allows users to send emails hands-free. Built using **speech recognition**, **text-to-speech**, and Gmail’s SMTP service, the app captures recipient, subject, and message via voice commands and sends emails seamlessly without manual typing.

## 🚀 Features

* 🎤 **Speech-to-Text Integration** using Google Speech Recognition API
* 🔊 **Text-to-Speech Feedback** with `pyttsx3`
* 📧 **Automated Email Sending** via Gmail SMTP server
* 🔄 **Recursive Multi-Email Sending** with voice prompts
* 🤖 **Completely Hands-Free Operation**

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:** `speech_recognition`, `pyttsx3`, `smtplib`, `email.message`
* **Service:** Gmail SMTP

## 📂 How It Works

1. App prompts user for the recipient’s name (from a predefined list).
2. Captures the **subject** and **message body** via voice input.
3. Sends the email through Gmail’s SMTP server.
4. Asks if the user wants to send more emails.

## 🔧 Installation & Setup

1. Clone the repository:

   ```bash
   git clone <repo-link>
   cd voice-email-sender
   ```
2. Install dependencies:

   ```bash
   pip install speechrecognition pyttsx3
   ```
3. Update Gmail credentials in the script.
4. Run the program:

   ```bash
   python main.py
   ```

## 📌 Future Enhancements

* Add **dynamic contact list integration** from CSV or database.
* Enable **OAuth2 authentication** for Gmail API.
* Support for **multiple email providers**.

## 📜 License

This project is licensed under the MIT License.

