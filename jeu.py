import scapy
messagePrinter="Message to printer"
printer=list()
line2Printer=messagePrinter
def mainSquare(message):
    line2Printer="New message for printer"
    printer=list(line2Printer)
    print(message);
mainSquare("Hello for nanosecond");
line2Printer=messagePrinter+" when print to a paper"
scapy.printMsg(line2Printer)

