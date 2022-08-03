#pandas
import pandas as qq

"""vv={"Name":['sathish','kumar','mani'],#pandas use create data frame
    "age":[22,33,44]}
v1=qq.DataFrame(vv,index=['c1','c2','c3'])
v1.to_csv('aaa.csv')#csv file nwe create"""
#this series is one Dimensional 
w=[2,4,7]
v1=qq.Series(w,index=['a','b','c'])# series like column table 
print(v1)

name={'m1':'55','m2':'77'}
name1=qq.Series(name,index=['m1'])#series sepcfer index 
print(name1)

print("--------------------------------------------------------")
#this two Dimensional row and column
name2={'name':['babu','yudhaya','santhosh'],'age':[88,99,10]}
name2_1=qq.DataFrame(name2,index=['one','Two','Three'])
print('Data Frame:',name2_1)
print("/n")
print(name2_1.loc['one'])#sepic column

print(name2_1.loc[['one','Two']])

ff=qq.read_csv('aaa.csv')
print(ff.to_string)

print("----------------------------------------------------------")
print(qq.options.display.max_rows)#this system row how many stored
