from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.shortcuts import render

from . import wrapper

from .forms import SignupForm, LoginForm
from .forms import PasswordResetForm, PasswordResetVerifiedForm
from .forms import EmailChangeForm
from .forms import PasswordChangeForm, UsersMeChangeForm
from .models import profile_image_path


# Create your views here.
# views.py



class SignupVerifyFrontEnd(View):
    def get(self, request, format=None):
        code = request.GET.get('code', '')

        account = wrapper.Authemail()
        response = account.signup_verify(code=code)

        # Handle other error responses from API
        if 'detail' in response:
            return HttpResponse( 'sorry we were unable to verify your email')

       return HttpResponseRedirect(reverse('signup_verified_page'))


class SignupVerifiedFrontEnd(TemplateView):
    template_name = 'signup_verified.html'


class PasswordResetFrontEnd(FormView):
        template_name = 'password_reset.html'
        form_class = PasswordResetForm
        success_url = reverse_lazy('password_reset_email_sent_page')

        def form_valid(self, form):
            email = form.cleaned_data['email']

            account = wrapper.Authemail()
            response = account.password_reset(email=email)

            # Handle other error responses from API
            if 'detail' in response:
                form.add_error(None, response['detail'])
                return self.form_invalid(form)

            return super(PasswordResetFrontEnd, self).form_valid(form)


class PasswordResetEmailSentFrontEnd(TemplateView):
    template_name = 'password_reset_email_sent.html'


class PasswordResetVerifyFrontEnd(View):
    def get(self, request, format=None):
        code = request.GET.get('code', '')

        account = wrapper.Authemail()
        response = account.password_reset_verify(code=code)

        # Handle other error responses from API
        if 'detail' in response:
            return HttpResponseRedirect(
                reverse('password_reset_not_verified_page'))

        request.session['password_reset_code'] = code

        return HttpResponseRedirect(reverse('password_reset_verified_page'))


class PasswordResetVerifiedFrontEnd(FormView):
    template_name = 'password_reset_verified.html'
    form_class = PasswordResetVerifiedForm
    success_url = reverse_lazy('password_reset_success_page')

    def form_valid(self, form):
        code = self.request.session['password_reset_code']
        password = form.cleaned_data['password']

        account = wrapper.Authemail()
        response = account.password_reset_verified(code=code, password=password)

        # Handle other error responses from API
        if 'detail' in response:
            form.add_error(None, response['detail'])
            return self.form_invalid(form)

        return super(PasswordResetVerifiedFrontEnd, self).form_valid(form)


class PasswordResetNotVerifiedFrontEnd(TemplateView):
    template_name = 'password_reset_not_verified.html'


class PasswordResetSuccessFrontEnd(TemplateView):
    template_name = 'password_reset_success.html'


class EmailChangeFrontEnd(FormView):
    template_name = 'email_change.html'
    form_class = EmailChangeForm
    success_url = reverse_lazy('email_change_emails_sent_page')

    def form_valid(self, form):
        token = self.request.session['auth_token']
        email = form.cleaned_data['email']

        account = wrapper.Authemail()
        response = account.email_change(token=token, email=email)

        # Handle other error responses from API
        if 'detail' in response:
            form.add_error(None, response['detail'])
            return self.form_invalid(form)

        return super(EmailChangeFrontEnd, self).form_valid(form)


class EmailChangeEmailsSentFrontEnd(TemplateView):
    template_name = 'email_change_emails_sent.html'


class EmailChangeVerifyFrontEnd(View):
    def get(self, request, format=None):
        code = request.GET.get('code', '')

        account = wrapper.Authemail()
        response = account.email_change_verify(code=code)

        # Handle other error responses from API
        if 'detail' in response:
            return HttpResponseRedirect(
                reverse('email_change_not_verified_page'))

        request.session['email_change_code'] = code

        return HttpResponseRedirect(reverse('email_change_verified_page'))


class EmailChangeVerifiedFrontEnd(TemplateView):
    template_name = 'email_change_verified.html'

class LogoutFrontEnd(View):
    def get(self, request):
        token = self.request.session['auth_token']

        account = wrapper.Authemail()
        account.logout(token=token)

        self.request.session.flush()

        return HttpResponse({'success': 'User Logged Out'})
    



def upload_image(request):
    if request.method == 'PUT':
        image_file = request.FILES['image']

        if image_file:
            # Handle the uploaded image here. You can save it to a specific directory or process it as needed.
            # For example, you can save it to a specific directory:

            with open(profile_image_path + image_file.name, 'wb') as destination:
                for chunk in image_file.chunks():
                    destination.write(chunk)

            return HttpResponse('Image uploaded successfully.')

   
