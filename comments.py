if True:
    import datetime
    class User: pass
    status = 0
    message = 0
    current_user = 0
    text = 0
    password = 0


### Meaningful variable names > Comments ###

## Example 1 ##

# A status of 5 means sent
if status == 5: 
    message.mark_sent()

MESSAGE_SENT = 5
if status == MESSAGE_SENT:
    message.mark_sent()


## Example 2 ##

# You can update a message IF the current user is the author of the message and 
# the message was delivered less than 5 minutes ago OR if the current user is 
# an administrator
# You can also edit the message if the message wasn't delivered yet
if (message.user.id == current_user.id and 
    (message.delivered_time() == None or 
     (datetime.now() - message.delivered_time()).seconds < 300)
    ) or current_user.type == User.Administrator:

    message.update_text(text)


FIVE_MINUTES = 5 * 60
user_is_author = message.user.id == current_user.id
is_recent = (message.delivered_time() == None or
             (datetime.now() - message.delivered_time()).seconds < FIVE_MINUTES)
user_is_admin = current_user.type == User.Administrator

if (user_is_author and is_recent) or user_is_admin:
    message.update_text(text)


def can_edit_message(current_user, message):
    FIVE_MINUTES = 5 * 60
    user_is_author = message.user.id == current_user.id
    is_recent = (message.delivered_time() == None or
                 (datetime.now() - message.delivered_time()
                  ).seconds < FIVE_MINUTES)
    user_is_admin = current_user.type == User.Administrator
    return (user_is_author and is_recent) or user_is_admin

if can_edit_message(current_user, message):
    message.update_text(text)


### Comments get bugs ###

# Verify that the user's password is at least 8 characters long
if len(password) < 10:
    valid_password = False


MIN_PASSWORD_LENGTH = 10
if len(password) < MIN_PASSWORD_LENGTH:
    valid_password = False


### When to comment ###

# 1. How to use a function or class
# 2. Can't make the code clearer
# 3. Explain why you did something
# 4. References
