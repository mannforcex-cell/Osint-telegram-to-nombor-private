import requests
import time
import sys
import os
from datetime import datetime

# ========== WARNA (ANSI) ==========
class Warna:
    HEADER = '\033[95m'
    BIRU = '\033[94m'
    HIJAU = '\033[92m'
    KUNING = '\033[93m'
    MERAH = '\033[91m'
    CYAN = '\033[36m'
    PUTIH = '\033[37m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

def cetak(teks, warna=Warna.PUTIH, bold=False):
    gaya = warna
    if bold:
        gaya += Warna.BOLD
    print(f"{gaya}{teks}{Warna.RESET}")

# ========== KELAS UTAMA ==========
class DarkForceOSINT:
    def __init__(self):
        self.api_url = "https://api-danxy-telenumb-rt2cfhi97hfaygvj.vercel.app/api/osint/tele-numb"
        self.token = None
        self.limit = 0
        self.baki = 0
        self.order_id = None
        self.pakej_nama = None

    def loading(self, mesej="Memproses", ulang=3):
        """Animasi loading yang lebih lancar"""
        for _ in range(ulang):
            for simbol in ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]:
                sys.stdout.write(f"\r{Warna.CYAN}[{simbol}] {mesej}...{Warna.RESET}")
                sys.stdout.flush()
                time.sleep(0.05)
        sys.stdout.write(f"\r✅ {Warna.HIJAU}{mesej} Selesai!{Warna.RESET}\n")

    def banner(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        cetak("""
╔══════════════════════════════════════════════════════════╗
║   ██████╗  █████╗ ██████╗ ██╗  ██╗                       ║
║   ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝                       ║
║   ██║  ██║███████║██████╔╝█████╔╝                        ║
║   ██║  ██║██╔══██║██╔══██╗██╔═██╗                        ║
║   ██████╔╝██║  ██║██║  ██║██║  ██╗                       ║
║   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝                       ║
║   DARK FORCE OSINT - TELEGRAM ID TO NUMBER               ║
║   DEVELOPER : MFX OFFICIAL                               ║
║   VERSION   : V1                                         ║
╚══════════════════════════════════════════════════════════╝
        """, Warna.CYAN, bold=True)
        cetak("💡 STATUS: ALATAN PENDIDIKAN & PENYELIDIKAN OSINT SELEKTIF", Warna.KUNING, bold=True)
        cetak("⚠️ AMARAN: Sila patuhi had kadar (rate limit) pelayan untuk mengelakkan sekatan.", Warna.MERAH)
        cetak("🔒 NOTA  : Penggunaan alatan ini tertakluk di bawah tanggungjawab pengguna sendiri.\n", Warna.PUTIH)

    def sahkan_token(self):
        """
        Menyemak status keaktifan dan kesahihan token terus melalui API.
        Mencuba request dummy untuk menguji respon pelayan terhadap token tersebut.
        """
        self.loading("Menyemak status kesahihan token anda", 4)
        
        # Menggunakan ID pengujian rawak untuk menyemak respon token
        test_url = f"{self.api_url}?id=12345678&token={self.token}"
        
        try:
            response = requests.get(test_url, timeout=10)
            res_text = response.text.lower()
            
            # Semakan status HTTP atau mesej ralat spesifik dalam respon JSON/Teks
            if response.status_code in [401, 403] or "invalid" in res_text or "expired" in res_text:
                cetak("\n❌ [RALAT] Token tidak sah atau telah tamat tempoh!", Warna.MERAH, bold=True)
                cetak("   Sila dapatkan token baharu yang sah daripada pembekal.", Warna.KUNING)
                return False
                
            elif response.status_code == 400 and ("token" in res_text):
                cetak("\n❌ [RALAT] Token ditolak oleh pelayan.", Warna.MERAH, bold=True)
                return False
                
            else:
                # Jika lepas (Status 200 atau 400 disebabkan isu ID sahaja, bermakna token sah)
                cetak("\n✅ [BERJAYA] Token disahkan aktif!", Warna.HIJAU, bold=True)
                return True
                
        except requests.exceptions.RequestException as e:
            cetak(f"\n⚠️ [AMARAN] Gagal menghubungi pelayan pengesahan ({e}).", Warna.KUNING)
            cetak("   Meneruskan sesi dengan andaian token sedia ada.", Warna.PUTIH)
            return True

    def payment_receipt(self, pakej):
        """Paparan resit transaksi yang lebih kemas dan korporat"""
        self.order_id = f"ORD-{datetime.now().strftime('%Y%m%d%H%M%S')}-MFX{os.urandom(4).hex().upper()}"
        harga = {"HARIAN": 6, "MINGGUAN": 12, "BULANAN": 16}
        limit = {"HARIAN": 50, "MINGGUAN": 120, "BULANAN": 1000}
        
        print("\n" + "─" * 60)
        cetak("   RESIT PENGESAHAN LANGGANAN API", Warna.HIJAU, bold=True)
        print("─" * 60)
        print(f" 📆 Jenis Pakej   : {pakej}")
        print(f" 💰 Amaun Proforma : RM{harga[pakej]}.00")
        print(f" 🆔 No. Rujukan   : {self.order_id}")
        print(f" 🔢 Had Akses     : {limit[pakej]} Permintaan")
        print(f" 📡 Titik Hujung  : {self.api_url}")
        print("─" * 60)
        cetak(f" 🔑 Kunci Token   : {self.token}", Warna.HIJAU)
        print("─" * 60)
        
        print("\n💡 Contoh Sintaks Integrasi (cURL):")
        cetak(f'   curl -X GET "{self.api_url}?id=TARGET_ID&token={self.token}"', Warna.KUNING)
        
        input(f"\n{Warna.BIRU}[Tekan ENTER untuk melancarkan konsol carian]{Warna.RESET}")

    def minta_token_dan_beli(self):
        """Aliran kemasukan token dan pengesahan mandatori"""
        cetak("\n🔐 [PENGESAHAN] Sila masukkan Kunci Token API anda", Warna.KUNING, bold=True)
        cetak("   Hubungi Sokongan Teknikal: @ManForceX_Official\n", Warna.CYAN)
        
        while True:
            self.token = input(f"{Warna.BIRU}🔑 Masukkan Token : {Warna.RESET}").strip()
            if not self.token:
                cetak("❌ Ruangan token tidak boleh dibiarkan kosong!", Warna.MERAH)
                continue
            
            # Lakukan semakan kesahihan token terlebih dahulu
            if not self.sahkan_token():
                cetak("🔄 Sila cuba masukkan token semula.\n", Warna.KUNING)
                continue
                
            break
        
        self.pilih_pakej_untuk_receipt()

    def pilih_pakej_untuk_receipt(self):
        """Menu pemilihan pakej simulasi"""
        print("\n" + "═" * 55)
        cetak("🛒  KONFIGURASI PAKEJ AKSES API MFX", Warna.BIRU, bold=True)
        print("═" * 55)
        print(f"  [1] {Warna.HIJAU}HARIAN{Warna.RESET}   - RM6  | Had: 50")
        print(f"  [2] {Warna.KUNING}MINGGUAN{Warna.RESET} - RM12 | Had: 120")
        print(f"  [3] {Warna.MERAH}BULANAN{Warna.RESET}  - RM16 | Had: 1000")
        print("═" * 55)
        
        pilihan = input(f"\n{Warna.BIRU}💳 Sila pilih kod pakej (1-3) : {Warna.RESET}").strip()
        
        pakej_map = {"1": "HARIAN", "2": "MINGGUAN", "3": "BULANAN"}
        limit_map = {"HARIAN": 50, "MINGGUAN": 120, "BULANAN": 1000}
        
        if pilihan in pakej_map:
            self.pakej_nama = pakej_map[pilihan]
            self.limit = limit_map[self.pakej_nama]
            self.baki = self.limit
            self.payment_receipt(self.pakej_nama)
        else:
            cetak("⚠️ Pilihan tidak ditemui. Sistem menetapkan pakej HARIAN secara lalai (default).", Warna.KUNING)
            self.pakej_nama = "HARIAN"
            self.limit = 50
            self.baki = 50
            self.payment_receipt("HARIAN")

    def cari_nombor(self, telegram_id):
        """Membuat permintaan carian maklumat ke API"""
        if self.baki <= 0:
            cetak("\n⚠️ [HAD DICAPAI] Baki kuota carian anda telah habis.", Warna.MERAH, bold=True)
            return None

        url = f"{self.api_url}?id={telegram_id}&token={self.token}"
        
        try:
            self.loading(f"Menjalankan query OSINT bagi ID {telegram_id}", 2)
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                self.baki -= 1
                cetak(f"\n✅ [BERJAYA] Sesi Dikemaskini. Baki Kuota: {self.baki}/{self.limit}", Warna.HIJAU, bold=True)
                
                nombor = None
                if isinstance(data, dict):
                    nombor = data.get("phone_number") or data.get("nombor") or data.get("phone") or data.get("result")
                elif isinstance(data, str):
                    nombor = data
                
                return nombor if nombor else "Maklumat tidak ditemui dalam pangkalan data."
                    
            elif response.status_code in [401, 403]:
                cetak("\n❌ [SEKATAN] Token anda telah ditarik balik atau tamat tempoh ditengah sesi.", Warna.MERAH)
                return None
            elif response.status_code == 429:
                cetak("\n⚠️ [KADAR TINGGI] Pelayan mengehadkan request buat masa ini. Sila tunggu sebentar.", Warna.KUNING)
                return None
            else:
                cetak(f"\n❌ [RALAT SISTEM] Pelayan memulangkan status {response.status_code}", Warna.MERAH)
                return None
                
        except requests.exceptions.RequestException as e:
            cetak(f"\n⚠️ [MASALAH RANGKAIAN] Gagal menyambung ke API: {e}", Warna.MERAH)
            return None

    def main(self):
        self.banner()
        self.minta_token_dan_beli()
        
        while True:
            if self.baki <= 0:
                cetak("\n🔥 [NOTIFIKASI] Kuota semasa telah kosong.", Warna.MERAH, bold=True)
                ulang = input(f"{Warna.BIRU}🔁 Tukar/Beli pakej baru? (y/n) : {Warna.RESET}").strip().lower()
                if ulang == 'y':
                    self.pilih_pakej_untuk_receipt()
                    continue
                else:
                    break
                
            print(f"\n📊 BAKI SEMASA: {self.baki} / {self.limit} Kuota")
            telegram_id = input(f"{Warna.BIRU}🆔 Masukkan ID Telegram target (atau taip 'exit'): {Warna.RESET}").strip()
            
            if telegram_id.lower() == 'exit':
                cetak("\n👋 Sesi ditamatkan secara selamat. Terima kasih!", Warna.HIJAU)
                break
                
            if not telegram_id.isdigit():
                cetak("⚠️ Format tidak sah. ID Telegram mestilah dalam bentuk angka integer!", Warna.KUNING)
                continue
                
            hasil = self.cari_nombor(telegram_id)
            if hasil:
                print("─" * 50)
                cetak(f"📞 HASIL CARIAN: {hasil}", Warna.HIJAU, bold=True)
                print("─" * 50)
            
            time.sleep(1.5)

# ========== JALANKAN PROGRAM ==========
if __name__ == "__main__":
    try:
        osint = DarkForceOSINT()
        osint.main()
    except KeyboardInterrupt:
        cetak("\n\n⚠️ Sesi dihentikan secara paksa oleh pengguna.", Warna.KUNING)
    except Exception as e:
        cetak(f"\n🔥 Ralat Kritikal Terbina: {e}", Warna.MERAH)
        cetak("   Sila laporkan pepijat ini ke bahagian teknikal.", Warna.PUTIH)

