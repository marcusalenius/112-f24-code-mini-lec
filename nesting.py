if True: 
    from datetime import datetime, timedelta
    class User: pass


### Inverting conditions ###

def register_user(existing_users, user):
    parts = user.split(':')
    if len(parts) == 2: 
        user_id = int(parts[0])
        if user_id >= 0:
            user_name = parts[1]
            if user_id in existing_users:
                existing_users[user_id].name = user_name
            else:
                existing_users[user_id] = User(user_id, user_name)
        else:
            print('Invalid user id:', user_id)
    else:
        print('Invalid user:', user)


def register_user(existing_users, user):
    parts = user.split(':')
    if len(parts) != 2:
        print('Invalid user:', user)
        return
    user_id = int(parts[0])
    if user_id < 0:
        print('Invalid user id:', user_id)
        return
    
    user_name = parts[1]
    if user_id in existing_users:
        existing_users[user_id].name = user_name
    else:
        existing_users[user_id] = User(user_id, user_name)

# My rule of thumb: No more than 3 levels of indentation


### Moving logic to helper functions ###

def remove_inactive_posts(users):
    six_months_ago = datetime.now() - timedelta(days=30)
    count = 0
    for user in users:
        for post in user.posts:
            if post.author == user:
                if post.latest_activity > six_months_ago:
                    user.posts.remove(post)
                    post.author = None
                    post.delete()
                    count += 1
    return count


def remove_inactive_posts(users):
    count = 0
    for user in users:
        count += remove_inactive_posts_for_user(user)
    return count

def remove_inactive_posts_for_user(user):
    six_months_ago = datetime.now() - timedelta(days=30)
    count = 0
    for post in user.posts:
        if (post.author != user or post.latest_activity <= six_months_ago):
            continue
        user.posts.remove(post)
        post.author = None
        post.delete()
        count += 1
    return count

