import statistics

input_string = "12.5
13.7
15.3
17.9
17
18.7
17.7
19.1
20.4
21.6
22.2
21
20.9
22
21.6
22.1
23.2
25.3
26.4
28
26.8
28.3
28.5
28.2
28.6
28.2
29.4
31
32.9
34.6
36.3
37.8
42.4
44.5
46.2
51.4"

# Split the input string into a list of numbers
numbers = [int(num) for num in input_string.split(", ")]

# Create a string with each number on a new line
output_string = "\n".join(str(num) for num in numbers)

# Calculate additional statistics
smallest = min(numbers)
largest = max(numbers)
median = statistics.median(numbers)
lower_quartile = statistics.quantiles(numbers, n=4)[0]
upper_quartile = statistics.quantiles(numbers, n=4)[2]

# Add the additional statistics to the output string
output_string += f"\nSmallest: {smallest}\nLargest: {largest}\nMedian: {median}\nLower Quartile: {lower_quartile}\nUpper Quartile: {upper_quartile}"

# Print the output string
print(output_string)