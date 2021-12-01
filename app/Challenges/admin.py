from django.contrib import admin
from .models import Challenges, ChallengeRewards, UserHasChallenges

# Register your models here.


class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('Challenge_Title',
                    'Challenge_Description', 'Commencement', 'Termination', 'Reward')
    search_fields = ['Challenge_Title',
                     'Challenge_Description']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class RewardsAdmin(admin.ModelAdmin):
    list_display = [('Reward')]
    search_fields = ['Reward']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class UserHasChallengesAdmin(admin.ModelAdmin):
    list_display = ('UserID', 'Completion', 'ChallengeID')
    search_fields = [str('UserID'), str('ChallengeID')]

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Challenges, ChallengeAdmin)
admin.site.register(ChallengeRewards, RewardsAdmin)
admin.site.register(UserHasChallenges, UserHasChallengesAdmin)
