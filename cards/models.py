from django.db import models

# Create your models here.
from django.db import models

from ckeditor.fields import RichTextField

# the number of question boxes
NUM_BOXES = 2
# used to index from 1 instead of 0
BOXES = range(1, NUM_BOXES + 1)

class Card(models.Model):
    question = RichTextField(blank=True, null=True)
    answer = RichTextField(blank=True, null=True)
    box = models.IntegerField(
        choices=zip(BOXES, BOXES),
        default=BOXES[0],
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def move(self, solved):
        new_box = self.box + 1 if solved else BOXES[0]

        if new_box in BOXES:
            self.box = new_box
            self.save()

        return self


    def __str__(self):
        return self.question