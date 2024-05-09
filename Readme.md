# ETL Report

Script that find a Excel file with specific caracteristics, load data to MySQL DB and create an inform that after is sended via mail using [Resend](https://resend.com).

## Tools

- [**Plot material:**](https://plotly.com/python/legend/) An interesting tool for drawing charts with interactivity. 
- **Matplotlib:**
- **Resend:**

## Resources

- [Log Control](https://programminghistorian.org/es/lecciones/trabajar-con-archivos-de-texto)
- [Exceptions](https://docs.python.org/3/tutorial/errors.html) this help me with create and understanding the functionality of exceptions.
- [Validate DIR exist](https://www.simplilearn.com/tutorials/python-tutorial/python-check-if-file-exists) another [DIR exist](https://www.python-engineer.com/posts/check-if-file-exists/)
- [Concatenate path](https://www.geeksforgeeks.org/python-os-path-join-method/)
- [Create DIR if not exist](https://www.geeksforgeeks.org/create-a-directory-in-python/) with ```os.mkdir```
- [Create function with multi returns](https://drbeane.github.io/python/pages/functions/returning_multiple.html#:~:text=It%20is%20possible%20for%20a,return%20statement%2C%20separated%20by%20commas.)
- [PyInstaller cannot add .txt files](https://stackoverflow.com/questions/39885354/pyinstaller-cannot-add-txt-files): This error was happening by the way the path was being passed.
- [Global variables](https://stackoverflow.com/questions/3400525/global-variable-from-a-different-file-python): It helps me to implment DRY calling to function currentFile more one time.
  - This implementation generated me multiples errors with imports, in my opinion, you must be careful with imports, it could be easily in [circular import](<https://rollbar.com/blog/how-to-fix-circular-import-in-python/#:~:text=The%20phrase%20(most%20likely%20due,neither%20import%20can%20complete%20first.>) error.