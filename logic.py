temperature = int(input("Enter today's temperature: "))
feel_c = temperature < 25   # True
feel_h = temperature >= 25  # True


if temperature < 25:
    print("it is hot -> ", feel_h)
else:
    print("it's cold -> ", feel_h)

# the boolean output gives unexpected result




