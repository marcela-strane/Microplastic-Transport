CNlist=[73,75,77,78,79,80,81,82,84,86,87,88,89,90,91,92,93,94,95,97,98];
def RS(array):
    #Creates an empty list
    rs= []
    for CN in array:
        #Stores our computed value to compute
        compute = (1000/CN) - 10 #S, retention max storage
        #Adds value to our return array
        rs.append(compute)
        #prints the comuted value for every entry in the array
        print(compute)
    #returns our list
    return rs #retention max (storage) inches based on CN
#Calls RS with CNlist as our parameter, the function returns an array which we save it by
#storing the output to a new variable
answerArray = RS(CNlist)
print(f"answer array={answerArray}")

#Initial Abstraction
c=0.2 #coefficient of I=.2S
iA = [i * c for i in answerArray]
print(f'{iA=}')

print("-------------------------------------------------------------------------------------------------)")
#Rainfall Intensity
from tabulate import tabulate;
#assign data
mydata = [
    ["2-year", "48.35", "9.07", "0.7244"],
    ["5-year", "52.32", "7.88", "0.69"],
    ["10-year", "54.68", "6.96", "0.6623"],
    ["25-year", "57.79", "5.89", "0.6294"],
    ["50-year", "61", "5.46", "0.6096"],
    ["100-year", "60.66", "4.44", "0.5797"],
    ["500-year", "62.17", "2.95", "0.5196"]
]
#create header
head= ["Rainfall Intensity", "b", "d", "e"]
#display table
print(tabulate(mydata,headers=head, tablefmt="grid"))

#Calculate rainfall intensity for each frequency using the  IDF curves and Houston IDF Equations
print("----------------------------------------------------------------")
TC=1140 #time of concentration in minutes

b1=48.35; b2=52.32; b3=54.68; b4=57.79; b5=61; b6=60.66; b7=62.15;
d1=9.07; d2=7.88; d3=6.96; d4=5.89; d5=5.46; d6=4.44; d7=2.95;
e1=0.7244; e2=0.69; e3=0.6623; e4=0.6294; e5=0.6096; e6=0.5797; e7=0.5196;
twoyi=b1/(d1+TC)**e1
fiveyi=b2/(d2+TC)**e2
tenyi=b3/(d3+TC)**e3
twentyfiveyi=b4/(d4+TC)**e4
fiftyyi=b5/(d5+TC)**e5
hundredyi=b6/(d6+TC)**e6
fivehundredyi=b7/(d7+TC)**e7

print("Rainfall Intensity Events:P2 or P") #now print the variables and outputs side by side
hr=24 #hours of a rainfall event
#assign the new values as a variables in the dictionary created
RIE=dict()
twoyihr= RIE['twoyihr=']= twoyi*hr
fiveyihr=RIE['fiveyihr=']= fiveyi*hr
tenyihr=RIE['tenyihr=']= tenyi*hr
twentyfiveyihr=RIE['twentyfiveyihr=']= twentyfiveyi*hr
fiftyyihr=RIE['fiftyyihr=']= fiftyyi*hr
hundredyihr=RIE['hundredyihr=']= hundredyi*hr
fivehundredyihr=RIE['fivehundredyihr=']= fivehundredyi*hr

for i in RIE:
    print("%s %f" % (i, RIE[i]))
print("                          inches")
print("--------------------------------------------------------------------------------")

#Flow Rate of the Precipitation P to Q



