
#Function to detetct brute force attempt
def detect_bruteforce(ips, threshold):

    #list of suspicious ips
    sus = []

    #Number of times each ip tried to login
    freq = {}


    for ip in ips:
        if ip in freq:
            freq[ip] += 1
        else:
            freq[ip] = 1

        # if frequency is equal to the threshold 
        if freq[ip] == threshold:

            # this ip might be trying to brute force
            sus.append(ip)

    return sus