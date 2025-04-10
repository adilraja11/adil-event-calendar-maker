from huey.contrib.djhuey import task
from datetime import datetime

@task()
def logging_user_activity(user, activity):
    if user:
        log_entry = f"{datetime.now()} - {user.username} performed: {activity}"
    else:
        log_entry = f"{datetime.now()} - Anonymous performed: {activity}"
    print('=== Clicked from User/Anonymous ===')
    print(log_entry)