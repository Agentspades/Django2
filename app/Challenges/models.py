from enum import unique
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Challenges(models.Model):
    ChallengeID = models.AutoField(primary_key=True)
    Challenge_Title = models.CharField(max_length=45)
    Challenge_Description = models.CharField(max_length=200)
    Commencement = models.DateTimeField()
    Termination = models.DateTimeField()
    Reward = models.ForeignKey('ChallengeRewards', on_delete=models.CASCADE,
                               db_column='Reward', default=0, verbose_name='Reward')

    class Meta:
        db_table = 'challenges'
        verbose_name_plural = 'Challenges'

    def __str__(self):
        return self.Challenge_Title


class ChallengeRewards(models.Model):
    ChallengeRewardsID = models.AutoField(primary_key=True)
    Reward = models.CharField(max_length=45)

    class Meta:
        db_table = 'challenge_rewards'
        verbose_name_plural = 'Challenge Rewards'

    def __str__(self):
        return self.Reward


class UserHasChallenges(models.Model):
    # REPLACE WHEN USER MODEL IS PLACED #
    UserID = models.ForeignKey("Auth.User", on_delete=models.CASCADE,
                               db_column='UserID', verbose_name='UserID', primary_key=True)
    ChallengeID = models.ForeignKey('Challenges', on_delete=models.CASCADE,
                                    db_column='ChallengeID', default=0, verbose_name='Challenge ID')
    Completion = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'user_has_challenges'
        verbose_name_plural = 'Users Challenges'
        unique_together = (('UserID', 'ChallengeID'))

    def __str__(self):
        return str(self.UserID)
