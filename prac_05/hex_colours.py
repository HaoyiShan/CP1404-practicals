
colours = {"absolute aero": "#0048ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff", "alizarin crimson": "#e32636",
           "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "	#9966cc", "antiqueWhite": "#faebd7",
           "apricot": "#fbceb1", "aqua": "#00ffff"}
print(colours)

input_colour = input("please enter the name of the colour:").lower()
while input_colour != "":
    if input_colour in colours:
        print("The code of the colour is", colours[input_colour])
    else:
        print("Invalid colour")
    input_colour = input("please enter the name of the colour:").lower()



