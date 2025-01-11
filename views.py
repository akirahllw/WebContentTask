from django.http import HttpResponse
from django.template import loader


# create a function
def main(request):
  template = loader.get_template('main-page.html')
  return HttpResponse(template.render())


def next_page(request):
  # Get the 'username' parameter from the request
  element = request.GET.get('element', '')  # Default to an empty string if not provided
  template = loader.get_template('next.html')
  context = {
    'element': element,
  }
  return HttpResponse(template.render(context, request))