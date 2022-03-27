from django.views.generic import TemplateView

from quiz_app.models import staff


class IndexView(TemplateView):
    template_name = 'admin/admin_index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        Staff=staff.objects.all()
        context['Staff']=Staff
        return context




