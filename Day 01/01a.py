input_file = open("Day 01/input.txt", "r")

comparing_number = int(input_file.readline().strip())
counting_increases = 0

for line in input_file.readlines():
    reading_number = int(line.strip())
    if reading_number > comparing_number:
        counting_increases += 1
    comparing_number = reading_number

print(counting_increases)
