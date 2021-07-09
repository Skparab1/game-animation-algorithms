# These game animation algorithms are free to use

# the word "object" refers to the object you are animating accross the screen, for example a ball

# all these algorithms assume some set global variables: line1,line2,line3,.....,line18.  I generally use 18 lines of animated area.

# these algorithms enable the ball to move in 8 different direction: right, rightup, rightdown, left, leftup, leftdown, up, down

# defining lines as blanks, with one ball
line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = ' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,((' '*50)+'o'+(' '*49)),' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100
pos = 50

# Algorithm #1: scanning the set of lines for the ball "o" and returning the number of the line wiht the ball
def get_line_num():
    global line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
    linein = 1 if ('o' in line1 ) else (1 if ('o' in line2 ) else (2 if ('o' in line3 ) else (2 if ('o' in line4 ) else (3 if ('o' in line5 ) else (4 if ('o' in line6 ) else (5 if ('o' in line7 ) else (6 if ('o' in line8 ) else (7 if ('o' in line9 ) else (8 if ('o' in line10 ) else (9 if ('o' in line11 ) else (10 if ('o' in line12 ) else (11 if ('o' in line13 ) else (12 if ('o' in line14 ) else (13 if ('o' in line15 ) else (14 if ('o' in line16 ) else (15 if ('o' in line17 ) else 16))))))))))))))))
    return linein

# Algortihm #2: removing the ball "o" from all lines
def removeball():
    global line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1.replace('o',' '),line2.replace('o',' '),line3.replace('o',' '),line4.replace('o',' '),line5.replace('o',' '),line6.replace('o',' '),line7.replace('o',' '),line8.replace('o',' '),line9.replace('o',' '),line10.replace('o',' '),line11.replace('o',' '),line12.replace('o',' '),line13.replace('o',' '),line14.replace('o',' '),line15.replace('o',' '),line16.replace('o',' '),line17.replace('o',' '),line18.replace('o',' ')
    return line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18

# Algorithm #3: Adding the ball to a position (set by global var pos) in a line
def addball(pos,line):
    linepart1 = line[:pos-1]
    linepart2 = line[pos+1:]
    line = linepart1 + 'o ' + linepart2
    return line

# Algorithm #4: Moving a ball right
def moveright():
    global pos, line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
    numtomove = 1  #(the number of spaces you want the ball to move)
    pos += numtomove
    linenum = 1 if ('o' in line1 ) else (2 if ('o' in line2 ) else (3 if ('o' in line3 ) else (4 if ('o' in line4 ) else (5 if ('o' in line5 ) else (6 if ('o' in line6 ) else (7 if ('o' in line7 ) else (8 if ('o' in line8 ) else (9 if ('o' in line9 ) else (10 if ('o' in line10 ) else (11 if ('o' in line11 ) else (12 if ('o' in line12 ) else (13 if ('o' in line13 ) else (14 if ('o' in line14 ) else (15 if ('o' in line15 ) else (16 if ('o' in line16 ) else (17 if ('o' in line17 ) else 18))))))))))))))))
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = removeball(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addball(pos,line1) if linenum == 1 else line1),(addball(pos,line2) if linenum == 2 else line2),(addball(pos,line3) if linenum == 3 else line3),(addball(pos,line4) if linenum == 4 else line4),(addball(pos,line5) if linenum == 5 else line5),(addball(pos,line6) if linenum == 6 else line6),(addball(pos,line7) if linenum == 7 else line7),(addball(pos,line8) if linenum == 8 else line8),(addball(pos,line9) if linenum == 9 else line9),(addball(pos,line10) if linenum == 10 else line10),(addball(pos,line11) if linenum == 11 else line11),(addball(pos,line12) if linenum == 12 else line12),(addball(pos,line13) if linenum == 13 else line13),(addball(pos,line14) if linenum == 14 else line14),(addball(pos,line15) if linenum == 15 else line15),(addball(pos,line16) if linenum == 16 else line16),(addball(pos,line17) if linenum == 17 else line17),(addball(pos,line18) if linenum == 18 else line18)
    
