from django.shortcuts import redirect

def authorizedUsersCanView(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('authsystem:login')
    return wrapper_func