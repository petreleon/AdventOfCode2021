input_file = open("Day 01/input.txt", "r")

numbers = [int(line.strip()) for line in input_file.readlines()] 
counting_increases = 0

sums = [numbers[i] + numbers[i+1] + numbers[i+2] for i in range(len(numbers) - 2)]

comparing_sum = sums[0]

for sum in sums[1:]:
    if sum > comparing_sum:
        counting_increases += 1
    comparing_sum = sum

print(counting_increases)