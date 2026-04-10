print("Student Attendance Analysis")
print("================================")
D1 = {101, 102, 103, 104} 
D2 = {103, 104, 105, 106}  

both_days = D1 & (D2)  
either_day = D1 | D2  
absent_D2 = D1 - D2 

print("Present on both days:", both_days)
print("Present on either day:", either_day)
print("Absent on second day:", absent_D2)

print("=================================")
print(" Course Interests of Two Users")

P1 = {"Python", "Data Science", "Machine Learning"}  
P2 = {"Data Science", "AI", "Cloud Computing"}       

common = P1 & (P2)      
suggestions = P2 - P1   

print("Common interests:", common)
print("Suggestions for user1:", suggestions)

print("===================================")
print(" Online Store Products")

available = {"lap", "phone", "tablet", "monitor"}  
sold = {"phone", "monitor"}                           

stock = available - sold  
sold_out = available &  (sold)  

print("Products in stock:", stock)
print("Products sold out:", sold_out)

print("====================================")

print(" IP Address Analysis")

L = {"192.168.1.1", "192.168.1.2","192.168.1.8"}  
F = {"192.168.1.2", "192.168.1.4","192.168.1.5"} 
B = {"192.168.1.5", "192.168.1.6"}                 

both_not_blacklisted = (L & (F)) - B  
attempted_not_succeeded = F - L      
only_blacklisted = B - (L | F)     

print("IPs in both success and fail, not blacklisted:", both_not_blacklisted)
print("IPs attempted but not succeeded:", attempted_not_succeeded)
print("Only blacklisted IPs:", only_blacklisted)

print("======================================")

print("Skills Matching")

required_skills = {"Python", "SQL", "Machine Learning", "Communication"}  
applicant_skills = {"Python", "Communication", "HTML"}                   
outdated_skills = {"SQL"}                                                

missing_skills = (required_skills - applicant_skills) - outdated_skills  

print("Missing required skills (excluding outdated):", missing_skills)
print("========================================")
