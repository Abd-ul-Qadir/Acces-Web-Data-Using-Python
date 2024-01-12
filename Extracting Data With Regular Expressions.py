import re
import urllib.request

url = "https://py4e-data.dr-chuck.net/comments_1618810.html"

response = urllib.request.urlopen(url)

data = response.read().decode()

numbers = re.findall('[0-9]+', data)

total_sum = sum(int(num) for num in numbers)

print("Sum:", total_sum)