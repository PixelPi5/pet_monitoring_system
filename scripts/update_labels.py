import os

# Define the mapping of folder names to class indices
class_mapping = {
    "eating": 0,
    "playing": 1,
    "sleeping": 2,
    "stretching": 3,
    "walking": 4
}

# Set the base paths to your dataset's train and validation directories
base_paths = [
    "/Users/botagozmaya/Downloads/PetMonitoringSystem/dataset/train",
    "/Users/botagozmaya/Downloads/PetMonitoringSystem/dataset/valid"
]

# Process each base path (train and valid)
for base_path in base_paths:
    print(f"Processing {base_path}...")

    for folder_name, class_index in class_mapping.items():
        # Construct the folder path for the current class
        folder_path = os.path.join(base_path, folder_name, "labels")  # Adjusted to include "labels"
        if os.path.exists(folder_path):  # Check if the folder exists
            print(f"Updating labels in {folder_path} for class '{folder_name}' (index {class_index})...")
            for file_name in os.listdir(folder_path):
                if file_name.endswith(".txt"):  # Only process .txt files
                    file_path = os.path.join(folder_path, file_name)
                    with open(file_path, "r") as file:
                        lines = file.readlines()

                    # Update the class index for each line in the file
                    with open(file_path, "w") as file:
                        for line in lines:
                            parts = line.split()
                            parts[0] = str(class_index)  # Update the class index
                            file.write(" ".join(parts) + "\n")

            print(f"Labels updated successfully for {folder_name}!")
        else:
            print(f"Folder not found: {folder_path}. Skipping...")
