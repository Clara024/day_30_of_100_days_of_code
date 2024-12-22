print("30 Days Down - What did you think?")

for i in range(1,31):
    response = input(f"Day {i}:")
    print( )
    text = f"You thought Day {i} was"
    print(f"{text: ^30}")
    print(f"{ response : ^30}")
    print( )
