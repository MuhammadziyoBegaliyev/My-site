from django.shortcuts import render, redirect
from django.contrib import messages
from blog.models import Post
from projects.models import Project

def home(request):
    try:
        latest_posts = Post.objects.filter(is_published=True).order_by('-created_at')[:3]
        featured_projects = Project.objects.all().order_by('-created_at')[:3]
    except:
        # Agar model migratsiya qilinmagan bo'lsa
        latest_posts = []
        featured_projects = []
    
    context = {
        'latest_posts': latest_posts,
        'featured_projects': featured_projects,
    }
    return render(request, 'pages/home.html', context)

# def about(request):
#     return render(request, 'pages/about.html')

def contact(request):
    if request.method == 'POST':
        # Bu yerda email yuborish logikasi bo'ladi
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Hozircha faqat xabarni ko'rsatamiz
        messages.success(request, f"Rahmat {name}! Xabaringiz qabul qilindi. Tez orada javob beraman.")
        return redirect('contact')
    
    return render(request, 'pages/contact.html')



def home(request):
    skills = [
        {
            'name': 'Python & Django',
            'icon': 'fab fa-python',
            'percentage': 90,
            'tags': ['Django', 'Flask', 'FastAPI', 'DRF']
        },
        {
            'name': 'Frontend',
            'icon': 'fab fa-js',
            'percentage': 85,
            'tags': ['Vue.js', 'React', 'Tailwind', 'Bootstrap']
        },
        # ... boshqa skills
    ]
    return render(request, 'pages/home.html', {'skills': skills})

# views.py ichida about funksiyasiga
def about(request):
    skills = [
        {'name': 'Python', 'level': 95},
        {'name': 'Django', 'level': 90},
        {'name': 'Django REST Framework', 'level': 85},
        {'name': 'PostgreSQL', 'level': 80},
        {'name': 'HTML/CSS', 'level': 85},
        {'name': 'JavaScript', 'level': 70},
        {'name': 'Docker', 'level': 65},
        {'name': 'Git', 'level': 85},
        {'name': 'Aiogram', 'level': 75},
        {'name': 'Redis', 'level': 60},
    ]
    
    context = {
        'skills': skills,
        # ... boshqa context ma'lumotlari
    }
    return render(request, 'pages/about.html', context)