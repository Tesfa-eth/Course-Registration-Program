from graphics import *
import csv

def main():
    skill = []
    courses_suggestion = []
    skills = 0
    print("Welcome to Easybusycozy! Easybusycosy will help you choose your classes for the next school term. \nIt will "
          "also show the course schedule grid and help you catch classes which clash!!!\nAll you have to do is input "
          "your preferences! You wanna give it a try?")
    input("Just Hit ENTER and see the magic!")
    print("Well, let's get started!")
    counter = 0 # counter evaluates the students background so that we can determine what level course they should take.
    level = input("What year student are you(1,2,3, or 4)?")
    if level == "1":
        counter = 0
    else:
        counter += 1
    next_term = input("Is there any class you are specifically looking for? (Y/N)")
    next_term = next_term.upper()
    if next_term == "Y":
        print("Please enter them and hit d when done.")
        # take a input and add it to a list
        while skills != "d":
            skills = input("-----> ")
            skills = skills.lower()

            if skills not in skill:
                skill.append(skills)

    print("In Bennington College, students are highly encouraged to explore new areas of study and \nimprove "
          "their skills in all ways. Skills, for eg., include coding, drawing, writing...etc")
    skills = input("Is there any skill that you want to develop next term?(Y/N)")
    skills = skills.upper()

    if skills == "Y":
        print("Cool! Please enter them and hit d when done!")
        skills = 0
        while skills != "d":
            skills = input("---->")
            skills = skills.lower()

            if skills not in skill:
                skill.append(skills)
    next_term1 = input("From your classes in this term, is there any class that you may want to take again or take "
                       "the next level(Y/N)")
    next_term1 = next_term1.upper()
    if next_term1 == "Y":
        print("Please enter them and hit d when done.")
        # take a input and add it to a list
        skills = 0
        while skills != "d":
            skills = input("-----> ")
            skills = skills.lower()

            if skills not in skill:
                skill.append(skills)

    # identification (catagorizing) stage using keywwords

    for n in range(len(skill)):
        if skill[n] in ['programming', 'coding', 'computer science', 'technology', 'cs', 'it', 'computers',
                        'distributed systems', 'introduction to cs', 'intro to cs', 'coding', 'programmig languages',
                        'python programming', 'python']:
            if 'CS' not in courses_suggestion:
                courses_suggestion.append('CS')  # classes from the csv dictionary

        elif skill[n] in ['mathematics', 'computation', 'algebra', "geometry", 'science', 'math', 'algebra',
                          'geometry']:
            if 'MATH' not in courses_suggestion:
                courses_suggestion.append('MATH')

        elif skill[n] in ['physics', 'geography', 'motion', 'physics I']:
            if 'PHYSICS' not in courses_suggestion:
                courses_suggestion.append('PHYSICS')
        elif skill[n] in ['biology', 'cells', 'bio', 'med', 'biochemistry']:
            if 'BIO' not in courses_suggestion:
                courses_suggestion.append('BIO')
        elif skill[n] in ['stage management', 'acting', 'drama', 'acting']:
            if 'DRAMA' not in courses_suggestion:
                courses_suggestion.append('DRAMA')

        elif skill[n] in ['video', 'filming', 'film', 'film making', 'recording', 'video editing']:
            if 'FILM' not in courses_suggestion:
                courses_suggestion.append('FILM')

        elif skill[n] in ['drawing', 'designing', 'painting', 'drw']:
            if 'DRAWING' not in courses_suggestion:
                courses_suggestion.append('DRAWING')

        elif skill[n] in ['architecture', 'designing', 'arch']:
            if 'ARCH' not in courses_suggestion:
                courses_suggestion.append('ARCH')

        elif skill[n] in ['photo', 'editing', 'shooting', 'photographing', 'camera']:
            if 'PHOTO' not in courses_suggestion:
                courses_suggestion.append('PHOTO')

    choice_list = []
    print("Awesome! Based on the information you've entered we've chosen courses for you!")
    print("Tell us your experience of with them and get your specific classes!!!")

    for i in range(len(courses_suggestion)):

        level = input("Have you done " + str(courses_suggestion[i]) + " before? (type Y/N): ")
        level = level.upper()
        if level not in ["Y", "N"]:
            print("Please enter Y/N")
            level = input("Have you done " + str(courses_suggestion[i]) + " before? (type Y/N): ")

        choosen_class = courses_suggestion[i]
        level = level.upper()

        if level == "Y":
            # open 4000 level course (higher difficulty class)
            counter += 1
        if counter > 1: # decide the difficulty level
            with open("4000level.csv", "r") as file:
                csv_reader = csv.DictReader(file)

                for line in csv_reader:
                    print("Great! Here is our class suggestion for it.")
                    print(line[choosen_class])

            # append the classes to the list
        else:
            # open 2000 level class
            with open("2000level.csv", "r") as file:
                csv_reader = csv.DictReader(file)
                for line in csv_reader:
                    print("Great! Here is our class suggestion for it.")
                    print(line[choosen_class])

        try:
            no_of_classes = int(input("How many class(es) did (could) you choose for this class?: "))
        except ValueError:
            print("Please enter the right input")
            no_of_classes = int(input("How many class(es) did (could) you choose for this class?: "))
        for classes in range(no_of_classes):
            choice = input("Enter the code of your class choice : ")
            if choice != "":
                if choice not in choice_list:
                    choice_list.append(choice)
    if len(choice_list) != 0:
        input("And your schedule is ready! Hit ENTER to get it.")
    else:
        input("You haven't selected any class!")


    # open the csv files and read the colomns based on the time slots
    first_class = []
    with open("Updatedspring2020.csv", "r") as file:
        csv_reader = csv.DictReader(file)
        for line in csv_reader:
            # for monday and thursday
            first_class = line["10:00am - 11:50am"]
            second_class = line["1:40pm - 3:30pm"]
            third_class = line["3:40pm - 5:30pm"]
            # for tuesday and friday
            first_class1 = line["8:30am - 10-20am"]
            second_class1 = line["10:30am - 12:20am"]
            third_class1 = line["2:10pm - 4:00pm"]
            fourth_class = line["4:10pm-6:00 pm"]
            # for wednesday
            first_class2 = line["8:30 - 12:00"]
            second_class2 = line["2:10 - 5:50"]

    win = GraphWin("course grid", 700, 700)
    # first draw the whole rectangular frame
    rec = Rectangle(Point(10, 10), Point(690, 500))
    rec.draw(win)
    # draw the cross line to write the days on
    line = Line(Point(10, 40), Point(690, 40))
    line.draw(win)
    # draw the fist line which separates the days and goes all the way down
    line = Line(Point(114, 10), Point(114, 500))
    line.draw(win)
    text_point = Point(114 // 2, 30)  # center to write the first text (Monday)
    text = Text(text_point, "Time")
    text.draw(win)
    # Multi_perpose for loop
    for n in range(5):  # draw the colomns by cloning and moving the same line. And at the same time writing the days.
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        line1 = line.clone()
        line1.move(115, 0)  # check the drawing for the last line of the colon here
        line1.draw(win)
        line = line1
        text_point.clone()
        text_point.move(114, 0)
        text = Text(text_point, days[n])
        text.draw(win)
    line = Line(Point(10, 58.4), Point(114, 58.4))  # the first line on Time colomn
    line.draw(win)
    text_point = Point(60, 50)
    text = Text(text_point, "8:30am- 9:00am")
    text.setSize(10)
    text.draw(win)
    p = 9
    for b in range(24):  # move it 19. Because 460//24 = 18.4. Draw the lines and write the time slot
        line1 = line.clone()
        line1.move(0, 18.4)
        line1.draw(win)
        line = line1
        new_point = text_point.clone()
        new_point.move(0, 18.4)
        # write down the time until it is one
        if p <= 12:
            if b % 2 == 0:
                p1 = p + 1
                n = ":00"
                text = Text(new_point, str(p) + n + "am-" + str(p) + ":30am")

            else:
                p2 = p - 1
                n = ":30"
                text = Text(new_point, str(p2) + n + "am-" + str(p) + ":00am")
            p = p1
            text.setSize(10)
            text.draw(win)
            text_point = new_point

        else:
            p = 1
            if b % 2 == 0:
                p1 = p + 1
                n = ":00"
                text = Text(new_point, str(p) + n + "am-" + str(p) + ":30am")

            else:
                p2 = p - 1
                n = ":30"
                text = Text(new_point, str(p2) + n + "am-" + str(p) + ":00am")
            p = p1
            text.setSize(10)
            text.draw(win)
            text_point = new_point
    # Draw the rectangle and fill it out based on the schedule
    # draw the horizontal lines for the structure of the table

    # polygon for M/Th
    polygon2 = Polygon(Point(114, 95.2), Point(229, 95.2), Point(229, 168.8), Point(114, 168.8), Point(114, 224),
                       Point(229, 224), Point(229, 297.9), Point(114, 297.9), Point(114, 371.5), Point(229, 371.5),
                       Point(114, 371.5))
    polygon2a = polygon2.clone()
    polygon2.move(345, 0)
    polygon2.draw(win)
    polygon2a.draw(win)
    # show no_class
    rect2 = Rectangle(Point(114, 168.8), Point(229, 224))
    rect2.setFill('grey')
    rect2.draw(win)
    rect2a = rect2.clone()
    rect2a.move(345, 0)
    rect2a.draw(win)
    text2 = Text(rect2.getCenter(), "No classes")
    text2.draw(win)
    text2a = text2.clone()
    text2a.move(345, 0)
    text2a.draw(win)

    rect3 = rect2.clone()
    rect3.move(0, 202.4)
    rect3.draw(win)
    text3 = Text(rect3.getCenter(), "No classes")
    text3.draw(win)
    rect3a = rect3.clone()
    rect3a.move(345, 0)
    rect3a.draw(win)
    text3a = text3.clone()
    text3a.move(345, 0)
    text3a.draw(win)

    # polygon for T/F
    polygon3 = Polygon(Point(229, 113.6), Point(344, 113.6), Point(344, 187.3), Point(229, 187.3), Point(229, 242.5),
                       Point(344, 242.5), Point(344, 316.5), Point(229, 316.5), Point(229, 390.1), Point(344, 390.1),
                       Point(229, 390.1))
    polygon3a = polygon3.clone()
    polygon3a.move(345, 0)
    polygon3.draw(win)
    polygon3a.draw(win)

    # polygon for Wed

    polygon4 = Polygon()

    # show no classes
    rect4 = Rectangle(Point(229, 389.6), Point(344, 426.4))
    rect4.setFill("grey")
    rect4.draw(win)
    text4 = Text(rect4.getCenter(), "No classes")
    text4.draw(win)
    rect4a = rect4.clone()
    rect4a.move(345, 0)
    rect4a.setFill("grey")
    rect4a.draw(win)
    text4a = Text(rect4a.getCenter(), "No classes")
    text4a.draw(win)
    rect5 = Rectangle(Point(344, 168.8), Point(459, 242.8))
    rect5.setFill("grey")
    rect5.draw(win)
    text5 = Text(rect5.getCenter(), "No classes")
    text5.draw(win)

    rect6 = rect4.clone()
    rect6.move(115, 0)
    rect6.draw(win)
    text6 = Text(rect6.getCenter(), "No classes")
    text6.draw(win)

    # The following is for M/Th
    R2 = Rectangle(Point(114, 95.2), Point(229, 168.8))
    R2a = R2.clone()
    R2a.move(345, 0)
    R3 = R2.clone()
    R3.move(0, 7 * 18.4)
    R3a = R3.clone()
    R3a.move(345, 0)
    R4 = R3.clone()
    R4.move(0, 4 * 18.4)
    R4a = R4.clone()
    R4a.move(345, 0)

    # draw for T/F
    R5 = Rectangle(Point(229, 40), Point(344, 113.6))
    R5a = R5.clone()
    R5a.move(345, 0)
    R6 = R5.clone()
    R6.move(0, 4 * 18.4)
    R6a = R6.clone()
    R6a.move(345, 0)
    R7 = R6.clone()
    R7.move(0, 7 * 18.4)
    R7a = R7.clone()
    R7a.move(345, 0)
    R8 = R7.clone()
    R8.move(0, 4 * 18.4)
    R8a = R8.clone()
    R8a.move(345, 0)
    # for wednesday
    R9 = Rectangle(Point(344, 40), Point(459, 169))
    R9a = Rectangle(Point(344, 243.5), Point(459, 391))

    counter2 = 0
    counter3 = 0
    counter4 = 0
    counter5 = 0
    counter6 = 0
    counter7 = 0
    counter8 = 0
    counter9 = 0
    counter9a = 0
    for m in range(len(choice_list)):
        if choice_list[m] in first_class:
            if counter2 < 1:
                R2.setFill("brown")
                R2a.setFill("brown")
                R2.draw(win)
                R2a.draw(win)

                text2 = Text(R2.getCenter(), choice_list[m])
                text2.draw(win)
                text2a = Text(R2a.getCenter(), choice_list[m])
                text2a.draw(win)
            else:
                # show clashes
                p = R2.getCenter()
                p.move(0, 17)
                text2 = Text(p, choice_list[1])
                text2.setSize(10)
                text2.setFill("red")
                text2.draw(win)
                text2a = text2.clone()
                text2a.move(345, 0)
                text2a.draw(win)
                R2.setOutline("Red")
                R2a.setOutline("Red")
            counter2 += 1
        elif choice_list[m] in second_class:
            if counter3 < 1:
                R3.setFill("red")
                R3a.setFill("red")
                R3.draw(win)
                R3a.draw(win)

                text3 = Text(R3.getCenter(), choice_list[m])
                text3.draw(win)
                text3a = Text(R3a.getCenter(), choice_list[m])
                text3a.draw(win)
            else:
                # show clashes
                p = R2.getCenter()
                p.move(0, 17)
                text3 = Text(p, choice_list[1])
                text3.setSize(10)
                text3.setFill("red")
                text3.draw(win)
                text3a = text3.clone()
                text3a.move(345, 0)
                text3a.draw(win)
                R3.setOutline("Red")
                R3a.setOutline("Red")
            counter3 += 1
        elif choice_list[m] in third_class:
            if counter4 < 1:
                R4.setFill("yellow")
                R4a.setFill("yellow")
                R4.draw(win)
                R4a.draw(win)

                text4 = Text(R4.getCenter(), choice_list[m])
                text4.draw(win)
                text4a = Text(R4a.getCenter(), choice_list[m])
                text4a.draw(win)
            else:
                # show clashes
                p = R4.getCenter()
                p.move(0, 17)
                text4 = Text(p, choice_list[1])
                text4.setSize(10)
                text4.setFill("red")
                text4.draw(win)
                text4a = text4.clone()
                text4a.move(345, 0)
                text4a.draw(win)
                R4.setOutline("Red")
                R4a.setOutline("Red")
            counter4 += 1
        elif choice_list[m] in first_class1:
            if counter5 < 1:
                R5.setFill("green")
                R5a.setFill("green")
                R5.draw(win)
                R5a.draw(win)

                text5 = Text(R5.getCenter(), choice_list[m])
                text5.draw(win)
                text5a = Text(R5a.getCenter(), choice_list[m])
                text5a.draw(win)
            else:
                # show clashes
                p = R5.getCenter()
                p.move(0, 17)
                text5 = Text(p, choice_list[1])
                text5.setSize(10)
                text5.setFill("red")
                text5.draw(win)
                text5a = text5.clone()
                text5a.move(345, 0)
                text5a.draw(win)
                R5.setOutline("Red")
                R5.setOutline("Red")
            counter5 += 1
        elif choice_list[m] in second_class1:
            if counter6 < 1:
                R6.setFill("orange")
                R6a.setFill("orange")
                R6.draw(win)
                R6a.draw(win)

                text6 = Text(R6.getCenter(), choice_list[m])
                text6.draw(win)
                text6a = Text(R6a.getCenter(), choice_list[m])
                text6a.draw(win)
            else:
                # show clashes
                p = R6.getCenter()
                p.move(0, 17)
                text6 = Text(p, choice_list[1])
                text6.setSize(10)
                text6.setFill("red")
                text6.draw(win)
                text6a = text6.clone()
                text6a.move(345, 0)
                text6a.draw(win)
                R6.setOutline("Red")
                R6.setOutline("Red")
            counter6 += 1
        elif choice_list[m] in third_class1:
            if counter7 < 1:
                R7.setFill("purple")
                R7a.setFill("purple")
                R7.draw(win)
                R7a.draw(win)
                text7 = Text(R7.getCenter(), choice_list[m])
                text7.draw(win)
                text7a = Text(R7a.getCenter(), choice_list[m])
                text7a.draw(win)

            else:
                # show clashes
                p = R7.getCenter()
                p.move(0, 17)
                text7 = Text(p, choice_list[1])
                text7.setSize(10)
                text7.setFill("red")
                text7.draw(win)
                text7a = text7.clone()
                text7a.move(345, 0)
                text7a.draw(win)
                R7.setOutline("Red")
                R7.setOutline("Red")
            counter7 += 1
        elif choice_list[m] in fourth_class:
            if counter8 < 1:
                R8.setFill("silver")
                R8a.setFill("silver")
                R8.draw(win)
                R8a.draw(win)
                text8 = Text(R8.getCenter(), choice_list[m])
                text8.draw(win)
                text8a = Text(R8a.getCenter(), choice_list[m])
                text8a.draw(win)
            else:
                # show clashes
                p = R8.getCenter()
                p.move(0, 17)
                text8 = Text(p, choice_list[1])
                text8.setSize(10)
                text8.setFill("red")
                text8.draw(win)
                text8a = text8.clone()
                text8a.move(345, 0)
                text8a.draw(win)
                R8.setOutline("Red")
                R8.setOutline("Red")
            counter8 += 1
        if choice_list[m] in first_class2:
            if counter9 < 1:
                R9.setFill("white")
                R9.draw(win)
                text9 = Text(R9.getCenter(), choice_list[m])
                text9.draw(win)
            else:
                # show clashes
                p = R9.getCenter()
                p.move(0, 17)
                text9 = Text(p, choice_list[m])
                text9.setSize(10)
                text9.setFill("red")
                text9.draw(win)
                R9.setOutline("Red")
                R9.setOutline("Red")
            counter9 += 1
        if choice_list[m] in second_class2:
            if counter9a < 1:
                R9a.setFill("lime")
                R9a.draw(win)
                text9a = Text(R9a.getCenter(), choice_list[m])
                text9a.draw(win)
            else:
                # show clashes
                p = R9a.getCenter()
                p.move(0, 17)
                text9a = Text(p, choice_list[m])
                text9a.setSize(10)
                text9a.setFill("red")
                text9a.draw(win)
                R9a.setOutline("Red")
                R9a.setOutline("Red")
            counter9a += 1

    # draw the last crossbar line
    line = Line(Point(114, 500 - 4 * 18.4), Point(690, 500 - 4 * 18.4))
    line.draw(win)
    input("over")


main()
