from django.db import models
from django.core.exceptions import ValidationError


class Book(models.Model):
    title = models.CharField(max_length=100)
    plot = models.TextField()
    book_format = models.CharField(
        max_length=10,
        choices=[
            ('electronic', 'Electronic'),
            ('physical', 'Physical'),
        ],
        default='physical'
    )
    word_count = models.PositiveIntegerField()
    read_time = models.IntegerField(default=0)
    amoun_of_series = models.IntegerField(default=1, max_length=2)

    MAX_WORD_COUNT = 50

    def clean(self):
        plot_word_count = len(self.plot.split())
        if plot_word_count > self.MAX_WORD_COUNT:
            raise ValidationError(f"Количество слов в сюжете не должно превышать {self.MAX_WORD_COUNT}.")

    def save(self, *args, **kwargs):
        self.clean()
        self.read_time = self.word_count // 490
        super().save(*args, **kwargs)

# Create your models here.
