import pandas as pd
from urllib.parse import urlparse
import matplotlib.pyplot as plt

# Analyzing Browser History Using Python and Pandas
# sqlite3 History "select datetime(last_visit_time/1000000-11644473600,'unixepoch'),url from  urls order by last_visit_time desc" > hist.txt
# https://applecrazy.github.io/blog/posts/analyzing-browser-hist-using-python/

'''
Linux: /home/<username>/.config/google-chrome/default

Linux

The default location is in ~/.config:

    [Chrome Stable] ~/.config/google-chrome
    [Chrome Beta] ~/.config/google-chrome-beta
    [Chrome Dev] ~/.config/google-chrome-unstable
    [Chromium] ~/.config/chromium
'''

# Open our file
with open('hist.txt') as f:
    content = f.readlines()
# Strip whitespace then split on first occurrence of pipe character
raw_data = [line.split('|', 1) for line in [x.strip() for x in content]]
# We now have a 2D list.
print(raw_data[1])

data = pd.DataFrame(raw_data, columns=['datetime', 'url'])

print(data.head(1))

data.datetime = pd.to_datetime(data.datetime)

print(data.datetime[0])

parser = lambda u: urlparse(u).netloc
data.url = data.url.apply(parser)

print(data.head(1))


# Aggregate domain entries
site_frequencies = data.url.value_counts().to_frame()
# Make the domain a column
site_frequencies.reset_index(level=0, inplace=True)
# Rename columns to appropriate names
site_frequencies.columns = ['domain', 'count']
# Display top 2
print(site_frequencies.head(2))


topN = 20
plt.figure(1, figsize=(10,10))
plt.title('Top $n Sites Visited'.replace('$n', str(topN)))
pie_data = site_frequencies['count'].head(topN).tolist()
pie_labels = None
# Uncomment to get specific domain names
# pie_labels = site_frequencies['domain'].head(topN).tolist()
plt.pie(pie_data, autopct='%1.1f%%', labels=pie_labels)
plt.show()
