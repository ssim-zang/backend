from c_shop.models import Member
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import get_object_or_404


def create(request):
    try:
        Member.objects.create(
            _id=request.POST['id'],
            pw=request.POST['pw'],
            name=request.POST['name']
        )
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=400)
    
def login(request):
    try:
        get_object_or_404(Member, pk=request.POST['id'], pw = request.POST['pw'])
        request.session['id'] = request.POST['id']
        return HttpResponse(status=200)
    except:
        return HttpResponse(status=400)
# def read(pk):
#     try:
#             question = get_object_or_404(Question, pk=question_id)

#         result = Member.objects.filter(pk=pk)
#         if(result < 1):
#             return NOT_FOUND_USER
#         return result
#     except:
#         return UNKNOWN_ERROR

# def update(member):
#     try:
#         member.save()
#         return SUCCESS # true: 성공, false: 실패
#     except:
#         return UNKNOWN_ERROR
    
# def delete(pk):
#     try:
#         result = Member.objects.filter(pk=pk)
#         if(result < 1):
#             return NOT_FOUND_USER
        
#         result.delete()
#         return SUCCESS # true: 성공, false: 실패
#     except:
#         return UNKNOWN_ERROR