# Algorithm #5: Moving a ball left (same as moveright, pos is -1 though)
def moveleft():
    global pos, line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
    numtomove = -1  #(the number of spaces you want the ball to move)
    pos += numtomove
    linenum = 1 if ('o' in line1 ) else (2 if ('o' in line2 ) else (3 if ('o' in line3 ) else (4 if ('o' in line4 ) else (5 if ('o' in line5 ) else (6 if ('o' in line6 ) else (7 if ('o' in line7 ) else (8 if ('o' in line8 ) else (9 if ('o' in line9 ) else (10 if ('o' in line10 ) else (11 if ('o' in line11 ) else (12 if ('o' in line12 ) else (13 if ('o' in line13 ) else (14 if ('o' in line14 ) else (15 if ('o' in line15 ) else (16 if ('o' in line16 ) else (17 if ('o' in line17 ) else 18))))))))))))))))
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = removeball(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addball(pos,line1) if linenum == 1 else line1),(addball(pos,line2) if linenum == 2 else line2),(addball(pos,line3) if linenum == 3 else line3),(addball(pos,line4) if linenum == 4 else line4),(addball(pos,line5) if linenum == 5 else line5),(addball(pos,line6) if linenum == 6 else line6),(addball(pos,line7) if linenum == 7 else line7),(addball(pos,line8) if linenum == 8 else line8),(addball(pos,line9) if linenum == 9 else line9),(addball(pos,line10) if linenum == 10 else line10),(addball(pos,line11) if linenum == 11 else line11),(addball(pos,line12) if linenum == 12 else line12),(addball(pos,line13) if linenum == 13 else line13),(addball(pos,line14) if linenum == 14 else line14),(addball(pos,line15) if linenum == 15 else line15),(addball(pos,line16) if linenum == 16 else line16),(addball(pos,line17) if linenum == 17 else line17),(addball(pos,line18) if linenum == 18 else line18)

# Algorithm #6: Moving a ball right and up diagonally
def moverightup():
    global pos, line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
    numtomove = 1  #(the number of spaces you want the ball to move)
    pos += numtomove
    linenum = 1 if ('o' in line1 ) else (2 if ('o' in line2 ) else (3 if ('o' in line3 ) else (4 if ('o' in line4 ) else (5 if ('o' in line5 ) else (6 if ('o' in line6 ) else (7 if ('o' in line7 ) else (8 if ('o' in line8 ) else (9 if ('o' in line9 ) else (10 if ('o' in line10 ) else (11 if ('o' in line11 ) else (12 if ('o' in line12 ) else (13 if ('o' in line13 ) else (14 if ('o' in line14 ) else (15 if ('o' in line15 ) else (16 if ('o' in line16 ) else (17 if ('o' in line17 ) else 18))))))))))))))))
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = removeball(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
    line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addball(pos,line2) if linenum == 1 else line2),(addball(pos,line3) if linenum == 2 else line3),(addball(pos,line4) if linenum == 3 else line4),(addball(pos,line5) if linenum == 4 else line5),(addball(pos,line6) if linenum == 5 else line6),(addball(pos,line7) if linenum == 6 else line7),(addball(pos,line8) if linenum == 7 else line8),(addball(pos,line9) if linenum == 8 else line9),(addball(pos,line10) if linenum == 9 else line10),(addball(pos,line11) if linenum == 10 else line11),(addball(pos,line12) if linenum == 11 else line12),(addball(pos,line13) if linenum == 12 else line13),(addball(pos,line14) if linenum == 13 else line14),(addball(pos,line15) if linenum == 14 else line15),(addball(pos,line16) if linenum == 15 else line16),(addball(pos,line17) if linenum == 16 else line17),(addball(pos,line18) if linenum == 17 else line18)

