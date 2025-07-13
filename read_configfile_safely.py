# human-friendly Python code with comments

def read_config_file(file_path):
    try:
        # Try to open and read the file
        with open(file_path, 'r') as file:
            content = file.read()
            print("✅ File content loaded successfully:")
            print(content)

    except FileNotFoundError:
        # File not found
        print("❌ Error: File not found. Please check the file path.")

    except PermissionError:
        # Lack of permissions to read the file
        print("❌ Error: You don't have permission to read this file.")

    except Exception as e:
        # Any other error
        print(f"❌ Unexpected error occurred: {e}")

    finally:
        print("🔚 File reading operation completed.")


# Call the function with your file path
file_path = 'config.txt'
read_config_file(file_path)
