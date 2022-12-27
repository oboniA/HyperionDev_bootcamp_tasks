swim = float(input("how long to swim in minutes: "))
cycle = float(input("how long to cycle in minutes: "))
run = float(input("how long to run in minutes: "))

tri_total = swim + cycle + run

if tri_total <= 100:
    print("Provincial Colours")
elif tri_total <= (100 + 4):
    print("Provincial Half Colours")
elif (tri_total <= 100) and (tri_total < 109):
    print("Provincial Scroll")
else:
    print("No award")