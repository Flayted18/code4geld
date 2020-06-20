import glob
filenames = sorted(glob.glob("inflammation*.csv"))
filenames = filenames[0:3]

for file in filenames:
    print(file)
