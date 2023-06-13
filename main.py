dict = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0} # first digit dictionary frequency distribution
c=0
with open("census_2009.txt","r") as f:
    for lines in f:
        line = lines.split() # function removes whitespaces from the begining and the end of the string
        #print(line)
        pn = str(line[-1]) # the population number is the last element of the line
        dict[pn[0]] += 1 # getting the first digit
        c += 1

for i in sorted (dict.keys()):
    rel = dict[i]*100/c # function calculates the relative frequencies
    print(i+"\t"+str(dict[i])+"\t"+str(rel))