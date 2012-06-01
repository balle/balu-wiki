#########
Security
#########

* http://pypi.python.org/pypi/django-passwords/

=============
User profile
=============

* member/models.py

.. code-block:: python

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    language = models.CharField(max_length=2, default=settings.LANGUAGE_CODE)

def user_registered_handler(sender, **kwargs):
    user = kwargs.get('user')
    language = kwargs.get("language")

    if not language:
        language = settings.LANGUAGE_CODE

    if user:
        profile, created = UserProfile.objects.get_or_create(user=user)
        profile.language = language

        profile.save()

user_registered_signal.connect(user_registered_handler)

* Register profile in settings

.. code-block:: python

AUTH_PROFILE_MODULE = "member.UserProfile"


===========================
Edir user profile in admin
===========================

* member/admin.py

.. code-block:: python

class UserProfileInline(admin.StackedInline):
 model = UserProfile
 max_num = 1
 can_delete = False

class UserAdmin(AuthUserAdmin):
 inlines = [UserProfileInline]

# unregister old user admin
admin.site.unregister(User)
# register new user admin
admin.site.register(User, UserAdmin)
