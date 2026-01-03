def onluktan_ikiliye(sayi):
    """
    Onluk tabandaki (decimal) bir sayıyı ikilik (binary) tabana çevirir.
    Hazır bin() fonksiyonu yerine matematiksel 'bölüm ve kalan' mantığı kullanılır.
    """
    if sayi == 0:
        return "0"

    ikili_string = ""
    gecici_sayi = sayi

    # Sayı 0 olana kadar 2'ye bölme işlemi yapıyoruz (Matematiksel döngü)
    while gecici_sayi > 0:
        kalan = gecici_sayi % 2  # Modulo operatörü ile kalanı bul (0 veya 1)
        ikili_string = str(kalan) + ikili_string  # Kalanı metnin BAŞINA ekle (Tersten dizilir)
        gecici_sayi = gecici_sayi // 2  # Tam bölme işlemi ile sayıyı küçült

    return ikili_string


def onluktan_onaltiliya(sayi):
    """
    Onluk tabandaki sayıyı onaltılık (hexadecimal) tabana çevirir.
    Hazır hex() fonksiyonu yerine liste indeksleme mantığı kullanılır.
    """
    if sayi == 0:
        return "0"

    # 0-15 arası kalanların karşılık geldiği karakterler
    hex_harfleri = "0123456789ABCDEF"
    hex_string = ""
    gecici_sayi = sayi

    while gecici_sayi > 0:
        kalan = gecici_sayi % 16  # 16'ya bölümden kalanı bul
        hex_string = hex_harfleri[kalan] + hex_string  # İlgili karakteri başa ekle
        gecici_sayi = gecici_sayi // 16  # Sayıyı 16'ya böl

    return hex_string


def bellek_gorsellestir(ikili_deger):
    """
    Binary stringi alır ve 8-bitlik (byte) kutucuklar halinde ekrana basar.
    Örnek görünüm: | 0 | 0 | 1 | 0 | ...
    """
    # 1. Adım: 8 bit olması için başa sıfır ekleme (Padding)
    # Eğer sayı 8 bitten büyükse 16 bite tamamlar
    bit_uzunlugu = len(ikili_deger)
    gerekli_uzunluk = ((bit_uzunlugu - 1) // 8 + 1) * 8  # En yakın 8'in katını bulur

    # zfill() stringin başına 0 ekler. Bunu manuel de yapabilirdik ama görselleştirme için string metodu uygundur.
    formatli_binary = ikili_deger.zfill(gerekli_uzunluk)

    print("\n--- 💾 BELLEK GÖRÜNÜMÜ (RAM) ---")
    print(f"Veri Uzunluğu: {gerekli_uzunluk} Bit")

    # Kutucukların üst çizgisi
    print("+" + "---+" * gerekli_uzunluk)

    # Bitlerin yazdırılması
    satir = "|"
    for bit in formatli_binary:
        satir += f" {bit} |"
    print(satir)

    # Kutucukların alt çizgisi
    print("+" + "---+" * gerekli_uzunluk)
    print("-" * 30)


def ana_program():
    print("==========================================")
    print("🤖 ÇOK FONKSİYONLU TABAN DÖNÜŞTÜRÜCÜ")
    print("==========================================")

    while True:
        try:
            # Kullanıcıdan onluk tabanda sayı al
            giris = input("\nÇevirmek istediğiniz onluk (Decimal) sayıyı girin (Çıkış için 'q'): ")

            if giris.lower() == 'q':
                print("Program kapatılıyor...")
                break

            sayi = int(giris)

            print("\nSeçenekler:")
            print("1. İkilik Tabana Çevir (Binary)")
            print("2. Onaltılık Tabana Çevir (Hexadecimal)")
            secim = input("Seçiminiz (1 veya 2): ")

            if secim == '1':
                sonuc = onluktan_ikiliye(sayi)
                print(f"\n✅ SONUÇ (Binary): {sonuc}")
                # Bellek görselleştirmesi her durumda binary üzerinden yapılır
                bellek_gorsellestir(sonuc)

            elif secim == '2':
                sonuc_hex = onluktan_onaltiliya(sayi)
                sonuc_bin = onluktan_ikiliye(sayi)  # Görselleştirme için yine binary lazım
                print(f"\n✅ SONUÇ (Hex): {sonuc_hex}")
                bellek_gorsellestir(sonuc_bin)

            else:
                print("❌ Hatalı seçim! Lütfen 1 veya 2'yi seçin.")

        except ValueError:
            print("❌ Lütfen geçerli bir tam sayı girin!")


# Programı başlat
if __name__ == "__main__":
    ana_program()
