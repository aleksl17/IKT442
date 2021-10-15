from os import path, write


file = open("dataset/faret_no_NaN").readlines()
patch = open("dataset/faret_1_no_Nan","w")
for f in file:
    patch.write(f.replace(" ","T"))