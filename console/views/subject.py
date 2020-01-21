from django.shortcuts import render, redirect, get_object_or_404
from console.models import Subject
from console.forms import SubjectForm
from django.contrib import messages

def add_subject(request):
    if request.user.is_staff:
        form=SubjectForm(request.POST)
        if form.is_valid():
            Subject=form.save()
            messages.success(request, 'New Subject has been added!')
            return redirect('add_subject')
        return render(request, 'console/jobs/add_subject.html',{'form':form})
    else:
        return redirect('dashboard')

def edit_sub(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            context={
                'subjects': Subject.objects.all()
            }
            return render(request, 'console/jobs/edit_sub.html', context)
        else:
            return redirect('dashboard')

def edit_sub_view(request, pk):
    if request.user.is_staff:
        obj = get_object_or_404(Subject, id=pk)
        form = SubjectForm(request.POST or None, instance=obj)
        context = {'form':form}
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context = {'form':form}
            messages.warning(request, 'Subject records has been updated')
            return redirect('edit_sub')
        return render(request, 'console/jobs/edit_sub_form.html', context)
    else:
        return redirect('edit_sub')

def delete_sub(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            context={
                'subjects': Subject.objects.all()
            }
            return render(request, 'console/jobs/delete_sub.html', context)
        else:
            return redirect('dashboard')

def delete_sub_view(request, pk):
    if request.user.is_authenticated:
        if request.user.is_staff:
            obj = Subject.objects.filter(id=pk)
            obj.delete()
            messages.error(request, 'Subject record has been deleted!')
            return redirect('delete_sub')
        return redirect('dashboard')
   