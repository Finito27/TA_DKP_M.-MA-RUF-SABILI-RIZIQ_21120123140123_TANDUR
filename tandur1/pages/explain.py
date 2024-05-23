import streamlit as st

class TandurPlatform:
    def __init__(self):
        self._button_label = None

    def set_button_label(self, button_label):
        self._button_label = button_label

    def get_button_label(self):
        return self._button_label

    def handle_navigation(self):
        button_label = self.get_button_label()
        if button_label == "Tentang Kami":
            self.about_us()
            st.switch_page("pages/explain.py")
        elif button_label == "Halaman Utama":
            self.home_page()
            st.switch_page("pages/home.py")
        elif button_label == "Investasi Sekarang":
            self.invest_now()
            st.switch_page("pages/main.py")

    def about_tandur(self):
        # Navbar
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Tentang Kami"):
                self.set_button_label("Tentang Kami")
        with col2:
            if st.button("Halaman Utama"):
                self.set_button_label("Halaman Utama")
        with col3:
            if st.button("Investasi Sekarang"):
                self.set_button_label("Investasi Sekarang")

        # Content of 'Tentang Tandur' page
        st.title('Tentang Tandur')
        st.write('Selamat datang di platform investasi petani kami - Tandur!')

        st.header('Cerita di Balik Tandur')
        st.write('Di balik Tandur, ada cerita tentang keinginan untuk membangun sebuah platform yang memungkinkan para petani untuk mengakses modal dengan lebih mudah. Seiring dengan pertumbuhan populasi dunia, kebutuhan akan makanan semakin meningkat. Namun, petani seringkali menghadapi tantangan dalam memperoleh modal untuk meningkatkan produksi mereka.')

        st.write('Tandur lahir dari visi untuk menciptakan solusi yang memadukan teknologi dengan kebutuhan dunia pertanian. Kami percaya bahwa dengan memberikan akses yang lebih mudah ke modal, kami dapat membantu petani meningkatkan produksi mereka, menghasilkan makanan lebih banyak, dan pada akhirnya mendukung ketahanan pangan secara global.')

        st.header('Misi Kami')
        st.write('Misi kami di Tandur adalah memberdayakan petani dengan sumber daya yang mereka butuhkan untuk sukses. Kami berkomitmen untuk:')
        st.write('- Menyediakan akses yang mudah dan adil ke modal bagi petani.')
        st.write('- Membangun kemitraan yang kuat antara petani dan investor.')
        st.write('- Mengembangkan solusi inovatif untuk meningkatkan efisiensi dan produktivitas pertanian.')

        st.header('Nilai Kami')
        st.write('1. Keadilan: Kami memprioritaskan kesetaraan dan keadilan dalam semua interaksi kami.')
        st.write('2. Keterbukaan: Kami berkomitmen untuk transparansi dan keterbukaan dalam semua aspek bisnis kami.')
        st.write('3. Kolaborasi: Kami percaya bahwa kolaborasi adalah kunci untuk mencapai tujuan bersama.')
        st.write('4. Inovasi: Kami terus mencari cara baru untuk meningkatkan dan memperbaiki platform kami.')

        st.header('Bergabunglah dengan Kami')
        st.write('Apakah Anda ingin menjadi bagian dari perubahan positif dalam industri pertanian? Bergabunglah dengan kami di Tandur! Hubungi kami di email info@tandur.com untuk informasi lebih lanjut.')

    def about_us(self):
        st.write("Anda akan dialihkan ke halaman 'Tentang Kami'.")  # Ganti dengan fungsi atau halaman yang sesuai

    def home_page(self):
        st.write("Anda akan dialihkan ke halaman 'Halaman Utama'.")  # Ganti dengan fungsi atau halaman yang sesuai

    def invest_now(self):
        st.write("Anda akan dialihkan ke halaman 'Investasi Sekarang'.")  # Ganti dengan fungsi atau halaman yang sesuai


if __name__ == "__main__":
    platform = TandurPlatform()
    platform.about_tandur()
    platform.handle_navigation()
