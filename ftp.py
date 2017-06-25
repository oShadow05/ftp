import subprocess
import ftplib
import os
import time
from hide_data import *
# Connessione al server tramite il comando NET USE di Windows controllo se è già stata stabilità una connessione
# CONNECT TO SERVER WITH NET USE WINDOWS COMMAND FOR DEPLOY THE FILES
ftp = ftplib.FTP(IP)
ftp.login(ftp_login_username, ftp_login_password)
try:
    os.chdir("G:\ICT")
except:
    networkPath = network_path_server
    password = password_for_network_path_server
    # Il primo richiamo a NET USE serve per creare una connessione al server
    call_to_server2003_with_CMD = " NET USE " + networkPath + " " + password
    subprocess.Popen(call_to_server2003_with_CMD, stdout=subprocess.PIPE, shell=True)

    # Il secondo richiamo a NET USE crea un'unità virtuale dove andar a scrivere i dati o elaborare dati
    call_to_server2003_with_CMD = " NET USE G: " + networkPath + " " + password
    subprocess.Popen(call_to_server2003_with_CMD, stdout=subprocess.PIPE, shell=True)


# --> FINE DELLA CREAZIONE DELLA COMUNICAZIONE TRA SERVER E DATI  ---- END CUMUNICATE BETWEEN SERVER AND DATA

# Creazione delle cartelle nominate per giorno, mese, anno, ora, minuti, secondi ---- CREATION FOLDER WITH NAME:  DAY, MONTH, YEAR, HOUR, MINUTE, SECOND


day = time.strftime("%d", time.localtime())
month = time.strftime("%m", time.localtime())
year = time.strftime("%y", time.localtime())
ora = time.strftime("%H", time.localtime())
minuti = time.strftime("%M", time.localtime())
secondi = time.strftime("%S", time.localtime())


# Creazione delle cartella a seconda dell'orario ----- CREATION OF FOLDER
path_for_G = initial_path_for_G + day + "-" + month + "-" + year + "-Ora" + ora + "-minuti" + minuti + "-secondi" + secondi + "-backup completo"

os.mkdir(path_for_G)
os.chdir(path_for_G)

ftp.cwd(ftp_initial_store_file)


filenames = ftp.nlst()

# Download File From COMPUTER IP
for filename in filenames:
    local_filename = os.path.join(path_for_G, filename)
    # WRITE A FILE  WITH BYNARY CODE
    file = open(local_filename, 'wb')
    # RETRPBINARY(RETR) GET THE FILES IN BYNARY CODE
    ftp.retrbinary('RETR '+ filename, file.write)

    file.close()

ftp.quit()







