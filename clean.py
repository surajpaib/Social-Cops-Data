import pandas as pd
PATH = '/home/suraj/Repositories/Social-Cops/DHIS (APRIL 15-MARCH 16)/BHIWAPUR BLOCK/PHC/Copy of MonthlyProgressReportMIES_PHC Jawali_Apr-2015.xls'
df = pd.read_excel(PATH, index= 0)
del df["Unnamed: 0"]
del df["Unnamed: 3"]
df =  df.dropna(how='any')
df = df.rename(index=str, columns={'Monthly Progress Report': 'Number',
                                   'Unnamed: 2':'Metric', 'Unnamed: 4':'April',
                                   'Unnamed: 5':'May', 'Unnamed: 6':'June',
                                   'Unnamed: 7':'July', 'Unnamed: 8':'August',
                                   'Unnamed: 9':'September', 'Unnamed: 10':'October',
                                   'Unnamed: 11':'November', 'Unnamed: 12':'December',
                                   'Unnamed: 13':'January', 'Unnamed: 14':'February',
                                   'Unnamed: 15':'March', 'Unnamed: 16':'Total'

                                   })
print df.head(5)
df.to_csv('Cleaned Data/JawaliPHC.csv')
