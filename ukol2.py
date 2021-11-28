import csv

# Kontroluje správnost/přístupnost načteného souboru
try:
    with open("vstup.csv", encoding="utf8") as csvinfile,\
            open("vystup_7dni.csv", "w", encoding="utf8") as csvoutfile_tyden,\
                open("vystup_rok.csv", "w", encoding="utf8") as csvoutfile_rok:
        reader = csv.reader(csvinfile, delimiter = ",")
except FileNotFoundError:
    print("Vstupní soubor nenalezen, zkontroluj správnost názvu či umístění!")
    exit()
except PermissionError:
    print("Pro přístup k souboru nemáš práva!")
    exit()   

# Sedmidenní průtoky
# Načte a definuje vstupní soubor a definuje výstupní soubor 
with open("vstup.csv", encoding="utf8") as csvinfile,\
        open("vystup_7dni.csv", "w", encoding="utf8") as csvoutfile_tyden:
        reader = csv.reader(csvinfile, delimiter = ",")
        writer_tyden = csv.writer(csvoutfile_tyden)

        # Definice proměnných
        soucet_prutoku = 0 
        cislo_radku = 0
        zbytek = 0

        for row in reader:
            # Informuje uživatele o nulovém či záporném průtoku a přeskakuje neplatný formát průtoku
            try:
                if float(row[5]) == 0:
                    print(f"Dne {row[4]}.{row[3]}.{row[2]} došlo k nulovému průtoku!")
                if float(row[5]) < 0:
                    print(f"Dne {row[4]}.{row[3]}.{row[2]} došlo k zápornému průtoku!")
            except ValueError:
                print(f"Průtok ze dne {row[4]}.{row[3]}.{row[2]} není v čísleném formátu!")
                pass        
            # Pokud se jedná o první ze sedmi řádků, uloží ho do proměnné prvni_den
            if cislo_radku % 7 == 0:
                prvni_den = row
            # Procedura sčítání průtoků, případné přeskočení neplatné hodnoty
            try:
                soucet_prutoku = soucet_prutoku + float(row[5])
                zbytek = zbytek + 1
            except ValueError:
                pass
            # Když program narazí na poslední ze sedmi dnů, spočítá průměr a zapíše do souboru
            if cislo_radku % 7 == 6:
                avg_prutok = soucet_prutoku / 7
                prvni_den[5] = f"{avg_prutok:.4f}"
                writer_tyden.writerow(prvni_den)
                soucet_prutoku = 0 
                zbytek = 0
            cislo_radku += 1
        print(cislo_radku)
        # Dopočítání průměru ze zbylých dnů
        if cislo_radku % 7 == 0:
            pass
        else: 
            avg_prutok = soucet_prutoku / zbytek
            prvni_den[5] = f"{avg_prutok:.4f}"
            writer_tyden.writerow(prvni_den)


# Roční průtoky
# Načte a definuje vstupní soubor a definuje výstupní soubor 
with open("vstup.csv", encoding="utf8") as csvinfile,\
            open("vystup_rok.csv", "w", encoding="utf8") as csvoutfile_rok:
            reader = csv.reader(csvinfile, delimiter = ",")
            writer_rok = csv.writer(csvoutfile_rok)        
            
            # Definice proměnných
            cislo_radku = 0
            soucet_prutoku_rok = 0
            zbytek_rok = 0
            for row in reader:
                # Pokud se jedná o první záznam roku, uloží ho do proměnné prvni_den_rok
                soucasny_rok = int(row[2])
                if cislo_radku == 0:
                    prutok_rok = soucasny_rok
                    prvni_den_rok = row
                # Procedura sčítání průtoků, případné přeskočení neplatné hodnoty
                try:
                    soucasny_prutok = float(row[5])
                    soucet_prutoku_rok = soucet_prutoku_rok + float(row[5])                    
                    zbytek_rok = zbytek_rok + 1
                except ValueError:
                    pass
                
                # Když program narazí na nový rok, spočítá průměr za předchozí rok a zapíše ho do souboru
                if soucasny_rok != prutok_rok:
                    avg_prutok_rok = (soucet_prutoku_rok - soucasny_prutok) / (zbytek_rok -1)
                    prvni_den_rok[5] = f"{avg_prutok_rok:.4f}"
                    writer_rok.writerow(prvni_den_rok)
                    soucet_prutoku_rok = soucasny_prutok
                    zbytek_rok = 1
                    prutok_rok = soucasny_rok
                    prvni_den_rok = row
                cislo_radku = cislo_radku + 1
            # Jelikož po posledním roce program na nový rok nenarazí, musí se spočítat a zapsat zvlášť
            if soucasny_rok == prutok_rok:
                avg_prutok_rok = soucet_prutoku_rok / zbytek_rok
                prvni_den_rok[5] = f" {avg_prutok_rok:.4f}"
                writer_rok.writerow(prvni_den_rok)

