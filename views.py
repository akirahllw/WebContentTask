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
  element_input = request.GET.get('element').lower()
  emoji_input = request.GET.get('emojis', '').lower()

  if element_input != emoji_input:
    error_message = "The text input does not match the selected emoji!"
    return render(request, 'main-page.html', {'error_message': error_message})

  return render(request, 'next.html',{'element': element_input})

def random_image_view(request):

    element_input = request.GET.get('element', '').lower()

    images_fire = [
      static('img/azula.jpg'),
      static('img/iroh.jpg'),
      static('img/zuko.jpg'),
    ]

    images_water = [
        static('img/korra.png'),
        static('img/katara.png'),
        static('img/unalaq.png'),
    ]

    images_earth = [
        static('img/toff.png'),
        static('img/bumi.png'),
        static('img/daili.png'),
        static('img/kioshi.png'),
    ]

    images_air = [
        static('img/aang.png'),
        static('img/tenzin.png'),
        static('img/zahir.png'),
    ]

    element_images = {
        'fire': images_fire,
        'water': images_water,
        'earth': images_earth,
        'air': images_air,
    }

    images = element_images.get(element_input, images_air)

    random_image = random.choice(images)

    return render(request, 'next.html', {
        'random_image': random_image,
        'element': element_input,
    })
