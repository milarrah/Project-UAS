import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Konversi Mata Uang",
    layout="wide",
    page_icon="🤑"
)

st.markdown(
    """
    <style>

    /* Gradien untuk sidebar */
        [data-testid="stSidebar"] {
        background-color: #13274F !important;
        color: #000000 !important;
    }

    /* Gradien untuk latar belakang utama */
    div[data-testid="stAppViewContainer"] {
        background: linear-gradient(to bottom right, #eeaeca, #94bbe9);
        color: #000000;
    }

    div[data-testid="stButton"] {
        background: linear-gradient(to right, #eeaeca, #bfe9ff);
        margin: 0px;
        padding: 7px 7px;
        text-transform: uppercase;
        transition: 0.5s;
        background-size: 100% auto;
        color: white;            
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        border-radius: 10px;
        display:inline-block;
        text-align: center;
        min-width: 110px;
        max-width: 110px; 
        cursor: pointer;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# nilai tukar mata uang berdasarkan kurs hari selasa, 31 desember 2024
nilai_mata_uang = {
    'USD': {'USD': 1.0, 'KRW': 1473.17, 'MYR': 4.4633, 'BATH': 34.198, 'IDR': 16.345},
    'KRW': {'USD': 0.00068, 'KRW': 1.0, 'MYR': 0.0030, 'BATH': 0.023, 'IDR': 10.98},
    'MYR': {'USD': 0.22, 'KRW': 329.63, 'MYR': 1.0, 'BATH': 7.64, 'IDR': 3618.26},
    'BATH': {'USD': 0.029, 'KRW': 43.00, 'MYR': 0.13, 'BATH': 1.0, 'IDR': 471.52},
    'IDR': {'USD': 0.000062, 'KRW': 0.091, 'MYR': 0.00028, 'BATH': 0.0021, 'IDR': 1.0}
}

# fungsi konversi mata uang
def mengkonversi_mata_uang(jumlah, dari_mata_uang, ke_mata_uang):
    if dari_mata_uang == ke_mata_uang:
        return jumlah
    else:
        nilai_konversi = nilai_mata_uang[dari_mata_uang][ke_mata_uang]
        return jumlah * nilai_konversi

#welcoming app
def welcoming_app():
    st.header("Selamat Datang di Aplikasi Pengonversi Mata Uang🙌🏽")
    st.markdown("Selamat menjelajahi fitur-fitur yang tersedia pada Aplikasi kami :)")
    #tambahin st.image disini
    st.image("2.png", width=500)


# halaman riwayat pengguna
def Riwayat_pengguna():
    st.header("Riwayat Pengguna 📜")
    if "riwayat" in st.session_state and st.session_state.riwayat:
        df = pd.DataFrame(st.session_state.riwayat)
        st.dataframe(df)
    else:
        st.info("Tidak ada riwayat yang tercatat untuk saat ini.")

# halaman tentang aplikasi
def tentang_aplikasi():
    st.header("Latar Belakang Aplikasi 👀")
    st.write("""
        Aplikasi ini adalah alat sederhana untuk mengonversi nilai mata uang berdasarkan nilai tukar tetap.
        Pilih menu di sebelah kiri untuk mulai menggunakan aplikasi.
    """)

    # Menampilkan tujuan aplikasi
    st.subheader("Tujuan Aplikasi")
    st.write("""
        Aplikasi ini bertujuan menyediakan alat yang mudah digunakan untuk melakukan konversi mata uang, Memungkinkan pengguna untuk memilih berbagai pasangan mata uang dan jumlah konversi, Memberikan pengalaman pengguna yang menarik dengan visualisasi data sederhana, seperti riwayat nilai tukar historis. 
    """)

    # Menampilkan manfaat aplikasi
    st.subheader("Manfaat Aplikasi")
    st.write("""
        - Mempermudah pengguna dalam menghitung nilai tukar antar mata uang secara cepat dan akurat.
        - Membantu traveler memahami nilai tukar secara langsung.
        - Mengetahui Nilai tukar tetap
        - Fleksibilitas
        - Memberikan pengalaman pengguna yang mudah dan efisien untuk kebutuhan sehari-hari.
    """)



# halaman konversi mata uang
def menu_konversi():
    st.title("💰Pengonversi Mata Uang")
    st.markdown("Selamat Datang di Aplikasi Pengonversi Mata Uang Sederhana👋🏾")

    dari_mata_uang = st.selectbox("Pilih Mata Uang yang akan di Konversi, dari:", ['USD', 'IDR', 'BATH', 'MYR', 'KRW'])
    ke_mata_uang = st.selectbox("Pilih Mata Uang yang akan di Konversi, ke:", ['IDR', 'KRW', 'MYR', 'USD', 'BATH'])
    jumlah = st.number_input("Masukkan Angka yang akan di Konversi:", min_value=0, value=0)

    if st.button("Konversi"):
        hasil_konversi = mengkonversi_mata_uang(jumlah, dari_mata_uang, ke_mata_uang)
        hasil_konversi_format = f"{hasil_konversi:,.2f}"
        st.success(f"{jumlah:,.2f} {dari_mata_uang} sama dengan {hasil_konversi_format} {ke_mata_uang}")

        # Menambahkan hasil ke riwayat
        if "riwayat" not in st.session_state:
            st.session_state.riwayat = []
        st.session_state.riwayat.append({
            "Jumlah": f"{jumlah:,.2f}",
            "Dari Mata Uang": dari_mata_uang,
            "Ke Mata Uang": ke_mata_uang,
            "Hasil": hasil_konversi_format
        })


# menjalankan program
if __name__ == "__main__":
    st.sidebar.title("📍 Menu")
    option = st.sidebar.radio("Silahkan Pilih Menu yang Tersedia:👇🏻", ["Welcome!", "Latar Belakang Aplikasi", "Konversi Mata Uang", "Riwayat Pengguna"])

    if option == "Latar Belakang Aplikasi":
        tentang_aplikasi()
    elif option == "Konversi Mata Uang":
        menu_konversi()
    elif option == "Riwayat Pengguna":
        Riwayat_pengguna()
    elif option == "Welcome!":
        welcoming_app()