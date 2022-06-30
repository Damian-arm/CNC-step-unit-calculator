
print("CNC calculator\n\n")

print("stepper motor with 1,8 degree/step have 200 steps/revolution , motor with 0,9 degree/step have 400 steps/revolution\n\n")

string = input("units: mm/in : ")
unit = str(string)
result = 0

string = input("calculate : belt/screw : ")
type = str(string)

if type=="belt":
	integer = input("motor steps per revolution : ")
	rslt1 = int(integer)
	integer = input("microsteps : ")
	rslt2 = int(integer)
	integer = input("belt pitch : ")
	rslt3 = int(integer)
	integer = input("pully number of teeth : ")
	rslt4 = int(integer)
	result=(rslt1*rslt2)/(rslt3*rslt4)
	print(result)
	if unit=="mm":
		print("steps/mm")
	if unit=="in":
		print("steps/in")

if type=="screw":
	integer = input("motor steps per revolution : ")
	rslt1 = int(integer)
	integer = input("microsteps : ")
	rslt2 = int(integer)
	integer = input("screw pitch : ")
	rslt4 = int(integer)
	result=(rslt1*rslt2)/(rslt4)
	print(result)
	if unit=="mm":
		print("steps/mm")
	if unit=="in":
		print("steps/in")



#pasek (ilosc krokow*mikrokrok)/(skok paska*ilosc zebow na zebatce)
#suba (ilosc krokow*mikrokrok)/(skok suby)
#extruder (ilosc krokow*mikrokrok*przezenie na zebatkach)/(pi * sednica radelka w miejscu styku)
