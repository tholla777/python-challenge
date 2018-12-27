## PyPoll
import os
import csv
from collections import Counter
csvpath = os.path.join ('Resources', 'election_data.csv')



# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    Voter_ID = []
    County = []
    Candidate = []
    #Candidate = ["Khan", "Correy", "Li", "O'Tooley"]
    Candidate_Count = 0
    # Candidate_1 = []#"Khan"
    # Candidate_2 = "Correy"
    # Candidate_3 = "Li"
    # Candidate_4 = "O'Tooley"

    for row in csvreader:

        #if Candidate = "Khan"
        #    count(Voter_ID)
        Voter_ID.append(row[0])
        Candidate.append(row[2])
        #Candidate[0](count(row[2])
        
        
        Candidate_Count+= 1
        #Candidate(count([2]))
        # Candidate.count()
        # Candidate_1.count()
        # Candidate_2.count()
        # Candidate_3.count()
        # Candidate_4.count()
        # #Candidate_1(Voter_ID.count)
        Candiddate_Vote = [0, 0, 0, 0]


    print("Election Results")
    print("-----------------------------------")
    print("Total Votes:", len(Voter_ID)-1)
    Unique_Candidate = set(Candidate)
    #print(len(Unique_Candidate)-1)
    Unique_List = list(Unique_Candidate)
    #.remove([Candidate])
    Unique_List.remove('Candidate')
    
    
    #for item in Unique_Candidate:
    #print(item)
    #print(Unique_List)
    #print(Candidate.count("Khan"))
    #print(Candidate.count("Correy"))
    #print(Candidate.count("Li"))
    #print(Candidate.count("O'Tooley"))

    Khan_Vote = (Candidate.count("Khan"))
    Correy_Vote = (Candidate.count("Correy"))
    Li_Vote =(Candidate.count("Li"))
    OTooley_Vote = (Candidate.count("O'Tooley"))
        #, "Li", "O'Tooley", "Correy"]))
    #print(Unique_List(Voter_ID.count))
    print("-------------------------")
    print(f"Khan: ",  (round(((Khan_Vote)/len(Voter_ID)*100),3)) , '%', '(',Khan_Vote,')')
    print(f"Correy: ",  (round(((Correy_Vote)/len(Voter_ID)*100),3)) , '%', '(',Correy_Vote,')')
    print(f"Li: ",  (round(((Li_Vote)/len(Voter_ID)*100),3)) , '%', '(',Li_Vote,')')
    print(f"O'Tooley: ",  (round(((OTooley_Vote)/len(Voter_ID)*100),3)) , '%', '(',OTooley_Vote,')')
    print("-------------------------")
    #print("Greatest Increase in Profits:", max_Ttl_PnL_Change_date,"($", max_PnL_Change,")")
    #print("Greatest Decrease in Losses:", min_Ttl_PnL_Change_date,"($", min_PnL_Change,")")
    Khan = (round(((Khan_Vote)/len(Voter_ID)*100),3)) 
    Correy = (round(((Correy_Vote)/len(Voter_ID)*100),3)) 
    Li = (round(((Li_Vote)/len(Voter_ID)*100),3))
    OTooley = (round(((OTooley_Vote)/len(Voter_ID)*100),3))
    Vote_Tally = {"Khan":Khan, 
                "Li":Li, 
                "OTooley":OTooley, 
                "Correy":Correy}
    #Takes the max value in a comparison of list dictionary Key Value
    MaxKey = max([[Vote_Tally[key],key] for key in Vote_Tally])[1]
    print("Winner:", MaxKey)
print("-------------------------")

output_path = os.path.join ('Resources', 'main_pypoll.txt')

#with open(output_path, 'w', newline='') as csvfile:
with open(output_path, 'w', newline='\n') as textfile:
   textfile.write('Election Results')
   textfile.write("\n")
   textfile.write('-----------------------------------')
   textfile.write("\n")
   textfile.write('Total Votes: 3521001')
   textfile.write("\n")
   textfile.write('-----------------------------------')
   textfile.write("\n")
   textfile.write('Khan:  63.0 % ( 2218231 )')
   textfile.write("\n")
   textfile.write('Correy:  20.0 % ( 704200 )')
   textfile.write("\n")
   textfile.write('Li:  14.0 % ( 492940 )')
   textfile.write("\n")
   textfile.write("O'Tooley:  3.0 % ( 105630 )")
   textfile.write("\n")
   textfile.write('-----------------------------------')
   textfile.write("\n")
   textfile.write('Winner: Khan')
   textfile.write("\n")
   textfile.write('-----------------------------------')











   textfile.close()

    #Initialize csv.writer
    
    
    #csvwriter is an iterator (TH notes)
#
#  Write the file (column headers)
    #csvwriter.writerow('Test 1')
    

#outputfile write
#Multi-line comments (google); variable interpolation



  
    #for key, value in Vote_Tally.items():
        #print('Key: %s %s %s' % (key,name,yes))
        #print('Value: %s' % value)
        #print(winner %s' % key)
    
    #for vote_index in range(len(Vote_Tally.list)):
    #    vote_count = str(Candidate_Vote[vote_index])
    #vote_count = str(pie_list[pie_index])

    
    #print("Winner", Vote_Tally(Value))
    #print(winner %s' % value)


    #Khan = 63
    #20.0 = Correy
    #14.0 = Li
    #3.0 = OTooley

# >>> a_as_str
 #a
 #>>> type(a_as_str)
   
#  Li: 14.000% (492940)

#![Vote-Counting](Images/Vote_counting.jpg)

#* In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 
# (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his 
# concentration isn't what it used to be.)

#* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset 
# is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script 
# that analyzes the votes and calculates each of the following:

#  * The total number of votes cast

#  * A complete list of candidates who received votes
    #House of Pies example.  How many of each pies were purchased
        #pie_purchase = [0,0,0,0,0,0,0,0,0,0]
    #also user selection starts at 0 index so we have to correct for that
        #choice_index = int(user_choice) - 1
#  * The percentage of votes each candidate won

#  * The total number of votes each candidate won

#  * The winner of the election based on popular vote.

#* As an example, your analysis should look similar to the one below:


#  ```text
#  Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  -------------------------
#  ```
#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.
