#!/usr/bin/env python
# coding: utf-8

# In[65]:


#import pandas
import pandas as pd


# In[66]:


#read csv file
poll_df = pd.read_csv(r'C:/Users/19706/Downloads/election_data.csv')


# In[67]:


#bring header into df
poll_df


# In[68]:


header = list(poll_df.columns)
header


# In[69]:


#total number of votes
total_votes = len(poll_df)
print(total_votes)


# In[85]:


# a complete list of candidates who received votes
Candidate_Votes = poll_df[["Candidate"]].value_counts()
Candidate_Votes


# In[83]:


#the total number of votes each candidate
candidates = poll_df["Candidate"].unique()
candidates[0],candidates[1],candidates[2]


# In[72]:


charles_votes = (poll_df["Candidate"] == candidates[0]).sum()
charles_votes


# In[73]:


diana_votes = (poll_df["Candidate"] == candidates[1]).sum()
diana_votes


# In[74]:


# percentages of votes for each candidate
raymon_votes = (poll_df["Candidate"] == candidates[2]).sum()
raymon_votes


# In[75]:


# percentages of votes for each candidate
raymon_percentage = raymon_votes/total_votes*100
raymon_percentage


# In[76]:


diana_percentage = diana_votes/total_votes*100
diana_percentage


# In[77]:


charles_percentage = charles_votes/total_votes*100
charles_percentage


# In[78]:


Candidate_Dict = {}

Candidate_Dict[candidates[0]] = [charles_percentage, charles_votes]

Candidate_Dict[candidates[1]] = [diana_percentage, diana_votes]

Candidate_Dict[candidates[2]] = [raymon_percentage, raymon_votes]

Candidate_Dict


# In[ ]:





# In[79]:


#the winner of the election based on popular vote
Winning_Candidate = ''
Vote_Count = 0
if diana_votes > Vote_Count:
    Vote_Count = diana_votes
    Winning_Candidate = candidates[1] 

if raymon_votes > Vote_Count:
    Vote_Count = raymon_votes
    Winning_Candidate = Candidate[2] 

if charles_votes > Vote_Count:
    Vote_Count = charles_votes
    Winning_Candidate = candidates [0]
    
    
print(Winning_Candidate)


# In[80]:


election_results = (
    f"Election Results\n"
    f"------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------\n"
    f"{candidates[0]}:{round(charles_percentage,3)}%,  ({charles_votes})\n"
    f"{candidates[1]}:{round(diana_percentage,3)}%,  ({diana_votes})\n"
    f"{candidates[2]}:{round(raymon_percentage,3)}%,  ({raymon_votes})\n"
    f"----------------------\n"
    f" Winner: {Winning_Candidate} \n"
    f"-----------------------\n"


)

print(election_results)


# In[81]:


PyPoll_Text = "PyPoll_Text_File.txt"
with open(PyPoll_Text, "w")as txt_file:
    txt_file.write(election_results)


# In[ ]:




