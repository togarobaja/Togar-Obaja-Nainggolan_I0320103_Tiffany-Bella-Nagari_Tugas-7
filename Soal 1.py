# Soal 1 Tugas 7
teks = "Selamat datang di biro jodoh 2k21, Tentukan jodoh mu!"
print(teks.center(100,"="))
nama = input("Siapakah nama kamu? :")
gender = input("Kamu perempuan atau laki-laki (L/P) :")
a = gender.capitalize()
usia = int(input("Usiamu berapa? :"))
if usia >= 23 :
    print(nama.upper(),f"usia : {usia}")
    if a == "L":
        print("""    1. Kamu suka yang mana : lokal atau bule?
    2. Kriteria usia : lebih muda, seusia, atau lebih dewasa?
    3. kamu suka yang mana : belum menikah atau sudah menikah?""")
        pertanyaan1 = input("1.")
        pertanyaan2 = input("2.")
        pertanyaan3 = input("3.")
        kuisoner = [pertanyaan1,pertanyaan2,pertanyaan3]
        print(f"jawaban kamu {kuisoner}, sedang mencari pasangan yang cocok")
    else :
        print("""    1. Kamu suka a.)lokal atau b.)bule?
            2. Kriteria usia a.)lebih muda b.)seusia c.)lebih tua?
            3. kamu suka yang mana a.belum menikah b.sudah menikah""")
        pertanyaan1 = input("1.")
        pertanyaan2 = input("2.")
        pertanyaan3 = input("3.")
        kuisoner2 = [pertanyaan1, pertanyaan2, pertanyaan3]
        print(f"jawaban kamu {kuisoner2}, sedang mencari pasangan yang cocok")
else :
    print("Yakin nih mau jalin hubungan? mending fokus studi dan karir dulu ya!")