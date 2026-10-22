# Take total seconds from user
total_seconds = int(input("Enter total seconds: "))

# Convert using // (integer division) and % (remainder)
hours   = total_seconds // 3600          # 1 hour = 3600 seconds
minutes = (total_seconds % 3600) // 60   # remaining seconds → minutes
seconds = total_seconds % 60             # remaining seconds

# Display result
print(f"{total_seconds} seconds = {hours} hours, {minutes} minutes, {seconds} seconds")