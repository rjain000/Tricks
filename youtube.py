import webbrowser
url=input("Enter URL of youtube: ")
download=url[:12]+"ss"+url[12:]
webbrowser.open(download)