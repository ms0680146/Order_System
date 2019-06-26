from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from orders.models import Order, OrderItem
from django.db.models import Count, Sum
# Create your views here.

def home(request):
    return render(request, 'layout.html')

def piechart(request):
    return render(request, 'pages/piechart.html')

def cohort(request):
    return render(request, 'pages/cohort.html')

def barchart(request):
    return render(request, 'pages/barchart.html')
	
def get_shipping_data(request):
    shipping_free_count = Order.objects.filter(shipping__exact=0).count()
    shipping_total_count = Order.objects.all().count()
    labels = ['free shipping', 'need shipping']
    counts = [shipping_free_count, shipping_total_count - shipping_free_count]
    data = {
	    "labels": labels,
	    "counts": counts
    }
    return JsonResponse(data)

def get_top3_products(request):
    top3_products = OrderItem.objects.values('product_name').annotate(total=Sum('qty')).order_by('-total')[:3]
    labels = []
    counts = []
    for product in top3_products:
        labels.append(product['product_name'])
        counts.append(product['total'])
    data = {
        "labels": labels,
        "counts": counts
    }
    return JsonResponse(data)
	