## Instructions

You are given an Apache-style access log (`access.log`) in the working directory.  
Write a program that analyzes the traffic and produces a JSON report.

### Success Criteria
1. Count the total number of requests.  
   - The report must include a key `"total_requests"` with an integer value greater than 0.

2. Count the number of unique client IPs.  
   - The report must include a key `"unique_ips"` with an integer value greater than 0.

3. Identify the most frequently requested path.  
   - The report must include a key `"top_path"` with a non-empty string value.

### Output
- Save the results in `/app/report.json`.  
- The JSON must contain exactly these three keys:  
  - `total_requests`  
  - `unique_ips`  
  - `top_path`
