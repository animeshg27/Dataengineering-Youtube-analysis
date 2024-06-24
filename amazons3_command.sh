#Change it according to your bucket name

# Make copy of JSON Reference data to same location:
aws s3 cp . s3://de-engineering-raw/animesh/raw_data/ --recursive --exclude "*" --include "*.json"

# Make copy of all csv files to same location
aws s3 cp CAvideos.csv s3://de-engineering-raw/animesh/stats_csv/region=ca/
aws s3 cp DEvideos.csv s3://de-engineering-raw/animesh/stats_csv/region=de/
aws s3 cp FRvideos.csv s3://de-engineering-raw/animesh/stats_csv/region=fr/
aws s3 cp GBvideos.csv s3://de-engineering-raw/animesh/stats_csv/region=gb/
aws s3 cp INvideos.csv s3://de-engineering-raw/animesh/stats_csv/region=in/
aws s3 cp JPvideos.csv s3://de-engineering-raw/animesh/stats_csv/region=jp/
aws s3 cp KRvideos.csv s3://de-engineering-raw/animesh/stats_csv/region=kr/
aws s3 cp MXvideos.csv s3://de-engineering-raw/animesh/stats_csv/region=mx/
aws s3 cp RUvideos.csv s3://de-engineering-raw/animesh/stats_csv/region=ru/
aws s3 cp USvideos.csv s3://de-engineering-raw/animesh/stats_csv/region=us/