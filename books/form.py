from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'plot', 'book_format', 'word_count', 'amoun_of_series']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'}),
            'plot': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the plot of the book'}),
            'book_format': forms.Select(attrs={'class': 'form-control'}),
            'word_count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter word count'}),
            'amoun_of_series': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the amount of series'}),
        }

    def clean_plot(self):
        plot = self.cleaned_data.get('plot')
        MAX_WORD_COUNT = 50
        plot_word_count = len(plot.split())
        if plot_word_count > MAX_WORD_COUNT:
            self.add_error('plot', f"The number of words in the story should not exceed {MAX_WORD_COUNT}. "
                                   f"Current quantity: {plot_word_count}")
        return plot

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if Book.objects.filter(title=title).exists():
            raise forms.ValidationError('A book with the same title already exists.')
        return title

