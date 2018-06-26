from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.db.models import QuerySet
from .forms import *
from .models import books, checked_out, library_cards
import datetime
import time
import inspect

'''class IndexView(generic.ListView):
    template_name = 'website_frontend/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]'''


def homepage(request):
    # if this is a POST request we need to process the form data
    return render(request, 'website_frontend/homepage.html')


def jon_library_logo(request):
    return render(request, 'website_frontend/jon_library_logo.html')


def add_book(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddBookForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            b = books(isbn=form.cleaned_data['isbn'], title=form.cleaned_data['title'],
                      author=form.cleaned_data['author'])
            b.save()
            return HttpResponse(
                '<HTML><body>hi<p>test</p><table><tr><td>a</td><td>b</td></tr><tr><td>1</td><td>1</td></tr></table>' +
                form.cleaned_data['title'] + ' was added</body></HTML>')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddBookForm()

    return render(request, 'website_frontend/add_book.html/', {'form': form})


def get_book(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':
        # create a form instance and populate it with data from the request:
        form = GetBookForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            input_type = form.cleaned_data['input_type']
            b = QuerySet
            if input_type.lower() == 'isbn':
                b = books.get_by_isbn(form.cleaned_data['input'])
            elif input_type.lower() == 'title':
                b = books.get_by_title(form.cleaned_data['input'])
            elif input_type.lower() == 'author':
                b = books.get_by_author(form.cleaned_data['input'])
            else:
                return HttpResponse('Invalid type')
            if len(b) == 0:
                return HttpResponse('No books were found')
            return get_book_result(request, b)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = GetBookForm()

    return render(request, 'website_frontend/get_book.html/', {'form': form})


def get_book_result(request, books_found):
    returnvalue = []
    for x in books_found:
        returnvalue.append(x.isbn)
    return render(request, 'website_frontend/get_book_result.html/', {'books': returnvalue, 'url': '../get_book_result_main_content/'})


def get_result_main_content(request):
    param={}
    value = request.GET.get('isbn', '')
    if value is not '':
        b =  books.get_by_isbn(value)
        returnvalue = []
        for x in b:
            returnvalue.append(x.isbn)
            returnvalue.append(x.title)
            returnvalue.append(x.author)
        param['attributes']=returnvalue
    else:
        param['attributes'] = ['No books displayed']
    return render(request, 'website_frontend/get_book_result_main_content.html/', param)


def generate_result_main_content(book=None):
    if book is None:
        return '<p id="displayedContent">No books displayed</p>'
    attributes = book.__dict__
    thislist = (a for a in attributes if not (a[0].startswith('_')))
    book_attributes = []
    for x in thislist:
        book_attributes.append(x)
    table = '<table>'
    for a in book_attributes:
        table += '<tr><td>' + book_attributes[a] + '</td></tr>'
    return table + '</table>'


def delete_book(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DeleteBookForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            if books.delete_by_isbn(form.cleaned_data['isbn']):
                return HttpResponse('Book of ISBN ' + form.cleaned_data['isbn'] + ' doesnt exist')
            return HttpResponse('Book of ISBN ' + form.cleaned_data['isbn'] + ' successfully deleted')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DeleteBookForm()

    return render(request, 'website_frontend/delete_book.html/', {'form': form})


def update_book(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UpdateBookForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            b = books.get_by_isbn(form.cleaned_data['isbn'])
            if len(b) == 0:
                return HttpResponse('Book of ISBN ' + form.cleaned_data['isbn'] + ' doesnt exist')
            b[0].title = form.cleaned_data['title']
            b[0].author = form.cleaned_data['author']
            b[0].save()
            return HttpResponse('Book of ISBN ' + form.cleaned_data['isbn'] + ' successfully updated')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UpdateBookForm()

    return render(request, 'website_frontend/update_book.html/', {'form': form})


def add_library_card(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddLibraryCardForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            b = library_cards(id=form.cleaned_data['id'], name=form.cleaned_data['name'],
                              phone_number=form.cleaned_data['phone_number'], email=form.cleaned_data['email'])
            b.save()
            return HttpResponse('hi, ' + form.cleaned_data['name'] + ' was added')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddLibraryCardForm()

    return render(request, 'website_frontend/add_library_card.html/', {'form': form})


def get_library_card(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':
        # create a form instance and populate it with data from the request:
        form = GetLibraryCardForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            input_type = form.cleaned_data['input_type']
            b = QuerySet()
            if input_type.lower() == 'id':
                b = library_cards.get_by_id(form.cleaned_data['input'])
            elif input_type.lower() == 'name':
                b = library_cards.get_by_name(form.cleaned_data['input'])
            else:
                return HttpResponse('Invalid type')
            if len(b) == 0:
                return HttpResponse('No library cards were found')
            return HttpResponse(b)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GetLibraryCardForm()

    return render(request, 'website_frontend/get_library_card.html/', {'form': form})


def delete_library_card(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DeleteLibraryCardForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            if library_cards.delete_by_id(form.cleaned_data['id']):
                return HttpResponse('Library card of ID ' + form.cleaned_data['id'] + ' doesnt exist')
            return HttpResponse('Library card of ID ' + form.cleaned_data['id'] + ' successfully deleted')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DeleteLibraryCardForm()

    return render(request, 'website_frontend/delete_library_card.html/', {'form': form})


def update_library_card(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UpdateLibraryCardForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            b = library_cards.get_by_id(form.cleaned_data['id'])
            if len(b) == 0:
                return HttpResponse('Library card of ID ' + form.cleaned_data['id'] + ' doesnt exist')
            b[0].name = form.cleaned_data['name']
            b[0].phone_number = form.cleaned_data['phone_number']
            b[0].email = form.cleaned_data['email']
            b[0].save()
            return HttpResponse('Library card of ID ' + form.cleaned_data['id'] + ' successfully updated')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UpdateLibraryCardForm()

    return render(request, 'website_frontend/update_library_card.html/', {'form': form})


def check_out_book(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddCheckedOutForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            b = books.get_by_isbn(isbn=form.cleaned_data['isbn'])
            card = library_cards.get_by_id(id=form.cleaned_data['id'])
            if len(b) == 0:
                return HttpResponse('Book with ISBN ' + form.cleaned_data['isbn'] + ' does not exist')
            if len(card) == 0:
                return HttpResponse('Library card with ID ' + form.cleaned_data['id'] + ' does not exist')
            c = checked_out(isbn=b[0], id=card[0], checked_out_date=datetime.datetime.today())
            c.save()
            return HttpResponse(
                'hi, book with ISBN ' + form.cleaned_data['isbn'] + ' was checked out by library card ' +
                form.cleaned_data['id'])

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddCheckedOutForm()

    return render(request, 'website_frontend/add_checked_out.html/', {'form': form})


def check_in_book(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DeleteCheckedOutForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            if checked_out.delete_by_isbn(form.cleaned_data['isbn']):
                return HttpResponse('Book of ISBN ' + form.cleaned_data['isbn'] + ' has not been checked out')
            return HttpResponse('hi, book with ISBN ' + form.cleaned_data['isbn'] + ' has been returned')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DeleteCheckedOutForm()

    return render(request, 'website_frontend/delete_checked_out.html/', {'form': form})


def thanks(request):
    return HttpResponse("Hello, world. You're at the thanks index.")


def bootstrap_example(request):
    return render(request, 'website_frontend/bootstrap_example.html/')