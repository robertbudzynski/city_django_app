from django.views.generic import TemplateView


# Create your views here.

class EducationView(TemplateView):
    template_name = 'education.html'


class HistoryView(TemplateView):
    template_name = 'history.html'


class SportView(TemplateView):
    template_name = 'sport.html'


class PromotionView(TemplateView):
    template_name = 'promotion.html'


class EducationBSW(TemplateView):
    template_name = 'subpages/BSW.html'


class EducationUKW(TemplateView):
    template_name = 'subpages/UKW.html'


class EducationUMK(TemplateView):
    template_name = 'subpages/UMK.html'


class EducationUTP(TemplateView):
    template_name = 'subpages/UTP.html'


class EducationWSB(TemplateView):
    template_name = 'subpages/WSB.html'


class EducationWSG(TemplateView):
    template_name = 'subpages/WSG.html'
