from datetime import datetime 
time = datetime.now()
whithoutmilsec = time.strftime("%d-%m-%Y %H:%M:%S")
print(whithoutmilsec)