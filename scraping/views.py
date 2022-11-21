from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from .forms import AddProductLinkForm
from .models import Product
# Create your views here.


class IndexView(View):
    template_name = "index.html"
    no_discounter = 0
    error = None
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        products_count = products.count()
        no_products_discounted = 0
        if products_count > 0:
            products_discounted = []
            for product in products:
                if product.old_current_price > product.current_price:
                    products_discounted.append(product)
                no_products_discounted = len(products_discounted)
        form = AddProductLinkForm()

        context = {
            'form':form,
            'products':products,
            'products_count':products_count,
            'no_products_discounted':no_products_discounted,
        }
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        if "add" in request.POST:
            form = AddProductLinkForm(request.POST)
            try:
                if form.is_valid():
                    form.save()
                    messages.success(request, "Product Added Successfully to the tracker")
                    return redirect("scraping:index")
            except AttributeError:
                self.error = "Ups... couldn't get the name or price"
            except:
                self.error = "Ups... something went wrong"

            form = AddProductLinkForm()
            context = {
                'form':form,
            }
            return render(request, self.template_name, context=context)
        if "delete" in request.POST:
            pk = request.POST.get('pk')
            print(pk)
            getProduct = get_object_or_404(Product, id=pk)
            getProduct.delete()
            messages.success(request, "Product deleted Successfully from the tracker")
            return redirect("scraping:index")


def update_prices(request):
    products = Product.objects.all()
    for product in products:
        product.save()
        return redirect("scraping:index")