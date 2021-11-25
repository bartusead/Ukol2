import csv
from os import read
#cd documents\python\du_2\ukol2

try:
    with open("data.csv", encoding="utf8") as csvinfile,\
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
            
    # Chyby - chybí soubor, nemám práva, není .csv...
with open("data.csv", encoding="utf8") as csvinfile,\
        open("vystup_7dni.csv", "w", encoding="utf8") as csvoutfile_tyden,\
            open("vystup_rok.csv", "w", encoding="utf8") as csvoutfile_rok:
        reader = csv.reader(csvinfile, delimiter = ",")
        writer_tyden = csv.writer(csvoutfile_tyden)
        writer_rok = csv.writer(csvoutfile_rok)
        
        poc_rok = next(reader)
        csvinfile.seek(0)

        
        """soucet_prutoku = 0 
        cislo_radku = 0
        zbytek = 0

        for row in reader:
            if float(row[5]) == 0:
                print(f"Dne {row[4]}.{row[3]}.{row[2]} došlo k nulovému průtoku!")

            if float(row[5]) < 0:
                print(f"Dne {row[4]}.{row[3]}.{row[2]} došlo k zápornému průtoku!")
            
            if cislo_radku % 7 == 0:
                prvni_den = row
            
            try:
                soucet_prutoku = soucet_prutoku + float(row[5])
                zbytek = zbytek + 1
            except ValueError:
                print("Průtok není v čísleném formátu!")
                pass

            if cislo_radku % 7 == 6:
                avg_prutok = soucet_prutoku / 7
                prvni_den[5] = f"{avg_prutok:.4f}"
                writer_tyden.writerow(prvni_den)
                soucet_prutoku = 0 
                avg_prutok = 0
                zbytek = 0
            cislo_radku += 1
            print(cislo_radku)"""

        rok = int(poc_rok[2])
        soucet_prutoku_rok = 0
        zbytek_rok = 0
        
        for row in reader:
            if int(row[2]) == rok and zbytek_rok == 0:
                prvni_den_rok = row
            try:
                soucet_prutoku_rok = soucet_prutoku_rok + float(row[5])
                zbytek_rok = zbytek_rok + 1
                print(zbytek_rok)
            except ValueError:
                print("Průtok není v čísleném formátu!")
                pass
            if int(row[3]) == 12 and int(row[4]) == 31:
                avg_prutok_rok = soucet_prutoku_rok / zbytek_rok
                prvni_den_rok[5] = f"{avg_prutok_rok:.4f}"
                writer_rok.writerow(prvni_den_rok)
                zbytek_rok = 0
                soucet_prutoku_rok = 0
                avg_prutok_rok = 0
                rok += 1
            

    


        

        

            
        
        


       
    
    
   

       