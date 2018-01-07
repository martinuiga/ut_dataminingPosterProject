import csv
from urllib.request import urlopen
import time

# This script is used for modifying and filtering the initial datasets. Main focus is on attributes Lest_X and Lest_Y
# and converting them into another coordinate system. This script also makes sure to only convert data from 2012 and 2016 as those
# years were used in project's map visualizations and comparisons. It takes several hours to convert mentioned values.

output_rows = []
with open('avalik_2.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    counter = 0 # this counter was used as a log
    for row in reader:
        counter += 1
        # print(counter) # log
        # Exclude years 2013, 2014 and 2015. Also don't try to convert empty and faulty values.
        if row[-3] != '' and row[-2] != '' and '-' in row[-3] and '-' in row[-2] and '2013' not in row[1] and '2014' not in row[1] and '2015' not in row[1]:
            try:
                lest_x = row[-3]
                lest_y = row[-2]

                # split x range
                lest_x1 = row[-3].split("-")[0]
                lest_x2 = row[-3].split("-")[1]

                # split y range
                lest_y1 = row[-2].split("-")[0]
                lest_y2 = row[-2].split("-")[1]

                # URL-converter, convert lest to geo
                # http://www.maaamet.ee/rr/geo-lest/url/?xy=lest_x_middle,lest_y_middle
                url_string_x = "http://www.maaamet.ee/rr/geo-lest/url/?xy=" + str(lest_x1) + "," + str(lest_y1)
                url_string_y = "http://www.maaamet.ee/rr/geo-lest/url/?xy=" + str(lest_x2) + "," + str(lest_y2)

                html_x = urlopen(url_string_x)
                html_x_content = str(html_x.read())

                content_x_split = html_x_content.split(',')
                geo_x1 = content_x_split[0].replace("b'", "")
                geo_y1 = content_x_split[1].replace("'", "")

                time.sleep(0.5) # necessary for the program to not crash, without causes overload

                html_y = urlopen(url_string_y)
                html_y_content = str(html_y.read())

                content_y_split = html_y_content.split(',')
                geo_x2 = content_y_split[0].replace("b'", "")
                geo_y2 = content_y_split[1].replace("'", "")

                row[-3] = geo_x1 + "-" + geo_x2
                row[-2] = geo_y1 + "-" + geo_y2

                time.sleep(0.5) # necessary for the program to not crash
            except:
                # if unable to get a response and converted values
                row[-3] = 0
                row[-2] = 0


        output_rows.append(row)

writer = csv.writer(open('output_2012_2016.csv', 'w',newline='')) # create a new csv file and write modified data there
writer.writerows(output_rows)

