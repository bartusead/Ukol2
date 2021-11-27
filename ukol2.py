import csv

# Kontroluje správnost/přístupnost načteného souboru
try:
    with open("vstup.csv", encoding="utf8") as csvinfile,\
            open("vystup_7dni.csv", "w", encoding="utf8") as csvoutfile_tyden,\
                open("vystup_rok.csv", "w", encoding="utf8") as csvoutfile_rok:
        reader = csv.reader(csvinfile, delimiter = ",")
        writer_tyden = csv.writer(csvoutfile_tyden)
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
        # Nastaví první řádek do proměnné poc_rok (pak se z něj zjišťuje první rok v souboru) a přeskočí opět na začátek souboru
        poc_rok = next(reader)
        csvinfile.seek(0)
        
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
                avg_prutok = 0
                zbytek = 0
            cislo_radku += 1
        
        # Dopočítání průměru ze zbylých dnů
        cislo_radku -= zbytek
        if cislo_radku % 7 != 6:     
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
            rok = int(poc_rok[2])
            soucet_prutoku_rok = 0
            zbytek_rok = 0
            for row in reader:
                # Pokud se jedná o první záznam roku, uloží ho do proměnné prvni_den_rok
                if int(row[2]) == rok and zbytek_rok == 0:
                    prvni_den_rok = row
                # Procedura sčítání průtoků, případné přeskočení neplatné hodnoty
                try:
                    soucet_prutoku_rok = soucet_prutoku_rok + float(row[5])
                    zbytek_rok = zbytek_rok + 1
                except ValueError:
                    pass
                
                # Když program narazí na poslední den v roce, spočítá průměr za celý rok a zapíše ho do souboru
                if int(row[3]) == 12 and int(row[4]) == 31:
                    avg_prutok_rok = soucet_prutoku_rok / zbytek_rok
                    prvni_den_rok[5] = f"{avg_prutok_rok:.4f}"
                    writer_rok.writerow(prvni_den_rok)
                    zbytek_rok = 0
                    soucet_prutoku_rok = 0
                    avg_prutok_rok = 0
                    rok += 1

with open("vstup.csv", encoding="utf-8") as csvinfile:
    reader = csv.reader(csvinfile, delimiter = ",")

    for row in reader:
        if reader.line_num == 1:
            radek_max_prutok = row
            radek_min_prutok = row
            max_prutok = float(radek_max_prutok[5])
            min_prutok = float(radek_min_prutok[5])
        
        aktualni_prutok = float(row[5])
        
        if aktualni_prutok > max_prutok:
            radek_max_prutok = row
            max_prutok = aktualni_prutok
        elif aktualni_prutok < min_prutok:
            radek_min_prutok = row
            min_prutok = aktualni_prutok

    print(f"Maximální průtok byl {radek_max_prutok[4]}.{radek_max_prutok[3]}.{radek_max_prutok[2]} s hodnotou {radek_max_prutok[5]}.")
    print(f"Minimální průtok byl {radek_min_prutok[4]}.{radek_min_prutok[3]}.{radek_min_prutok[2]} s hodnotou {radek_min_prutok[5]}.")

       


    


        

        

            
        
        


       
    
    
   

       