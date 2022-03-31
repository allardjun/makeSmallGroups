def makeSmallGroups():

    import random
    import os
    import sys
    import xlsxwriter
    import pandas as pd
    import drawSvg as draw
    from datetime import date

    # Get command-line arguments
    if len(sys.argv)>1:
        courseNumber = sys.argv[1]
    else:
        courseNumber = 'M227C'

    studentListFile = 'studentList_' + courseNumber + '.xlsx'
    if courseNumber == 'M227C':
        Teams_list = [
            ['Door', [-120-5,-40-55,80,70], 3],
            ['Window', [+55-5,-40-55,95,70], 3],
            ['Lectern',[+60-5,120-55,90,70], 4],
            ['Whiteboard',[-120-5,120-55,115,70], 3],
            ['Center', [-20-5,40-55,90,70], 3]
            ]
    elif courseNumber == 'P50':
        Teams_list = [
            ['Front Door', [-120-5,-40-55,80,70], 3],
            ['Back Door', [+55-5,-40-55,95,70], 3],
            ['Lectern',[+60-5,120-55,90,70], 4],
            ['Middle',[-120-5,120-55,115,70], 3],
            ['Back Corner', [-20-5,40-55,90,70], 3]
            ]

    # SHUFFLE STUDENTS

    student_df = pd.read_excel(studentListFile)
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


    Teams = pd.DataFrame(Teams_list, columns=['Name', 'Coords', 'NumberOfThinkers'])

    d = draw.Drawing(300, 350, origin='center', displayInline=False)

    # Draw text
    d.append(draw.Text(datestr, 12, -120, 150, fill='black'))

    iStudent = 0
    for iTeam, thisTeam in Teams.iterrows():
        box = draw.Rectangle(
            thisTeam['Coords'][0],
            thisTeam['Coords'][1],
            thisTeam['Coords'][2],
            thisTeam['Coords'][3],
            fill='#ffffff',stroke_width=2,stroke='black')

        groupLabel = draw.Text('Team ' + thisTeam['Name'],
            12,thisTeam['Coords'][0]+5,thisTeam['Coords'][1]+55,fill='black')
        d.append(box)
        d.append(groupLabel)
        for iStudent_inThisTeam in range(thisTeam['NumberOfThinkers']):
            studentLabel = draw.Text(student_list[iStudent],
            12,thisTeam['Coords'][0]+5,thisTeam['Coords'][1]+55-10*(iStudent_inThisTeam+1),fill='black')
            iStudent = iStudent + 1
            d.append(studentLabel)
            if iStudent > len(student_list):
                break

    

    d.saveSvg('teams.svg')

    os.system('/Applications/Inkscape.app/Contents/MacOS/inkscape teams.svg -o teams.png')


if __name__ == '__main__':
    makeSmallGroups()
