""" Bag app views file """
from django.shortcuts import render, redirect


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """A view to add a quantity of the specified product to the shopping bag"""

    # Get quantity as integer and redirect URL from the form
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # Get the bag variable's content from the session, or create it as an empty
    # dictionary if doesn't exist
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
