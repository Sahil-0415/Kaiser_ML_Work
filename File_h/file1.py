# import os

# # Define the filename to use for these operations
# FILE_NAME = "demo_file.txt"

# # 1. WRITE OPERATION ('w') - Creates a new file or overwrites an existing one
# print("--- 1. Writing to a new file ---")
# with open(FILE_NAME, "w", encoding="utf-8") as file:
#     file.write("Hello, World!\n")
#     file.write("This is line number two.\n")
# print(f"File '{FILE_NAME}' created successfully.")


# # 2. READ OPERATION ('r') - Reads the entire file content at once
# print("\n--- 2. Reading the entire file content ---")
# try:
#     with open(FILE_NAME, "r", encoding="utf-8") as file:
#         content = file.read()
#         print("File Content:")
#         print(content.strip())
# except FileNotFoundError:
#     print("Error: The file does not exist.")


# # 3. APPEND OPERATION ('a') - Adds new text to the end of the existing file
# print("\n--- 3. Appending data to the file ---")
# with open(FILE_NAME, "a", encoding="utf-8") as file:
#     file.write("This is an appended line.\n")
# print("New data appended successfully.")


# # 4. READ LINE BY LINE - Memory-efficient way to process large files
# print("\n--- 4. Reading file line by line ---")
# with open(FILE_NAME, "r", encoding="utf-8") as file:
#     for index, line in enumerate(file, start=1):
#         print(f"Line {index}: {line.strip()}")


# # 5. READ INTO A LIST - Stores each line as an item in a Python list
# print("\n--- 5. Reading lines into a list ---")
# with open(FILE_NAME, "r", encoding="utf-8") as file:
#     lines_list = file.readlines()
#     print("List of lines:", lines_list)


# # 6. EXCLUSIVE CREATION ('x') - Fails safely if the file already exists
# print("\n--- 6. Attempting exclusive creation ---")
# try:
#     with open(FILE_NAME, "x", encoding="utf-8") as file:
#         file.write("This will fail because the file exists.")
# except FileExistsError:
#     print(f"Safe check passed: '{FILE_NAME}' already exists. Will not overwrite.")


# # # 7. CLEANUP / DELETE OPERATION - Removes the file from the system
# # print("\n--- 7. Deleting the file ---")
# # if os.path.exists(FILE_NAME):
# #     os.remove(FILE_NAME)
# #     print(f"File '{FILE_NAME}' has been deleted cleanly.")
# # else:
# #     print("File not found to delete.")

import json

# Define the file name
FILE_NAME = "data_storage.json"

# 1. Initialize the Python collection objects
sample_list = ["apple", "banana", "cherry", "apple"]
sample_tuple = ("red", "green", "blue")
sample_set = {"python", "java", "c++"}

# 2. Prepare data for file writing (Convert set and tuple to lists for JSON compatibility)
data_to_save = {
    "my_list": sample_list,
    "my_tuple": list(sample_tuple),
    "my_set": list(sample_set)
}

# 3. WRITE OPERATION: Save the data to a file
print("--- Writing Data to File ---")
with open(FILE_NAME, "w") as file:
    json.dump(data_to_save, file, indent=4)
print(f"Data successfully saved to {FILE_NAME}\n")

# 4. READ OPERATION: Load the data back from the file
print("--- Reading Data from File ---")
with open(FILE_NAME, "r") as file:
    loaded_data = json.load(file)

# 5. Restore original object types (JSON reads everything back as lists)
retrieved_list = loaded_data["my_list"]
retrieved_tuple = tuple(loaded_data["my_tuple"])
retrieved_set = set(loaded_data["my_set"])

print(f"Retrieved List: {retrieved_list} (Type: {type(retrieved_list)})")
print(f"Retrieved Tuple: {retrieved_tuple} (Type: {type(retrieved_tuple)})")
print(f"Retrieved Set: {retrieved_set} (Type: {type(retrieved_set)})\n")

# 6. PERFORM OPERATIONS ON THE RETRIEVED OBJECTS
print("--- Performing Operations ---")

# List Operation: Append a new item and count occurrences
retrieved_list.append("orange")
apple_count = retrieved_list.count("apple")
print(f"Updated List: {retrieved_list}")
print(f"Occurrences of 'apple' in list: {apple_count}")

# Tuple Operation: Access by index and slicing (Tuples are immutable)
first_color = retrieved_tuple[0]
sliced_tuple = retrieved_tuple[1:]
print(f"First element of tuple: {first_color}")
print(f"Sliced tuple (index 1 onwards): {sliced_tuple}")

# Set Operation: Add a new unique item and perform an intersection test
retrieved_set.add("javascript")  # Will be added
retrieved_set.add("python")      # Duplicate, will be ignored
framework_set = {"python", "django", "react"}
common_languages = retrieved_set.intersection(framework_set)

print(f"Updated Set: {retrieved_set}")
print(f"Common elements between sets: {common_languages}")
