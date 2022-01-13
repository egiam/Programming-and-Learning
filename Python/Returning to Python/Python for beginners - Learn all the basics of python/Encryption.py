
def Crypted(sentence):
    encryption = ""
    for el in sentence:
        if el in "Aa":
            encryption = encryption + "1"
        elif el in "Bb":
            encryption = encryption + "2"
        elif el in "Cc":
            encryption = encryption + "3"
        elif el in "Dd":
            encryption = encryption + "4"
        elif el in "Ee":
            encryption = encryption + "5"
        elif el in "Ff":
            encryption = encryption + "6"
        elif el in "Gg":
            encryption = encryption + "7"
        elif el in "Hh":
            encryption = encryption + "8"
        elif el in "Ii":
            encryption = encryption + "9"
        elif el in "Jj":
            encryption = encryption + "!"
        elif el in "Kk":
            encryption = encryption + "@"
        elif el in "Ll":
            encryption = encryption + "#"
        elif el in "Mm":
            encryption = encryption + "$"
        elif el in "Nn":
            encryption = encryption + "%"
        elif el in "Oo":
            encryption = encryption + "^"
        elif el in "Pp":
            encryption = encryption + "&"
        elif el in "Qq":
            encryption = encryption + "*"
        elif el in "Rr":
            encryption = encryption + "("
        elif el in "Ss":
            encryption = encryption + ")"
        elif el in "Tt":
            encryption = encryption + "-"
        elif el in "Uu":
            encryption = encryption + "_"
        elif el in "Vv":
            encryption = encryption + "+"
        elif el in "Ww":
            encryption = encryption + "="
        elif el in "Xx":
            encryption = encryption + "~"
        elif el in "Yy":
            encryption = encryption + "}"
        elif el in "Zz":
            encryption = encryption + "{"
        else:
            encryption = encryption + el
    
    return encryption

print(Crypted(input("Write what do you want to crypt: ")))


