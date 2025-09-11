import sys
sys.path.append('..')
from config import DATASET_FILE, PROCESSED_DATA_DIR
import pandas as pd

def clean_data():
    df = pd.read_csv(DATASET_FILE)
    # Processing logic
    df.to_csv(PROCESSED_DATA_DIR / "cleaned_data.csv")

if __name__ == "__main__":
    clean_data()
