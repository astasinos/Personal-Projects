# Small script to extract Energy Delay Area Product from text files produced my gem5 + mcpat.


import glob
textfiles =  glob.glob("C:\Users\dawnm\Desktop\\txtres\*.txt")
statsfiles = glob.glob("C:\Users\dawnm\Desktop\def\\bzips\*\stats.txt")

def getArea(file):


    with open(file,'r') as txt:
        lines = [line.strip() for line in txt]
        areas = [i for i, x in enumerate(lines) if "Area" in x and x]
        peakpower = [i for i, x in enumerate(lines) if "Peak Power" in x and x]
        if len(areas):
             corearea = float(lines[areas[1]].split("=")[1].split()[0])
             l2area = float(lines[areas[2]].split("=")[1].split()[0])
             peakpower = lines[peakpower[0]]

             print file + "\tCore = " +  str(corearea)  + "\tL2 = " + str(l2area) +"\t " + peakpower
             totalarea = corearea + l2area
             return totalarea

def getDelay(file):
    with open(file,'r') as txt:
        lines = [line.strip() for line in txt]
        for line in lines:
            parts = line.split()
            if len(parts) > 1:
                if parts[0] == "sim_seconds":
                    print file + "\tsim_seconds = " + parts[1]


for file in textfiles:
    area = getArea(file)

for file in statsfiles:
    getDelay(file)
