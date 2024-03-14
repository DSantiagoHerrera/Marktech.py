from django.shortcuts import redirect

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.session.get('sesion') == 1:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('inicio')
    return wrapper

def vendedor_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.session.get('sesion') == 2:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('inicio')
    return wrapper

def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.session.get('sesion'):
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')
    return wrapper

def logout_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('sesion'):
            return view_func(request, *args, **kwargs)
        else:
            # Si la sesión está activa, eliminarla y redirigir al usuario al login
            del request.session['sesion']
            response = redirect('login')
            # Agregar cabecera Cache-Control para evitar almacenamiento en caché
            response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
            return response
    return wrapper
