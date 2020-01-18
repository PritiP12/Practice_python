class Calculator:
    def Add(self, num1, num2):
        result=num1+num2
        print("Addition is:",result)
    def Sub(self,num1, num2):
        result=num1-num2
        print("Substraction is:",result)
    def Mul(self,num1,num2):
        result=num1*num2
        print("Multiplicaton is:",result)
    def Div(self,num1,num2):
        result=num1/num2
        print("Division is:",result)

C=Calculator()

try:
    print("Enter Your Choice:")
    dict1={1: C.Add, 2: C.Sub, 3: C.Mul, 4: C.Div}
    get_input=int(input("1:Additon\n2:Substraction\n3:Multiplocation\n4:Division"))
    dict1.get(get_input)
    num1=int(input("Enter First Number:"))
    num2=int(input("Enter Second Number:"))

    if get_input == 1:
        C.Add (num1,num2)
    elif get_input == 2:
        C.Sub (num1,num2)
    elif get_input == 3:
        C.Mul (num1,num2)
    elif get_input == 4:
        C.Div (num1,num2)
    elif get_input <= 5:
        print ("Its not avaliable try again")
              #exit ()
except ValueError:
    print("Wrong input")
    exit()