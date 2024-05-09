import currentPath

def fileDate(t = ''):
    from datetime import datetime

    # Files date
    if t == 'date':
        # Get datetime
        fecha_actual = datetime.now()

        return fecha_actual.strftime("%Y%m%d%H%M%S")
    # Date log
    elif t == 'log':
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    
    # Date to find file
    else:
        # Get date
        fecha_actual = datetime.now().date()

        return fecha_actual.strftime("%Y%m%d")

date = fileDate('date')

def process(file):
    import pandas as pd
    import pymysql
    import sys
    from log import manageLog

    
    try:
        df = pd.read_excel(file, sheet_name='Hoja1')
    except FileNotFoundError:
        print(f"File or directory {file} not found.")

        # Create log when file wasn't found
        text = f"File or directory {file} not found."
        manageLog('Process', text) # file not found in log

        sys.exit(1)
    else:
        
        # Create log when file was found
        text = f"File or directory {file} found."
        manageLog('Process', text) # file found in log

        connection = pymysql.connect(host='localhost', user='root', passwd='', db='information')

        cur = connection.cursor() # Cursor DB

        # load data
        for row in df.itertuples():
            # Call SP updt
            cur.execute("CALL UpdateData("+str(row.Identificación)+",'"+row.Nombre+"',"+str(row.Cantidad)+")")
            connection.commit() # Keep changes to BD

        # Create log when insert was succesful
        text = 'Insert | Update table.'
        manageLog('Process', text) # Insert | Update in log

        connection.close()

# Checking whether the specified path exists
def validateDIR (currentPath, path):
    import os
    from log import manageLog

    # Specifying path
    valPath = os.path.join(currentPath, path)
    
    isExisting = os.path.isdir(valPath)
    
    # If not exist DIR create
    if isExisting:

        # Mssg log
        text = 'DIR ' +path+ ' exist'
        manageLog('Process', text)

        # Create subdir
        if path == '../Informes':
            validateDIR(currentPath,'../Informes/Procesados')

    else:

        # Mssg log don't exist
        text = 'DIR ' +path+ ' not exist'
        manageLog('Process', text)

        # Create DIR
        os.mkdir(valPath)

        # Mssg log created
        text = 'DIR ' +path+ ' created'
        manageLog('Process', text)
        
        # Create subdir
        if path == '../Informes':
            validateDIR(currentPath,'../Informes/Procesados')

def inform():
    # %%
    import pymysql
    import os
    import sys
    import pandas as pd
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_pdf import PdfPages
    from log import manageLog


    connection = pymysql.connect(host='localhost', user='root', passwd='', db='information')
    list_products = {}
    figs = []

    # %%
    cur = connection.cursor()

    # Call SP Quantity
    cur.execute("CALL QueryQuantity()")
    for NAME, QUANTITY in cur.fetchall():
        list_products[NAME] = {'Quantity': QUANTITY}
    df_inform = pd.DataFrame.from_dict(list_products, orient= 'index')
    connection.close()
    print(list_products)

    # Evaluate dict is not empty
    text = 'Query succesful' if bool(list_products) else 'No Data'
    manageLog('Process', text)

    # %% [markdown]
    # # Bar Diagram

    # %%
    def notEmpty():
        if bool(list_products):
            global diagram
            diagram = df_inform.plot.bar()
            plt.suptitle('Quantity products',fontsize=20)
        else:
            raise Exception('Dict is empty: '+str(list_products))
    try:
        notEmpty()
    except Exception as e:
        print(e)
        manageLog('Process', e) # Log with error no data in BD
        sys.exit(1)

    # %% [markdown]
    # # Pie Diagram

    # %%
    explode = (0, 0, 0, 0, 0, 0.1, 0, 0)

    pie = df_inform.plot.pie(subplots=True, explode=explode, figsize=(10, 10), shadow=True, autopct='%1.1f%%', startangle=90)
    plt.legend(loc="lower left")
    plt.suptitle('Quantity products',fontsize=20)

    # %% [markdown]
    # # Save into pdf
    fig = diagram.get_figure()
    fig2 = pie[0].get_figure()

    figs.append(fig)
    figs.append(fig2)

    fig.set_size_inches(10, 10)

    # c, extFile = currentFile()
    
    # c =currentFile()

    validateDIR(currentPath.c,'../Informes') # Validate DIR exist

    extFile = '../Informes/Inform'+date+'.pdf'
    pathInformFile = os.path.join(currentPath.c, extFile)
    # manageLog('Process', 'Directory search: '+extFile)#  Delete validate DIR

    with PdfPages(pathInformFile) as pdf:
        for x in figs:
            try:
                pdf.savefig(x)
            except FileNotFoundError as e:
                print(e)
                manageLog('Process','Error en save pdf file: '+pathInformFile)
                manageLog('Process', e)
                sys.exit(1)
    
    manageLog('Diagram', extFile) # Create diagram in log

def Mail():
    import sys
    import os
    import resend
    from log import manageLog


    resend.api_key = os.environ["RESEND_API_KEY"]

    try:
        #c, extFile =  currentFile()
        # c =currentFile()
        f = open(
            os.path.join(currentPath.c, "../Informes/inform"+date+".pdf"), "rb"
        ).read()
    except FileNotFoundError:
        print(f"File inform.pdf not found.")
        text = f"File inform.pdf not found."
        manageLog('Process', text) # File not found in log
        sys.exit(1)
    else:

        # Making a mail better

        html = """
        <div>
            <p><strong>Successful Delivery of Daily Information!</strong></p>
            <p>Dear Stakeholder,</p>
            <p>We are pleased to inform you that the daily information report has been successfully processed and is ready for your review. You will find detailed reports and charts attached to this email.</p>
            <p>If you have any questions or need further assistance, please feel free to reach out to us.</p>
            <p>Thank you for your attention.</p>
            <p>Best regards,</p>
            <p>The Data Analysis Team</p>
        </div>
        """
        
        params = {
            "from": "Testing <onboarding@resend.dev>",
            "to": ["riableo.dev@gmail.com"],
            "subject": "Daily inform",
            "html": html,
            "attachments": [{"filename": "inform.pdf", "content": list(f)}],
            
        }

        email = resend.Emails.send(params)

        if email:        
            text = 'Mail have been sended.'
            manageLog('Process', text) # send mail in log
            
            # To construct move files
            source = os.path.join(currentPath.c, "../Informes/inform"+date+".pdf")
            destination = os.path.join(currentPath.c, "../Informes/Procesados/inform"+date+".pdf")
            
            res = move(source, destination)
            
            # Protect path user
            srcPath = "../Informes/inform"+date+".pdf"
            destPath = "../Informes/Procesados/inform"+date+".pdf"

            # Change file path
            moved = 'File have been moved from '+srcPath+ ' -> ' + destPath
            error = "File haven't been moved to "+destPath
            manageLog('Process', moved) if res else manageLog('Process', error) # Move file in log 
            
            return res

def move(source, destination):
    import shutil
    from shutil import copy2

    return bool(shutil.move(source, destination, copy_function = copy2))
