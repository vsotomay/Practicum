import DB_search
import ast


workshops = DB_search.WS_collection.find()
# DB_search.print_WS()
# Create as many files as there are workshops
for document in workshops:
    wsu_num = document['num_ws_units']

    # Get the first letters of each word in the workshop name
    WS_name = document['name']
    abbreviation = ""
    for i in WS_name.upper().split():
        abbreviation += i[0]

    # print abbreviation
    file_name = abbreviation + "_upstream.conf"
    # print file_name

    # Create file with writing permissions
    # (this will overwite any files that are named the same)
    conf_file = open(file_name, 'w')

    # Counting the #of workshop units
    count = 0
    while (count < wsu_num):

        # Get the workshop unit by index
        temp = document['ws_units'][count]
        WS_unit = DB_search.search_DB_by_ID(temp)

        # Counting the #of ip's in this workshop unit
        count_1 = 0
        try:
            ip_list = WS_unit['ip_addresses']
            # print ip_list
            ip_count = len(WS_unit['ip_addresses'])
            while (count_1 < ip_count):
                WS_ip = ip_list[count_1]
                conf_file.write('upstream '+abbreviation+''+str(count)+'-'+str(count_1)+'{\n'
                '\t server '+WS_ip+';\n'
                '}\n')
                count_1 += 1
        except Exception, e:
            print "This workshop unit has no IPs...?"
            # print str(e)

        # print 'COUNT: %i' % count
        count += 1

# print Workshops
