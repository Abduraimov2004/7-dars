from django.db import models
from django.contrib.auth.models import AbstractUser, User
# Create your models here.


class User(AbstractUser):
    phone = models.CharField(max_length=13, blank=True, unique=True, db_index=True, null=True)
    auth_code = models.CharField(max_length=6, blank=True) 

    # def get_absolute_url(self):
    #     print(self)
    #     return reverse("main:account", kwargs={"id": self.id})


    def __str__(self) -> str:
        return f"{self.username}"
    


class Category(models.Model):
    title = models.CharField(max_length=15)

    def __str__(self) -> str:
        return f"{self.title}"


class Tag(models.Model):
    title = models.CharField(max_length=15)

    def __str__(self) -> str:
        return f"{self.title}"
    


class Course(models.Model):
    LANGUAGES = (
        ('uz', 'O\'zbekcha'),
        ('ru', 'Ruscha'),
        ('en', 'Inglizcha'),
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField()
    duration = models.DurationField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2) # 100.00
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="courses")
    created_at = models.DateTimeField(verbose_name="Boshlanish vaqti", null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilanish vaqti", null=True, blank=True)
    language = models.CharField(max_length=100, blank=True, choices=LANGUAGES)
    rating = models.PositiveBigIntegerField(verbose_name="Rating", default=0)
    image = models.ImageField(upload_to="images", blank=True)
    tags = models.ManyToManyField(Tag, verbose_name="tags", )

    class Meta:
        ordering = ['-rating']


# -------------------------------------------------------------------

class Header(models.Model):
    message = models.CharField(max_length=150)
    facebook = models.CharField(max_length=30)
    twitter = models.CharField(max_length=30)
    youtube = models.CharField(max_length=30)
    linkedin = models.CharField(max_length=30)
    logo = models.ImageField(upload_to="header/logo/")
    address = models.CharField(max_length=150)
    phone1 = models.CharField(max_length=15)
    phone2 = models.CharField(max_length=15)
    email1 = models.EmailField()
    email2 = models.EmailField()

    def __str__(self):
        return f"{self.message}"


class HeaderImage(models.Model):
    service = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    header = models.ForeignKey(Header, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='header/images/')



class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.subject}'




class NewsView(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title




