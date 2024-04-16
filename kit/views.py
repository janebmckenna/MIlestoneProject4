from django.shortcuts import (
    render, redirect, reverse, get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Product, Category
from .forms import ProductForm, CategoryForm


def all_products(request):
    """ 
    A view to show all products page
    """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search parameters!")
                return redirect(reverse('kit'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
    
    current_sorting = f'{sort}_{direction}'

    context = {
        "products" : products,
        'search_term' : query,
        'current_categories' : categories,
    }
    return render(request, 'kit/products.html', context)


def product_detail(request, product_id):
    """ 
    A view to show individual product detail page
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        "product" : product,
    }
    return render(request, 'kit/product_detail.html', context)


@login_required
def add_product(request):
    """ 
    Add a product to the shop
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry. This action requires club admin access')
        return redirect(reverse('home'))

    on_admin_page = True 

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Product has not been added. Please check the form is valid')
    else:
        form = ProductForm()
    template = 'kit/add_product.html'
    context ={
        'form': form,
        'on_admin_page': on_admin_page,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ 
    Edit an exisiting product
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry. This action requires club admin access')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES,  instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'{product.name} successfully updated')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Product has not been updated, please check form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'kit/edit_product.html'
    context ={
        'form': form,
        'product': product,
        'on_admin_page': True,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ 
    Delete an exisiting product
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry. This action requires club admin access')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product has been deleted!')

    return redirect(reverse('edit_delete_admin'))


@login_required
def add_category(request):
    """ 
    Add a Product category
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry. This action requires club admin access')
        return redirect(reverse('home'))

    on_admin_page = True 

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save()
            messages.success(request, 'Category added successfully!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Category has not been added. Please check the form is valid')
    else:
        form = CategoryForm()
    template = 'kit/add_category.html'
    context ={
        'form': form,
        'on_admin_page': on_admin_page,
    }

    return render(request, template, context)


@login_required
def delete_category(request, category_id):
    """ 
    Delete an exisiting category
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry. This action requires club admin access')
        return redirect(reverse('home'))

    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    messages.success(request, 'Category has been deleted!')

    return redirect(reverse('manage_categories'))


@login_required
def edit_category(request, category_id):
    """ 
    Edit an exisiting category
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry. This action requires club admin access')
        return redirect(reverse('home'))

    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES,  instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, f'{category.name} successfully updated')
            return redirect(reverse('manage_categories'))
        else:
            messages.error(request, 'Category has not been updated, please check form is valid.')
    else:
        form = CategoryForm(instance=category)
        messages.info(request, f'You are editing {category.name}')

    template = 'kit/edit_category.html'
    context ={
        'form': form,
        'category': category,
        'on_admin_page': True,
    }

    return render(request, template, context)