# legge il log di missione e restituisce due file txt contenenti tutti gli oggetti_distrutti_Sx.txt e gli oggetti_distrutti_Dx.txt

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

    ####################  oggetti_Sx  ########################################
    log = open(missionReport)
    oggettiSx = open("oggetti_Sx.txt", "w")
    for linea_oggetti in log:
        linea_oggetti = linea_oggetti.rstrip()
        #   T:25389 AType:12 ID:182272 TYPE:arf_dugouts_3[25011,1] COUNTRY:201 NAME:< Lin N 5 Rif Dug < PID:-1 POS(188777.2344,142.5266,178376.0156)
        #   if oggettoSx := re.findall('AType:12(.*)< PID', linea_oggetti):
        if oggettoSx := re.findall('AType:12(.*) TYPE:(.*) COUNTRY:(.*) NAME:(.*)< PID', linea_oggetti):

            #print(oggettoSx)
            for lineaSx in oggettoSx:
                oggettiSx.write(lineaSx[0] + ' ' + lineaSx[1] + ' ' + lineaSx[3] + "\n")

    oggettiSx.close()
    log.close()

    ####################  oggetti_Dx  ########################################
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

    ####################  oggetti_distrutti  ########################################
    log = open(missionReport)
    oggetti_distrutti = open("oggetti_distrutti.txt", "w")
    for linea_distrutti in log:
        linea_distrutti = linea_distrutti.rstrip()
        #   T:25378 AType:3 AID:8193 TID:182272 POS(188777.2344,142.5266,178376.0156)
        #   if oggetto_distrutto := re.findall('AType:3(.*)POS', linea_distrutti):
        if oggetto_distrutto := re.findall('AType:3 A(.*) T(.*)POS', linea_distrutti):

            #print(oggetto_distrutto)
            for lineaDis in oggetto_distrutto:
                #if lineaDis == re.escape('AID:-1 TID:(.*)'):
                if lineaDis[0] != 'ID:-1':
                #     print(lineaDis)
                # else:
                    oggetti_distrutti.write(lineaDis[1] + "\n")

    oggetti_distrutti.close()
    log.close()
    #print(lineaOggettiSxLista)

    log = open(missionReport)
    oggetti_distrutti_Sx = open("oggetti_distrutti_Sx.txt", "w")
    oggetti_distrutti_Dx = open("oggetti_distrutti_Dx.txt", "w")
    for linea_log in log:
        if oggetto_distrutto := re.findall('AType:3 A(.*) T(.*)POS', linea_log):
            for lineaDis in oggetto_distrutto:
                if lineaDis[0] != 'ID:-1':
                    print(lineaDis[1])
                    #next(linea_log)

                    for linea_log in log:
                        if oggettoSx := re.findall('AType:12(.*) TYPE:(.*) COUNTRY:(.*) NAME:(.*)< PID', linea_log):
                            for lineaSx in oggettoSx:
                                print(lineaSx[0] + ' ' + lineaSx[1] + ' ' + lineaSx[3])
                                #next(lineaSx)

                                for linea_log in log:
                                    if lineaSx[0] == lineaDis[1]:
                                        oggetti_distrutti_Sx.write(lineaSx[0] + ' ' + lineaSx[1] + ' ' + lineaSx[3] + "\n")
                                        #next(lineaDis)
                                            #elif lineaDis[1] == lineaDx[0]:
                                                #oggetti_distrutti_Dx.write(lineaDx[0] + ' ' + lineaDx[1] + ' ' + lineaDx[3] + "\n")

    oggetti_distrutti_Sx.close()
    oggetti_distrutti_Dx.close()
    log.close()
    print("\nFile oggetti_distrutti.txt, oggetti_Dx.txt e oggetti_Sx.txt creati!")
else:
    print("\nIl file mission inserito non esiste! Programma terminato.")

input("\nPremi un tasto per chiudere...")