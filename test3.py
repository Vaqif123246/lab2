import re

# Log faylının yolu
log_file_path = 'access_log.txt'

# Faylı oxumaq
with open(log_file_path, 'r') as log_file:
    log_content = log_file.readlines()

# Regex şablonu
pattern = r'\"[A-Z]+ (.*?) HTTP\/\d\.\d\" (\d{3})'

# URL-ləri və status kodlarını çıxarmaq
url_status_list = []
for line in log_content:
    match = re.search(pattern, line)
    if match:
        url = match.group(1)
        status_code = match.group(2)
        url_status_list.append((url, status_code))

# Məlumatları fayla yazmaq
output_path = 'url_status_report.txt'
with open(output_path, 'w') as text_file:
    for url, status in url_status_list:
        text_file.write(f"URL: {url}, Status: {status}\n")

print(f"Nəticələr '{output_path}' faylında saxlanıldı.")
