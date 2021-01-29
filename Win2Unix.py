#for python 3.7
#By judi_Co & Ecstasyyy

import platform
import os


# Variables
version = "░░V 0.1░░░"
sysos = platform.system()

# Help is Doc of Win2Unix.help(arg)
def help(arg = ""):

	arg = arg.lower()
	
	cl = ["clean","cls","clear"] # Liste des nom a entré en tant qu'argument pour le cls
	co = ["color","colors","coleur","coleurs","colour"] # Liste des nom a entré en tant qu'argument pour le color

	if arg in cl:
		print("Cleaning your screen")
	
	elif arg in co:
		print("======= { Windows Colors } =======")
		print("0 = Noir        8 = Gris")
		print("1 = Bleu        9 = Bleu-clair")
		print("2 = Vert        A = Vert-clair")
		print("3 = Bleu-gris   B = Cyan")
		print("4 = Rouge       C = Rouge-clair")
		print("5 = Violet      D = Violet-clair")
		print("6 = Jaune       E = Jaune-clair")
		print("7 = Blanc       F = Blanc-brillant")

		print("======= { linux Colors } =======")
		print("  ? = Noir        008 = Gris")
		print("004 = Bleu          ? = Bleu-clair")
		print("002 = Vert          ? = Vert-clair")
		print("  ? = Bleu-gris   006 = Cyan")
		print("001 = Rouge         ? = Rouge-clair")
		print("005 = Violet        ? = Violet-clair")
		print("003 = Jaune         ? = Jaune-clair")
		print("007 = Blanc         ? = Blanc-brillant")
	else:
		print("")
		print("   ╔═════════════════════════════════╗ ")
		print(f"  ╠╬╗░░Tools░[Win2Unix]░{version}░░╔╬╣ ")
		print("  ╔╬╣░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░╠╬╗ ")
		print("  ╠╬╣░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░╠╬╣ ")
		print("  ╚╬╣░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░╠╬╝ ")
		print("  ╠╬╝░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░╚╬╣ ")
		print("   ╚═════════════════════════════════╝ ")
		print("")

		print(f"la commande '{arg}' n'éxiste pas")
		print(f"vous pover utilisuer les argument : ")
		print(f"Win2Unix.help({cl})")
		print(f"Win2Unix.help({co})")

# Cleaning => Win2Unix.Clean()
def Clean(sysos = sysos):
    if sysos == "Windows":
        os.system("cls")
    else:
        os.system("clear")

#Color => Win2Unix.Colors(color= <arg>) /!\ (color = <arg>) obligatoir /!\
def Colors(color = "", sysos = sysos):
	color = str(color).lower()
	#print(f"colore : {color}")

	color0  = ["noir","black","0"]
	color1  = ["bleu","blue","1","004"]
	color2  = ["vert","green","2","002"]
	color3  = ["bleu-gris","blue-grey","3"]
	color4  = ["rouge","red","4","001"]
	color5  = ["violet","purple","5","005"]
	color6  = ["jaune","yellow","6","003"]
	color7  = ["blanc","white","7","007"]
	color8  = ["gris","grey","8","008"]
	color9  = ["bleu-clair","light-blue","9"]
	color10 = ["vert-clair","light-green","a","10"]
	color11 = ["cyan","b","11","006"]
	color12 = ["Rouge-clair","light-red","c","12"]
	color13 = ["violet-clair","light-purple","d","13"]
	color14 = ["jaune-clair","light-yellow","e","14"]
	color15 = ["blanc-brillant","brilliant-white","f","15"]

	allcolor = color0 + color1 + color2 + color3 + color4 + color5 + color6 + color7 + color8 + color9 + color10 + color11 + color12 + color13 + color14 + color15
	
	if color != allcolor:
		print("tu na pas indiqur de couleur")

	if sysos == "Windows":
		if color in color0:
			os.system("color 0")
		elif color in color1:
			os.system("color 1")
		elif color in color2:
			os.system("color 2")
		elif color in color3:
			os.system("color 3")
		elif color in color4:
			os.system("color 4")
		elif color in color5:
			os.system("color 5")
		elif color in color6:
			os.system("color 6")
		elif color in color7:
			os.system("color 7")
		elif color in color8:
			os.system("color 8")
		elif color in color9:
			os.system("color 9")
		elif color in color10:
			os.system("color A")
		elif color in color11:
			os.system("color B")
		elif color in color12:
			os.system("color C")
		elif color in color13:
			os.system("color D")
		elif color in color14:
			os.system("color E")
		elif color in color15:
			os.system("color F")

	elif sysos != "Windows":
		if color in color0:
			os.system("tput setaf {}")
		elif color in color1:
			os.system("tput setaf 004")
		elif color in color2:
			os.system("tput setaf 002")
		elif color in color3:
			os.system("tput setaf {}")
		elif color in color4:
			os.system("tput setaf 001")
		elif color in color5:
			os.system("tput setaf 005")
		elif color in color6:
			os.system("tput setaf 003")
		elif color in color7:
			os.system("tput setaf 007")
		elif color in color8:
			os.system("tput setaf 008")
		elif color in color9:
			os.system("tput setaf {}")
		elif color in color10:
			os.system("tput setaf {}")
		elif color in color11:
			os.system("tput setaf 006")
		elif color in color12:
			os.system("tput setaf {}")
		elif color in color13:
			os.system("tput setaf {}")
		elif color in color14:
			os.system("tput setaf {}")
		elif color in color15:
			os.system("tput setaf {}")


