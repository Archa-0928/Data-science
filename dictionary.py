dict1={
    "name":"anu",
    "age":20,
    "branch":"mca"
}
print("name:",dict1["name"])
dict1["college"]="Mangalam college"
dict1["age"]=22
del dict1["branch"]
print("all key value pairs in the dictionary:")
for key,value in dict1.items():
    print(key,":",value)