
pal1 = input("coloque una palabra: ")
pal2 = input("coloque otra palabra: ")

if len(pal1) < 3 or len(pal2) < 3:
    print("las palabras no riman, porque no pueden")
elif pal1[-3:] == pal2[-3:]:
    print("las palabras riman")
elif pal1[-2:] == pal2[-2:]:
    print("las palabras riman un poco")
else:
    print("las palabras no riman")
