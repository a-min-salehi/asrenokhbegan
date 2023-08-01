import time
seconds = time.time()
result = time.gmtime(seconds)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)
print("tm_hour:", result.tm_min)