# Algorithm #7: Moving a ball left and up diagonally
def moveleftup():
    global pos, line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
    numtomove = -1  # (the number of spaces you want the ball to move)
    pos += numtomove
    linenum = 1 if ('o' in line1 ) else (2 if ('o' in line2 ) else (3 if ('o' in line3 ) else (4 if ('o' in line4 ) else (5 if ('o' in line5 ) else (6 if ('o' in line6 ) else (7 if ('o' in line7 ) else (8 if ('o' in line8 ) else (9 if ('o' in line9 ) else (10 if ('o' in line10 ) else (11 if ('o' in line11 ) else (12 if ('o' in line12 ) else (13 if ('o' in line13 ) else (14 if ('o' in line14 ) else (15 if ('o' in line15 ) else (16 if ('o' in line16 ) else (17 if ('o' in line17 ) else 18))))))))))))))))
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = removeball(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
    line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addball(pos,line2) if linenum == 1 else line2),(addball(pos,line3) if linenum == 2 else line3),(addball(pos,line4) if linenum == 3 else line4),(addball(pos,line5) if linenum == 4 else line5),(addball(pos,line6) if linenum == 5 else line6),(addball(pos,line7) if linenum == 6 else line7),(addball(pos,line8) if linenum == 7 else line8),(addball(pos,line9) if linenum == 8 else line9),(addball(pos,line10) if linenum == 9 else line10),(addball(pos,line11) if linenum == 10 else line11),(addball(pos,line12) if linenum == 11 else line12),(addball(pos,line13) if linenum == 12 else line13),(addball(pos,line14) if linenum == 13 else line14),(addball(pos,line15) if linenum == 14 else line15),(addball(pos,line16) if linenum == 15 else line16),(addball(pos,line17) if linenum == 16 else line17),(addball(pos,line18) if linenum == 17 else line18)

# Algorithm #8: Moving a ball right and down diagonally
def moverightdown():
    global pos, line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
    numtomove = 1  #(the number of spaces you want the ball to move)
    pos += numtomove
    linenum = 1 if ('o' in line1 ) else (2 if ('o' in line2 ) else (3 if ('o' in line3 ) else (4 if ('o' in line4 ) else (5 if ('o' in line5 ) else (6 if ('o' in line6 ) else (7 if ('o' in line7 ) else (8 if ('o' in line8 ) else (9 if ('o' in line9 ) else (10 if ('o' in line10 ) else (11 if ('o' in line11 ) else (12 if ('o' in line12 ) else (13 if ('o' in line13 ) else (14 if ('o' in line14 ) else (15 if ('o' in line15 ) else (16 if ('o' in line16 ) else (17 if ('o' in line17 ) else 18))))))))))))))))
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = removeball(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addball(pos,line1) if linenum == 2 else line1),(addball(pos,line2) if linenum == 3 else line2),(addball(pos,line3) if linenum == 4 else line3),(addball(pos,line4) if linenum == 5 else line4),(addball(pos,line5) if linenum == 6 else line5),(addball(pos,line6) if linenum == 7 else line6),(addball(pos,line7) if linenum == 8 else line7),(addball(pos,line8) if linenum == 9 else line8),(addball(pos,line9) if linenum == 10 else line9),(addball(pos,line10) if linenum == 11 else line10),(addball(pos,line11) if linenum == 12 else line11),(addball(pos,line12) if linenum == 13 else line12),(addball(pos,line13) if linenum == 14 else line13),(addball(pos,line14) if linenum == 15 else line14),(addball(pos,line15) if linenum == 16 else line15),(addball(pos,line16) if linenum == 17 else line16),(addball(pos,line17) if linenum == 18 else line17),(addball(pos,line18) if linenum == False else line18)

# Algorithm #9: Moving a ball right and down diagonally
def moveleftdown():
    global pos, line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
    numtomove = -1  #(the number of spaces you want the ball to move)
    pos += numtomove
    linenum = 1 if ('o' in line1 ) else (2 if ('o' in line2 ) else (3 if ('o' in line3 ) else (4 if ('o' in line4 ) else (5 if ('o' in line5 ) else (6 if ('o' in line6 ) else (7 if ('o' in line7 ) else (8 if ('o' in line8 ) else (9 if ('o' in line9 ) else (10 if ('o' in line10 ) else (11 if ('o' in line11 ) else (12 if ('o' in line12 ) else (13 if ('o' in line13 ) else (14 if ('o' in line14 ) else (15 if ('o' in line15 ) else (16 if ('o' in line16 ) else (17 if ('o' in line17 ) else 18))))))))))))))))
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = removeball(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addball(pos,line1) if linenum == 2 else line1),(addball(pos,line2) if linenum == 3 else line2),(addball(pos,line3) if linenum == 4 else line3),(addball(pos,line4) if linenum == 5 else line4),(addball(pos,line5) if linenum == 6 else line5),(addball(pos,line6) if linenum == 7 else line6),(addball(pos,line7) if linenum == 8 else line7),(addball(pos,line8) if linenum == 9 else line8),(addball(pos,line9) if linenum == 10 else line9),(addball(pos,line10) if linenum == 11 else line10),(addball(pos,line11) if linenum == 12 else line11),(addball(pos,line12) if linenum == 13 else line12),(addball(pos,line13) if linenum == 14 else line13),(addball(pos,line14) if linenum == 15 else line14),(addball(pos,line15) if linenum == 16 else line15),(addball(pos,line16) if linenum == 17 else line16),(addball(pos,line17) if linenum == 18 else line17),(addball(pos,line18) if linenum == False else line18)

