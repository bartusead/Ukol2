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
        if cislo_radku % 7 == 0:
            prvni_den = row
        
        try:
            soucet_prutoku = soucet_prutoku + float(row[5])
            zbytek = zbytek + 1
            print(f"soucet prutoku je {soucet_prutoku} ")
            print(zbytek)
        except ValueError:
            pass

        

            
        
        


       
    
    
   

       