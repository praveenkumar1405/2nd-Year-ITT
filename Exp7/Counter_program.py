# ===============================
# Counter Programs
# ===============================


# ===============================
# 1. Counter  Unique Elements
# Given a list:
# nums = [5,3,5,2,3,1,4,1,2]
# Print numbers that appear only once using Counter
# ===============================
from collections import Counter, defaultdict, OrderedDict, deque, namedtuple, ChainMap
from datetime import datetime, timedelta
import calendar

nums = [5,3,5,2,3,1,4,1,2]
count = Counter(nums)
print([num for num in count if count[num] == 1])


# ===============================
# 2. Counter  Equal Frequency
# Given a string:
# s = "aabbccddeeffgg"
# Check whether all characters occur same number of times
# ===============================
s = "aabbccddeeffgg"
freq = Counter(s)
print(len(set(freq.values())) == 1)


# ===============================
# 3. Counter Find Missing Numbers
# list1 = [1,2,3,4,5]
# list2 = [1,2,2,3,4,4,5]
# Find elements that occur extra times in list2
# ===============================
list1 = [1,2,3,4,5]
list2 = [1,2,2,3,4,4,5]
print(list((Counter(list2) - Counter(list1)).elements()))


# ===============================
# 4. defaultdict – Word Length Grouping
# words = ["python","java","go","c","ruby","php"]
# Group words based on their length
# ===============================
words = ["python","java","go","c","ruby","php"]
d = defaultdict(list)
for word in words:
    d[len(word)].append(word)
print(dict(d))


# ===============================
# 5. defaultdict – Student Marks
# data = [("Alice",85),("Bob",78),("Alice",92),("Bob",88)]
# Store all marks for each student
# ===============================
data = [("Alice",85),("Bob",78),("Alice",92),("Bob",88)]
d = defaultdict(list)
for name, marks in data:
    d[name].append(marks)
print(dict(d))


# ===============================
# 6. OrderedDict – First Non-Repeating Character
# s = "swiss"
# Find first non-repeating character
# ===============================
s = "swiss"
od = OrderedDict()
for ch in s:
    od[ch] = od.get(ch, 0) + 1
for ch in od:
    if od[ch] == 1:
        print(ch)
        break


# ===============================
# 7. deque – Sliding Window Sum
# nums = [1,2,3,4,5,6], window = 3
# ===============================
nums = [1,2,3,4,5,6]
k = 3
dq = deque(nums[:k])
print(sum(dq))
for i in range(k, len(nums)):
    dq.popleft()
    dq.append(nums[i])
    print(sum(dq))


# ===============================
# 8. deque – Check Palindrome
# Input: "level"
# ===============================
s = "level"
dq = deque(s)
is_palindrome = True
while len(dq) > 1:
    if dq.popleft() != dq.pop():
        is_palindrome = False
        break
print("Palindrome" if is_palindrome else "Not Palindrome")


# ===============================
# 9. namedtuple Highest Salary
# Create Employee(name, salary) and print highest
# ===============================
Employee = namedtuple("Employee", ["name", "salary"])
emps = [Employee("A",5000), Employee("B",7000), Employee("C",6000)]
print(max(emps, key=lambda x: x.salary))


# ===============================
# 10. ChainMap – Combine Dictionaries
# d1 = {"a":10,"b":20}
# d2 = {"b":30,"c":40}
# Find value of key 'b'
# ===============================
d1 = {"a":10,"b":20}
d2 = {"b":30,"c":40}
cm = ChainMap(d1, d2)
print(cm["b"])


# ===============================
# 11. Leap Year Check (2028)
# ===============================
year = 2028
print(calendar.isleap(year))


# ===============================
# 12. Current Date Format

now = datetime.now()
print(now.strftime("%d-%B-%Y %A"))


# ===============================
# 13. Week Number of Date (2026-03-10)

date = datetime.strptime("2026-03-10", "%Y-%m-%d")
print(date.strftime("%U"))


# ===============================
# 14. Difference in Seconds
# ===============================
t1 = datetime.strptime("2026-03-10 10:00:00", "%Y-%m-%d %H:%M:%S")
t2 = datetime.strptime("2026-03-10 12:30:00", "%Y-%m-%d %H:%M:%S")
print(int((t2 - t1).total_seconds()))


# ===============================
# 15. Next 5 Days
# ===============================
today = datetime.now()
for i in range(1, 6):
    print((today + timedelta(days=i)).date())


# ===============================
# 16. Previous Month Same Date
# ===============================
date = datetime.strptime("2026-03-10", "%Y-%m-%d")
prev_month = date.replace(day=1) - timedelta(days=1)
print(prev_month.replace(day=date.day))


# ===============================
# 17. Count Sundays in January 2025
# ===============================
year, month = 2025, 1
count = 0
for day in range(1, calendar.monthrange(year, month)[1] + 1):
    if datetime(year, month, day).weekday() == 6:
        count += 1
print(count)


# ===============================
# 18. Detect Weekend (2026-03-14)
# ===============================
date = datetime.strptime("2026-03-14", "%Y-%m-%d")
print("Weekend" if date.weekday() >= 5 else "Weekday")


# ===============================
# 19. Daily Login Counter
# ===============================
logins = [
    "2026-03-10 10:00",
    "2026-03-10 12:00",
    "2026-03-11 09:30",
    "2026-03-11 11:45",
    "2026-03-11 14:00"
]
dates = [datetime.strptime(l, "%Y-%m-%d %H:%M").date() for l in logins]
print(Counter(dates))


# ===============================
# 20. Most Frequent Login Hour
# ===============================
hours = [datetime.strptime(l, "%Y-%m-%d %H:%M").hour for l in logins]
print(Counter(hours).most_common(1))


# ===============================
# 21. Monthly Event Counter
# ===============================
events = [
    "2025-01-10",
    "2025-01-20",
    "2025-02-05",
    "2025-02-15",
    "2025-03-01"
]
months = [datetime.strptime(e, "%Y-%m-%d").month for e in events]
print(Counter(months))


# ===============================
# 22. Group Dates by Weekday
# ===============================
dates = [datetime.strptime(e, "%Y-%m-%d") for e in events]
d = defaultdict(list)
for dt in dates:
    d[dt.strftime("%A")].append(dt.date())
print(dict(d))


# ===============================
# 23. Find Oldest Date
# ===============================
print(min(dates))


# ===============================
# 24. Detect Duplicate Dates
# ===============================
print([date for date, cnt in Counter(events).items() if cnt > 1])


# ===============================
# 25. Recent Activity Tracker (last 24 hours)
# ===============================
now = datetime.now()
recent = [l for l in logins if now - datetime.strptime(l, "%Y-%m-%d %H:%M") <= timedelta(days=1)]
print(recent)
