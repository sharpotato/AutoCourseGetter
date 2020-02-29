import requests

className = "just discovered"
units = "Units: "
coid = 39267


url = 'https://catalog.ucmerced.edu/ajax/preview_course.php?catoid=16&coid=' + str(coid) + '&link_text=&display_options=a:2:{s:8:~location~;s:6:~search~;s:10:~best_match~;s:30:~%3Cstrong%3E%20Best%20Match:%20%3C/strong%3E~;}&show'
response = requests.get(url)
html = str(response.content)
print("\nENTIRE HTML FILE: " + html +"\n")


if html.find(className) != -1:
    start = html.find(className) + 18
    end = html.find("\'", start) -1
    print(html[start : end])

if html.find(units):
    start = html.find(units)
    print(html[start : start+8])

if html.find(".<br><br>", start+17):
    end = html.find(".<br><br>", start+18)
    print("Description: " + html[start+16: end])
