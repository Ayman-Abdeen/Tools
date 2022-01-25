# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import os
import pandasql as ps
#from pandasql import sqldf

##!pip install pandasql

directoryPath=os.getcwd()

for folders, sub_folders, file in os.walk(directoryPath):
          for name in file:
                if (name.startswith("TCRS")):
                    filename = os.path.join(folders, name)
                    data1 = pd.read_excel(filename)

#data1 = pd.read_excel("E://DT]//New folder//TCRS Template.xlsx")

    
dfT=data1.drop('Number of affected site', axis=1).join(data1['Number of affected site'].str.split('\n', expand=True).stack().reset_index(level=1, drop=True).rename('affected sites'))


dfTg=dfT.drop(['Domain','TCRSeverity','Date','TCR#','Title/Description','MajorAction','Status','Comments','ServiceImpact','RequiredPM',"AffectedKPI's",'RequiresSPOCs','TestingReadiness','RollbackProcedure','SparesAvailable','TotalOutageduration','Outagedurationpersite'], axis=1).groupby('affected sites').size().rename('countOfsites')

result = dfT.join(dfTg , on="affected sites")


result=result.rename(columns={"TCR#": "TCR","affected sites": "affectedSites"}, errors="raise")
                
                              
result.to_csv("result TCRS Template.csv", encoding='utf-8')
    
    
    
q1 = """SELECT A.TCR AS TCR1, B.TCR AS TCR2, A.affectedSites
FROM result A, result B
WHERE A.TCR <> B.TCR
AND A.affectedSites = B.affectedSites 
ORDER BY A.affectedSites;"""

DDDf=ps.sqldf(q1, locals())


DDDf.to_csv("result TCRS DDDf Template.csv", encoding='utf-8')