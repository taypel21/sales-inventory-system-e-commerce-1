from django.shortcuts import redirect, HttpResponse


def authenticated_user(view_func):
    """
    This decorator makes sure no logged in user should be able 
    to access the registeration form or login form after been logged in.
    """
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("product_list")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    """
    This decorator restricts users according to the group they belong to
    The users can only perform certain operations they are restricted to.
    """
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponse(f"you are logged in as {request.user} and you don't have this privilege")
            return wrapper_func
        return decorator


def admin_only(view_func):
    """
    This function allows only customer users to access specific pages
    related to them. users with Admin access can't login into customers dashboards.
    """
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exits():
            group = request.user.groups.all()[0].name
            if group == "customer":
                return redirect("user-dashboard")
            else:
                return HttpResponse(f"you are not authorised to visit this page")
        return view_func(request, *args, **kwargs)
    return wrapper_func
