from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort = request.GET.get('sort')

    if sort == 'name':
        result = phones.order_by('name')
    elif sort == 'min_price':
        result = phones.order_by('price')
    elif sort == 'max_price':
        result = phones.order_by('price').reverse()
    else:
        result = phones

    context = {'phones': result}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.all()

    for phone in phones:
        if slug == phone.slug:
            phone_info = phone

    context = {'phone_info': phone_info}
    return render(request, template, context)
