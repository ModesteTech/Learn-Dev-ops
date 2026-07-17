import argparse

parser = argparse.ArgumentParser(description="Calculatrice en ligne")
parser.add_argument("nombre1",type=float, help="le premier nombre")
parser.add_argument("nombre2",type=float, help="le deuxieme nombre")
parser.add_argument("--operation",choices=["addition","soustraction","multiplication","division"], default="addition",help="choix de l'operation")
parser.add_argument("--verbose",action="store_true", help="affiche detail du calcul")
args = parser.parse_args()

if args.verbose:
    if args.operation == "addition":
        print(f"Calcul: {args.nombre1} additionne {args.nombre2}")
        print("Resultat :",args.nombre1 + args.nombre2)
    elif args.operation == "sostraction":
        print(f"Calcul: De {args.nombre1} est soustrait {args.nombre2}")
        print("Resultat :",args.nombre1 - args.nombre2)
    elif args.operation == "multiplication":
        print(f"Calcul: {args.nombre1} multiplier par {args.nombre2}")
        print("Resultat :",args.nombre1 * args.nombre2)
    elif args.operation == "division":
        print(f"Calcul: {args.nombre1} diviser {args.nombre2}")
        try:
            print("Resultat :",args.nombre1 / args.nombre2)
        except ZeroDivisionError:
            print("Deuxieme nombre nul : Division impossible")
else:
    if args.operation == "addition":
        print("Resultat :",args.nombre1 + args.nombre2)
    elif args.operation == "sostraction":
        print("Resultat :",args.nombre1 - args.nombre2)
    elif args.operation == "multiplication":
        print("Resultat :",args.nombre1 * args.nombre2)
    elif args.operation == "division":
        try:
            print("Resultat :",args.nombre1 / args.nombre2)
        except ZeroDivisionError:
            print("Deuxieme nombre nul : Division impossible")