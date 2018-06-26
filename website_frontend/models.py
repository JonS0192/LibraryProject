from django.db import models


class BetterCharField(models.CharField):
    def __init__(self, max_length, *args, **kwargs):
        self.max_length = max_length
        super(BetterCharField, self).__init__(max_length, *args, **kwargs)

    def db_type(self, connection):
        return 'char(%s)' % self.max_length


class books(models.Model):
    isbn = models.CharField(max_length=7, primary_key=True, null=False)
    title = models.CharField(max_length=50, null=False)
    author = models.CharField(max_length=30, null=False)

    def __str__(self):
        return 'ISBN: ' + self.isbn + '\nTitle: ' + self.title + '\nAuthor ' + self.author

    def get_by_isbn(isbn):
        return books.objects.filter(isbn__contains=isbn)

    def get_by_title(title):
        return books.objects.filter(title__contains=title)

    def get_by_author(author):
        return books.objects.filter(author__contains=author)

    # Returns 0 if successful, 1 if not
    def delete_by_isbn(isbn):
        b = books.objects.filter(isbn=isbn)
        if len(b) == 0:
            return 1
        b.delete()
        return 0


class library_cards(models.Model):
    id = models.CharField(max_length=7, primary_key=True, null=False)
    name = models.CharField(max_length=50, null=False)
    phone_number = models.CharField(max_length=10, null=False)
    email = models.CharField(max_length=50, null=False)

    def __str__(self):
        return 'ID: ' + self.id + '\nName: ' + self.name + '\nPhone Number: ' + self.phone_number + '\nEmail: ' + self.email

    def get_by_id(id):
        return library_cards.objects.filter(id=id)

    def get_by_name(name):
        return library_cards.objects.filter(name=name)

    # Returns 0 if successful, 1 if not
    def delete_by_id(id):
        b = library_cards.objects.filter(id=id)
        if len(b) == 0:
            return 1
        b.delete()
        return 0


class checked_out(models.Model):
    isbn = models.ForeignKey(books, primary_key=True, null=False)
    id = models.ForeignKey(library_cards, null=False)
    checked_out_date = models.DateField(null=False)

    def __str__(self):
        return 'ID: ' + self.id + '\nISBN: ' + self.isbn + '\nChecked out date: ' + self.checked_out_date

    def get_by_isbn(isbn):
        return checked_out.objects.filter(isbn=isbn)

    def delete_by_isbn(isbn):
        b = checked_out.objects.filter(isbn=isbn)
        if len(b) == 0:
            return 1
        b.delete()
        return 0
