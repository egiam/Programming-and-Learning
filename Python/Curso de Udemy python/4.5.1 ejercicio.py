
capitales = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

letra = input("Diga un pais y le diremos su capital: ")
capital = letra.capitalize()

if capital in capitales:
    print(capitales[capital])
else:
    print("el pais no se encuentra en el diccionario")
