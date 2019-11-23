import csv
candidate = ""
voter_id = ""
vote = ""
Correy = 0
Khan = 0
Li = 0
OTooley = 0

with open('election_data.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
for line in csv_reader:
    
    data = [l for l in csv_reader]
    voter_id = line[0]
    vote = line[2]
    if vote =="Correy":
        Correyresult = Correy + 1
    if vote =="Khan":
        Khanresult = Khan + 1
    if vote =="Li":
        Liresult = Li +1
    if vote =="OTooley": 
        OTooleyresult = OTooley + 1


    number_of_votes_cast = len(data)

print("Election Results")
print("__________________")
print("Total Votes:" + str(number_of_votes_cast))
print("__________________")   
print(Correyresult)
print(Khanresult)
print(Liresult)
print(OTooleyresult)
