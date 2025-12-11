
values =[1,2, "rahul",3,4]
#list id data type thal allows multipal vlues and can be different data type

print(values[0])

print(values[3])

print(values[1:3])   #silicing   

values.insert(3,"shetty")
print(values)

values.append("End")
print(values)

values[2]="RAHUL"   #update   and upper case
print(values)
del values[1]
print(values)

# Tuple -same as List Data type but immutable
val =(1, 2,"rahul",4.5)

 #val[2]="Rahul"
print(val)

#Dictionary
dic={"a":20, "b":25, 3:"fdvsc" }

print(dic)



dict={}

dict["fristname"]="mangesh"
dict["Lastname"]="bhosale"
dict["No."]=8308259494

print(dict)

print(dict["Lastname"])