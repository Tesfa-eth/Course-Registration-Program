import csv

with open("Updatedspring2020.csv", "w", newline='') as file:
    time_slots = ["10:00am - 11:50am", "1:40pm - 3:30pm", "3:40pm - 5:30pm", "8:30am - 10-20am", "10:30am - 12:20am",
                  "2:10pm - 4:00pm", "4:10pm-6:00 pm", "8:30 - 12:00", "2:10 - 5:50"]
    writer = csv.DictWriter(file, fieldnames=time_slots)

    writer.writeheader()
    writer.writerow(
        {"10:00am - 11:50am": ["BIO2104.01", "CS4115.01", "MAT4115.01", "DRA4268.01", "PHY4327.01", "MAT4108.01"],
         "1:40pm - 3:30pm": ["PHY2118.01", "DRA2177.01", "DRA2116.01", "DRW4237.01", "ARC4239.01", "PHO4131.01"],
         "3:40pm - 5:30pm": ["MAT2100.01", "DRA2170.01", "CS4280.01"], "8:30am - 10-20am": ["FV2303.01",
                                                                                            "BIO4201.01(Lab)",
                                                                                            "DRW4401.01"],
         "10:30am - 12:20am": ["CS2124.01", "DRA2169.01", "BIO4307.01", "MAT4144.01"],
         "2:10pm - 4:00pm": ["MAT2106.01", "DRW2120.01", "BIO4201.01(Lab)", "DRA4332.01", "FV4236.01", "PHO4113.01"],
         "4:10pm-6:00 pm": ["CS4129.01", "DRA4119.01"], "8:30 - 12:00": ["DRA2168.01", "PHO2141.01", "CS4106.01", "PHY4327.01",
         "BIO4109.01"], "2:10 - 5:50": ["DRW2149.01", "CS4280.01", "DRA4151.01"]})

# 4000-level classes

with open("4000level.csv", "w", newline='') as file:
    classes_catagories = ["CS", "PHYSICS", "BIO", "MATH", "DRAMA", "FILM", "DRAWING", "ARCH", "PHOTO"]
    writer = csv.DictWriter(file, fieldnames=classes_catagories)
    writer.writeheader()
    writer.writerow({"CS": ["Distributed Systems (with Lab) (CS4280.01)", "How to Think Like a Data Scientist ("
                                                                          "CS4115.01)", "Design Patterns and Data "
                                                                                        "Structures(CS4106.01)",
                            "Failure(CS4129.01)"],
                     "PHYSICS": ["Physics II: Electricity and Magnetism (with lab)(PHY4327.01)"],
                     "BIO": ["Protein Research Methods(BIO4109.01)",
                             "Comparative Animal Physiology (with lab)(BIO4201.01)",
                             "Animal Social Behavior(BIO4307.01)", "Field Course in Coral Reef(BIO4239.01)"],
                     "MATH": ["Differential Equations and Non-linear Dynamical Systems(MAT4108.01)",
                              "Linear Algebra(MAT4115.01)"
                         , "Abstract Algebra(MAT4144.01)"],
                     "DRAMA": ["Patternmaking and Garment Construction9(DRA4119.01)", "Meisner Technique(DRA4268.01)",
                               "Directing I: The Director's Vision( DRA4332.01)", "Bennington Plays(DRA4151.01)"],
                     "FILM": "Topics In Video(FV4236.01)",
                     "DRAWING": ["Visible Language(DRW4401.01)", "Traces, Mistakes, and Leftovers(DRW4237.01)"],
                     "ARCH": ["Simultaneous Occupancies(ARC4239.01)", "Architectural Analysis(ARC4157.01)"],
                     "PHOTO": ["100 Experiments(PHO4131.01)",
                               "Observations: Photography and the Environment(PHO4113.01)"]})

# 2000 level classes
with open("2000level.csv", "w", newline='') as file:
    classes_catagories = ["CS", "PHYSICS", "BIO", "MATH", "DRAMA", "FILM", "DRAWING", "ARCH"]
    writer = csv.DictWriter(file, fieldnames=classes_catagories)
    writer.writeheader()
    writer.writerow(
        {"CS": "Introduction to Computer Science (CS2124.01)", "PHYSICS": "How to Build a Habitable Planet(PHY2118.01)",
         "BIO": "Introduction to the Biology of Cancer(BIO2104.01)",
         "MATH": ["Entry to Mathematics(MAT2100.01)", "Geometry(MAT2106.01)",
                  "Puzzles(MAT2108.01)", "Logarithms(MAT2107.02)", "Certainty(MAT2119.04)"],
         "DRAMA": ["Stage Management(DRA2241.01)", "Scene Painting(DRA2168.01)", "The History of Directing(DRA2169.01)",
                   "Devising: Moving through Time and Space(DRA2177)", "The Actor's Instrument(DRA2170.01)",
                   "The Magical Object - Visual Metaphor(DRA2116.01)"],
         "FILM": ["Introduction to Video(FV2303.01)", "Introduction to Video, sec-1 (FV2303.01)"],
         "DRAWING": ["Markmaking and Representation(DRW2149.01)",
                     "Drawing As A Verb: Exploring Uncertainty(DRW2120.01)",
                     "Life Drawing Lab(DRW2118.01)"],
         "ARCH": "Sorry there is no introductory arch class for beginners this spring!"})
