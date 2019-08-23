from django.views import generic
from .forms import SearchForm
from .models import Wish
# Create your views here.


class IndexView(generic.ListView):
	model = Wish
	paginate_by = 10

	def get_context_data(self):
		context = super().get_context_data()
		context['form'] = SearchForm(self.request.GET)
		return context

	def get_queryset(self):
		"""テンプレートにn渡すwish_listの作成"""
		form = SearchForm(self.request.GET)
		form.is_valid()

		queryset = super().get_queryset()

		genre = form.cleaned_data['genre']
		if genre:
			queryset = queryset.filter(genre=genre) #引数＝変数

		return queryset