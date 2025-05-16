add= lambda x, y: x+y

print(add(1,2))


employees=[
    {"name": "smith","salary":500000},
    {"name": "praveen", "salary":60000},
    {"name" : "arun", "salary":80000}
]


#sort employees by salary using lambda

sorted_employees = sorted(employees, key=lambda x : x["salary"])

for emp in sorted_employees:
    print(emp)