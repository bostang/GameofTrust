# TheGameOfTrust

Tugas Besar EL4236 Perancangan Perangkat Lunak Jaringan berupa permainan dua orang yang menjelaskan suatu konsep dalam teori permainan

## Anggota

1. Karma Kunga (13220028)
2. Bostang Palaguna (13220055)
3. Yansen Dwiputra (13220056)

## Perintah

### Fungsional Umum
Buatlah suatu aplikasi _server_ dan _multiple clients_ dengan _server_ bersifat pasif dan _client_ bersifat aktif. _Client_ diimplementasikan dengan dua protokol aplikasi yang berbeda (boleh diganti dengan _socket_). _Client_ dapat melakukan dua tipe request:
- `POST` atau `PUBLISH` (mengirimkan data)
- `GET` atau `SUBSCRIBE` (menerima data)

_Server_ selalu memberikan _response_ terhadap _request_ dari _client_.

_Server_ bisa mendaftarkan profil _client_, _client_ bisa menyimpan profil miliknya. Pada saat _client_ _reconnect_, profilnya tidak hilang. Namun _client_ bisa di-_reset_, _request_ ke _server_ untuk _register_ profil _client_ baru.

Server bisa menyimpan _history request_ dari _client_ (termasuk profil _client_) yang berbeda-beda dengan alternatif metode:
- log file
- database

_Client_ bisa menyimpan _history request_ dan _response_, atau _history publish_, atau _history subscribe_ (termasuk profil dirinya) beserta _time stamp_. Metode penyimpanan bergantung _environment_ di _client_.

### Komunikasi Data

ㆍRegistrasi
- client mengirimkan profil-nya untuk di register di server
- server menerima request dan memberikan respons, atau memberikan acknowledge
- Server harus bisa menerima proses registrasi dari client yang berbeda-beda.

_Client_ `get` informasi _time_ ke _server_ untuk disimpan atau disinkronkan di lokal.

_Client_ mengirimkan-`post`/`publish` (`message-1`, `message-2`,.., `message-n` dan menyimpan _history_-nya. Selanjutnya menerima _response_/_acknowedge_ dari server apakah `message-n` itu berhasil diterima dan disimpan oleh _server_.

_Client_ meminta `get` _history_ `message-n` ke server terkait client tersebut

Context message, punya arti dan dapat dikembangkan lebih lanjut, misal: message kehadiran; bukan "hello world".

## Deskripsi Aplikasi

Permainan 'game of trust' diimplementasikan pada client python dengan menggunakan GUI : Tkinter. Aplikasi akan memiliki fitur-fitur sebagai berikut:

#### 1. Registrasi Pemain
- Pemain akan melakukan registrasi dengan mengirimkan profil mereka ke server.
- Server akan menerima permintaan registrasi dari setiap pemain dan memberikan respons atau acknowledgement.
- Profil pemain akan disimpan oleh server untuk memungkinkan pemain untuk tetap terdaftar bahkan setelah mereka keluar dan masuk kembali ke permainan.

#### 2. Sinkronisasi Waktu
- Pemain dapat melakukan permintaan ke server untuk mendapatkan informasi waktu yang akan disimpan atau disinkronkan secara lokal di perangkat pemain.
  
#### 3. Mengirim Pesan Kepercayaan
- Pemain dapat mengirimkan pesan kepercayaan (misalnya, "Aku mempercayaimu") kepada pemain lain.
- Pesan ini akan dikirim melalui aplikasi kepada pemain yang dituju dan akan disimpan dalam riwayat pesan pemain yang mengirimnya.
- Server akan memberikan respons atau pengakuan kepada pemain pengirim apakah pesan kepercayaan tersebut berhasil diterima dan disimpan.

#### 4. Meminta Riwayat Pesan
- Pemain dapat meminta riwayat pesan yang mereka kirimkan kepada pemain lain.
- Permintaan ini akan dikirim ke server, dan server akan memberikan riwayat pesan terkait kepada pemain yang bersangkutan.

#### Metode Penyimpanan Data
- Server akan menyimpan riwayat pesan dan profil pemain dalam log file atau basis data, sesuai dengan kebutuhan dan lingkungan sistem.
- Pemain juga dapat menyimpan riwayat pesan dan respons dalam aplikasi mereka secara lokal.

## Pranala

[PPT Presentasi](https://www.canva.com/design/DAGEWLBVOyk/dGYrbv8lbxtO0rnk2iWqfw/edit?utm_content=DAGEWLBVOyk&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

## Referensi

[The Evolution of Trust](https://ncase.me/trust/)
