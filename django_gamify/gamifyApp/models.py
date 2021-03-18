from django.db import models


class BadgesCategories(models.Model):

    title = models.CharField(max_length=150)

    shorttitle = models.CharField(max_length=200)

    description = models.TextField()

    BADGE_TYPES = (
        (1, 'Badges'),
        (2, 'Rewards'),
        (3, 'Levels'),
        (4, 'Points'),
        (5, 'Credits'),
        (6, 'Packages')
    )

    category_type = models.SmallIntegerField(default=1, choices=BADGE_TYPES)

    priority = models.IntegerField(default=0)


class BadgeEvents(models.Model):

    title = models.CharField(max_length=150)

    description = models.TextField()

    event_key = models.CharField(max_length=50)

    category_id = models.SmallIntegerField()

    #category = models.ForeignKey("BadgesCategories", on_delete=models.SET_NULL, null=True)


class Badges(models.Model):

    title = models.CharField(max_length=150)

    description = models.TextField()

    icon = models.CharField(max_length=150)

    icon_sm = models.CharField(max_length=150)

    icon_lg = models.CharField(max_length=150)

    category_id = models.SmallIntegerField()

    BADGE_TYPES = (
        (1, 'Badges'),
        (2, 'Rewards'),
        (3, 'Levels'),
        (4, 'Points'),
        (5, 'Credits'),
        (6, 'Packages')
    )

    badge_type = models.SmallIntegerField(default=1, choices=BADGE_TYPES)

    icon_css = models.CharField(max_length=150)

    priority = models.IntegerField(default=0)

    credits = models.IntegerField(default=0)

    xp = models.IntegerField(default=0)

    price = models.FloatField(default=0)

    notification = models.CharField(max_length=300)

    isdeduct = models.SmallIntegerField(default=0)

    ilevel = models.SmallIntegerField(default=0)

    ishide = models.SmallIntegerField(default=0)

    ismultiple = models.SmallIntegerField(default=0)

    img_url = models.CharField(max_length=150)

    categories = models.ForeignKey(
        "BadgesCategories", on_delete=models.SET_NULL, null=True)

    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.title, self.description)


class BadgesUserAchievements(models.Model):

    userid = models.IntegerField()

    description = models.TextField()

    createda_at = models.DateTimeField()

    BADGE_TYPES = (
        (1, 'Badges'),
        (2, 'Rewards'),
        (3, 'Levels'),
        (4, 'Points'),
        (5, 'Credits'),
        (6, 'Packages')
    )

    badge_type = models.SmallIntegerField(default=1, choices=BADGE_TYPES)


class UserBadges(models.Model):

    userid = models.IntegerField()

    badgeid = models.IntegerField()

    BADGE_TYPES = (
        (1, 'Badges'),
        (2, 'Rewards'),
        (3, 'Levels'),
        (4, 'Points'),
        (5, 'Credits'),
        (6, 'Packages')
    )

    badge_type = models.SmallIntegerField(default=1, choices=BADGE_TYPES)

    createda_at = models.DateTimeField()

    repeated = models.SmallIntegerField()

    badges = models.ForeignKey("Badges", on_delete=models.SET_NULL, null=True)
