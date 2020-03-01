from bs4 import BeautifulSoup
import requests, time
from selenium import webdriver

def requestClassAvail():
    #Selenium Stuff
    url = "https://mystudentrecord.ucmerced.edu/pls/PROD/xhwschedule.P_SelectSubject"
    driver = webdriver.Chrome(executable_path=r"C:\Users\colin\Downloads\chromedriver.exe")
    driver.get(url)
    springBtn = driver.find_elements_by_xpath("//input[@value='202010']")[0]
    allCourses = driver.find_elements_by_xpath("//input[@value='N' and @name='openclasses']")[0]
    submit_button = driver.find_elements_by_xpath('/html/body/div[3]/h4/form/input')[0]
    springBtn.click()
    allCourses.click()
    submit_button.click()

    html = driver.page_source
    newHTML = ''
    driver.close()
    category = '<tbody><tr bgcolor="#FFC605">\n<th class="ddlabel" scope="row"><p class="leftaligntext"><small>CRN</small></p></th>\n<th class="ddlabel" scope="row"><p class="leftaligntext"><small>Course #</small></p></th>\n<th class="ddlabel" scope="row"><p class="centeraligntext"><small>Course Title</small></p></th>\n<th class="ddlabel" scope="row"><p class="centeraligntext"><small>Units</small></p></th>\n<th class="ddlabel" scope="row"><p class="centeraligntext"><small>Actv</small></p></th>\n<th class="ddlabel" scope="row"><p class="centeraligntext"><small>Days</small></p></th>\n<th class="ddlabel" scope="row"><p class="centeraligntext"><small>Time</small></p></th>\n<th class="ddlabel" scope="row"><p class="centeraligntext"><small>Bldg/Rm</small></p></th>\n<th class="ddlabel" scope="row"><p class="centeraligntext"><small>Start - End</small></p></th>\n<th class="ddlabel" scope="row"><p class="centeraligntext"><small>Instructor</small></p></th>\n<th class="ddlabel" scope="row"><p class="centeraligntext"><small>Max Enrl</small></p></th>\n<th class="ddlabel" scope="row"><p class="centeraligntext"><small>Act Enrl</small></p></th>\n<th class="ddlabel" scope="row"><p class="centeraligntext"><small>Seats Avail</small></p></th>\n</tr>'

    absMin = html.find("NOTE: Schedule Subject to Change")
    absMax = html.find("This is table displays line separator at end of the page")
    newHTML = html[absMin+len("NOTE: Schedule Subject to Change")+29 : absMax-58]
    arr=[[],[],[],[]]
    #[[subjcode],[crsenumb],[crn],[available]

    for x in range(41):
        min = newHTML.find("<h3>")
        max = newHTML.find("</h3>")
        if (min >= 0) and (max >= 0):
            newHTML = newHTML[0:min] + newHTML[max+5:len(newHTML)]
    for x in range(41):
        if (newHTML.find("#FFC605")-85 >= 0):
            newHTML = newHTML[0 : newHTML.find("#FFC605")-85] + newHTML[newHTML.find("#FFC605")-85+len(category)+66 : len(newHTML)]

    def createArr(searchType, arrSpot, thingAfter):
        currentSpot = 0
        for x in range(1676):
            if (newHTML.find(searchType) >= 0):
                currentSpot = newHTML.find(searchType, currentSpot) - 1
                arr[arrSpot].append(newHTML[newHTML.find(searchType, currentSpot)+len(searchType) : newHTML.find(thingAfter, newHTML.find(searchType, currentSpot)+len(searchType))])
                currentSpot += 2

    createArr("subjcode=", 0, "&amp")
    createArr("crsenumb=", 1, "&amp")
    createArr("crn=", 2, "\">")

    available = "</small></p></td>\n</tr>"
    currentSpot = 0
    for x in range(1676):
        if (newHTML.find(available)-7 != 0):
            currentSpot = newHTML.find(available, currentSpot) - 7
            beforeAvail = newHTML.find(">", currentSpot) + 1
            afterAvail = newHTML.find("<", currentSpot)
            numAvail = newHTML[beforeAvail: afterAvail]
            if numAvail == "Closed":
                numAvail = "Full"
            arr[3].append(numAvail)
            currentSpot += 8

    return arr





#requestClassAvail("CSE", "015")
