import pyfirmata
import time

board = pyfirmata.Arduino('COM4')
a5 = board.get_pin('a:5:i')

def s(t):
    board.digital[11].write(1)
    time.sleep(t)
    board.digital[11].write(0)

    board.digital[10].write(1)
    time.sleep(t)
    board.digital[10].write(0)

    board.digital[9].write(1)
    time.sleep(t)
    board.digital[9].write(0)

    board.digital[8].write(1)
    time.sleep(t)
    board.digital[8].write(0)

it = pyfirmata.util.Iterator(board)
it.start()
while True:
    ti = a5.read()
    print(ti)
    if ti != None:
        s(ti/10)
