from django.db import models

class UserInfo(models.Model):
    user_id = models.CharField(max_length=64, primary_key=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    blog = models.URLField(default=None, blank=True, null=True)
    location = models.CharField(max_length=256, blank=True, null=True)
    email = models.EmailField(max_length=32, blank=True, null=True)
    public_repos_count = models.IntegerField(default=None, blank=True, null=True)
    public_gists_count = models.IntegerField(default=None, blank=True, null=True)
    follower_count = models.IntegerField(default=None, blank=True, null=True)
    following_count = models.IntegerField(default=None, blank=True, null=True)
    fetched_data_timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.user_id)

"""class RepoInfo(models.Model):
    name = models.CharField(max_length=30)
    repo_name = models.CharField(max_length=250)
    repo_url = models.URLField()
    repo_language = models.CharField(max_length=250)

    def __str__(self):
        return self.name"""