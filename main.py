from src.analyzer import extract_failed_ips
from src.detector import detect_bruteforce
from src.alert import generate_alerts
from config.settings import THRESHOLD


def main():
    log_file = "logs/sample.log"

    # Step 1: Extract failed login IPs
    ips = extract_failed_ips(log_file)
  

    # Step 2: Detect brute-force attacks
    suspicious_ips = detect_bruteforce(ips, THRESHOLD)
   
    # Step 3: Generate alerts
    generate_alerts(suspicious_ips)
    


if __name__ == "__main__":
    main()

