from cart.context_processor import cart_total_amount
from django.shortcuts import render, redirect
from django.views.generic.base import View

from .models import Product, Order
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

from ..team.models import Team


@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/shop")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("/shop")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/shop")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("/shop")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'shop/detail_cart.html', {"total": cart_total_amount(request)})


#@login_required(login_url="users/login")
#def cart_send(request):

class SendCart(View):

    def get(self, request):
        cart = Cart(request)
        if cart.cart:
            queryset = {}
            team = Team.objects.get(id=cart.request.user.team.id)
            prod = ""
            cost = 0
            for key, value in cart.cart.items():
                prod += "id: " + str(value['product_id']) + ", " + str(value['name']) + ", Кол-во: " + str(value['quantity']) + "; \n"
                cost += value['quantity']*int(value['price'])
            if team.score - cost >= 0:
                a = Order.objects.create(
                    team=team,
                    products=prod,
                    status='В обработке'
                )

                team.score -= cost
                team.save()
                cart.clear()
                queryset['answer'] = "Покупка совершена. Остаток на счете: " + str(team.score)
            else:
                queryset['answer'] = "Недостаточно средств."
            #return redirect('/shop/cart/success')

            return render(request, 'shop/success.html', {"answer": queryset})
        return redirect('/shop')
            #return render(request, 'shop/success.html')
        #return render(request, 'shop/base.html')


class ShopView(View):

    def get(self, request):
        queryset = {}
        products = Product.objects.all()
        queryset['products'] = products
        cart = Cart(request)
        # queryset['cart'] = cart
        queryset['cart'] = []
        for el in cart.cart:
            queryset['cart'].append(cart.cart[el])
        queryset['request'] = request
        return render(request, "shop/base.html", {"products": queryset})
