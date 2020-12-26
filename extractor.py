from zipfile import ZipFile

file_name="chromedriver_win32.zip"

with ZipFile(file_name,'r') as zip:
    zip.printdir()

    print("extracting all the files now...")
    zip.extractall()
    print("done!!")