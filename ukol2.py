import csv

with open("data.csv", encoding="utf8") as csvinfile,\
       open("vystup_7dni.csv", "w", encoding="utf8") as csvoutfile_tyden:
    reader = csv.reader(csvinfile, delimiter = ",")
    writer_tyden = csv.writer(csvoutfile_tyden)
    
    
           
# Chyby - chybí soubor, nemám práva, není .csv...

    soucet_prutoku = 0 
    cislo_radku = 0
    zbytek = 0

    for row in reader:
        if float(row[5]) <= 0:
            print(f"Dne {row[4]}.{row[3]}.{row[2]} došlo k nulovému či zápornému průtoku!")
        if cislo_radku % 7 == 0:
            prvni_den = row
        
        try:
            soucet_prutoku = soucet_prutoku + float(row[5])
            zbytek = zbytek + 1
        except ValueError:
            print("Průtok není v čísleném formátu!")

        if cislo_radku % 7 == 6:
            avg_prutok = soucet_prutoku / 7
            prvni_den[5] = f"{avg_prutok:.4f}"
            writer_tyden.writerow(prvni_den)
            soucet_prutoku = 0 
            avg_prutok = 0
            zbytek = 0
        cislo_radku += 1
        

        

            
        
        


       
    
    
   

       