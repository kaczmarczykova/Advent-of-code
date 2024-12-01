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
        for i in range (0, len(left)):
            if left[i] > right[i]:
                distance.append(left[i] - right[i])
            else:
                distance.append(right[i] - left[i])
        for cislo in distance:
            result += cislo
        print(result)

def druha_sifra(zadani):
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
        for cislo in left:
            count = 0
            for i in range (0, len(left)):
                if cislo == right[i]:
                    count += 1
            distant = cislo * count            
            distance.append(distant)
        for number in distance:
            result += number
        print(result)



prvni_sifra('D:\Advent of code\letos\Day1\day1.txt')
druha_sifra('D:\Advent of code\letos\Day1\day1.txt')