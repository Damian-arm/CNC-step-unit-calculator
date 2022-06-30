
import math

print("CNC calculator\n\n")

print("stepper motor with 1,8 degree/step have 200 steps/revolution , motor with 0,9 degree/step have 400 steps/revolution\n")
print("for extruder direct drive type gear big 1 gear small 1, this will set gear ratio to 1\n\n")

string = input("units: mm/in : ")
unit = str(string)
result = 0

string = input("calculate : belt/screw/extruder : ")
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
	string = input("create configuration file cncofig.txt? 	y/n : ")
	yn = str(string)

	if yn=="y":
		with open('cnconfig.txt', 'x') as f:
			f.write("\nbelt cnc calculation :" + "\n" + "-motor steps per revolution : " + str(rslt1) + "\n" + "-microsteps : " + str(rslt2) + "\n" + "-belt pitch : " + str(rslt3) + "\n" + "-pully number of teeth : " + str(rslt4) + "\n" + str(result) + " steps/" + str(unit) + "\n\n" )


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

	string = input("create configuration file cncofig.txt? 	y/n : ")
	yn = str(string)

	if yn=="y":
		with open('cnconfig.txt', 'x') as f:
			f.write("screw cnc calculation :" + "\n" + "-motor steps per revolution : " + str(rslt1) + "\n" + "-microsteps : " + str(rslt2) + "\n" + "-screw pitch : " + str(rslt4) + "\n" + str(result) + " steps/" + str(unit) + "\n\n" )



if type=="extruder":
	integer = input("motor steps per revolution : ")
	rslt1 = int(integer)
	integer = input("microsteps : ")
	rslt2 = int(integer)
	integer = input("gear big wheel : ")
	rslt3 = int(integer)
	integer = input("gear small wheel : ")
	rslt4 = int(integer)
	rsltratio=rslt3/rslt4
	print("gear ratio : " + str(rslt3) + "/" + str(rslt4) + 	"=" + str(rsltratio))
	integer = input("pinch wheel diameter : ")
	rslt5 = int(integer)
	result=round((rslt1*rslt2*rsltratio)/(math.pi*rslt5))
	print(result)
	if unit=="mm":
		print("steps/mm")
	if unit=="in":
		print("steps/in")

	string = input("create configuration file cncofig.txt? 	y/n : ")
	yn = str(string)

	if yn=="y":
		with open('cnconfig.txt', 'x') as f:
			f.write("\nextruder cnc calculation :" + "\n" + "-motor steps per revolution : " + str(rslt1) + "\n" + "-microsteps : " + str(rslt2) + "\n" + "-gear big wheel : " + str(rslt3) + "\n" + "-gear small wheel : " + str(rslt4) + "\n" + "-gear ratio : " + str(rslt3)+ "/" + str(rslt4) + " = " + str(rsltratio) + "\n" + str(result) + " steps/" + str(unit) + "\n\n" )


#pasek (ilosc krokow*mikrokrok)/(skok paska*ilosc zebow na zebatce)
#suba (ilosc krokow*mikrokrok)/(skok suby)
#extruder (ilosc krokow*mikrokrok*przezenie na zebatkach)/(pi * sednica radelka w miejscu styku)
