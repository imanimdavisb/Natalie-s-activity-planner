mood = input("How is your toddler feeling today? (happy, energetic, tired): ")
weather = input("What is the weather? (sunny, rainy, cold): ")

print("\nToday's Activity Suggestion:\n")

if mood == "energetic" and weather == "sunny":
    print("Visit a playground and play outside.")
elif mood == "happy" and weather == "rainy":
    print("Try coloring, reading books, or building blocks indoors.")
elif mood == "tired":
    print("Read a story together and enjoy quiet time.")
else:
    print("Go for a walk, listen to music, or have a family game session.")
