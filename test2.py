import re
from collections import Counter

# Log faylının yolu
log_file_path = 'access_log.txt'

# Faylı oxumaq
with open(log_file_path, 'r') as log_file:
    log_content = log_file.readlines()

# Regex şablonu
pattern = r'\"[A-Z]+ (.*?) HTTP\/\d\.\d\" 404'

# 404 status kodu ilə olan URL-ləri çıxarmaq
urls_404 = [match.group(1) for line in log_content if (match := re.search(pattern, line))]

# URL-lərin sayını hesablamaq
url_counts = Counter(urls_404)

# Nəticələri göstərmək
for url, count in url_counts.items():
    print(f"URL: {url}, Say: {count}")
