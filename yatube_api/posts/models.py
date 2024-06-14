from django.contrib.auth import get_user_model
from django.db import models

MAX_LENGTH = 15

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True, blank=True
    )
    group = models.ForeignKey(
        'Group',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.text[:MAX_LENGTH]


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    def __str__(self):
        return f'{self.author}: {self.text[:MAX_LENGTH]}'


class Group(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title[:MAX_LENGTH]


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user',
        null=True,
        blank=True
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        null=True,
        blank=True)

    class Meta:
        unique_together = [['user', 'following']]

    def __str__(self):
        return f'{self.user.username} подписан на {self.following.username}'
