
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



#pasek (ilo�� krok�w*mikrokrok)/(skok paska*ilo�� z�b�w na z�batce)
#�ruba (ilo�� krok�w*mikrokrok)/(skok �ruby)
#extruder (ilo�� krok�w*mikrokrok*prze�o�enie na z�batkach)/(pi * �rednica rade�ka w miejscu styku)
