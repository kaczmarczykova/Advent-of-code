def prvni_sifra(zadani):
    with open (zadani, encoding = 'utf-8') as soubor:
        left = []
        right = []
        distance = []
        result = 0
        for radek in soubor:
            radek = radek.split("   ")
            radek = list(radek)
            left.append(int(radek[0]))
            right.append(int(radek[1]))
        left.sort()
        right.sort()
        print(left)

prvni_sifra('D:\Advent of code\2024\Day1\day1.txt')