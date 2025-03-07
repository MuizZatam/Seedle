import os

def create_project(directory=None):
    """
    Create a new Python project directory.
    
    Args:
        directory (str, optional): The directory where the project will be created.
                                  If not specified, the current directory is used.
    Returns:
        str: The absolute path of the created directory
    """
    # Use current directory if not specified
    if directory is None:
        directory = os.getcwd()
    else:
        # Create the directory if it doesn't exist
        os.makedirs(directory, exist_ok=True)
        
    print(f"Creating new Python project in: {directory}")
    return os.path.abspath(directory)