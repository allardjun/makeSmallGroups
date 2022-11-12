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

    layout = 'B'

    print((courseNumber == 'P230' and layout == 'B'))

    # rectangle positions are specified by bottom left corner

    studentListFile = 'studentList_' + courseNumber + '.xlsx'
    if courseNumber == 'M227C':
        ySize = 200
        Teams_list = [
            ['Whiteboard',   [200, 102, 117, 70], 4],
            ['Door',         [  5,  17, 117, 70], 4],
            ['Window',       [250,  17, 117, 70], 4],
            ['Lectern',      [ 35, 102, 117, 70], 4],
            ['Projector',    [125,  17, 117, 70], 4]
            ]
        datepos = [5, 20]
    elif courseNumber == 'P50':
        ySize = 200
        yShift = ySize/2+20
        Teams_list = [
            ['Lectern',     [200, yShift- 30, 117, 70], 4],
            ['Back Corner', [  5, yShift-115, 120, 70], 4],
            ['Back Door',   [250, yShift-115, 117, 70], 4],
            ['Front Door',  [ 35, yShift- 30, 117, 70], 4],
            ['Middle',      [125, yShift-115, 117, 70], 4]
            ]
        datepos = [5, 20]
    elif (courseNumber == 'P230' and layout == 'B'):
        print(layout)
        ySize = 350
        yShift = ySize/2+70
        Teams_list = [
            ['Door',          [ 15,  57, 120], 3],
            ['Clock',         [ 15, 142, 117], 3],
            ['Whiteboards',   [ 15, 227, 121], 4],
            ['Motion Sensor', [180,  57, 135], 3],
            ['Metal Disk',    [180, 142, 117], 3],
            ['Lectern',       [180, 227, 117], 4]
            ]
        datepos = [5, 20]
    elif courseNumber == 'P230':
        ySize = 350
        yShift = ySize/2+70
        Teams_list = [
            ['Lectern',      [200, 227, 117, 80], 5],
            ['Door',         [ 35,  57, 117, 70], 4],
            ['Window',       [200,  57, 117, 70], 4],
            ['Whiteboard',   [ 35, 227, 117, 70], 4],
            ['Center',       [125, 142, 117, 70], 4]
            ]
        datepos = [5, 20]

    # SHUFFLE STUDENTS

    student_df = pd.read_excel(studentListFile)
    student_list = list(student_df['Students'])

    print(student_list)
    print(len(student_list))

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
                (thisTeam['NumberOfThinkers']+1)*emSize+5,#thisTeam['Coords'][3],
                fill='#ffffff',stroke_width=2,stroke='black')

            groupLabel = draw.Text('Team ' + thisTeam['Name'],
                12,thisTeam['Coords'][0]+5,thisTeam['Coords'][1]+emSize*thisTeam['NumberOfThinkers']+5,fill='black')
            d.append(box)
            d.append(groupLabel)
            for iStudent_inThisTeam in range(thisTeam['NumberOfThinkers']):
                studentLabel = draw.Text(student_list[iStudent],
                    12,
                    thisTeam['Coords'][0]+5,
                    thisTeam['Coords'][1]+emSize*thisTeam['NumberOfThinkers']+5-emSize*(iStudent_inThisTeam+1),
                    fill='black')
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
