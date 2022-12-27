# number of pupil name entered by user INITIATED
pupil = 0
while True:
    # enter nth number of pupil name
    pupil += 1
    names = input("enter the name of the pupil: ")
    if names == "Stop":
        print("-----END-----")
        break

print("Total Number of students:", pupil-1)
