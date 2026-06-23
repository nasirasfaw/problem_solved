t = int(input())
for i in range(t):
  rating = int(input())
  if rating >= 1900:
    division = "Division 1"
  elif 1600 <= rating and rating <= 1899:
      division = "Division 2"
  elif 1400 <= rating and rating <= 1599:
      division = "Division 3"
  elif rating <= 1399:
      division = "Division 4"
 
  print(division)
