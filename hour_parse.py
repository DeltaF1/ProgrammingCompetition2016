import math
import random
import re
import pprint



#print(hours_raw)

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "overnight"]

hours_d = {}

for day in DAYS[:7]:
    hours_d[day] = [[] for i in range(9)]


##print(hours_d)

pat = r"("

for day in DAYS:
    pat += day + "|"

pat = pat [:-1] #to strip the leading "|"

pat += ")s"

#print("pat = "+pat)

pat = re.compile(pat)



time_pat_str = r"(\d?\d):?(\d\d)?((p|a)m)"

time_pat = re.compile(time_pat_str)

def time_to_index(string):
    parts = string.split("-")
    start, end = parts[0], parts[1]
    
    times = []
    for i, s in enumerate((start, end)):
        #print("s = "+s)
        groups = re.match(time_pat, s).groups()
        #print(groups)
        hour = int(groups[0])

        if groups[1] == None:
            minutes = 0
        else:
            minutes = int(groups[1])
        meridian = groups[2]

        minutes = minutes / 60

        #convert to military
        if meridian == "pm" and hour != 12:
            hour = hour + 12

        #remove offset to get to 0 index at 8:00
        hour = hour - 8
        
        hour = math.ceil(hour + minutes)

        times.append(int(hour))

    return times[0], times[1] - 1

def generate_availability(text):
	hours_d = {}

	for day in DAYS[:7]:
		hours_d[day] = [[] for i in range(9)]
	
	#Convert 'Mondays' to Monday
	text = re.sub(pat, r"\1", text)
	
	#no overnight is redundant, remove it
	text = re.sub("no overnight", "", text)
		
	for line in text.split("\n"):
		if line.startswith("Employee"):
			continue
		s = line.split("\t")
		if len(s) == 2:
			name, time_string = s[0], s[1]
			#print((name, time_string))

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

			#print(times)

			#day-day expansion
			for i, time in enumerate(times):
				times[i] = time.strip()
				if "-" in time and not "m-" in time:
					
					parts = time.split("-")

					a,b = parts[0], parts[1]
					suffix = ""
					if " " in b:
						#if there is stuff after the second day
						b_parts = b.split()
						b = b_parts[0]
						suffix = b_parts[1]

					#print("suffix = ",suffix)
					#print("a = "+a)
					#print("b = "+b)
					a = DAYS.index(a)
					b = DAYS.index(b)
					del times[i]
					#print(str(a)+", "+str(b))
					for n in range(a,b+1):
						times.append(DAYS[n]+suffix)
						
			#print(times)
			for i, time in enumerate(times):
				times[i] = time.strip()
				times[i].replace("\t", "")
				if len(time) == 0:
					continue
				#print("time = "+time)
				if time in DAYS:
					#print("It's all day")
					#it's an all day affair
					
					for n in range(9):
						#if name in hours_d[time][n]:
								#print("WARNING: INSERTING TWICE!!!!!!!!!!!!!!!!!!!!!!!!")
						hours_d[time][n].append(name)
				else:
					#print("It's not")
					#We need to be picky choosy

					parts = time.split()

					if re.match(time_pat, parts[1]):
						#print("time range = "+str(parts[1]))
						time_range = time_to_index(parts[1])

						for n in range(time_range[0], time_range[1]):
							#print("n = "+str(n))
							#if name in hours_d[parts[0]][n]:
								#print("WARNING: INSERTING TWICE!!!!!!!!!!!!!!!!!!!!!!!!")
							hours_d[parts[0]][n].append(name)
	return hours_d
	
def generate_schedule(availability):
	schedule = {}
	
	for day in DAYS:
		schedule[day] = []
	
		for n in range(9):
			offset = 5 if day == "overnight" else 8
			hour = (n + offset) % 12
			hour = str(hour) + ":30"
			name = random.choice(availability[day][n])
			schedule[day].append((hour, name))
	
	return schedule

if __name__ == '__main__':
	
	f = open("hours_test.txt","r")

	hours_raw = f.read()

	f.close()
	
	hours_d = generate_availability(hours_raw)

	schedule = generate_schedule(hours_d)

	pprint.pprint(schedule)    
