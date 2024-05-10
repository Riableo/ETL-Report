# ETL Report

Script that find a Excel file with specific caracteristics, load data to MySQL DB and create an inform that after is sended via mail using [Resend](https://resend.com "Tool for send mails").

## Diagrams

![Bar chart first version](/assets/images/grafica.png "Bar chart of Quantity")
![Better than diagram of the first veersion](/assets/images/pie.png "Pie chart of Quantity")

## Mail

image of mail

## Tools & Libs

- [**Pymysql**](https://pypi.org/project/pymysql/ "Doc library"): For the connection with MySQL
- [**Pandas**](urlPandas): 
- [**Matplotlib**](urlMatplot):
- [**Resend**](urlResend):
- [**Shutil**](urlShutil):

## Resources

- [Log Control](https://programminghistorian.org/es/lecciones/trabajar-con-archivos-de-texto "Work with plain text"): It's helps me with sintax about work with plain text files.

- [Exceptions](https://docs.python.org/3/tutorial/errors.html "Doc about errors & exceptions"): This helps me with create and understanding the functionality of exceptions.

- [Validate DIR exist](https://www.simplilearn.com/tutorials/python-tutorial/python-check-if-file-exists "Tutorial about validate existence of file") another [DIR exist](https://www.python-engineer.com/posts/check-if-file-exists/ "Post about check if DIR exist"): With these two resources I've validated the existence of the DIR.

- [Concatenate path](https://www.geeksforgeeks.org/python-os-path-join-method/ "Use os to concatenate path"): Union of string chains to pass a path complete.

- [Create DIR if not exist](https://www.geeksforgeeks.org/create-a-directory-in-python/ "How create a DIR"): I've used for create the DIR in case this doesn't exist with ```os.mkdir``` .

- [Create function with multi returns](https://drbeane.github.io/python/pages/functions/returning_multiple.html#:~:text=It%20is%20possible%20for%20a,return%20statement%2C%20separated%20by%20commas. "Multi returns function"): I've used this to test the origin path. In the final version I've deleted those returns because aren't neccesary.

- [PyInstaller cannot add .txt files](https://stackoverflow.com/questions/39885354/pyinstaller-cannot-add-txt-files "Forum about fix create a plain text file"): This error was happening by the way the path was being passed.

- [Global variables](https://stackoverflow.com/questions/3400525/global-variable-from-a-different-file-python "Forum about global vars"): It helps me to implment DRY calling to function currentFile more one time.

  >This implementation generated me multiples errors with the imports, in my opinion, you must be careful with the imports, it could convert easily in [circular import](<https://rollbar.com/blog/how-to-fix-circular-import-in-python/#:~:text=The%20phrase%20(most%20likely%20due,neither%20import%20can%20complete%20first.> "How fix circular import") error.

## To improve Project

- [**Plot material**](https://plotly.com/python/legend/ "Tool with interactivity"): An interesting tool for drawing charts with interactivity.