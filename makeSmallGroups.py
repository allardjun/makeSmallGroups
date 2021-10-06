def makeSmallGroups(STUDENTLIST):

    import pandas as pd
    import xlsxwriter
    import random
    from datetime import date
    import drawSvg as draw
    import os


    # SHUFFLE STUDENTS

    student_df = pd.read_excel(STUDENTLIST)
    student_list = list(student_df['Students'])

    random.shuffle(student_list)

    print(student_list)

    # DATE

    today = date.today()

    datestr = today.strftime("%A, %-d %B")
    print(datestr)

    # Team Window Corner
    # Team Lectern
    # Team Center
    # Team Door
    # Team Whiteboard Corner

    d = draw.Drawing(300, 350, origin='center', displayInline=False)

    # Draw text
    d.append(draw.Text(datestr, 12, -120, 150, fill='black'))

    box = draw.Rectangle(-120-5,-40-55,80,70,fill='#ffffff',stroke_width=2,stroke='black')
    groupLabel = draw.Text(['Team Door',
        student_list[0],
        student_list[1],
        student_list[2]],
        12,-120,-40,fill='black')
    d.append(box)
    d.append(groupLabel)

    # Draw a rectangle
    box = draw.Rectangle(+55-5,-40-55,95,70,fill='#ffffff',stroke_width=2,stroke='black')
    groupLabel = draw.Text(['Team Window',
        student_list[3],
        student_list[4],
        student_list[5]],
        12,+55,-40,fill='black')
    d.append(box)
    d.append(groupLabel)

    box = draw.Rectangle(+60-5,120-55,90,70,fill='#ffffff',stroke_width=2,stroke='black')
    groupLabel = draw.Text(['Team Lectern',
        student_list[6],
        student_list[7],
        student_list[8],
        student_list[9]],
        12,+60,120,fill='black')
    d.append(box)
    d.append(groupLabel)

    box = draw.Rectangle(-120-5,120-55,115,70,fill='#ffffff',stroke_width=2,stroke='black')
    groupLabel = draw.Text(['Team Whiteboard',
        student_list[10],
        student_list[11],
        student_list[12],
        student_list[13]],
        12,-120,120,fill='black')
    d.append(box)
    d.append(groupLabel)

    box = draw.Rectangle(-20-5,40-55,90,70,fill='#ffffff',stroke_width=2,stroke='black')
    groupLabel = draw.Text(['Team Center',
        student_list[14],
        student_list[15],
        student_list[16]],
        12,-20,40,fill='black')
    d.append(box)
    d.append(groupLabel)

    d.saveSvg('teams.svg')

    os.system('/Applications/Inkscape.app/Contents/MacOS/inkscape teams.svg -o teams.png')


if __name__ == '__main__':
    # write the folder containing input data. Output data will be written to same folder.
    STUDENTLIST = 'studentList.xlsx'  # EDIT FOLDERNAME HERE
    makeSmallGroups(STUDENTLIST)
