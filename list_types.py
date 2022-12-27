friend_names = ['Saab Kht', 'Annie Zfali', 'Asi Skti']

print("first friend:", friend_names[0])
print("last friend:", friend_names[-1])

friends_age = []

for i in range(len(friend_names)):
    age = int(input("enter age: "))
    friends_age.append(age)
    print(f"{friend_names[i]} : {friends_age[i]}")

print(f"{friend_names} : {friends_age}")