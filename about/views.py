from django.shortcuts import render

# Create your views here.
def about_view(request):
    # Get About content from the database (if applicable)
    about_content = About.objects.all().first()  # Get the first record

    context = {'about': about_content}
    return render(request, 'templates/about/about.html', context)