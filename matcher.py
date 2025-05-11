import csv

def score_sleep_time(pref1, pref2):
    sleep_order = ["Early", "Moderate", "Late"]
    diff = abs(sleep_order.index(pref1) - sleep_order.index(pref2))
    return 100 if diff == 0 else 70 if diff == 1 else 30

def score_cleanliness(c1, c2):
    diff = abs(int(c1) - int(c2))
    return 100 if diff <= 1 else 70 if diff == 2 else 30

def score_work_schedule(s1, s2):
    if s1 == s2:
        return 100
    elif "Mixed" in [s1, s2]:
        return 70
    return 30

def score_food(f1, f2):
    if f1 == f2:
        return 100
    if "Vegetarian" in [f1, f2] and "Vegan" in [f1, f2]:
        return 70
    return 30

def compute_score(p1, p2):
    scores = [
        score_sleep_time(p1["Sleep Time"], p2["Sleep Time"]),
        score_cleanliness(p1["Cleanliness"], p2["Cleanliness"]),
        score_work_schedule(p1["Work Schedule"], p2["Work Schedule"]),
        score_food(p1["Food Habits"], p2["Food Habits"])
    ]
    return sum(scores) // 4

def load_profiles(csv_path):
    with open(csv_path, newline='') as csvfile:
        return list(csv.DictReader(csvfile))

def rank_matches(user_profile, profiles):
    results = []
    for p in profiles:
        score = compute_score(user_profile, p)
        results.append((p["Name"], score))
    return sorted(results, key=lambda x: x[1], reverse=True)

# Example usage
if __name__ == "__main__":
    user = {
        "Name": "You",
        "Sleep Time": "Moderate",
        "Cleanliness": "4",
        "Work Schedule": "Day",
        "Food Habits": "Vegetarian"
    }

    profiles = load_profiles("profiles.csv")
    matches = rank_matches(user, profiles)

    for name, score in matches:
        print(f"{name}: {score}")
