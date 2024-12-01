def druha_sifra(zadani):
    with open (zadani, encoding = 'utf-8') as soubor:
        cisla = []
        slovnik = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero':'0'}
        for radek in soubor:
            for slovo in slovnik:
                if slovo in radek:
                    radek = radek.replace(slovo, slovnik[slovo])
        #for radek in soubor:
            digit = ''
            for znak in radek:
                if znak.isdigit() == True:
                    digit = digit + znak
                    break
            for i in range (len(radek) - 1, -1, -1):
                if radek[i].isdigit() == True:
                    digit = digit + radek[i]
                    break
            cisla.append(digit)
        vysledek = 0
        for i in range (0, len(cisla)):
            vysledek = vysledek + int(cisla[i])
    print(vysledek)

'''
def prvni_sifra(zadani):
    with open (zadani, encoding = 'utf-8') as soubor:
        cisla = []
        for radek in soubor:
            digit = ''
            for znak in radek:
                if znak.isdigit() == True:
                    digit = digit + znak
                    break
            reverse_radek = ''
            for i in range (len(radek) - 1, -1, -1):
                if radek[i].isdigit() == True:
                    digit = digit + radek[i]
                    break
            cisla.append(digit)
        vysledek = 0
        for i in range (0, len(cisla)):
            vysledek = vysledek + int(cisla[i])
    print(vysledek)
'''

#prvni_sifra('D:\Advent of code\day_1.txt')
druha_sifra('D:\Advent of code\day_1.txt')
    

