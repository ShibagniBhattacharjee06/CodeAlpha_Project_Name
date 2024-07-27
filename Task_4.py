import os
import shutil

#path of the file you want to organize 
DIRECTORY_TO_ORGANIZE = r'C:\Users\shiba\Downloads\Online-Study-main\Online-Study-main\education-website'


FILE_CATEGORIES = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    "Documents": ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    "Videos": ['.mp4', '.avi', '.mov', '.mkv'],
    "Music": ['.mp3', '.wav', '.aac', '.flac'],
    "Archives": ['.zip', '.rar', '.tar', '.gz'],
    "Scripts": ['.py', '.js', '.html', '.css'],
    "Others": []  
}

def organize_files(directory):
    print(f"Organizing files in directory: {directory}")
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        
        if os.path.isdir(file_path):
            continue
        
        
        _, file_extension = os.path.splitext(filename)
        
        
        file_category = None
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension.lower() in extensions:
                file_category = category
                break
        else:
            file_category = "Others"  
        
    
        category_folder = os.path.join(directory, file_category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)
            print(f"Created folder: {category_folder}")
        

        destination = os.path.join(category_folder, filename)
        shutil.move(file_path, destination)
        print(f"Moved file: {file_path} to {destination}")

if __name__ == "__main__":
    organize_files(DIRECTORY_TO_ORGANIZE)
    print("File organization complete.")
