import re

with open('page_source.txt') as f_txt:
    lines = f_txt.readlines()

lines = ' '.join(lines)

urls = re.findall(r'(?:http\:|https\:)?\/\/.*\.(?:zip|zip)', lines)
urls = [url for url in urls if 'Full.zip' in url]

print('%d urls were found' % len(urls))

with open('zip_urls.txt', 'w') as f:
    for url in urls:
        f.write(url + '\n')

