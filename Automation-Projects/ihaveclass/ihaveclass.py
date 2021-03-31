from flask import Flask, redirect
from datetime import datetime

app = Flask(__name__)

# str(datetime.today().weekday())

links = {
    "Digital VLSI": "99421818609",
    "Industrial Automation": "93549251669",
    "Analog VLSI": "99421818609",
    "Pattern Recognition": "97454820666?pwd=RWZDV0N4L0dGMGI2cWpwYmlOcUx3Zz09",
    "Databases": "96793780637",
    "Economics": "96567876705?pwd=MkRDL0pvaUx6aFB1clhGUkhnZ2szZz09",
    "Hardware-Software Codesign":"98169060279"
}


class lecture:

    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end


schedule = [

    [lecture("Digital VLSI", 11, 2), lecture("Industrial Applications", 18, 20)],
    [lecture("Analog VLSI", 11, 13), lecture("Economics", 14, 16), lecture("Pattern Recognition", 16, 18), lecture("Databases", 18, 20)],
    [lecture("Hardware-Software Codesign", 15, 17)],
    [lecture("Economics", 15, 17), lecture("Pattern Recognition", 17, 19)],
    [lecture("Databases", 11, 13)]
]


@app.route('/')

def getmetoclass():
    day = datetime.today().weekday()
    hour = datetime.today().hour

    classes_today = schedule[day]
    class_now = ""
    for c in classes_today:
        if (hour >= c.start) and (hour <= c.end):
            class_now = c.name
            print(class_now)

    if class_now != "":
        return redirect("https://authgr.zoom.us/j/{link}".format(link=links[class_now]), 302)

    else:
        return "No class now :)"




if __name__ == '__main__':
    app.run()
