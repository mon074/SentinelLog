#import  regex module
import re


#defining function to extract the failed login attempts ip addresses from log entries
def extract_failed_ips(file_path):

    #List of suspicious ip addresses
    ips = []

    #open log file as file
    with open(file_path, 'r') as file:

        #iterating each line(log entry) in log file
        for line in file:
            

            #extract ip if it is a failed login 
            if "failed password" in line.lower():
                

                #finding ips using regex pattern we get match object
                match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
               

                #if ip field is not empty 
                if match:

                    #extracting required ip from match object and add to ips list
                    ips.append(match.group())
                 

    return ips

