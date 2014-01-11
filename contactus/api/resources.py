from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication, BasicAuthentication
from tastypie.authorization import Authorization
from tastypie.validation import Validation, FormValidation
from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized
#from tastypie import fields

from contactus.models import ContactUs, ContactUsForm


class AnonymousPostAuthentication(BasicAuthentication):
    """ No auth on post / for user creation """

    def is_authenticated(self, request, **kwargs):
        """ If POST, don't check auth, otherwise fall back to parent """
        if request.method == "POST":
            return True
        else:
            return super(AnonymousPostAuthentication, self).is_authenticated(request, **kwargs)


class ContactUsResource(ModelResource):
    class Meta:
        queryset = ContactUs.objects.all()
        resource_name = 'auth/user'
        allowed_methods = ['get', 'post']
        detail_allowed_methods = ['post']
        authentication = AnonymousPostAuthentication()
        validation = FormValidation(form_class=ContactUsForm)
