from django.shortcuts import render

# Create your views here.
MENU_ITEMS = [
    {'id': 1,'name':'Cola', 'category': 'Drinks','price': 40,'currency': 'EGP','available': True},
    {'id': 2,'name':'Orange Juice','category':'Drinks','price': 50,'currency': 'EGP','available': True},
    {'id': 3,'name':'Burger','category': 'Food','price': 120,'currency': 'EGP','available': True},
    {'id': 4,'name':'Pizza','category': 'Food','price': 150,'currency': 'EGP','available': False},
    {'id': 5,'name':'Water','category': 'Drinks','price': 10,'currency': 'EGP','available': True},
]

def search (request):

    search_query    = request.GET.get('q', '')
    category_filter = request.GET.get('category','')

    filtered_items = MENU_ITEMS.copy()

    if search_query:
        filtered_items = [
            item for item in filtered_items 
            if search_query.lower() in item['name'].lower()
        ]

    if category_filter:
        filtered_items = [
            item for item in filtered_items 
            if item['category'] == category_filter
        ]

    categories = (list(set(item['category'] for item in MENU_ITEMS))) # Unique

    context = {
        'items': filtered_items,
        'categories': categories,
        'search_query': search_query,
        'selected_category': category_filter,
    }

    return render(request, 'meals/index.html',context)