# Maximální a minimální průtok
# Načtení souboru

with open("vstup.csv", encoding="utf-8") as csvinfile:
    reader = csv.reader(csvinfile, delimiter = ",")

    for row in reader:
        # Stanovení max. a min. průtoku podle prvního řádku
        if reader.line_num == 1:
            prutok_max_radek = row
            prutok_min_radek = row
            prutok_max = float(prutok_max_radek[5])
            prutok_min = float(prutok_min_radek[5])
        soucasny_prutok = float(row[5])
        # Program vždy porovná současný průtok s max. a min. průtokem a pokud je větší (menší), přepíše proměnnou max a min
        if soucasny_prutok > prutok_max:
            prutok_max_radek = row
            prutok_max = soucasny_prutok
        if soucasny_prutok < prutok_min:
            prutok_min_radek = row
            prutok_min = soucasny_prutok
    print(f"Dne {prutok_max_radek[4]}.{prutok_max_radek[3]}.{prutok_max_radek[2]} byl detekován maximální průtok, a to {prutok_max} m^3/s.")
    print(f"Dne {prutok_min_radek[4]}.{prutok_min_radek[3]}.{prutok_min_radek[2]} byl detekován minimální průtok, a to {prutok_min} m^3/s.")

# Kontrola chybějících dnů
# Načtení souboru
with open("vstup.csv", encoding="utf8") as csvinfile:
            reader = csv.reader(csvinfile, delimiter = ",")
            # Definice proměnných          
            cislo_radku_mes = 0
            zbytek_mesic = 0
            for row in reader:
                # Definice prvního měsíce
                soucasny_mes = int(row[3])
                if cislo_radku_mes == 0:
                    mesic = soucasny_mes
                try:
                    zbytek_mesic += 1 
                except ValueError:
                    pass
                
                # Když program zjistí nový měsíc, porovná, kolik dnů měl mít měsíc a kolik jsich skutečně měl
                if soucasny_mes != mesic:
                    if (int(row[3]) == 5 or int(row[3]) == 7 or int(row[3]) == 10 or int(row[3]) == 12) and zbytek_mesic != 31:
                        print(f"V měsíci {int(row[3])-1} roku {row[2]} chybí {31 - zbytek_mesic} dny")
                    
                    elif int(row[3]) == 3 and int(row[2]) % 4 == 0 and zbytek_mesic != 30:    
                        print(f"V měsíci {int(row[3])-1} roku {row[2]} chybí {30 - zbytek_mesic} dny")
                    elif int(row[3]) == 3 and int(row[2]) % 4 != 0 and zbytek_mesic != 29:
                        print(f"V měsíci {int(row[3])-1} roku {row[2]} chybí {29 - zbytek_mesic} dny")

                    elif (int(row[3]) == 2 or int(row[3]) == 4 or int(row[3]) == 6 or int(row[3]) == 8 or int(row[3]) == 9 or int(row[3]) == 11) and zbytek_mesic != 32:
                        print(f"V měsíci {int(row[3])-1} roku {row[2]} chybí {32 - zbytek_mesic} dny")
                    
                    elif int(row[3]) == 1 and zbytek_mesic != 32:
                        print(f"V měsíci 12 roku {row[2]} chybí {32 - zbytek_mesic} dny")
                    
                    mesic = soucasny_mes
                    zbytek_mesic = 1
                cislo_radku_mes +=1

                
