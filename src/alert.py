
#Function to generate alerts
def generate_alerts(suspicious_ips):

    #opening file in append mode so we can add multiple alerts in this file
    with open("output/alerts.txt", 'a') as alerts:

        for ip in suspicious_ips:
            message = f"[ALERT] Suspicious activity detected from IP: {ip}"

            print(message)              # console output for persistence of alert
            alerts.write(message + "\n")  # file output for realtime alert message