import random

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.templatetags.static import static

# create a function
def main(request):
  template = loader.get_template('main-page.html')
  return HttpResponse(template.render())


def next_page(request):
  template = loader.get_template('next.html')
  element_input = request.GET.get('element').lower()
  emoji_input = request.GET.get('emojis', '').lower()

  if element_input != emoji_input:
    error_message = "The text input does not match the selected emoji!"
    return render(request, 'main-page.html', {'error_message': error_message})

  return render(request, 'next.html',{'element': element_input})

def random_image_view(request):
    images = [
      static('img/azula.jpg'),
      static('img/iroh.jpg'),
      static('img/zuko.jpg'),
    ]


    random_image = random.choice(images)
    random_image_input = request.GET.get('image_input',)
    return render(request, 'next.html', {'random_image': random_image})
