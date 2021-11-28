# Úkol 2 - výpočet a zápis sedmidenních a ročních průtoků z historických dat ČHMÚ


Program má za úkol načíst vstupní data o denních průtocích ze souboru vstup.csv (data pochází z webu ČHMÚ) a z nich spočítat průměrné sedmidenní a roční průtoky, které            následně zapíše do příslušných souborů. Dále program zobrazí maximální a minimální průtok za sledované období, nulové či záporné průtoky a poukáže na chybějící data.

1) **Načtení vstupních dat a jejich kontrola**
     Program se pokusí načíst soubor _vstup.csv_ a zkontroluje, zda takový soubor s daným umístěním existuje a zdali má práva na jeho čtení.

2) **Definice vstupního a výstupního souboru pro výpočet sedmidenních průtoků a definice proměnných**

3) **For cyklus pro výpočet sedmidenních průtoků**
    
    a) Program prochází vstupní soubor po řádcích. Nejdříve program kontroluje, jestli na daném řádku není hodnota průtoku nulová či záporná a pokud ano, vypíše kdy. Dále pokud     je hodnota průtoku neplatná, vypíše toto zjištění do konzole a hodnotu přeskočí.
    
    b) Když je na některém řádku proměnná _cislo_radku_ dělitelná beze zbytku 7, přiřadí tento řádek do proměnné _prvni_den_, jelikož to nutně musí být první ze sedmi dnů, pro         které se průměr počítá.
    
    c) Následně do proměnné _soucet_prutoku_ přiřadí vždy aktuální součet průtoků sečtený s průtokem na aktuálním řádku, průtoky se tedy kumulují.
    
     d) Jakmile program narazí na poslední ze sedmi dnů (_cislo_radku_ je dělitelné 7 se zbytkem 6), vydělí aktuální součet průtoků sedmi a získá tak průměrný průtok za              uplynulých 7 dnů. Proměnné _prvni_den_ přiřadí jako hodnotu průtoku průměrný průtok zaokrouhlený na 4 desetinná místa. Pak už jen daný řádek s datem prvního dne a                průměrným průtokem za 7 dní zapíše do souboru _vystup_7dni.csv_. Pak už je jen potřeba vynulovat součet průtoků, zbytek (ten bude potřeba při dopočítávání poseldní              skupiny dnů) a zvýšit číslo řádku o 1.
    
4) **Zbylé dny** 
     
     a) Nakonec program dopočítá průměr ze zbylých dnů. Když dojede na poslední řádek, vezme součet průtoků a vydělí jej současným zbytkem a výsledek zapíš na konec souboru          _vystup_7dni.csv_. Pokud je číslo posledního řádku násobkem 7, nic se nestane. 
    
5) **Definice vstupního a výstupního souboru pro výpočet ročních průtoků a definice proměnných**

6) **For cyklus pro výpočet ročních průtoků**

    a) Program prochází vstupní soubor po řádcích. Nejdříve program určí rok z prvního řádku jako _soucasny_rok_.
    
    b) Pokud je číslo řádku rovno 0, program přiřadí rok ze _soucasny_rok_ do proměnné _prutok_rok_. Zároveň první řádek přiřadí do proměnné _prvni_den_rok_.
   
    c) Pak program kumuluje průtoky stejně jako u sedmidenních průtoků. Po každém řádku se zvýší zbytek o 1.
    
    d) Když program narazí na nový rok, tak vezme součet průtoků nakumulovaný za celý rok, odečte od něj aktuální průtok (jelikož ten patří až do dalšího roku) a vydělí ho           zbytkem - 1 (protože přebývá jeden den). Proměnné _prvni_den_rok_ přiřadí jako hodnotu průtoku průměrný průtok zaokrouhlený na 4 desetinná místa. Pak už jen daný řádek s         datem prvního dne a průměrným průtokem za 7 dní zapíše do souboru _vystup_rok.csv_. Poté přiřadí do součtu průtoků aktuální průtok, aby nedošlo k nezapočítání průtoku z         prvního dne roku. Zbytek se přepíše na 1, do _prutok_rok_ se přiřadí nový rok, do proměnnné _prvni_den_rok_ se přiřadí první řádek nového roku a nakonec se _cislo_radku_         zvedne o 1.
    
7) **Zbylé dny**

    a) Nakonec je potřeba dopočítat i průměr pro poslední rok, jelikož po něm nenásleduje žádný nový rok. Program vezme současný nakumulovaný součet průtoků a vydělí jej             zbytkem, výsledek opět zapíše do souboru _vystup_rok.csv_.
    
8) **Maximální a minimální průtoky**

    a) Program načte vstupní data.
    
    b) Podle prvního řádku stanoví jeho průtok jako maximální i minimální a uloží daný řádek do proměnné _prutok_max_radek_ resp. _prutok_min_radek_. Poté u každého řádku           porovná jeho průtok s maximem a minimem a pokud dosahuje většího extrému, přiřadí současný řádek do proměnné _prutok_max_radek_ resp. _prutok_min_radek_ a aktualizuje           hodnotu maxima a minima. Pak už jen do konzole vytiskne hlášku o maximálním a minimálním průtoku za celé sledované období.
    
9) **Kontrola chybějících dnů**

    a) Program načte vstupní data.
    
    b) Definuje základní proměnné.
    
    c) Měsíc, který je na prvním řádku vstupního souboru, určí jako současný měsíc a přiřadí ho i do proměnné _mesic_. Jinak pořád jen přeskakuje dny a zvyšuje vždy zbytek o 1.
    
    d) Pokud ale program narazí na řádek, u kterého se měsíc už nerovná proměnné _mesic_, zkusí, jestli byl předešlý měsíc dělitelný počtem dnů (zbytkem), který měl mít. Program     počítá i s přestupnými roky - v takovém případě musí být zbytek v únoru dělitelný 30 místo 29 (zbytek je vždy o 1 vyšší, jelikož došlo k načtení prvního dne z dalšího           měsíce).
    
    c) Pak už jen aktualizuje současný měsíc, změní zbytek na 1 (jako u roku) a nakonec po projetí každého řádku (dne) přičte k proměnné _cislo_radku_mes_.
    
   
    

