# tuple
# tuples =(1, 2, 3,)
# tuple1 = (1,)#
# print(tuples[2])
# for i in tuples:
#     print(i+2)

# dictionary

# dict_1 = {
#     "name1": ["Nazgul", "Ait"],
#     "name2": "Mirlan",
#     "name3": "Andrew",

#}
#
# print(dict_1['name1'])
#
# dict_1['name2'] = "Yasir"
# dict_1['name1'].append('Ulan')

#items()     vyvodyi s kluchom
# for i in dict_1.iteams():
#     print(i)
#
# for i in dict_1.values():
#     print(i)
#
# for i in dict_1.keys():#vyvodyb kluchi
#     print(i)

#
# print(type(dict_1.keys()))
# print(dict_1.values())#toliko znachenya


#dict_1['name4'] = 'kunduz'###dovlaem
#print(dict_1)
#
# students = {
#  "Ulan": 98,
#  "Kunduz": 90,
#  "vadim": 99,
#     "NURDIN ":100
#
# }
# other = {
#     "Tanru": 88,
#     "Azamat": 78
# }
# students.update(other)
# print(students)

# resualt = sum (students.values()) /len(students)
# print(resualt)



#update()
# after_exam = {}
# for key, values in students.items():
#
#     val= values-2
#     after_exam.update(
#         {key:val}



#fromkeys()
# lists = ["book1","book2","book3"]
# dickts = dict().fromkeys(lists, 20)
# # print(dickts)
# #dickts.clear()
# dickts_1 = dickts.copy()#id drigaya
# print(dickts)


products = {}
for i in range(2):
    name = input("enter name")
    price = input("enter price")
    products[name] = price
