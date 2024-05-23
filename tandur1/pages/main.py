import streamlit as st
import random

# Informasi detail petani
petani_info = {
    'Petani A': {'modal': 'Rp10.000.000', 'deskripsi': 'Untuk pembelian bibit padi berkualitas', 'kebutuhan': 'Pembelian bibit dan pupuk', 'gambar': 'petani_a.png', 'max_keuntungan': 20},
    'Petani B': {'modal': 'Rp15.000.000', 'deskripsi': 'Untuk pengembangan lahan sayuran', 'kebutuhan': 'Pengolahan lahan dan peralatan', 'gambar': 'petani_b.png', 'max_keuntungan': 40},
    'Petani C': {'modal': 'Rp8.000.000', 'deskripsi': 'Untuk peningkatan produksi ternak', 'kebutuhan': 'Pakan ternak dan vaksinasi', 'gambar': 'petani_c.png', 'max_keuntungan': 15}
}

# Fungsi untuk mengonversi string modal menjadi integer
def konversi_modal_ke_int(modal_str):
    return int(modal_str.replace('Rp', '').replace('.', ''))

# Fungsi untuk menghitung total keuntungan
def hitung_total_keuntungan(modal, persentase_keuntungan, jumlah_musim):
    return modal * (persentase_keuntungan / 100) * jumlah_musim

# Fungsi untuk menghasilkan kode pembayaran acak
def generate_kode_pembayaran():
    return ''.join(random.choices('0123456789', k=6))

# Judul aplikasi
st.title('Platform Investasi Petani')

# Navbar
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Tentang Kami"):
        st.switch_page("pages/explain.py")
with col2:
    if st.button("Halaman Utama"):
        st.switch_page("pages/home.py")
with col3:
    if st.button("Investasi Sekarang"):
        st.switch_page("pages/main.py")

# Input jumlah investasi
jumlah_investasi = st.number_input('Masukkan jumlah investasi (Rp):', min_value=1000000, step=1000000)

# Dropdown untuk memilih petani
petani_terpilih = st.selectbox('Pilih petani:', list(petani_info.keys()))

# Tampilkan deskripsi petani
if petani_terpilih:
    st.write(f"Modal yang dibutuhkan: {petani_info[petani_terpilih]['modal']}")
    st.write(f"Deskripsi: {petani_info[petani_terpilih]['deskripsi']}")
    st.write(f"Investasi akan digunakan untuk: {petani_info[petani_terpilih]['kebutuhan']}")
    st.write(f"Maksimal keuntungan: {petani_info[petani_terpilih]['max_keuntungan']}%")
    # Tampilkan gambar petani
    st.image(petani_info[petani_terpilih]['gambar'])

# Slider untuk persentase keuntungan
persentase_keuntungan = st.slider('Persentase keuntungan yang diinginkan:', 1, 50, 20)

# Dropdown pilih durasi investasi berdasarkan musim panen
jumlah_musim = st.selectbox('Pilih durasi investasi:', [1, 2, 3, 4, 5], format_func=lambda x: f"{x} musim panen")

# Tombol submit
if st.button('Submit'):
    modal_petani = konversi_modal_ke_int(petani_info[petani_terpilih]['modal'])
    if jumlah_investasi < modal_petani:
        st.error(f"Jumlah investasi harus setidaknya sama dengan modal yang dibutuhkan oleh {petani_terpilih}, yaitu {petani_info[petani_terpilih]['modal']}.")
    elif persentase_keuntungan > petani_info[petani_terpilih]['max_keuntungan']:
        st.error(f"Persentase keuntungan tidak boleh lebih dari {petani_info[petani_terpilih]['max_keuntungan']}% untuk {petani_terpilih}.")
    else:
        total_keuntungan = hitung_total_keuntungan(jumlah_investasi, persentase_keuntungan, jumlah_musim)
        kode_pembayaran = generate_kode_pembayaran()
        st.success(f"Investasi berhasil! Jumlah: Rp{jumlah_investasi}, Petani: {petani_terpilih}, Durasi: {jumlah_musim} musim panen, Keuntungan: Rp{total_keuntungan} ({persentase_keuntungan}% per musim). Silakan melakukan pembayaran dengan kode: {kode_pembayaran}")
