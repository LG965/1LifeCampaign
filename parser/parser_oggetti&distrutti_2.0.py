# legge il log di missione e restituisce tre file txt contenenti tutti gli oggetti.txt e gli oggetti_distrutti.txt
import os.path
import re

print("#################################################################################################################\n")
print("Inserisci il nome del file es: missionReport(2021-04-23_16-52-50)[0].txt\n")
print("ATTENZIONE! Se i tre file oggetti_distrutti.txt, oggetti_Dx.txt e oggetti_Sx.txt esistono, verranno sovrascritti!\n")

missionReport = input()

if os.path.isfile(missionReport):

    #   inserire il nome del report missione (log)
    #   al posto di "missionReport(2021-04-23_16-52-50)[0].txt" qui sotto

    #   missionReport = "missionReport(2021-04-23_16-52-50)[0].txt"

    log = open(missionReport)
    oggettiSx = open("oggetti_Sx.txt", "w")
    for linea_oggetti in log:
        linea_oggetti = linea_oggetti.rstrip()

        if oggettoSx := re.findall('AType:12(.*)< PID', linea_oggetti):

            #print(oggettoSx)
            for lineaSx in oggettoSx:
                oggettiSx.write(lineaSx + "\n")

    oggettiSx.close()
    log.close()

    log = open(missionReport)
    oggettiDx = open("oggetti_Dx.txt", "w")
    for linea_oggetti in log:
        linea_oggetti = linea_oggetti.rstrip()

        if oggettoDx := re.findall('AType:12(.*)> PID', linea_oggetti):

            #print(oggettoDx)
            for lineaDx in oggettoDx:
                oggettiDx.write(lineaDx + "\n")

    oggettiDx.close()
    log.close()

    log = open(missionReport)
    oggetti_distrutti = open("oggetti_distrutti.txt", "w")
    for linea_distrutti in log:
        linea_distrutti = linea_distrutti.rstrip()

        if oggetto_distrutto := re.findall('AType:3(.*)POS', linea_distrutti):

            #print(oggetto_distrutto)
            for lineaDis in oggetto_distrutto:
                oggetti_distrutti.write(lineaDis + "\n")

    oggetti_distrutti.close()
    log.close()
    print("\nFile oggetti_distrutti.txt, oggetti_Dx.txt e oggetti_Sx.txt creati!")
else:
    print("\nIl file mission inserito non esiste! Programma terminato.")

input("\nPremi un tasto per chiudere...")
