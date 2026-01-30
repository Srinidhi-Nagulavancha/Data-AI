#  import re
# text = "python is powerful"
# result = re.search("powerful",text)
# if result:
#     print("Match found:", result.group())

# text = "my number is 1234567890 and 9876543210"
# number = re.findall(r"\d{10}", text)
# print(number)

# for match in re.finditer(r"\d{10}", text):
#     print("Match at index:", match.start(), "to", match.end())

import re

text = "my phone number is 1234567890"
masked = re.sub(r'\d','*',text)
print(masked)