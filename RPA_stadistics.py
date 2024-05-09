from functions import Mail, fileDate, inform, move, process
from log import manageLog

d = fileDate() # Current date
date = fileDate('date') # FormatDate by functions

# archivo = 'C:/temp/Datos/Información20240506.xlsx' # Fecha actual

archivo = 'C:/temp/Datos/Información'+d+'.xlsx' # Fecha actual

# Init Log
manageLog(text='Start Process...')

# File processing
process(archivo)

# Create diagram
inform()

# Send mail
respMail = Mail()

# Move file if all success
if respMail:
    source = 'C:/temp/Datos/Información'+d+'.xlsx'
    destination = 'C:/temp/Datos/Procesados/Información'+d+'.xlsx' 
    res = move(source,destination)
    
    
    # Move file in log
    if res:
        moved = 'File have been moved from '+source+ ' -> ' + destination
        print('move success')
        manageLog('Process',moved)
    else:
        error = "File haven't been moved to "+destination
        print('Error on move file')
        manageLog('Process',error)