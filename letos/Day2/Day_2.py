def prvni_sifra(zadani):
    safe = 0
    with open (zadani, encoding = 'utf-8') as soubor:
        passed = 0
        for radek in soubor:
            radek = [int(cislo) for cislo in radek.split()]
            incs = True
            descs = True
            for i in range (0, len(radek) - 1):                
                distance = int(radek[i+1]) - int(radek[i])
                '''if  1 <= distance <= 3 :                        
                    incs = incs + 1 
                elif -3 <= distance <= -1:
                    descs = descs + 1
                else:
                    break
            if (incs > 0 and descs == 0) or (incs == 0 and descs > 0):
                safe = safe + 1'''
                if not (1 <= abs(distance) <= 3):
                    incs = False
                    descs = False
                    break
                
                # Kontrola směru
                if distance > 0:
                    descs = False
                elif distance < 0:
                    incs = False
            
            # Pokud jsou všechny hodnoty buď rostoucí, nebo klesající, řádek je bezpečný
            if incs or descs:
                safe += 1
            
        print(safe)

prvni_sifra('D:\Advent-of-code\letos\Day2\day2.txt')