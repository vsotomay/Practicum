import xmlrpclib
import ast

s = xmlrpclib.ServerProxy('http://129.108.18.139:61209')

system_info = s.getSystem()


# This method calculates how much throughput is being sent through the server
def calculate_throughput():
    # The current network output
    network_out = 0

    # The current network input
    network_in = 0

    # Total traffic
    network_cx = 0

    # Traverse all the network interfaces
    for interfaces in Network_stats:
        # Traverse all the keys in each interface dictionary
        for values in interfaces:
            # print sets[values]
            try:
                # Try to parse the value as a number

                # This is transmission rate
                if values == 'tx':
                    network_out += int(interfaces[values])

                # This is receiving rate
                if values == 'rx':
                    network_in += int(interfaces[values])

                # This is the total bandwidth (in+out)
                if values == 'cx':
                    network_cx += int(interfaces[values])

            except Exception, e:
                # If it failed then it was a word, just ignore
                pass

    print "NETWORK OUT = %d bits per second" % network_out
    print "NETWORK IN = %d bits per second" % network_in
    print "NETWORK CX = %d bits per second" % network_cx


CPU_stats = ast.literal_eval(s.getCpu())
# print CPU_stats
CPU_used = CPU_stats['total']
CPU_free = CPU_stats['idle']

RAM_stats = ast.literal_eval(s.getMem())
# print RAM_stats
RAM_total = RAM_stats['total']
RAM_used = RAM_stats['used']
RAM_free = RAM_stats['available']

SWAP_stats = ast.literal_eval(s.getMemSwap())
# print SWAP_stats
SWAP_total = SWAP_stats['total']
SWAP_used = SWAP_stats['used']
SWAP_free = SWAP_stats['free']

Network_stats = ast.literal_eval(s.getNetwork())
print Network_stats
calculate_throughput()

Process_list = s.getProcessList()
print Process_list

Monitored_list = s.getAllMonitored()
print Monitored_list
