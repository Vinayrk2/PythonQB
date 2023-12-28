# Get N of rooms, Rate of Non TV and TV rooms, there will be priority to the non-TV rooms
# calculate the total revenue, if revenue > given revenue : True
# Else number of rooms decrease and check

# Generating List for the Calc

# month = [6-M]^2
month = [(6-i)**2 for i in range(0,13)]
monthDay = [abs(i-15) for i in range(0,32)]
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]


month[0] = monthDay[0] = days[0] = sum = getMin =  0
print(month, monthDay, days, sep="\n")

# rooms = int(input("Enter The Numbers of Rooms : "))
# NTR = int(input("Enter Non-TV Rooms : "))
# TR =  int(input("Enter TV Rooms : "))
# revenue = int(input("Enter The Wanted revenue : "))

rooms = 10
NTR = 1500
TR = 1000
revenue = 10000000
N = rooms
temp =0
while(rooms):
    for mon in range(1,13):
        for day in range(1,days[mon]+1):
            getMin = min(month[mon] + monthDay[day],N)
            sum += min(getMin, rooms )*NTR + (getMin - min(getMin, rooms ))*TR

    if sum >= revenue:
        temp = rooms
        break
    rooms -= 1

print(rooms, N,N-temp, sum)

