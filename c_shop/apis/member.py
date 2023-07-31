from c_shop.models import Member

SUCCESS = 1

NOT_FOUND_USER = 3

UNKNOWN_ERROR = 999

def create(_id, pw):
    try:
        Member.objects.create(_id=_id, pw=pw)
        return SUCCESS
    except:
        return UNKNOWN_ERROR
def read(pk):
    try:
        result = Member.objects.filter(pk=pk)
        if(result < 1):
            return NOT_FOUND_USER
        return result
    except:
        return UNKNOWN_ERROR

def update(member):
    try:
        member.save()
        return SUCCESS # true: 성공, false: 실패
    except:
        return UNKNOWN_ERROR
    
def delete(pk):
    try:
        result = Member.objects.filter(pk=pk)
        if(result < 1):
            return NOT_FOUND_USER
        
        result.delete()
        return SUCCESS # true: 성공, false: 실패
    except:
        return UNKNOWN_ERROR
