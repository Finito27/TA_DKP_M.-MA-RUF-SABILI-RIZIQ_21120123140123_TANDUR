import streamlit as st
import json
import os

st.title("Selamat Datang Di Tandur")

st.write("Platform Penghubung Investor dan Petani")

# Fungsi untuk memverifikasi login
def verify_login(username, password):
    if os.path.exists('users.json'):
        with open('users.json', 'r') as file:
            users = json.load(file)
        if username in users and users[username] == password:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.experimental_rerun()  # Rerun aplikasi untuk memperbarui konten
        else:
            st.error("Username atau password salah!")
    else:
        st.error("Database pengguna tidak ditemukan.")

# Fungsi untuk mendaftarkan akun baru
def register_account(username, password):
    if not username or not password:
        st.error("Username dan password tidak boleh kosong!")
        return

    if os.path.exists('users.json'):
        with open('users.json', 'r') as file:
            users = json.load(file)
    else:
        users = {}

    if username in users:
        st.error("Username sudah digunakan!")
        return

    users[username] = password
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)
    st.success(f"Akun baru dengan username '{username}' berhasil dibuat!")

# Fungsi untuk menampilkan konten dari halaman home
def home_page():
    st.write(f"Selamat datang, {st.session_state['username']}!")
    st.switch_page("pages/home.py")
   

# Main program
def main():
    # Jika pengguna sudah login, tampilkan konten home
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        home_page()
    # Jika pengguna belum login, tampilkan form login dan registrasi
    else:
        with st.form("login_form"):
            st.title("Halaman Login")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")
            if submitted:
                verify_login(username, password)

        with st.form("register_form"):
            st.title("Registrasi Akun Baru")
            new_username = st.text_input("Buat Username Baru")
            new_password = st.text_input("Buat Password Baru", type="password")
            register_submitted = st.form_submit_button("Daftar")
            if register_submitted:
                register_account(new_username, new_password)

# Panggil fungsi main untuk menjalankan aplikasi
if __name__ == "__main__":
    main()
