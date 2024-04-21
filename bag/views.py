from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages

from kit.models import Product


def view_bag(request):
    """
    A view that returns the shopping bag contents page
    """
    bag = request.session.get('bag', {})
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Adds the specified quantity of an item to the bag
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request, f'''
                    Updated size {size.upper()} {product.name}
                    quantity to {bag[item_id]["items_by_size"][size]}
                    ''')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request, f'''
                    Added size {size.upper()} {product.name} to your bag
                    ''')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request, f'''
                Added size {size.upper()} {product.name} to your bag''')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request, f'''
                Updated {product.name} quantity
                to {bag[item_id]} in your bag''')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Changes the specified quantity of an item to the bag
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(
                    request, f'''
                    Updated size {size.upper()} {product.name}
                    quantity to {bag[item_id]["items_by_size"][size]}
                    ''')
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
                messages.success(
                    request, f'''Removed size {size.upper()}
                    {product.name} from your bag''')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request, f'''Updated {product.name}
                quantity to {bag[item_id]} in your bag''')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """
    Removes an item to the bag
    """

    product = get_object_or_404(Product, pk=item_id)

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(
                request, f'''Removed size {size.upper()}
                {product.name} from your bag''')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def add_subs_to_bag(request, item_id):
    """
    Adds Subs form to the bag in the session
    """

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        player_name = request.POST.get('player_name')
        team_name = request.POST.get('team')
        period = int(request.POST.get('period'))
        bag = request.session.get('bag', {})

        if item_id in list(bag.keys()):
            bag[item_id]['subs'].append({
                'player_name': player_name,
                'team_name': team_name,
                'period': period,
                'quantity': quantity
            })
            messages.success(request, 'Added subs to the bag')
        else:
            bag[item_id] = {'subs': [{
                'player_name': player_name,
                'team_name': team_name,
                'period': period,
                'quantity': quantity
            }]}
            messages.success(request, 'Added Subs to your bag')

        request.session['bag'] = bag
        return redirect('subs')


def remove_subs_from_bag(request, item_id):
    """
    Removes subs from the bag
    """
    try:
        player_name = request.POST.get('player_name')
        bag = request.session.get('bag', {})

        for sub in bag[item_id]['subs']:
            if sub.get('player_name') == player_name:
                bag[item_id]['subs'].remove(sub)
                request.session['bag'] = bag
                return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing subs {e}')
        return HttpResponse(status=500)
