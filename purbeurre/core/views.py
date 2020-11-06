from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from products.models import ProductForm


class HomeView(FormView):
	template_name = 'core/index.html'
	form_class = ProductForm
	success_url = reverse_lazy('products:results')

	def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
		return super().form_valid(form)


class LegalNoticeView(TemplateView):
	template_name = 'core/legal_notice.html'
	def get(self, request):
		return render(request, self.template_name)

