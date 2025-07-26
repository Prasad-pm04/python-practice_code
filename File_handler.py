import os
import shutil

# Define file type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".c"]
}

# Function to get the category based on file extension
def get_category(filename):
    _, ext = os.path.splitext(filename)
    for category, extensions in FILE_TYPES.items():
        if ext.lower() in extensions:
            return category
    return "Others"  # If file doesn't match any known type

# Function to organize files in the given folder
def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print("The folder path does not exist.")
        return

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        # Only work with files, skip folders
        if os.path.isfile(file_path):
            category = get_category(file)
            category_folder = os.path.join(folder_path, category)

            # Create the category folder if it doesn't exist
            if not os.path.exists(category_folder):
                os.mkdir(category_folder)

            # Move file to its category folder
            shutil.move(file_path, os.path.join(category_folder, file))
            print(f"Moved: {file} → {category}/")

    print("\n✅ Folder organized successfully!")

# === Main Execution ===
folder = input("Enter the path of the folder you want to organize: ")
organize_folder(folder)
