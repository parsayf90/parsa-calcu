from sys import exit

print(str(""" 
██████╗  █████╗ ██████╗ ███████╗ █████╗  
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗ 
██████╔╝███████║██████╔╝███████╗███████║ 
██╔═══╝ ██╔══██║██╔══██╗╚════██║██╔══██║ 
██║     ██║  ██║██║  ██║███████║██║  ██║ 
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ 
                                         
 ██████╗ █████╗ ██╗      ██████╗██╗   ██╗
██╔════╝██╔══██╗██║     ██╔════╝██║   ██║
██║     ███████║██║     ██║     ██║   ██║
██║     ██╔══██║██║     ██║     ██║   ██║
╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ 
    *** Coder: Parsa Yeganeh Faal ***                                  
"""))

print("""
 [1] callculator   
 [2] help
 [3] exit        
""")

# is_running = True

while True:
    try:
        golabi = int(input("kodam ra entekhab mikonid?"))
    except:
        continue

    if golabi == 1:
        print("shoma vared calculator shodid.")

        while True:
            try:
                number_one = float(input("number one:"))
                number_two = float(input("number two:"))
            except:
                print("ahay golabi!?! bayad adad entekhab koni!")
                continue

            # if type(number_one) != float:
            #     print("ahay golabi!?! bayad adad entekhab koni!")
            #     exit()
            
            op = input("enter operator , + , - , * , / , % , **:")

            # op = ["+", "%", "**", "*", "/", "-"]
            # for i in range(0, 5):
            #     pass

            if op == "+":
                print(str(number_one + number_two))
            elif op == "-":
                print(str(number_one - number_two))
            elif op == "/":
                print(str(number_one / number_two))
            elif op == "*":
                print(str(number_one * number_two))
            elif op == "%":
                print(str(number_one % number_two))
            elif op == "**":
                print(str(number_one ** number_two))
            else:
                print("lotfan khar naBASHID!")

    elif golabi == 2:
        print("""
    shoma vared help shodid:
    agar mikhahid az calculator estefade konid adad 1 ra vared konid. 
    agar mikhahid az calculator khareg shavid adad 3 ra vared konid.
    ba tashakor;
                        [parsa yeganeh faal]
            """)
    elif golabi == 3:
        print("shoma az calculator khareg shodid.")
        break

    else:
        continue
    