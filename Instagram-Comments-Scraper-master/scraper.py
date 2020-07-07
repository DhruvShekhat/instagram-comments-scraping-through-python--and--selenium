from selenium import webdriver
import time
import sys

chrome_path = r'C:\Users\shekh\Desktop\instagramscrap\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(chrome_path)
driver.get("https://www.instagram.com/p/CCNT5QsjJN4/")

try:
    load_more_comment = driver.find_element_by_css_selector('.MGdpg > button:nth-child(1)')
    print("Found {}".format(str(load_more_comment)))
    i = 0
    while load_more_comment.is_displayed() and i < int(sys.argv[2]):
        load_more_comment.click()
        time.sleep(1.5)
        load_more_comment = driver.find_element_by_css_selector('.MGdpg > button:nth-child(1)')
        print("Found {}".format(str(load_more_comment)))
        i += 1
except Exception as e:
    print(e)
    pass

user_names = []
user_comments = []
comment = driver.find_elements_by_class_name('gElp9 ')
for c in comment:
    container = c.find_element_by_class_name('C4VMK')
    name = container.find_element_by_class_name('_6lAjh').text
    content = container.find_element_by_tag_name('span').text
    content = content.replace('\n', ' ').strip().rstrip()
    user_names.append(name)
    user_comments.append(content)

#user_names.pop(0)
#user_comments.pop(0)
print(user_names)
print(user_comments)
import csv
from itertools import zip_longest
list1 = user_names
list2 = user_comments
d = [list1, list2]
export_data = zip_longest(*d, fillvalue = '')
with open('comment.csv', 'w', encoding="utf-8", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("user_name", "User_comments"))
      wr.writerows(export_data)
myfile.close()
driver.close()
