# Muhamad Rizki
# Input
pertama = int(input("Input Nilai Soal Pertama: "))
faktorial = 1

# for
for i in range(1,pertama+1):
    faktorial *=i
    
    # Output
    print('Hasil Faktorial 'f'{pertama}! = {faktorial}')