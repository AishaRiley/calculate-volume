def main(): 
    f = open('speeds.txt', 'r')  # Open the input file
    fine = []
    print("Name", '\t','\t', "MPH Over", '\t', "Fine")
    print("----------------------------------------")
    for line in f:
        ##Split the record at the tab
        OffenderName, TicketedSpeed, SpeedLimit = line.split('\t')
        ##Calculate the speed over and print
        ticketedSpeed = int(TicketedSpeed)  # convert string values to integers
        speedLimit = int(SpeedLimit)
        speedOver = ticketedSpeed - speedLimit
        g = getFine(speedOver)   #function call
        for i in range(1):
            fine.append(g)
            print(OffenderName, '\t','\t', speedOver, '\t','\t', g)
        i += 1
    print(" ")
    print("There are", fine.count(65), "tickets with a 65.00 fine")
    print("There are", fine.count(85), "tickets with a 85.00 fine")
    print("There are", fine.count(120), "tickets with a 120.00 fine")
    print("There are", fine.count(150), "tickets with a 150.00 fine")
    print("There are", fine.count(200), "tickets with a 200.00 fine")
        
        
   
def getFine(speedOver):
    if speedOver > 0 and speedOver < 5:
        fine = 65
    elif speedOver >= 5 and speedOver < 10:
        fine = 85
    elif speedOver >= 10 and speedOver < 15:
        fine = 120
    elif speedOver >= 15 and speedOver < 25:
        fine = 150
    else:
        fine = 200
    return fine

    
main()
getFine(speedOver)







