import csv

candidate = ""
voter_id = ""
vote=""
Correyvote= 0
Khanvote= 0
Livote = 0
OTooleyvote = 0

file_to_open = "election_data.csv"

with open(file_to_open, 'r') as this_csv_file:
    csv_reader = csv.reader(this_csv_file, delimiter=',')      
    

    for line in csv_reader:    
        voter_id = line[0]
        vote = line[2]
        #if voter_id==" * "
            #number_of_votes_cast=number_of_votes_cast+1
        if vote =="Correy":
            Correyvote=Correyvote+1
        if vote =="Khan":
            Khanvote = Khanvote + 1
        if vote =="Li":
            Livote = Livote +1
        if vote =="O'Tooley": 
            OTooleyvote = OTooleyvote + 1

      
  
  
print("Election Results")
print("______________________")
#print("Total Votes:" + str(number_of_votes_cast))
print("______________________")   
print("Correy " + str(Correyvote))
print("Khan " +str(Khanvote))
print("Li " +str(Livote))
print("Otooley " +str(OTooleyvote))
print("______________________") 
if (Correyvote>Khanvote) and (Correyvote>Livote) and (Correyvote>OTooleyvote):
    print("Winner: Correy")
if (Khanvote>Correyvote) and (Khanvote>Livote) and (Khanvote>OTooleyvote):
    print("Winner: Khan")
if (Livote>Correyvote) and (Livote>Khanvote) and (Livote>OTooleyvote):
    print("Winner: Li") 
if (OTooleyvote>Correyvote) and (OTooleyvote>Khanvote) and (OTooleyvote>Livote):
    print("Winner: OTooley")           
