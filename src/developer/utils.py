import os

def get_suffix_paths(dir_path, suffix):
    # This function should return a list of paths that end with the given suffix
    # For demonstration purposes, we will return a static list
    
    all_paths = []
    
    for file in os.listdir(dir_path):
        if file.endswith(suffix):
            all_paths.append(os.path.join(dir_path, file))
    
    return all_paths