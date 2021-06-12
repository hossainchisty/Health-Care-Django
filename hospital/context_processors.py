from .models import Doctor
from .models import Testimonial

def context_data(request):
    testimonial = Testimonial.objects.all()
    doctors = Doctor.objects.all()

    context = {
        'object_list': doctors,
        'testimonial_list': testimonial,
    }

    return context