# Algorithm #10: Moving a ball up
def moveup():
    global pos, line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
    numtomove = 0  #(the number of spaces you want the ball to move)
    pos += numtomove
    linenum = 1 if ('o' in line1 ) else (2 if ('o' in line2 ) else (3 if ('o' in line3 ) else (4 if ('o' in line4 ) else (5 if ('o' in line5 ) else (6 if ('o' in line6 ) else (7 if ('o' in line7 ) else (8 if ('o' in line8 ) else (9 if ('o' in line9 ) else (10 if ('o' in line10 ) else (11 if ('o' in line11 ) else (12 if ('o' in line12 ) else (13 if ('o' in line13 ) else (14 if ('o' in line14 ) else (15 if ('o' in line15 ) else (16 if ('o' in line16 ) else (17 if ('o' in line17 ) else 18))))))))))))))))
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = removeball(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
    line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addball(pos,line2) if linenum == 1 else line2),(addball(pos,line3) if linenum == 2 else line3),(addball(pos,line4) if linenum == 3 else line4),(addball(pos,line5) if linenum == 4 else line5),(addball(pos,line6) if linenum == 5 else line6),(addball(pos,line7) if linenum == 6 else line7),(addball(pos,line8) if linenum == 7 else line8),(addball(pos,line9) if linenum == 8 else line9),(addball(pos,line10) if linenum == 9 else line10),(addball(pos,line11) if linenum == 10 else line11),(addball(pos,line12) if linenum == 11 else line12),(addball(pos,line13) if linenum == 12 else line13),(addball(pos,line14) if linenum == 13 else line14),(addball(pos,line15) if linenum == 14 else line15),(addball(pos,line16) if linenum == 15 else line16),(addball(pos,line17) if linenum == 16 else line17),(addball(pos,line18) if linenum == 17 else line18)

# Algorithm #11: Moving a ball down
def movedown():
    global pos, line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
    numtomove = 0  #(the number of spaces you want the ball to move)
    pos += numtomove
    linenum = 1 if ('o' in line1 ) else (2 if ('o' in line2 ) else (3 if ('o' in line3 ) else (4 if ('o' in line4 ) else (5 if ('o' in line5 ) else (6 if ('o' in line6 ) else (7 if ('o' in line7 ) else (8 if ('o' in line8 ) else (9 if ('o' in line9 ) else (10 if ('o' in line10 ) else (11 if ('o' in line11 ) else (12 if ('o' in line12 ) else (13 if ('o' in line13 ) else (14 if ('o' in line14 ) else (15 if ('o' in line15 ) else (16 if ('o' in line16 ) else (17 if ('o' in line17 ) else 18))))))))))))))))
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = removeball(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addball(pos,line1) if linenum == 2 else line1),(addball(pos,line2) if linenum == 3 else line2),(addball(pos,line3) if linenum == 4 else line3),(addball(pos,line4) if linenum == 5 else line4),(addball(pos,line5) if linenum == 6 else line5),(addball(pos,line6) if linenum == 7 else line6),(addball(pos,line7) if linenum == 8 else line7),(addball(pos,line8) if linenum == 9 else line8),(addball(pos,line9) if linenum == 10 else line9),(addball(pos,line10) if linenum == 11 else line10),(addball(pos,line11) if linenum == 12 else line11),(addball(pos,line12) if linenum == 13 else line12),(addball(pos,line13) if linenum == 14 else line13),(addball(pos,line14) if linenum == 15 else line14),(addball(pos,line15) if linenum == 16 else line15),(addball(pos,line16) if linenum == 17 else line16),(addball(pos,line17) if linenum == 18 else line17),(addball(pos,line18) if linenum == False else line18)