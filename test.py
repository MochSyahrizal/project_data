# Fungsi untuk penjumlahan
def tambah(x, y):
    return x + y

# Fungsi untuk pengurangan
def kurang(x, y):
    return x - y

# Fungsi untuk perkalian
def kali(x, y):
    return x * y

# Fungsi untuk pembagian
def bagi(x, y):
    if y != 0:
        return x / y
    else:
        return "Tidak bisa membagi dengan nol!"

# Menu kalkulator
def kalkulator():
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    
    # Memilih operasi
    pilihan = input("Masukkan pilihan (1/2/3/4): ")
    
    # Memasukkan angka
    num1 = float(input("Masukkan angka pertama: "))
    num2 = float(input("Masukkan angka kedua: "))
    
    # Melakukan operasi berdasarkan pilihan
    if pilihan == '1':
        print(f"Hasil: {num1} + {num2} = {tambah(num1, num2)}")
    elif pilihan == '2':
        print(f"Hasil: {num1} - {num2} = {kurang(num1, num2)}")
    elif pilihan == '3':
        print(f"Hasil: {num1} * {num2} = {kali(num1, num2)}")
    elif pilihan == '4':
        print(f"Hasil: {num1} / {num2} = {bagi(num1, num2)}")
    else:
        print("Pilihan tidak valid!")

# Menjalankan kalkulator
kalkulator()