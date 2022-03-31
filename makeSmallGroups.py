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
            ['Whiteboard',   [+60-5,  120-55, 120, 70], 4],
            ['Door',         [-120-5, 20-55,  80, 70], 4],
            ['Window',       [+85-5,  20-55,  95, 70], 4],
            ['Lectern',      [-120-5, 120-55, 115,70], 4],
            ['Projector',    [-20-5,  20-55,   100, 70], 4]
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

    #print(student_list)
    #print(len(student_list))

    # DATE

    today = date.today()

    datestr = today.strftime("%A, %-d %B")
    print(datestr)

    Teams = pd.DataFrame(Teams_list, columns=['Name', 'Coords', 'NumberOfThinkers'])

    d = draw.Drawing(350, 350, origin='center', displayInline=False)

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
            if iStudent >= len(student_list):
                break
   

    d.saveSvg('teams_' + courseNumber + '.svg')

    os.system('/Applications/Inkscape.app/Contents/MacOS/inkscape teams_' + courseNumber + '.svg -o teams_' + courseNumber + '.png')

    if courseNumber=='M227C':
        os.system('./sendToGithub.sh')


if __name__ == '__main__':
    makeSmallGroups()
