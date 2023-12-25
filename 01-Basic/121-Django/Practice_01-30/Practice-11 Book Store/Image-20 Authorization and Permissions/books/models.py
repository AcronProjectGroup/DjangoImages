from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model



class Book(models.Model):
    '''
        This model create book object
        Title, Author, Description, Price, Cover or Image Cover
        for use this class:
            example:
            from django.views import generic
            class BookListView(generic.ListView):
                model = Book
                paginate_by = 4
                template_name = 'books/book_list.html'
                context_object_name = 'books'
    '''
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2) 
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])



# =============================================================================================


class Comment(models.Model):
    '''
        This model create Comment in every page you want.
        You can use it like this:
        Example:
        forms.py
            class CommentForm(forms.ModelForm):
                class Meta:
                    model = Comment
                    fields = ('text', 'recommend', ) 

        views.py
            from django.contrib.auth.decorators import login_required
            
            from .forms import CommentForm

            @login_required
            def book_detail_view(request, pk):
                # get book object
                book = get_object_or_404(Book, pk=pk)
                # get book comments
                book_comments = book.comments.all()

                if request.method == 'POST':
                    comment_form = CommentForm(request.POST)
                    if comment_form.is_valid():
                        new_comment = comment_form.save(commit=False)
                        new_comment.book = book
                        new_comment.user = request.user
                        new_comment.save()
                        comment_form = CommentForm()
                else:
                    comment_form = CommentForm()


                return render(request, 'books/book_detail.html', {
                    'book': book, 
                    'comments': book_comments,
                    'comment_form': comment_form,    
                })
    '''
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    is_active = models.BooleanField(default=True)
    recommend = models.BooleanField(default=True)



    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}: {self.text}'











