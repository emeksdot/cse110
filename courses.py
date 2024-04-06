# # c_file = open("./courses.txt")

# # for line in c_file:
# #     print(line, line[0], line[1], line[2])

# # c_file.close()

# # # same code above in the preferred way
# # with open("./courses.txt") as courses_file:
# #     for line in courses_file:
# #         print(line, line[0], line[4], line[6])
# # same code above in the preferred way


# with open("./hr_system.txt") as hr_file:
#     for line in hr_file:
#         # print(line, line[0], line[4], line[6])
#         ln = line.strip("")
#         ln2 = ln.split()
#         # print(ln, ln2[0] )
#         # print(f"Name: {ln2[0]}, Title: {ln2[2]}")
#         print(f"Name: {ln2[0]}, (ID: {ln2[1]}), {ln2[2]} - ${int(ln2[3]):.2f}")








with open("./hr_system.txt") as hr_file:
    for line in hr_file:
        # First step remove the blank spaces
        stripped_line = line.strip()
        # Second step split the line into parts of a list
        splitted_line = stripped_line.split()
        # print(stripped_line)

        ln2 = splitted_line
        # The final task
        print(f"Name: {ln2[0]}, (ID: {ln2[1]}), {ln2[2]} - ${int(ln2[3]):.2f}")
        # name id_number job_title salary
