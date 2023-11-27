import os

def create_dummy_file_in_folders(directory, filename="del.txt"):
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            filepath = os.path.join(root, dir, filename)
            if not os.path.exists(filepath):
                with open(filepath, 'w') as f:
                    f.write('This is a dummy file for Git visibility.\n')

# Replace 'your_directory_path' with the path to your target directory
your_directory_path = '.'
create_dummy_file_in_folders(your_directory_path)
