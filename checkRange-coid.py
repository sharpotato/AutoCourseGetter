import requests
crn = 14925
courseInfo = "CLASS=\"dddefault\""
print(courseInfo)
url = 'https://mystudentrecord.ucmerced.edu/pls/PROD/xhwschedule.P_ViewCrnDetail?subjcode=HIST&crsenumb=008&validterm=202010&crn=' + str(crn)
html = str(requests.get(url).content)
if html.find(courseInfo) != -1:
    start = html.find(courseInfo)+len(courseInfo)+1
    print("Start: " + str(start))
    end = html.find("<", start)
    print("End: " + str(end))
    print(html[start: end])
    start = html.find(courseInfo, start) + len(courseInfo) + 1
print(html)
        