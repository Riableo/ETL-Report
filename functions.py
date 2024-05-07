def fileDate(t = True):
    from datetime import datetime

    if t:
        # Get datetime
        fecha_actual = datetime.now()

        return fecha_actual
    else:
        # Get date
        fecha_actual = datetime.now().date()

        return fecha_actual.strftime("%Y%m%d")


def process(file):
    import pandas as pd
    import pymysql
    import sys
    
    try:
        df = pd.read_excel(file, sheet_name='Hoja1')
    except FileNotFoundError:
        print(f"File or directory {file} not found.")
        sys.exit(1)
    else:
        connection = pymysql.connect(host='localhost', user='root', passwd='', db='information')

        cur = connection.cursor() # cursor db

        # load data
        for row in df.itertuples():
            # Call SP updt
            cur.execute("CALL UpdateData("+str(row.Identificación)+",'"+row.Nombre+"',"+str(row.Cantidad)+")")
            connection.commit() # Keep changes to BD
        connection.close()

def inform():
    # %%
    import pymysql
    import pandas as pd
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_pdf import PdfPages

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

    # %% [markdown]
    # # Bar Diagram

    # %%
    diagram = df_inform.plot.bar()
    plt.suptitle('Quantity products',fontsize=20)

    # %% [markdown]
    # # Pie Diagram

    # %%
    explode = (0, 0, 0, 0, 0, 0.1, 0, 0)

    pie = df_inform.plot.pie(subplots='true', explode=explode, figsize=(10, 10), shadow=True, autopct='%1.1f%%', startangle=90)
    plt.legend(loc="lower left")
    plt.suptitle('Quantity products',fontsize=20)

    # %% [markdown]
    # # Save into pdf
    fig = diagram.get_figure()
    fig2 = pie[0].get_figure()

    figs.append(fig)
    figs.append(fig2)

    fig.set_size_inches(10, 10)

    d = fileDate()
    extFile = 'Inform'+d+'.pdf'

    with PdfPages(extFile) as pdf:
        for x in figs:
            pdf.savefig(x)

def Mail():
    import sys
    import os
    import resend

    resend.api_key = os.environ["RESEND_API_KEY"]

    try:
        f = open(
            os.path.join(os.path.dirname(__file__), "../Informes/inform.pdf"), "rb"
        ).read()
    except FileNotFoundError:
        print(f"File inform.pdf not found.")
        sys.exit(1)
    else:
        params = {
            "from": "Testing <onboarding@resend.dev>",
            "to": ["riableo.dev@gmail.com"],
            "subject": "Daily inform",
            "html": "<strong>it works!</strong>",
            "attachments": [{"filename": "inform.pdf", "content": list(f)}],
            
        }

        email = resend.Emails.send(params)

        if email:        
            source = os.path.join(os.path.dirname(__file__), "../Informes/inform.pdf")
            destination = os.path.join(os.path.dirname(__file__), "../Informes/Procesados/inform.pdf")
            res = move(source, destination)
            return res

def move(source, destination):
    import shutil
    from shutil import copy2

    return bool(shutil.move(source, destination, copy_function = copy2))
