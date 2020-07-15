from django.db import models

# migration gitignore test용
class MigrationTest(models.Model):
    isIgnore = models.TextField()