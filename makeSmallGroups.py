def makeSmallGroups():

    import random
    import os
    import sys
    import xlsxwriter
    import pandas as pd
    import drawsvg as draw
    from datetime import date

    from cairosvg import svg2png


    # Get command-line arguments
    if len(sys.argv)>1:
        courseNumber = sys.argv[1]
    else:
        courseNumber = 'M227C'

    emSize = 12 # font size in pixels

    layout = 'A' 
    # layout = 'B' 

    #print((courseNumber == 'P230' and layout == 'B'))

    # coordinate system: (0,0) is top left corner
    # positive x is to the right, positive y is down.
    # rectangle positions are specified by bottom left corner

    studentListFile = 'studentList_' + courseNumber + '.xlsx'
    if courseNumber == 'M227C' and layout == 'A':
        ySize = 100
        x_shift = 90
        Teams_list = [
            ['Lectern', [ 17+0*x_shift, 17, 80, 70], 4],
            ['B',       [ 17+1*x_shift, 17, 80, 70], 4],
            ['Projector',       [ 17+2*x_shift, 17, 80, 70], 4],
            ['Green Board',    [ 17+3*x_shift, 17, 80, 70], 3]#,
            #['Projector',    [125,  17, 117, 70], 3]
            ]
        datepos = [5, 10]
    if courseNumber == 'M227C' and layout == 'B':
        ySize = 200
        Teams_list = [
            ['LB40',   [200, 102, 117, 70], 3],
            ['Door',    [ 35,  17, 117, 70], 3],
            ['Lectern',[200,  17, 117, 70], 4],
            ['Lookers Right',      [ 35, 102, 117, 70], 3]#,
            #['Projector',    [125,  17, 117, 70], 3]
            ]
        datepos = [5, 10]
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
        ySize = 400
        yShift = ySize/2+70 # depracted
        Teams_list = [
            ['Door',          [ 15,  350-57, 120], 4],
            ['Clock',         [ 15, 350-142, 117], 3],
            ['Whiteboards',   [ 15, 350-227, 121], 4],
            ['Motion Sensor', [180, 350- 57, 135], 4],
            ['Metal Disk',    [180, 350-142, 117], 4],
            ['Lectern',       [180,350- 227, 117], 4]
            ]
        datepos = [5, 100]
    elif courseNumber == 'P230':
        ySize = 260
        Teams_list = [
            ['Whiteboards', [ 35,  57, 117, 70], 3],
            ['Lectern',     [200,  57, 117, 70], 3],
            ['Door',        [ 35, 160, 117, 70], 3],
            ['Window',      [200, 160, 117, 80], 4],
            ]
        datepos = [5, emSize+5]
    # elif courseNumber == 'P230':
    #     ySize = 350
    #     yShift = ySize/2+70 # depracted
    #     Teams_list = [
    #         ['Lectern',      [200, 227, 117, 80], 4],
    #         ['Door',         [ 35,  57, 117, 70], 4],
    #         ['Window',       [200,  57, 117, 70], 4],
    #         ['Whiteboard',   [ 35, 227, 117, 70], 4],
    #         ['Center',       [125, 142, 117, 70], 4]
    #         ]
    #     datepos = [5, 0]

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


    if len(sys.argv)>2 and sys.argv[2]=="open":
        print('Open seating')
        d.append(draw.Text("OPEN SEATING TODAY", 12, datepos[0], datepos[1]+emSize+15, fill='black'))

    else:
        iStudent = 0
        for iTeam, thisTeam in Teams.iterrows():
            if iStudent < len(student_list):
                box = draw.Rectangle(
                    thisTeam['Coords'][0],
                    thisTeam['Coords'][1],
                    thisTeam['Coords'][2],
                    (thisTeam['NumberOfThinkers']+1)*emSize+15,
                    fill='#ffffff',stroke_width=2,stroke='black')

                groupLabel = draw.Text('Team ' + thisTeam['Name'],
                    12,thisTeam['Coords'][0]+5,
                    thisTeam['Coords'][1]+emSize+5,
                    fill='black')
                d.append(box)
                d.append(groupLabel)
                for iStudent_inThisTeam in range(thisTeam['NumberOfThinkers']):
                    studentLabel = draw.Text(student_list[iStudent],
                        12,
                        thisTeam['Coords'][0]+5,
                        thisTeam['Coords'][1]+emSize+5+emSize*(iStudent_inThisTeam+1),
                        fill='black')
                    iStudent = iStudent + 1
                    d.append(studentLabel)
                    if iStudent >= len(student_list):
                        break
   
    d.append(draw.Text(datestr, 12, datepos[0], datepos[1], fill='black'))

    d.save_svg('teams_' + courseNumber + '.svg')

    #os.system('/Applications/Inkscape.app/Contents/MacOS/inkscape teams_' + courseNumber + '.svg -o teams_' + courseNumber + '.png')

    # with open('teams_' + courseNumber + '.svg', 'rb') as f:
    #     svg2png(file_obj=f, write_to='teams_' + courseNumber + '.png', background_color="white")

    if courseNumber=='M227C':
         os.system('./sendToGithub.sh')

if __name__ == '__main__':
    makeSmallGroups()
