import requests
from django.shortcuts import render


def user_list(request):
    page = request.GET.get('page', '1')
    
    try:
        page = int(page)
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    
    api_url = f'https://randomuser.me/api/?results=10&seed=abc&page={page}'
    
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        users = data.get('results', [])
        
        context = {
            'users': users,
            'current_page': page,
            'next_page': page + 1,
            'prev_page': page - 1 if page > 1 else None,
        }
        return render(request, 'users/lista.html', context)
    
    except requests.exceptions.RequestException:
        return render(request, 'errors/error.html')
    except ValueError:
        return render(request, 'errors/error.html')


def user_detail(request, uuid):
    page = 1
    user_found = None
    
    while page <= 100:
        api_url = f'https://randomuser.me/api/?results=10&seed=abc&page={page}'
        
        try:
            response = requests.get(api_url, timeout=10)
            response.raise_for_status()
            data = response.json()
            users = data.get('results', [])
            
            for user in users:
                if user.get('login', {}).get('uuid') == uuid:
                    user_found = user
                    break
            
            if user_found:
                break
            
            page += 1
        
        except requests.exceptions.RequestException:
            return render(request, 'errors/error.html')
        except ValueError:
            return render(request, 'errors/error.html')
    
    if user_found:
        context = {'user': user_found}
        return render(request, 'users/detalle.html', context)
    else:
        return render(request, 'errors/error.html')
