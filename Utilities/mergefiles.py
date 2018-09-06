import glob
import os

#os.listdir(path)

def listdir_path(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

dirs = listdir_path("HealthcareDatasets")
print(dirs)

for dir in dirs:
    fullpath = dir+"/*.txt"
    read_files = glob.glob(fullpath)
    outfilename = dir+".txt"
    print(fullpath + ", " + outfilename)

    with open(outfilename, "w") as outfile:
        for f in read_files:
            with open(f, "r") as infile:
                #outfile.write(infile.read())
                for line in infile:
                    if line.strip() == "==== Refs":
                        #print("AHA!")
                        break
                    print(line, end="", file=outfile)
