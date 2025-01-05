def prvni_sifra(zadani):
    with open (zadani, encoding = 'utf-8') as soubor:
        
        data = soubor.read()
        #data = "UXMUL(1234,34)SFLKHJASMASDLKMUASDLALASDKLJH"
        index = 0
        state = 1
        detekce_cisla = ""
        prvni_cislo = 0
        druhe_cislo  = 0
        vysledek = 0
        while (index < len(data)):
            
            match state:
                case 1: #Detekce M
                    detekce_cisla = ""
                    if data[index] == 'm': state = 2
                    
                case 2: #Detekce U
                    if data[index] == 'u': state = 3
                    else: state = 1

                case 3: #Detekce L
                    if data[index] == 'l': state = 4
                    else: state = 1

                case 4: #Detekce (
                    if data[index] == '(': state = 5
                    else: state = 1

                case 5: #Detekce 1. cislice 1. cisla
                    if data[index].isdigit():
                        detekce_cisla += data[index]
                        state = 6
                    else:
                        state = 1

                case 6: #Detekce 2. a 3. cislice
                    if data[index].isdigit() and len(detekce_cisla) < 3:
                        detekce_cisla += data[index]
                    elif data[index] == ',': 
                        #Musime si ulozit cislo
                        prvni_cislo = int(detekce_cisla)
                        detekce_cisla = ""
                        state = 7
                    else:
                        state = 1

                case 7: #Detekce 1. cislice 2. cisla
                    if data[index].isdigit():
                        detekce_cisla += data[index]
                        state = 8
                    else:
                        state = 1

                case 8: #Detekce 2. a 3. cislice 2. cisla
                    if data[index].isdigit() and len(detekce_cisla) < 3:
                        detekce_cisla += data[index]
                    elif data[index] == ')': 
                        #Musime si ulozit cislo
                        druhe_cislo = int(detekce_cisla)
                        detekce_cisla = ""
                        #MUL je hotov
                        vysledek += prvni_cislo * druhe_cislo
                        state = 1
                    else:
                        state = 1

            index += 1
    return vysledek

print(prvni_sifra('D:\Advent-of-code\letos\Day3\day3.txt'))

