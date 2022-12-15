import csv
from statistics import mean, stdev

with open('Negara.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)

luas_mean = mean([int(row['Luas']) for row in data])
luas_stdev = stdev([int(row['Luas']) for row in data])
populasi_mean = mean([int(row['Populasi']) for row in data])
populasi_stdev = stdev([int(row['Populasi']) for row in data])

with open('NegaraStandarDeviasi.csv', 'w') as csvfile:
    fieldnames = ['Negara', 'Luas Mean', 'Luas Std Dev', 'Populasi Mean', 'Populasi Std Dev']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in data:
        writer.writerow({
            'Negara': row['Negara'],
            'Luas Mean': luas_mean,
            'Luas Std Dev': luas_stdev,
            'Populasi Mean': populasi_mean,
            'Populasi Std Dev': populasi_stdev
        })

with open('NegaraMean.csv', 'w') as csvfile:
    fieldnames = ['Negara', 'Luas Mean', 'Populasi Mean']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in data:
        writer.writerow({
            'Negara': row['Negara'],
            'Luas Mean': luas_mean,
            'Populasi Mean': populasi_mean
        })
