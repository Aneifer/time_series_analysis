import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_data(datasets: dict, base_save_path: str):
    # Resolve paths relative to the current script's directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    base_full_save_path = os.path.join(base_dir, base_save_path)

    # Authenticate and download the datasets using Kaggle API
    api = KaggleApi()
    api.authenticate()
    
    for dataset_name, subfolder in datasets.items():
        # Create the full save path for each dataset (e.g., course or competition folder)
        full_save_path = os.path.join(base_full_save_path, subfolder)
        
        # Ensure that the target directory exists
        if not os.path.exists(full_save_path):
            os.makedirs(full_save_path)
        
        print(f"Downloading dataset {dataset_name} to {full_save_path}...")
        # Download and unpack the dataset
        api.dataset_download_files(dataset_name, path=full_save_path, unzip=True)
        print(f"Data from {dataset_name} downloaded successfully into {full_save_path}!")

if __name__ == "__main__":
    # Dictionary with datasets and their corresponding subdirectories
    datasets = {
        'mikegsmith/ts-course-data': 'course',
        'ryanholbrook/linear-regression-with-time-series': 'competition'
    }
    
    # Base directory where data will be saved (adjust this as needed)
    base_save_path = '../data/raw/'  # This is the root directory where the subfolders will be created
    
    # Download the datasets
    download_data(datasets, base_save_path)
