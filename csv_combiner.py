import glob
import pandas as pd

def main(argv):
        for one_filename in glob.glob('*.csv'):
             new_df = pd.read_csv(one_filename)
             new_df["filename"] = one_filename
             new_df.to_csv(one_filename,index=False)
        combined_csv = pd.concat( [ pd.read_csv(one_filename) for one_filename in glob.glob('*.csv') ] )
        combined_csv.to_csv( "combined_csv.csv", index=False )
        print(combined_csv)
if __name__ == '__main__':
    main([])
