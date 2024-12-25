Tugas 1 

# Caesar Cipher - Enkripsi dan Dekripsi

## Deskripsi Tugas
Aplikasi ini adalah implementasi dari algoritma Caesar Cipher untuk proses enkripsi dan dekripsi teks. Pengguna dapat memasukkan teks, memilih mode (Enkripsi atau Dekripsi), dan menentukan jumlah pergeseran karakter. Hasil dari proses akan ditampilkan di aplikasi.

## Isi Tugas
1. **Masukkan Teks**: Pengguna dapat memasukkan teks yang akan dienkripsi atau didekripsi.
2. **Masukkan Pergeseran**: Pengguna perlu menentukan jumlah pergeseran karakter dalam angka.
3. **Pilih Mode**: Pengguna dapat memilih mode "Enkripsi" untuk mengenkripsi teks atau "Dekripsi" untuk mendekripsi teks.
4. **Proses**: Tombol untuk memproses teks dengan Caesar Cipher.
5. **Bersihkan**: Tombol untuk menghapus semua input dan hasil.
6. **Keluar**: Tombol untuk menutup aplikasi.

## Cara Menjalankan Aplikasi

### Prasyarat
Pastikan Anda memiliki **Python 3.x** terinstal di komputer Anda. Selain itu, Anda juga memerlukan pustaka **Tkinter** dan **ttk**, yang sudah termasuk dalam instalasi Python standar.

### Langkah-langkah Menjalankan
1. Salin kode Python di atas ke file dengan nama `caesar_cipher_app.py`.
2. Buka terminal atau command prompt.
3. Navigasikan ke direktori tempat file `caesar_cipher_app.py` disimpan.
4. Jalankan perintah berikut:

   ```bash
   python caesar_cipher_app.py
   ```

5. Aplikasi akan terbuka dengan antarmuka pengguna.
6. Masukkan teks, pergeseran, dan pilih mode, lalu tekan tombol **Proses** untuk mendapatkan hasil.
7. Gunakan tombol **Bersihkan** untuk menghapus input dan hasil, atau tombol **Keluar** untuk menutup aplikasi.

## Catatan
- Pergeseran harus berupa angka.
- Pastikan input teks valid sebelum memproses.
- Hasil enkripsi atau dekripsi akan ditampilkan di bagian "Hasil" pada aplikasi.

## Contoh Penggunaan
1. Masukkan teks: `HELLO`
2. Masukkan pergeseran: `3`
3. Pilih mode: **Enkripsi**
4. Tekan tombol **Proses**
5. Hasil: `KHOOR`

## Penulis
Tugas ini disusun sebagai bagian dari pembelajaran algoritma kriptografi sederhana menggunakan bahasa pemrograman Python.




Tugas 2

# DES Encryption/Decryption Tool

## Deskripsi Tugas
Aplikasi ini adalah implementasi algoritma Data Encryption Standard (DES) untuk mengenkripsi dan mendekripsi teks menggunakan kunci 8 karakter. Aplikasi ini memiliki antarmuka pengguna berbasis GUI yang dibuat dengan Tkinter.

## Isi Tugas
1. **Input Key**: Pengguna harus memasukkan kunci yang terdiri dari 8 karakter.
2. **Input Text**: Masukkan teks yang akan dienkripsi atau didekripsi.
3. **Encrypt**: Tombol untuk mengenkripsi teks yang dimasukkan.
4. **Decrypt**: Tombol untuk mendekripsi teks terenkripsi.
5. **Output Text**: Hasil enkripsi atau dekripsi akan ditampilkan di area output.

## Cara Menjalankan Aplikasi

### Prasyarat
- **Python 3.x** terinstal di sistem.
- Pustaka **pycryptodome** terinstal. Anda dapat menginstalnya dengan perintah:
  ```bash
  pip install pycryptodome
  ```

### Langkah Menjalankan
1. Simpan kode di atas ke file bernama `des_tool.py`.
2. Buka terminal atau command prompt.
3. Navigasikan ke direktori tempat file `des_tool.py` disimpan.
4. Jalankan aplikasi dengan perintah berikut:
   ```bash
   python des_tool.py
   ```
5. Aplikasi akan terbuka.

### Catatan Penggunaan
- **Kunci harus tepat 8 karakter**. Jika tidak, aplikasi akan menampilkan pesan kesalahan.
- Teks masukan bisa berupa teks biasa untuk enkripsi atau teks terenkripsi (Base64) untuk dekripsi.
- Hasil proses akan ditampilkan di area "Output Text".

## Penulis
Tugas ini dibuat sebagai bagian dari eksplorasi algoritma enkripsi DES menggunakan Python dan pustaka Pycryptodome.




Tugas 3

# Aplikasi Steganografi

## Deskripsi Tugas
Aplikasi ini digunakan untuk menyembunyikan (Hide) dan menampilkan (Show) data pada gambar menggunakan teknik steganografi. Data yang disisipkan akan disembunyikan dalam bit piksel gambar. Aplikasi ini juga memungkinkan pengguna untuk membuka gambar, menyimpan gambar dengan data yang telah disisipkan, serta keluar dari aplikasi.

## Cara Menjalankan Aplikasi
1. **Persiapan**
   - Pastikan Python 3 sudah terinstal di komputer Anda.
   - Instal pustaka yang dibutuhkan dengan menjalankan perintah berikut di terminal:
     ```
     pip install pillow
     ```

2. **Jalankan Program**
   - Simpan kode Python di file dengan nama, misalnya, `steganography_app.py`.
   - Jalankan program dengan perintah:
     ```
     python steganography_app.py
     ```

3. **Penggunaan Aplikasi**
   - **Open Image**: Buka gambar yang akan digunakan untuk menyisipkan data.
   - **Hide Data**: Masukkan data yang ingin disembunyikan di dalam gambar.
   - **Show Data**: Tampilkan data yang telah disembunyikan di dalam gambar.
   - **Save Image**: Simpan gambar yang telah dimodifikasi.
   - **Exit**: Keluar dari aplikasi.

## Catatan Penting
- Gunakan file gambar dalam format `PNG`, `JPG`, atau `JPEG`.
- Data yang disisipkan akan diakhiri dengan tanda "***" sebagai penanda akhir data.
- Pastikan ukuran gambar cukup besar untuk menyimpan data yang ingin disisipkan.

