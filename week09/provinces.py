
with open("provinces.txt", 'rt') as file:
    provinces = []
    for line in file:
        provinces.append(line.strip())
    print(provinces)
    provinces.pop(0)
    provinces.pop()
    while True:
        try:
            index = provinces.index("AB")
            provinces[index] = "Alberta"
        except:
            break
    
    count = provinces.count("Alberta")
    print("Alberta occurs", count, "times")