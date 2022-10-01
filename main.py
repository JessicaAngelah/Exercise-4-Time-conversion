#Exercise 4: Time conversion
seconds = int(input("Enter the number of seconds: "))

hour = seconds // 3600
minute = (seconds % 3600) // 60
sec = seconds - ((hour * 3600) + (minute * 60))

print(f"Results: {hour:02d}:{minute:02d}:{sec:02d}")