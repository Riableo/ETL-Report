from functions import Mail, fileDate, inform, move, process

d = fileDate() # Current date

# archivo = 'C:/temp/Datos/Información20240506.xlsx' # Fecha actual

archivo = 'C:/temp/Datos/Información'+d+'.xlsx' # Fecha actual

# File processing
process(archivo)

# Create diagram
inform()

# Send mail
path = Mail()

# Move file if all success
if path:
    res = move('C:/temp/Datos/Información'+d+'.xlsx','C:/temp/Datos/Procesados/Información'+d+'.xlsx')
    
    # Move file in log
    if res:
        print('move success')