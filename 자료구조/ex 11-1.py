
mem={"name":"홍길동", "age":25, "city":"seoul"}
mem["age"]=26
print(mem)

for key in mem.keys():
    print(key,'~',mem[key])

print(mem)

print(mem["name"],"은", mem["citi"],"에 사는")