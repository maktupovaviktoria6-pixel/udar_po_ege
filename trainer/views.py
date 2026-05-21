import random
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Word

def index(request):
    if 'learned' not in request.session:
        request.session['learned'] = []
    if 'progress' not in request.session:
        request.session['progress'] = {}

    learned_ids = request.session['learned']
    available_words = Word.objects.exclude(id__in=learned_ids)
    
    if not available_words.exists():
        return render(request, 'trainer/index.html', {'all_done': True})

    word = random.choice(available_words)
    word_id_str = str(word.id)
    count = request.session['progress'].get(word_id_str, 0)
    
    return render(request, 'trainer/index.html', {
        'word': word, 
        'count': count
    })


def update_progress(request, word_id):
    word_id_str = str(word_id)
    progress = request.session.get('progress', {})
    
    current_count = progress.get(word_id_str, 0) + 1
    progress[word_id_str] = current_count
    
    if current_count >= 3:
        learned = request.session.get('learned', [])
        if word_id not in learned:
            learned.append(word_id)
            request.session['learned'] = learned
            
    request.session['progress'] = progress
    request.session.modified = True 
    return JsonResponse({'status': 'ok'})


def learned_list(request):
    learned_ids = request.session.get('learned', [])
    words = Word.objects.filter(id__in=learned_ids)
    return render(request, 'trainer/list.html', {'items': words, 'title': 'Выученные слова'})
