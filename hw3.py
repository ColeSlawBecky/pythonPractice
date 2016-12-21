# hw3.py due 9/28/2016
# Becky Jacob

# Problem 1
def displayFractions( n ):
    'Display fractions for 2/n,3/n,... n/n.'
    for i in range(2, n+1):
        dec = i/n
        print(('{0}/{1}={2:.4f}, '.format(i, n, dec)),end='') #the instructions said use a comma, but the example used a semi-colon, so I went with comma. 
        
'''
>>> displayFractions ( 6 )
2/6=0.3333, 3/6=0.5000, 4/6=0.6667, 5/6=0.8333, 6/6=1.0000,
'''

#Problem 2
def avgScore( fname ):
    '''Writes to 'output.txt' all students names (first letter capital, the rest lower),
followed by a numeric list of their grades, and finally their calculated average score.''' 
    infile = open( fname, 'r')
    listLines = infile.readlines()
    infile.close

    listLines.sort()
    
    outfile = open ( 'output.txt', 'w')
    for line in listLines:
        strippedLine = line.strip()
        splitLine = strippedLine.split(sep=',')
        name = (splitLine[0])
        scores = splitLine[1:]
        numScores = [int(i) for i in scores]
        avgScore = (sum(numScores)/len(numScores))
        outfile.write('{}: {}, avg score = {}\n'.format(name.capitalize(), numScores, avgScore))
    outfile.close()

'''
>>> avgScore('scores.txt')
Albright: [91, 76, 89, 81, 89, 86, 94, 79], avg score = 85.625
Barnard: [74, 75, 81, 95, 73, 92, 95, 94], avg score = 84.875
Boswell: [81, 75, 85, 73, 84, 76, 96, 98], avg score = 83.5
Brantley: [91, 89, 73, 92, 70, 95, 92, 85], avg score = 85.875
Connolly: [100, 80, 74, 76, 82, 96, 90, 77], avg score = 84.375
Daly: [75, 88, 99, 91, 89, 82, 70, 90], avg score = 85.5
Edmonds: [87, 73, 89, 96, 78, 96, 98, 96], avg score = 89.125
Hargrove: [77, 95, 76, 87, 94, 96, 83, 94], avg score = 87.75
Inman: [81, 92, 76, 85, 83, 82, 88, 96], avg score = 85.375
Kenney: [88, 98, 71, 97, 95, 73, 86, 70], avg score = 84.75
Land: [98, 72, 95, 89, 95, 100, 76, 71], avg score = 87.0
Lund: [96, 100, 90, 84, 93, 97, 100, 76], avg score = 92.0
Muller: [88, 100, 94, 75, 80, 86, 98, 71], avg score = 86.5
Murdock: [86, 98, 82, 97, 75, 77, 76, 98], avg score = 86.125
Padgett: [85, 93, 95, 86, 82, 90, 71, 100], avg score = 87.75
Pierre: [84, 97, 82, 89, 72, 77, 85, 87], avg score = 84.125
Quintana: [75, 83, 89, 98, 78, 75, 89, 96], avg score = 85.375
Quintero: [90, 78, 96, 100, 76, 100, 81, 79], avg score = 87.5
Simons: [70, 70, 72, 70, 94, 89, 74, 89], avg score = 78.5
Villegas: [88, 84, 88, 96, 81, 72, 82, 86], avg score = 84.625
'''
