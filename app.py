import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# ==========================================
# 1. PENGATURAN HALAMAN
# ==========================================
st.set_page_config(page_title="Yuli F - Mekanik Mobil AI", page_icon="🚗")
st.title("🚗 Yuli F Hacktiv8 - Chatbot Perawatan Mobil Mandiri")
st.caption("Asisten AI untuk membantu Anda merawat, mengecek, dan mengatasi masalah ringan pada mobil Anda di rumah.")

# ==========================================
# 2. KONFIGURASI API KEY (Input Manual di Sidebar)
# ==========================================
st.sidebar.header("Konfigurasi")
groq_api_key = st.sidebar.text_input("Masukkan Groq API Key Anda", type="password")

# Menghentikan aplikasi sementara jika API Key belum diisi
if not groq_api_key:
    st.info("Silakan masukkan API Key Groq di sidebar sebelah kiri untuk memulai chatbot.")
    st.stop()

# Menggunakan model Llama 3.1 terbaru yang aktif
llm = ChatGroq(
    groq_api_key=groq_api_key, 
    model_name="llama-3.1-8b-instant", 
    temperature=0.5 # Angka 0.5 agar jawaban lebih faktual dan logis untuk hal teknis
)

# ==========================================
# 3. MEMORI & PARAMETER KREATIF (SYSTEM PROMPT)
# ==========================================
if "messages" not in st.session_state:
    # Memberikan "Kepribadian" dan batasan pengetahuan pada AI
    st.session_state.messages = [
        {"role": "system", "content": "Kamu adalah seorang mekanik mobil profesional dan ramah. Tugasmu adalah memberikan panduan step-by-step perawatan mobil mandiri (DIY), mendiagnosis masalah ringan (seperti aki soak, ban kempes, ganti oli, cek radiator), dan memberikan tips keselamatan. Gunakan bahasa Indonesia yang mudah dipahami oleh orang awam. Jika masalahnya terlihat berat, melibatkan bongkar mesin inti, atau berbahaya, selalu sarankan pengguna untuk membawa mobilnya ke bengkel resmi. Jangan menjawab pertanyaan di luar topik otomotif."}
    ]

# Tampilkan riwayat chat di layar (Pesan 'system' disembunyikan agar UI terlihat rapi)
for msg in st.session_state.messages:
    if msg["role"] != "system":
        st.chat_message(msg["role"]).write(msg["content"])

# ==========================================
# 4. INTERAKSI PENGGUNA & AI
# ==========================================
# Kolom input untuk pengguna mengetik pesan
if prompt := st.chat_input("Tanyakan soal ganti oli, tekanan ban, radiator, dll..."):
    
    # Menampilkan pesan pengguna di layar
    st.chat_message("user").write(prompt)
    
    # Menyiapkan riwayat percakapan untuk dibaca oleh LangChain
    langchain_messages = []
    for msg in st.session_state.messages:
        if msg["role"] == "system":
            langchain_messages.append(SystemMessage(content=msg["content"]))
        elif msg["role"] == "user":
            langchain_messages.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            langchain_messages.append(AIMessage(content=msg["content"]))
            
    # Menambahkan pertanyaan terbaru dari pengguna
    langchain_messages.append(HumanMessage(content=prompt))
    
    # Menyimpan pertanyaan ke memori internal Streamlit
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Meminta AI (Llama) memberikan jawaban
    with st.chat_message("assistant"):
        with st.spinner("Mekanik AI sedang menganalisis..."):
            try:
                # Mengirim seluruh riwayat percakapan ke Groq
                response = llm.invoke(langchain_messages)
                # Menampilkan jawaban
                st.write(response.content)
                # Menyimpan jawaban AI ke memori internal
                st.session_state.messages.append({"role": "assistant", "content": response.content})
            except Exception as e:
                st.error(f"Terjadi kesalahan pada sistem: {e}")