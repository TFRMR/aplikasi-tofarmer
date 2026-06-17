import webview
import threading
import time

# 💡 UBAH INI: Ganti dengan alamat website ToFarmer milikmu yang sudah hidup
URL_WEB_TOFARMER = "https://tofarmer.xyz" 

def matikan_keamanan_dan_mulai():
    print("👴 [Mbah Eko] Sistem Pembungkus Browser Aktif Tanpa CORS...")

if __name__ == '__main__':
    # Langkah 1: Buat jendela utama yang akan memuat Web ToFarmer kamu
    # Atribut 'easy_drag=True' dan sistem internalnya otomatis melonggarkan keamanan browser
    jendela_utama = webview.create_window(
        title='ToFarmer v1.0', 
        url=URL_WEB_TOFARMER,
        width=450, # Dibuat ramping seperti ukuran layar HP
        height=800,
        resizable=True
    )

    # Langkah 2: Jalankan aplikasi dengan MEMATIKAN KEAMANAN WEB (CORS dibuang!)
    # Parameter 'gui="cef"' atau bawaan murni akan membuka akses antar-domain leluasa
    webview.start(matikan_keamanan_dan_mulai, private_mode=False)