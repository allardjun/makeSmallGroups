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

    emSize = 12

    studentListFile = 'studentList_' + courseNumber + '.xlsx'
    if courseNumber == 'M227C':
        ySize = 200
        yShift = ySize/2+20
        Teams_list = [
            ['Whiteboard',   [200, yShift- 30, 117, 70], 4],
            ['Door',         [  5, yShift-115, 117, 70], 4],
            ['Window',       [250, yShift-115, 117, 70], 4],
            ['Lectern',      [ 35, yShift- 30, 117, 70], 4],
            ['Projector',    [125, yShift-115, 117, 70], 4]
            ]
        datepos = [5, 20]
    elif courseNumber == 'P50':
        ySize = 200
        yShift = ySize/2+20
        Teams_list = [
            ['Lectern',     [200, yShift- 30, 117, 70], 4],
            ['Back Corner', [  5, yShift-115, 120, 70], 3],
            ['Back Door',   [250, yShift-115, 117, 70], 4],
            ['Front Door',  [ 35, yShift- 30, 117, 70], 4],
            ['Middle',      [125, yShift-115, 117, 70], 4]
            ]
        datepos = [5, 20]


    # SHUFFLE STUDENTS

    student_df = pd.read_excel(studentListFile)
    student_list = list(student_df['Students'])

    random.shuffle(student_list)

    print(student_list)
    print(len(student_list))

    # DATE

    today = date.today()

    datestr = today.strftime("%A, %-d %B")
    print(datestr)

    Teams = pd.DataFrame(Teams_list, columns=['Name', 'Coords', 'NumberOfThinkers'])

    d = draw.Drawing(380, ySize, origin=(0,0), displayInline=False)

    iStudent = 0
    for iTeam, thisTeam in Teams.iterrows():
        if iStudent < len(student_list):
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
                12,thisTeam['Coords'][0]+5,thisTeam['Coords'][1]+55-emSize*(iStudent_inThisTeam+1),fill='black')
                iStudent = iStudent + 1
                d.append(studentLabel)
                if iStudent >= len(student_list):
                    break
   
    d.append(draw.Text(datestr, 12, datepos[0], ySize-datepos[1], fill='black'))

    d.saveSvg('teams_' + courseNumber + '.svg')

    os.system('/Applications/Inkscape.app/Contents/MacOS/inkscape teams_' + courseNumber + '.svg -o teams_' + courseNumber + '.png')

    if courseNumber=='M227C':
        os.system('./sendToGithub.sh')

if __name__ == '__main__':
    makeSmallGroups()
