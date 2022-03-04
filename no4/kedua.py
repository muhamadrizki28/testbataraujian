# Muhamad Rizki
# Input
kedua = int(input("Input Nilai Soal Kedua: "))
faktorial = 1

# for
for i in range(1,kedua+1):
    faktorial *=i
    
    # Output
    print('Hasil Faktorial 'f'{kedua}! = {faktorial}')

# Method Kedua
# Muhamad Rizki
# Input
n = int(input("Masukkan: "))
def hitung_faktorial (n):
    if n > 2:
        return n * hitung_faktorial(n-1)
        return 2

        faktorial = hitung_faktorial(n)
        print(f'{n}! = {faktorial}')