from django.shortcuts import render
from django.views import View
from .models import MenuItem, OrderModel

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')

class Order(View):
    def get(self, request, *args, **kwargs):
        pizza = MenuItem.objects.filter(category__name__contains='pizza')
        samosa = MenuItem.objects.filter(category__name__contains='samosa')
        burger = MenuItem.objects.filter(category__name__contains='burger')
        chocolatecoffee = MenuItem.objects.filter(category__name__contains='chocolatecoffee')

        context = {
            'pizza': pizza,
            'samosa': samosa,
            'burger': burger,
            'chocolatecoffee': chocolatecoffee,
        }

        return render(request, 'customer/order.html', context)

    def post(self, request, *args, **kwargs):

        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')

        for item in items:
            menu_item = MenuItem.objects.get(pk=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price,
            }

            order_items['items'].append(item_data)

        price = sum(item['price'] for item in order_items['items'])
        item_ids = [item['id'] for item in order_items['items']]

        order = OrderModel.objects.create(price=price)

        order.items.add(*item_ids)

        context = {
            'items': order_items['items'],
            'price': price
        }

        return render(request, 'customer/order_confirmation.html', context)
