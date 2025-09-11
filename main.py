from scripts.download_data import check_and_download
from scripts.process_data import clean_data
# from scripts.analyze import generate_analysis

def main():
    print("🔄 Checking for data updates...")
    if check_and_download():
        print("📊 Processing new data...")
        clean_data()
    
    print("📈 Generating analysis...")
    # generate_analysis()
    
    print("✅ Complete!")

if __name__ == "__main__":
    main()
