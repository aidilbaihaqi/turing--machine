
## Instal Python

Unduh Python: Kunjungi Python.org dan unduh versi terbaru.

Periksa Instalasi Python: Buka Command Prompt (CMD) dan ketik perintah berikut untuk memastikan Python terinstal dengan benar:

```bash
  python --version
```

## Membuat Virtual Environment
Virtual Enviroment dibutuhkan untuk menghubungkan aplikasi front-end (HTML-CSS) dan back-end (Python) dengan menggunakan library Flask.

- Buka Command Prompt dan navigasikan ke folder proyek Anda, misalnya
```bash
  cd C:\Users\NamaPengguna\Documents\my_project
```
- Buat Virtual Enviroment dengan perintah berikut:
```bash
  python -m venv venv
```
- Aktifkan Virtual Environment:
```bash
  venv\Scripts\activate
```
Setelah diaktifkan, prompt akan berubah menjadi:
```bash
  (venv) C:\Users\NamaPengguna\Documents\my_project>
```

## Instalasi Depedensi
Jika Anda belum memiliki dependensi yang diperlukan, Anda harus menginstal Flask untuk menjalankan aplikasi ini.
- Instal Flask di virtual environment dengan perintah:
```bash
  pip install Flask
```

## Menjalankan Program
Sekarang Anda siap untuk menjalankan aplikasi web.
- Jalankan Flask App dengan perintah:
```bash
  python app.py
```
- Flask akan mulai berjalan, dan Anda akan melihat output seperti ini:
```bash
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
- Akses Program:
Buka browser web Anda dan kunjungi alamat berikut:
```bash
  http://127.0.0.1:5000/
```

## Menggunakan Program
Setelah aplikasi berjalan di browser, Anda dapat mulai menggunakan Mesin Turing untuk mengonversi kata ke kode biner.

### Masukkan kata
- Pada halaman utama, Anda akan melihat formulir dengan kolom input.
- Masukkan kata (gunakan hanya huruf kecil a-z, seperti halo) di kolom "Masukkan Kata (huruf kecil a-z)".

### Klik Tombol Konversi
- Setelah memasukkan kata, klik tombol Konversi.
- Mesin Turing akan memproses kata yang dimasukkan dan mengonversi setiap huruf menjadi kode biner, sambil menampilkan transisi state.

### Lihat Hasil
- Setelah tombol Konversi ditekan, hasilnya akan ditampilkan di bawah formulir input.
- Hasil ini akan menunjukkan karakter yang dimasukkan, state yang dilalui, dan kode biner untuk setiap karakter.
- Jika kata yang dimasukkan valid, Anda akan melihat hasil dalam format seperti ini:
```bash
  h (q_h) -> 01101000
  a (q_a) -> 01100001
  l (q_l) -> 01101100
  o (q_o) -> 01101111
  State akhir: accept
```

### Input Tidak Valid
Jika Anda memasukkan karakter yang tidak valid, seperti angka atau simbol, program akan memberikan pesan kesalahan:
```bash
  Input tidak valid. Hanya huruf kecil a-z yang diperbolehkan.
```

### Menonaktifkan Virtual Enviroment
Jika Anda sudah selesai menggunakan virtual environment, Anda dapat menonaktifkannya dengan perintah:
```bash
  deactivate
```
Ini akan mengembalikan prompt ke kondisi semula tanpa (venv).
    