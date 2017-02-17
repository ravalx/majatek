import csv
import io
from .models import NrSt, NrStc



def handle_files(f):
	#fr = TextIOWrapper(f.file, encoding='UTF-8', errors='replace')
	 with open (f, 'rt') as csvfile:
	 	czytacz = csv.DictReader(csvfile)
	 	for row in czytacz:
	 		print(row['Nr-st'], row['Nr-stc'], row['name'], row['price'], row['date'])

	 		#st = NrSt(row['Nr-st'], row['name'], row['price'], row['date'])

