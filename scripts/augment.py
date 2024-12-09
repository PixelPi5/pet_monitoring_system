import albumentations as A
import cv2
import os
from glob import glob
import matplotlib.pyplot as plt

# Define the augmentation pipeline
augmentation_pipeline = A.Compose([
    A.HorizontalFlip(p=0.5),  # Flip horizontally
    A.RandomBrightnessContrast(p=0.2),  # Change brightness and contrast
    A.Rotate(limit=15, p=0.5),  # Rotate within ±15 degrees
    A.GaussianBlur(blur_limit=3, p=0.2),  # Apply Gaussian blur
    A.Resize(416, 416)  # Resize to YOLO input size
])

# Function to augment images for a specific class
def augment_images(input_folder, output_folder, augmentations, num_augmentations=3):
    os.makedirs(output_folder, exist_ok=True)  # Create output folder if not exists
    images = glob(f"{input_folder}/*.jpg") + glob(f"{input_folder}/*.png") + glob(f"{input_folder}/*.jpeg")  # Include all common formats

    print(f"Found {len(images)} images in {input_folder}")  # Debugging: Check if files are detected

    if not images:
        print(f"No images found in {input_folder}. Skipping augmentation.")
        return

    for i, img_path in enumerate(images):
        image = cv2.imread(img_path)  # Load image
        for j in range(num_augmentations):
            # Apply augmentation
            augmented = augmentations(image=image)
            augmented_image = augmented['image']

            # Save augmented image
            output_path = os.path.join(output_folder, f"{i}_augmented_{j}.jpg")
            cv2.imwrite(output_path, augmented_image)

    print(f"Augmented {len(images) * num_augmentations} images and saved to {output_folder}")

# Classes to augment
classes = ['eating', 'playing', 'sleeping', 'stretching', 'walking']

# Loop through each class and augment its images
for cls in classes:
    input_folder = f"dataset/train/{cls}/images"  # Include the "images" subfolder
    output_folder = f"dataset_augmented/train/{cls}"  # Output folder for augmented images
    augment_images(input_folder, output_folder, augmentation_pipeline, num_augmentations=3)

print("Augmentation complete for all classes.")

# (Optional) Visualize original and augmented images
def visualize_augmentation(original_path, augmented_path):
    original_image = cv2.imread(original_path)
    augmented_image = cv2.imread(augmented_path)

    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))

    plt.subplot(1, 2, 2)
    plt.title("Augmented Image")
    plt.imshow(cv2.cvtColor(augmented_image, cv2.COLOR_BGR2RGB))

    plt.show()

# Example visualization
# Replace the paths with actual file paths
# visualize_augmentation("dataset/train/walking/images/sample.jpg", "dataset_augmented/train/walking/0_augmented_0.jpg")
