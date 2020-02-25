import csv
from datetime import datetime as dt

def read_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)

enrollments = read_csv('enrollments.csv')
project_submissions = read_csv('project_submissions.csv')
daily_engagement = read_csv('daily_engagement.csv')

def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')

def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)

# type updating for enrollments
unique_enroll_keys = set()
for enrollment in enrollments:
    unique_enroll_keys.add(enrollment['account_key'])
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
    enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
    enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
    enrollment['join_date'] = parse_date(enrollment['join_date'])

    # type updating for daily_engagement
unique_engage_keys = set()
for engagement_record in daily_engagement:
    unique_engage_keys.add(engagement_record['acct'])
    engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
    engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
    engagement_record['projects_completed'] = int(float(engagement_record['projects_completed']))
    engagement_record['total_minutes_visited'] = float(engagement_record['total_minutes_visited'])
    engagement_record['utc_date'] = parse_date(engagement_record['utc_date'])

# type updating for project_submissions
unique_subm_keys = set()
for submission in project_submissions:
    unique_subm_keys.add(submission['account_key'])
    submission['completion_date'] = parse_date(submission['completion_date'])
    submission['creation_date'] = parse_date(submission['creation_date'])


if True:
    # Contains accounts with their general information
    print("\nenrollment data:")
    print(len(enrollments))
    print(enrollments[0])
    print(len(unique_enroll_keys))

    # Contains the projects made by accounts (with account key)
    print("\nengagement data:")
    print(len(project_submissions))
    print(project_submissions[0])
    print(len(unique_subm_keys))

    # Contains information about the account on a day-by-day activety basis
    print("\ndaily records:")
    print(len(daily_engagement))
    print(daily_engagement[0])
    print(len(unique_engage_keys))
