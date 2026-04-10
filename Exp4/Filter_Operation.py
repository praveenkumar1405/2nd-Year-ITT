records = ["Arun:AI,ML,Robotics", "Bala:ML,IoT", "Chitra:AI,CyberSecurity", 
           "Divya:Robotics,IoT,AI", "Ezhil:ML,CyberSecurity", "Farah:AI,ML", 
           "Ganesh:IoT,Robotics,AI", "Hari:ML"]

# --- 1, 2, 3 & 4: Data Processing ---
student_names = set()
all_clubs = set()
student_clubs = {}

for record in records:
    name, clubs_str = record.split(":")
    club_list = clubs_str.split(",")
    club_set = set(club_list) # Automatically removes duplicates
    
    student_names.add(name)
    all_clubs.update(club_set)
    student_clubs[name] = club_set

# --- 5 & 6: Specific Membership ---
ai_and_ml = {s for s, c in student_clubs.items() if "AI" in c and "ML" in c}
ai_not_robotics = {s for s, c in student_clubs.items() if "AI" in c and "Robotics" not in c}

# --- 7: Clubs never appearing alone ---
alone_clubs = set()
for s, c in student_clubs.items():
    if len(c) == 1:
        alone_clubs.update(c)
never_alone = all_clubs - alone_clubs

# --- 8 & 9: Vowels and Consonants ---
vowels = "AEIOU"
vowel_start_clubs = [c for s, c in student_clubs.items() if s[0].upper() in vowels]
intersect_vowel = set.intersection(*vowel_start_clubs) if vowel_start_clubs else set()

consonant_end_clubs = [c for s, c in student_clubs.items() if s[-1].upper() not in vowels]
union_consonant = set().union(*consonant_end_clubs)

# --- 10, 11 & 12: Character Logic ---
all_chars = set("".join(student_names).lower())
common_chars = set.intersection(*[set(s.lower()) for s in student_names])
arun_set = set("arun")
subset_arun = {s for s in student_names if set(s.lower()).issubset(arun_set)}

# --- 13: Identical Memberships ---
club_sets_list = list(student_clubs.values())
shared_count = 0
for i in range(len(club_sets_list)):
    if club_sets_list.count(club_sets_list[i]) > 1:
        shared_count += 1

# --- 14: Sorting ---
# Sort by count (negative for descending), then by name (alphabetical)
sorted_students = sorted(student_names, key=lambda s: (-len(student_clubs[s]), s))

# --- 15: Final Filter ---
def is_prime(n):
    if n < 2: return False
    for i in range(2, n):
        if n % i == 0: return False
    return True

final_set = set()
hari_clubs = student_clubs["Hari"]

for s, c in student_clubs.items():
    # Length is prime
    cond1 = is_prime(len(s))
    # At least one club starts with a vowel (A, E, I, O, U)
    cond2 = any(club[0].upper() in vowels for club in c)
    # No common clubs with Hari
    cond3 = c.isdisjoint(hari_clubs)
    
    if cond1 and cond2 and cond3:
        final_set.add(s)

# --- Output ---
print("Students with AI & ML:", ai_and_ml)
print("Sorted Students:", sorted_students)
print("Final Filtered Set:", final_set)
