import streamlit as st
from streamlit_carousel import carousel

# Function to open other Python scripts
def open_script(script_name):
    subprocess.Popen(["streamlit", "run", script_name])

# Creating the home screen
def create_home_screen():
    st.set_page_config(page_title="Home Page", layout="wide")

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

    # Sambutan Section
    st.markdown("## Selamat Datang, Pelanggan Yang Terhormat!")

    # Image files for cards (assuming images are in the same directory as the script)
    card_images = ["petani_a.png", "petani_b.png", "petani_c.png"]

    # Membuat dan menambahkan card ke content_frame
    card_columns = st.columns(3)
    for i, col in enumerate(card_columns):
        with col:
            st.image(card_images[i], caption="Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
            if st.button("Investasi Sekarang", key=f'button{i}'):
                st.switch_page("pages/main.py")

    # Mengapa Investasi ke Petani Section
    st.markdown("## Mengapa Investasi ke Petani")
    st.write("Investasi ke petani memiliki dampak positif yang luas, di antaranya:")

    st.markdown("- **Pemberdayaan Ekonomi Lokal**: Investasi ke petani membantu memperkuat ekonomi lokal dengan memberdayakan para petani untuk menghasilkan lebih banyak dan meningkatkan pendapatan mereka.")
    st.markdown("- **Ketahanan Pangan**: Dengan mendukung pertanian, investasi ke petani juga membantu memastikan ketersediaan makanan yang mencukupi untuk masyarakat.")
    st.markdown("- **Perlindungan Lingkungan**: Banyak petani yang menerapkan praktik pertanian berkelanjutan, sehingga investasi ke petani juga membantu dalam pelestarian lingkungan.")

    # Judul Carousel
    st.markdown("<h2 style='text-align: center; color: white;'>Pesan Dari Petani Kami</h2>", unsafe_allow_html=True)

    # Carousel
    carousel_items = [
        {"title": "Gambar 1", "text": "Deskripsi gambar 1", "img": "https://usetrust.io/wp-content/uploads/2023/04/image-1-1024x750.png"},
        {"title": "Gambar 2", "text": "Deskripsi gambar 2", "img": "https://www.groovehq.com/blog/wp-content/uploads/2014/09/example-mini-testimonial.jpg"},
        {"title": "Gambar 3", "text": "Deskripsi gambar 3", "img": "https://images.ctfassets.net/vztl6s0hp3ro/6Y20huxb2HhPYEokBFHNAj/b4a734b3cde761b6661eeee855b90720/example-of-employee-testimonial.jpg"},
        {"title": "Gambar 4", "text": "Deskripsi gambar 4", "img": "https://embedsocial.com/wp-content/uploads/2022/02/semrush-customer-reviews-example.jpg"}
    ]
    carousel(items=carousel_items, width=0.5)

# Running the home screen function
if __name__ == "__main__":
    create_home_screen()
