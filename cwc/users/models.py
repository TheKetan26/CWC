from django.db import models


class User(models.Model):
    user_id                  = models.IntegerField(default=0)

    first_name          = models.CharField(max_length=25, default="")
    last_name           = models.CharField(max_length=25, default="")

    email               = models.EmailField(default="")

    password            = models.CharField(max_length=16, default="12345678")

    contact             = models.PositiveBigIntegerField(blank=True)

    gender_choice       = [("m", "Male"), ("F", "Female"), ("O", "Other")]
    gender              = models.CharField(max_length=6, default="m", choices=gender_choice)

    dob                 = models.DateField(auto_now=True, blank=True)

    nation_choices      = [("INDIA", "INDIA"), ("ENGLAND", "ENGLAND"), ("NEW ZEALAND", "NEW ZEALAND"), ("WEST INDIES", "WEST INDIES"), ("SOUTH AFRICA", "SOUTH AFRICA"), ("SRI LANKA", "SRI LANKA"), ("BANGLADESH", "BANGLADESH"), ("AUSTRALIA", "AUSTRALIA")]
    nation              = models.CharField(max_length=12, default="INDIA", choices=nation_choices)


    def __str__(self):
        return str(self.id) + " - " + str(self.email)