def create_user_session(request, user):
    if (user):
        request.session['user_id'] = user.id
        request.session['username'] = user.full_name
        request.session['logged_in'] = True
        request.session['user_hash'] = user.create_user_hash()
        return True
    else:
        return False