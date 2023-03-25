from rest_framework import serializers
from .models import Folder


def arrayfilter(txt):
    a =[]
    i = 1
    j = 1
    n = len(txt)
    while i < n-1:
        if txt[i] == ",":
            a.append(txt[j:i])
            j = i + 1
        i+=1
    a.append(txt[j:i])
    return a

def arrayfilter2(txt):
    a =[]
    i = 2
    j = 2
    n = len(txt)
    while i < n-2:
        if txt[i] == ",":
            a.append(txt[j:i])
            j = i + 1
        i+=1
    a.append(txt[j:i])
    return a

class FolderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Folder
        fields = (
            'id',
            'user',
            'folder_name',
            'sender',
            'keyword',
        )
    '''
    def concatenate_sender(self, sender_list):
        sender = ''.join(sender_list)
        return [sender]
    '''
    def validate_sender(self, value):
        if not value:
            # sender 값이 빈 리스트인 경우 "모든"으로 변경
            value = ["모든"]
        return value
    
    def validate_keyword(self, value):
        if not value:
            value = ["모든"]
        return value
    def to_representation(self, instance):
        data = super().to_representation(instance)
        res = data['sender']
        re_res = '{' + ''.join(res).replace('{', '').replace('}', '') + '}'
        tmp = data['keyword']
        re_tmp = '{' + ''.join(tmp).replace('{', '').replace('}', '') + '}'
        if '{"' in re_res:
            resres = arrayfilter2(re_res)
            tmptmp = arrayfilter2(re_tmp)
        else:
            resres = arrayfilter(re_res)
            tmptmp = arrayfilter(re_tmp)

        print(resres)
        print(tmptmp)
        data['sender'] = resres
        data['keyword'] = tmptmp
        return data

