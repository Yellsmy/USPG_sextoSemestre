import os, time
banner = ["█","10%", "██", "20%", "███","30%","████","40%","█████","50%","██████", "60%","███████",\
"70%","████████","80%","█████████","90%","█████████","100%"]
banner2= ["10%", "20%","30%","40%","50%","60%",\
"70%","80%","90%","█████████","100%"]
 
L = len(banner)
n = 1
for j in range(0,n):
   for i in range(0,L):
       os.system("cls")
       print(banner[i])
       time.sleep(1)