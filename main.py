import turtle

import pandas
import pandas as pd

screen = turtle.Screen()
image = "Bundesländer.gif"
screen.addshape(image)
turtle.shape(image)


data = {
    "Bundeslaender": [
        "Baden-Württemberg",
        "Bayern",
        "Berlin",
        "Brandenburg",
        "Bremen",
        "Hamburg",
        "Hessen",
        "Mecklenburg-Vorpommern",
        "Niedersachsen",
        "Nordrhein-Westfalen",
        "Rheinland-Pfalz",
        "Saarland",
        "Sachsen",
        "Sachsen-Anhalt",
        "Schleswig-Holstein",
        "Thüringen"],
    "X_Koordinate": [-96, 30, 113, 123, -57, 23, -72, 55, -94, -153, -159, -171, 95, 31, 37, 3],
    "Y_Koordinate": [-175, -153, 84, 53, 123, 154, -31, 161, 103, 28, -80, -108, -23, 42, 190, -24]
}

new_data = pd.DataFrame(data)
new_data.to_csv("Bundeslaender_Koordinaten.csv")

laender = new_data.Bundeslaender.to_list()

erratene_laender = []

while len(erratene_laender) < 16:
    geratenes_land = screen.textinput(title=f"{len(erratene_laender)}/16 richtig", prompt="Nenne ein weiteres Bundesland").title()

    if geratenes_land == "Verlassen":
        fehlende_bundeslaender = []
        for land in laender:
            if land not in erratene_laender:
                fehlende_bundeslaender.append(land)
        daten = pandas.DataFrame(fehlende_bundeslaender)
        daten.to_csv("bundeslaender_zum_lernen")
        break


    if geratenes_land in laender:
        erratene_laender.append(geratenes_land)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        bundesland_daten = new_data[new_data.Bundeslaender == geratenes_land]
        t.goto(int(bundesland_daten.X_Koordinate.iloc[0]), int(bundesland_daten.Y_Koordinate.iloc[0]))
        t.pendown()
        t.write(geratenes_land)


