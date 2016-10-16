import re

f = open("hours_test.txt","r")

hours_raw = f.read()

f.close()

#print(hours_raw)

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "no overnight", "overnight"]

hours_d = {}

for day in DAYS[:6]:
    hours_d[day] = [[] for i in range(9)]

hours_d["overnight"] = []

print(hours_d)

pat = r"("

for day in DAYS:
    pat += day + "|"

pat = pat [:-1] #to strip the leading "|"

pat += ")s"

print("pat = "+pat)

pat = re.compile(pat)

hours_raw = re.sub(pat, r"\1", hours_raw)

hours_raw = re.sub("no overnight", "", hours_raw)

time_pat = re.compile(r"(\d\d):?(\d\d)?((p|a)m)")

def time_to_index(string):
    parts = string.split("-")
    start, end = parts[0], parts[1]
    times = []
    for i, s in enumerate((start, end)):
        groups = re.match(time_pat, s).groups()
        print(groups)

for line in hours_raw.split("\n"):
    if line.startswith("Employee"):
        continue
    s = line.split("\t")
    if len(s) == 2:
        name, time_string = s[0], s[1]
        print((name, time_string))

        times = time_string.split(",")

        for i, item in enumerate(times):
            times[i] = item.strip()
            day_count = 0
            for day in DAYS:
                if day in item:
                    day_count += 1

                    if day_count > 1:
                        # i = len(times)
                        index = item.index(day)
                        if item[index] == "o" and "no" in item or item[index-1]=="-":
                            continue
                        a = item[0:index]
                        b = item[index:]
                        times[i] = a
                        times.append(b)
                        break

        print(times)

        #day-day expansion
        for i, time in enumerate(times):
            times[i] = item.strip()
            if "-" in time:
                del times[i]
                parts = time.split("-")

                a,b = parts[0], parts[1]
                suffix = ""
                if " " in b:
                    #if there is stuff after the second day
                    b_parts = b.split()
                    b = b_parts[0]
                    suffix = b_parts[1]
                
                a = DAYS.index(a)
                b = DAYS.index(b)

                print(str(a)+" , "+str(b))
                for n in range(a,b+1):
                    times.append(DAYS[n]+suffix)
                    
        print(times)
        for time in times:
            times[i] = item.strip()
            if len(time) == 0:
                continue
            print("time = "+time)
            if time in DAYS:
                print("It's all day")
                #it's an all day affair
                if time == "overnight":
                    hours_d[time].append(name)
                else:
                    for n in range(9):
                        hours_d[time][n].append(name)
            else:
                print("It's not")
                #We need to be picky choosy

                parts = time.split()

                if re.match(time_pat, parts[1]):
                    time_range = time_to_index(parts[1])

                    for n in range(time_range[0], time_range[1]):
                        hours_d[time][n].append(name)

print(hours_d)
        
