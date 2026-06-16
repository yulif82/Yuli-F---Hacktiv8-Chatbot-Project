# 🚗 Chatbot Perawatan Mobil Mandiri (AI-Powered)

Selamat datang di project **Chatbot Perawatan Mobil Mandiri**! 

Aplikasi ini adalah asisten mekanik virtual berbasis kecerdasan buatan (AI) yang dirancang untuk membantu pemilik kendaraan melakukan perawatan mobil dasar secara mandiri (DIY), mendiagnosis masalah ringan (seperti aki soak, ganti oli, cek radiator), dan memberikan panduan keselamatan.

🌐 **[COBA APLIKASINYA SECARA LANGSUNG DI SINI](https://yuli-f---hacktiv8-chatbot-project-knhktczegctkwlkitbsgvd.streamlit.app/)**

## 🛠️ Teknologi yang Digunakan
Project ini dikembangkan menggunakan Large Language Model (LLM) dengan integrasi:
* **Bahasa Pemrograman:** Python
* **Frontend/UI:** Streamlit
* **AI Model:** Llama-3.1-8b-instant (via Groq API)
* **Framework AI:** LangChain

## ✨ Fitur Utama
* **Fokus Otomotif (System Prompting):** AI telah diberikan "kepribadian" dan instruksi khusus agar hanya fokus menjawab permasalahan seputar mobil dengan bahasa awam yang mudah dipahami.
* **Memori Percakapan:** Chatbot mengingat alur interaksi (*chat history*) sehingga percakapan terasa natural dan berkelanjutan.
* **Sistem Keamanan Logika:** Jika AI mendeteksi masalah berat (seperti bongkar mesin inti) atau tindakan yang berisiko, ia diprogram untuk mengarahkan pengguna ke bengkel resmi.
* **Respon Cepat:** Didukung oleh infrastruktur Groq LPU untuk kecepatan inferensi model.

## 🚀 Cara Menjalankan di Komputer Lokal
Jika Anda ingin mencoba menjalankan kode ini di komputer Anda sendiri:
1. Pastikan Python sudah terinstal.
2. Download repositori ini dan buka terminal/Command Prompt di folder tersebut.
3. Instal semua *library* yang dibutuhkan dengan perintah:
   `pip install -r requirements.txt`
4. Jalankan aplikasi Streamlit dengan perintah:
   `python -m streamlit run app.py`

---
*Project ini adalah Final Project program LLM-Based Tools & Gemini API Integration for Data Scientists oleh Hacktiv8.*
