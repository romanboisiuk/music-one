from django.db import models

from main.models.user_info import MusicOneUser


class StoryHashtag(models.Model):
    hash_tag = models.CharField(max_length=128)

    def __str__(self):
        return self.hash_tag


class IgtvHashtag(models.Model):
    hash_tag = models.CharField(max_length=128)

    def __str__(self):
        return self.hash_tag


class Highlight(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Story(models.Model):
    hash_tag = models.ForeignKey(StoryHashtag, on_delete=models.CASCADE, related_name='stories')
    highlight = models.ForeignKey(Highlight, on_delete=models.CASCADE, related_name='stories')
    user = models.OneToOneField(MusicOneUser, on_delete=models.CASCADE, related_name='stories')
    url = models.URLField(max_length=500)

    def __str__(self):
        return f'story---{self.pk}'


class Igtv(models.Model):
    hash_tag = models.ForeignKey(IgtvHashtag, on_delete=models.CASCADE, related_name='igtvs')
    user = models.OneToOneField(MusicOneUser, on_delete=models.CASCADE, related_name='igtvs')
    url = models.URLField(max_length=500)

    def __str__(self):
        return f'igtv---{self.pk}'
