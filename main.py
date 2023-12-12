import turtle
import pandas as pd

screen = turtle.Screen()
image = "Bundesländer.gif"
screen.addshape(image)
turtle.shape(image)


data = {
    "Bundesländer": [
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
    "X-Koordinate": [-96, 30, 113, 123, -57, 23, -72, 55, -94, -153, -159, -171, 95, 31, 37, 3],
    "Y-Koordinate": [-175, -153, 84, 53, 123, 154, -31, 161, 103, 28, -80, -108, -23, 42, 190, -24]
}

new_data = pd.DataFrame(data)
new_data.to_csv("Bundeslaender_Koordinaten.csv")
