import xmlrpclib
import ast

s = xmlrpclib.ServerProxy('http://129.108.18.139:61209')

system_info = s.getSystem()


# This method calculates how much throughput is being sent through the server
def calculate_throughput():
    network_sum = 0

    # Traverse all the network interfaces
    for interfaces in Network_stats:
        for values in interfaces:
            # print sets[values]
            try:
                network_sum += int(interfaces[values])
            except Exception, e:
                pass
            # print network_sum

    print "NETWORK SUM = %d" % network_sum


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
