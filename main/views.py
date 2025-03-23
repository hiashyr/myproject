from django.shortcuts import render
import os

def index(request):
    plants = [
        {
            "name": "Фикус",
            "image": "images/ficus.jpg",
            "params_list": ["Свет: яркий", "Полив: умеренный", "Температура: 18-24°C"],
            "params_dict": {
                "Освещение": "яркий свет",
                "Полив": "умеренный",
                "Влажность": "средняя"
            },
            "show": True
        },
        {
            "name": "Кактус",
            "image": "images/cactus.jpg",
            "params_list": ["Свет: прямой", "Полив: редкий", "Температура: 20-30°C"],
            "params_dict": {
                "Освещение": "прямой свет",
                "Полив": "редкий",
                "Влажность": "низкая"
            },
            "show": True
        },
        {
            "name": "Монстера",
            "image": "images/monstera.jpg",
            "params_list": ["Свет: рассеянный", "Полив: обильный", "Температура: 20-25°C"],
            "params_dict": {
                "Освещение": "рассеянный свет",
                "Полив": "обильный",
                "Влажность": "высокая"
            },
            "show": True
        }
    ]

    file_content = None
    if request.method == 'POST':
        filename = request.POST.get('filename')
        file_path = os.path.join(os.path.dirname(__file__), '..', 'static', 'files', filename)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
        except FileNotFoundError:
            file_content = "Файл не найден."
        except Exception as e:
            file_content = f"Ошибка при чтении файла: {e}"

    context = {
        "page_name": "База знаний о домашних растениях",
        "plants": plants,
        "file_content": file_content
    }
    return render(request, 'index.html', context)

def about(request):
    # Статистика проекта
    project_stats = {
        "total_plants": 3,  # Количество растений
        "creation_date": "10.03.2025",  # Дата создания
        "author": "Шлимаков Владимир Александрович",  # Автор проекта
    }

    # Передаем данные в шаблон
    context = {
        "page_name": "О проекте",
        "project_stats": project_stats,  # Добавляем статистику проекта
    }
    return render(request, 'about.html', context)

def tips(request):
    return render(request, 'tips.html')

def plants(request):
    return render(request, './plants.html')