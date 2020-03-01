import requests
from HackMerced_2020 import coidGet
from bs4 import BeautifulSoup
search = "CSE 015"
coid = coidGet.findCourse(search)
className = "just discovered"
units = "Units: "
terms = "offered:"

def getCourseInfo(coid):
    if coid == "Error: ":
        print("\tNo class with that name and number found")
    else:
        url = 'https://catalog.ucmerced.edu/ajax/preview_course.php?catoid=16&coid=' + str(coid) + '&link_text=&display_options=a:2:{s:8:~location~;s:6:~search~;s:10:~best_match~;s:30:~%3Cstrong%3E%20Best%20Match:%20%3C/strong%3E~;}&show'
        html = str(requests.get(url).content)
        soup = str(BeautifulSoup(html, 'html.parser').get_text())
        print("\nENTIRE HTML FILE: " + soup +"\n")
        x = 0
        betterSoup = ""
        while x < len(soup):
            if (soup[x:x+2] != "\\t"):
                betterSoup += soup[x]
                x += 1
            elif(soup[x:x+2] == "\\t"):
                x += 2
            elif(soup[x:x+2] == "\\r"):
                x += 2
            elif(soup[x:x+2] == "\\n"):
                x += 2
        print(betterSoup)

        #Class Name
        if html.find(className) != -1:
            start = html.find(className) + 18
            otherEnd = html.find(":", start)
            end = html.find("\'", start) -1
            numTypeEnd = html.find(":", start)
            id = html[start : otherEnd]
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
            global betterDetails
            betterDetails = ""
            details = html[start + 27 : html.find(topicUnder)]
            x=0
            while x < len(details):
                if details[x] != "<":
                    betterDetails += details[x]
                    x+=1
                else:
                    newEnd = details.find(">", x)
                    x += (newEnd-x+1)


        #Stuff under Course Details
        if html.find("Course Details") != 1:
            start = html.find("Course Details")
            if html.find("GE Req") != 1:
                CourseDetailRemoveHTML("GE Req")

            elif html.find("Req") != 1:
                CourseDetailRemoveHTML("Req")

            print("Course Details: " + betterDetails)


        return id, name, numUnits, description, betterDetails




print(getCourseInfo(coid))