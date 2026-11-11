# BandungTales

Website latihan jasa tur jalan kaki di Bandung dengan pemandu berbahasa Inggris. Proyek ini hanya berjalan lokal untuk praktikum, bukan untuk dipublikasikan atau menerima pesanan nyata.

## Struktur file
- `app.py`: Flask, validasi form, dan perhitungan estimasi
- `templates/index.html`: isi dan struktur halaman
- `static/style.css`: tampilan

## Menyiapkan (sekali saja)
Windows (PowerShell):
```
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install flask
```
macOS / Linux:
```
python3 -m venv .venv
./.venv/bin/python -m pip install flask
```

## Menjalankan
Windows: `.\.venv\Scripts\python.exe -m flask --app app run --debug`

macOS / Linux: `./.venv/bin/python -m flask --app app run --debug`

Buka alamat yang muncul di terminal, biasanya http://127.0.0.1:5000/. Hentikan dengan Ctrl+C.

## Aturan estimasi
Rp150.000 per jam per grup, untuk 1 sampai 4 tamu. Jumlah tamu tidak mengalikan harga. Durasi hanya 2, 3, atau 4 jam.

## Contoh uji
- 3 jam, 2 tamu: Rp450.000
- 4 jam, 3 tamu: Rp600.000
- 2 jam, 4 tamu: Rp300.000
- 0 atau 5 tamu: pesan input tidak valid
