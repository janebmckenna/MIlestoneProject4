from decimal import Decimal
from django.conf import settings
from  django.shortcuts import get_object_or_404
from kit.models import Product


def bag_contents(request):
    
    bag_items = []
    total = 0
    product_count = 0
    subs_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if 'subs' in item_data:  # Handle subscriptions
            for sub in item_data['subs']:
                subs_count += sub['quantity']
                total += sub['period'] * 50  
                sub_price = sub['period'] * 50
                bag_items.append({
                    'item_id': item_id,
                    'player_name': sub['player_name'],
                    'team_name': sub['team_name'],
                    'period': sub['period'],
                    'price': sub_price,
                    'quantity': 1
                })
        else:
            product = get_object_or_404(Product, pk=item_id)
            if isinstance(item_data, int):
                total += item_data * product.price
                product_count += item_data
                bag_items.append({
                    'item_id' :item_id,
                    'quantity' : item_data,
                    'product' : product,
                })
            else:
                product = get_object_or_404(Product, pk=item_id)
                for size, quantity in item_data['items_by_size'].items():
                    total += quantity * product.price
                    product_count += quantity
                    bag_items.append({
                    'item_id' :item_id,
                    'quantity' : quantity,
                    'product' : product,
                    'size' : size,
                    })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total

    context = {
        'bag_items' : bag_items,
        'total' : total,
        'product_count' : product_count,
        'subs_count': subs_count,
        'delivery' : delivery,
        'free_delivery_delta' : free_delivery_delta,
        'free_delivery_threshold' : settings.FREE_DELIVERY_THRESHOLD,
        'grand_total' : grand_total,
        'total': 0,
    }

    return context