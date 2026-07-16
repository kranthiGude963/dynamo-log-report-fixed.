import json
import re
from collections import Counter

def main():
    log_path = "/app/access.log"
    ips = set()
    paths = Counter()
    total_requests = 0

    # Regex to capture IP and path from Apache log lines
    log_pattern = re.compile(r'^(?P<ip>\S+).*?"(?:GET|POST) (?P<path>\S+)')

    with open(log_path) as f:
        for line in f:
            total_requests += 1
            match = log_pattern.search(line)
            if match:
                ips.add(match.group("ip"))
                paths[match.group("path")] += 1

    report = {
        "total_requests": total_requests,
        "unique_ips": len(ips),
        "top_path": paths.most_common(1)[0][0] if paths else ""
    }

    with open("/app/report.json", "w") as out:
        json.dump(report, out)

if __name__ == "__main__":
    main()
