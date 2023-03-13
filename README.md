# PyBank
#!/usr/bin/env python
# coding: utf-8

# In[49]:


# import pandas
import pandas as pd


# In[50]:


# read CSVfile using pandas
df = pd.read_csv(r'C:/Users/19706/Downloads/budget_data.csv') 


# In[51]:


print(df)


# In[52]:


df.head(0)


# In[53]:


# define total_months and print total
total_months = len(df)
print(total_months)


# In[54]:


#Total revenue
total = df['Profit/Losses'].sum()
print(total)


# In[55]:


# loop through DF
greatest_increase= 0
greatest_decrease= 0
for i in df["Profit/Losses"].keys():
    if i == 0:
        difference = df["Profit/Losses"] [i + 1] - df["Profit/Losses"][i]
        if difference > greatest_increase:
            greatest_increase = difference
            date_increase = df["Date"][i+1]
        elif difference < greatest_decrease:
            greatest_decrease = difference
            date_increase = df ["Date"][i + 1]
else:
    difference = df['Profit/Losses'][i] - df['Profit/Losses'][i-1]
    if difference > greatest_increase:
        greates_increase = difference
        date_increase = df["Date"][i+1]
    elif difference < greatest_decrease:
        greatest_decrease = difference
        date_increase = df["Date"][i + 1]


# In[61]:


# Shift down column 
df["Profit/Losses_Shifted"] = df["Profit/Losses"].shift(1)


# In[64]:


#Greatest increase of profits
df["difference"] = df["Profit/Losses"] - df["Profit/Losses_Shifted"]


# In[67]:


#find average change
df["shifted"]= df["Profit/Losses"].shift(1)
df["growth"]=df["Profit/Losses"]-df["shifted"]
Average_Change= round(df["growth"].mean(),2)
print(Average_Change)


# In[70]:


#Greatest Increase
greatest_increase = int(df["difference"].max())
greatest_increase


# In[71]:


#Greates Decrease
greatest_decrease = int(df["difference"].min())
greatest_decrease


# In[72]:


print(total_months)


# In[75]:


#Terminal Window output
output = (
f"Financial Analysis\n"
f"-------------------------------------\n"
f"Total Months: {total_months}\n"
f"Total: ${total}\n"
f"Average Change: ${Average_Change:.2f}\n"
f"Greatest Increase in Profits: {greatest_increase}\n"
f"Greatest Decrease in Profits: {greatest_decrease}\n")
print(output)


# In[76]:


#txt. file print
with open('my_text_file.txt', "w")as txt_file:
    txt_file.write(output)


# In[ ]:
