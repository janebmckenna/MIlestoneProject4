from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages

from kit.models import Product


# Create your views here.
def view_bag(request):
    """ 
    A view that returns the shopping bag contents page
    """
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
                    request, f'Added size {size.upper()} {product.name} to your bag')
        else:
            bag[item_id] = {'items_by_size':{size:quantity}}
            messages.success(
                request, f'Added size {size.upper()} {product.name} to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request, f'Updated {product.name} quantity to {bag[item_id]} in your bag')
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
                    request, f'Removed size {size.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request, f'Updated {product.name} quantity to {bag[item_id]} in your bag')
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
                request, f'Removed size {size.upper()} {product.name} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def add_subs_to_bag(request):
    """ 
    Adds Subs form to the bag in the session
    """
    if request.method =='POST':
        product = get_object_or_404(Product, pk='9')
        player_name = request.POST.get('player_name')
        team_name = request.POST.get('team')
        period = int(request.POST.get('period'))
        quantity = 1

        subs = request.session.get('subs', {})
        bag = request.session.get('bag', {})
        
        if product in list(bag.keys()):
            bag['product'] += quantity
        else:
            bag['product'] = quantity
        
        if product in list(subs.keys()):
            subs['product'].append({
                'player_name': player_name,
                'team_name': team_name,
                'period': period
            })
            messages.success(request, 'Added subs to the bag')
        else:
            subs['product'] = [{
                'player_name': player_name,
                'team_name': team_name,
                'period': period
            }]
            messages.success(request, 'Added subs to the bag')
    
        request.session['bag'] = bag
        print(bag)
        request.session['subs'] = subs
        print(subs)
        return redirect('subs')


def remove_subs_from_bag(request, item_id):
    """ 
    Removes subs from the bag
    """
    product = get_object_or_404(Product, pk=item_id)

    try:
        if 'player_name' in request.POST:
            player = request.POST['player_name']
        bag = request.session.get('bag', {})
        print(bag)

        if player:
            del bag[item_id]['player']
            messages.success(
                request, f'Removed subs from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)