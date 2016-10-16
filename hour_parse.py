import re

f = open("hours_test.txt","r")

hours_raw = f.read()

f.close()

#print(hours_raw)

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "no overnight", "overnight"]

hours_d = {}

for day in DAYS[:6]:
    hours_d[day] = [{}]

hours_d["overnight"] = []

print(hours_d)

pat = "("

for day in DAYS:
    pat += day + "|"

pat = pat [:-1] #to strip the leading "|"

pat += ")s"

print("pat = "+pat)

pat = re.compile(pat)

hours_raw = re.sub(pat, r"\1", hours_raw)

hours_raw = re.sub("no overnight", "", hours_raw)

def time_to_index(string)

for line in hours_raw.split("\n"):
    if line.startswith("Employee"):
        continue
    s = line.split("\t")
    if len(s) == 2:
        name, time_string = s[0], s[1]
        print((name, time_string))

        times = time_string.split(",")

        for i, item in enumerate(times):
            day_count = 0
            for day in DAYS:
                if day in item:
                    day_count += 1

                if day_count > 1:
                    # i = len(times)
                    index = item.index(day)
                    if item[index] == "o" and "no" in item:
                        continue
                    a = item[0:index]
                    b = item[index:]
                    times[i] = a
                    times.append(b)
                    break

        print(times)
        
        
