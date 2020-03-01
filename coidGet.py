def findCourse(search):
    master = open("masterCourses.txt", "r")
    course = -1
    for entery in master:
        course = entery.find(search)
        if course != -1:
            coid = entery[0 : course-2]
            print(search+" - "+coid)
            return coid
    if course == -1:
        return "Error: "

