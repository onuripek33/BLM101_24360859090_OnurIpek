Öğrenci Bilgileri: ONUR İPEK 24360859090

Proje Konusu: Veri Depolama ve Sayısal Sistemler

YouTube Linki: https://youtu.be/GqRHrf7dhE4

Proje Açıklaması: 
# 📄 Proje Dokümantasyonu: Çok Fonksiyonlu Taban Dönüştürücü

## 1. Proje Özeti
Bu proje, kullanıcıdan onluk (decimal) tabanda alınan bir tam sayıyı, Python'un hazır fonksiyonlarını (`bin()`, `hex()`) kullanmadan; tamamen matematiksel algoritmalarla ikilik (binary) ve onaltılık (hexadecimal) tabanlara dönüştüren bir hesaplama aracıdır. Ayrıca, elde edilen ikilik verinin bilgisayar belleğinde (RAM) nasıl saklandığını simüle eden görsel bir arayüz sunar.

## 2. Kullanılan Kütüphaneler ve Bağımlılıklar
Bu projede herhangi bir harici kütüphane (import) kullanılmamıştır.
Program, Python programlama dilinin standart yerleşik (built-in) özellikleri kullanılarak geliştirilmiştir. Bu tercih, algoritma mantığının arka planda nasıl işlediğini tam olarak göstermek amacıyla yapılmıştır.

## 3. Algoritma Mantığı (Matematiksel Temel)
Taban dönüşümleri için bilgisayar bilimlerinde standart olan "Sürekli Bölme Yöntemi" (Euclidean Division) kullanılmıştır. Algoritma şu iki temel operatör üzerine kuruludur:

1.  Modulo Operatörü (`%`): Sayının tabana bölümünden kalanı verir. Bu kalan, dönüşümün o basamağındaki rakamı oluşturur.
2.  Tam Bölme Operatörü (`//`): Sayıyı tabana böler ve ondalık kısmı atar. Bu işlem, sayıyı bir sonraki basamağa hazırlar.

### Döngü Mantığı:
* Sayı 0'dan büyük olduğu sürece bir `while` döngüsü çalışır.
* Her adımda sayının tabana (2 veya 16) bölümünden kalan bulunur.
* Bulunan kalan, sonuç metninin başına eklenir (Çünkü matematiksel olarak ilk bulunan kalan, en sağdaki basamaktır).
* Sayı tabana bölünerek küçültülür ve döngü başa döner.

## 4. Fonksiyonların Teknik İşleyişi

### A. `onluktan_ikiliye(sayi)`
* Girilen sayıyı sürekli olarak **2'ye böler**.
* Kalanlar (0 veya 1), string birleştirme yöntemiyle yan yana getirilir.
* **Örnek:** 5 sayısı için -> `1` (kalan), sonra `0` (kalan), sonra `1` (kalan) -> Sonuç: "101".

### B. `onluktan_onaltiliya(sayi)`
* Girilen sayıyı sürekli olarak **16'ya böler**.
* Kalanlar 9'dan büyükse (10-15 arası), sayısal değerler yerine harf karşılıkları kullanılır.
* Bunun için `hex_harfleri = "0123456789ABCDEF"` şeklinde bir karakter dizisi (string lookup table) tanımlanmıştır. Kalan sayı bu dizinin indeksi olarak kullanılarak doğru karakter (Örn: 10 için 'A') çekilir.

### C. `bellek_gorsellestir(ikili_deger)`
* Bu fonksiyon, elde edilen ham binary veriyi (Örn: "101") alır.
* **Padding (Doldurma): Bilgisayar belleği 8-bitlik (1 Byte) bloklardan oluştuğu için, veri uzunluğu 8'in katı olacak şekilde baş tarafı '0' ile doldurulur (Örn: "00000101").
* Sonuç, ASCII karakterleri kullanılarak kutucuklar halinde konsola çizdirilir.

## 5. Hata Yönetimi ve Kontrol
* **`try-except` Bloğu: Kullanıcının sayı yerine harf veya geçersiz karakter girmesi durumunda programın çökmesini engeller ve kullanıcıyı "Geçerli bir tam sayı girin" şeklinde uyarır.
* **Sonsuz Döngü:** `while True` yapısı ile program, kullanıcı 'q' tuşuna basıp çıkış yapana kadar sürekli yeni işlem kabul eder.
