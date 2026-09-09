# import statistics

# # Sample dataset
# data = [1, 2, 2, 3, 4, 7, 9]

# # 1. Calculate Mean (Average)
# mean_value = statistics.mean(data)

# # 2. Calculate Median (Middle value)
# median_value = statistics.median(data)

# # 3. Calculate Mode (Most frequent value)
# mode_value = statistics.mode(data)

# # Display the results
# print(f"Dataset: {data}")
# print(f"Mean:   {mean_value}")
# print(f"Median: {median_value}")
# print(f"Mode:   {mode_value}")



data = [1, 2, 2, 3, 4, 7, 9]
n = len(data)

# 1. Manual Mean
manual_mean = sum(data) / n

# 2. Manual Median
sorted_data = sorted(data)
mid = n // 2
if n % 2 == 0:
    manual_median = (sorted_data[mid - 1] + sorted_data[mid]) / 2
else:
    manual_median = sorted_data[mid]

# 3. Manual Mode
frequency = {}
for num in data:
    frequency[num] = frequency.get(num, 0) + 1
manual_mode = max(frequency, key=frequency.get)

print(f"Mean: {manual_mean}, Median: {manual_median}, Mode: {manual_mode}")
