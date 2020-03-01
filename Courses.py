import requests
from HackMerced_2020 import coidGet
search = "CSE 015"
coid = coidGet.findCourse(search)
className = "just discovered"
units = "Units: "
terms = "offered:"

def getCourseInfo(coid):
    url = 'https://catalog.ucmerced.edu/ajax/preview_course.php?catoid=16&coid=' + str(coid) + '&link_text=&display_options=a:2:{s:8:~location~;s:6:~search~;s:10:~best_match~;s:30:~%3Cstrong%3E%20Best%20Match:%20%3C/strong%3E~;}&show'
    html = str(requests.get(url).content)

    print("\nENTIRE HTML FILE: " + html +"\n")

    #Class Name
    if html.find(className) != -1:
        start = html.find(className) + 18
        end = html.find("\'", start) -1
        numTypeEnd = html.find(":", start)
        name = html[start : end]
        print(html[start : end])

    #Units
    if html.find(units) != 1:
        start = html.find(units)
        numUnits = html[start : start+8]
        print(html[start : start+8])

    #Description
    if html.find("<br><br>", start+17) != 1:
        end = html.find("<br><br>", start+18)
        description = html[start+16: end]
        print("Description: " + html[start+16: end])


    def CourseDetailRemoveHTML(topicUnder):
        global details
        details = str(html[start + 27: html.find(topicUnder)])
        for i, word in enumerate(details):
            if word == "<":
                details = details[0 : i] + "    " + details[i + 4: len(details)-1]

    #Stuff under Course Details
    if html.find("Course Details") != 1:
        start = html.find("Course Details")
        if html.find("GE Req") != 1:
            CourseDetailRemoveHTML("GE Req")
        if html.find("Req") != 1:
            CourseDetailRemoveHTML("Req")

        print(details)

if coid == "Error: ":
    print("\tNo class with that name and number found")
else:
    getCourseInfo(coid)