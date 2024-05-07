def fileDate():
    from datetime import datetime

    # Get date
    fecha_actual = datetime.now().date()

    return fecha_actual.strftime("%Y%m%d")

def process(file):
    import pandas as pd
    import pymysql

    connection = pymysql.connect(host='localhost', user='root', passwd='', db='information')

    cur = connection.cursor() # cursor db

    df = pd.read_excel(file, sheet_name='Hoja1')

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

    connection = pymysql.connect(host='localhost', user='root', passwd='', db='information')
    list_products = {}

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

    # %%
    fig = diagram.get_figure()
    fig.set_size_inches(10, 10)
    diagram.get_figure().savefig('../Informes/Inform.pdf')

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
