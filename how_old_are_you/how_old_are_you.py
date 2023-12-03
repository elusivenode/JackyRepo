def no_of_days(y,m):
    return 365 * y + 30 * m

def no_of_sec(d):
    return 60 * 60 * 24 * d

print('Hello and welcome to jack\'s age calculator')
user_age_years, user_age_months = map(int, input('Enter your age in years and months with 1 space between (eg. 12 6): ').split())

user_age_days = no_of_days(user_age_years,user_age_months)
user_age_secs = no_of_sec(user_age_days)
print(f'You have been alive for approximately {user_age_secs:,} seconds.')