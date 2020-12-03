# import pandas lib as pd 
import pandas as pd 
import matplotlib.pyplot as plt

# read by default 1st sheet of an excel file 
filepath = "SCC-CollectedDataSetOne\\Traffic\\Ipswich Traffic Flow data 14_10_19 to 10_11_19\\Week_Volume-00008005-Total Flow-2019_10_28-2.xlsx"

#dataframe for plotting fluctuation of daily counts for a single file
# dataframe1 = pd.read_excel(filepath, skiprows=5, nrows=1440) 

dataframe1 = pd.read_excel(filepath, skiprows=5)

#dataframe for plotting variation of daily totals by day of week
#dataframe2 = dataframe1.loc[[1445], dataframe1.columns[1:8]]
dataframe2 = pd.DataFrame({"Day": dataframe1.columns[1:8], "Total": dataframe1.loc[1445,:][1:8]})

print(dataframe2)
#dataframe1.plot(x=dataframe1.columns[0], y=dataframe1.columns[1:8]) 
dataframe2.plot.bar(x="Day", y="Total", rot=0)
plt.show()
