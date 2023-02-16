from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import Emaillist2Serializer
from .models import Emaillist2User
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
import imaplib
import email
from datetime import datetime
from email.header import decode_header, make_header
import json
from django.http import JsonResponse
from django.core import serializers
from email import policy


def find_encoding_info(txt):
    info = email.header.decode_header(txt)
    subject, encode = info[0]
    return subject, encode

#메일 인증 API : post로 해당 정보로 imap 로그인이 되는지 결과 반환
class ImapView2(APIView):
    def post(self, request):
        serializer = Emaillist2Serializer(data=request.data)
        tmp = request.data.get('email')
        #gmail 인증 로직
        if tmp.find('@gmail.com') != -1:
            res = request.data.get('gmailkey')
            imap = imaplib.IMAP4_SSL('imap.gmail.com')
            #serializer.initial_data['g_email'] = request.data.get('email')
            #serializer.initial_data['g_key'] = request.data.get('gmailkey')
            try:
                imap.login(tmp, res)
                if serializer.is_valid():
                    serializer.validated_data['email'] = request.data.get('email')
                    serializer.validated_data['password'] = request.data.get('password')
                    serializer.validated_data['g_key'] = request.data.get('gmailkey')
                    serializer.save(user=request.user)
                    serializer.save()
                return Response({"message":"success"}, status=status.HTTP_200_OK)
            except:
                return Response({"message":"fail"}, status=status.HTTP_409_CONFLICT)
        if tmp.find('@naver.com') != -1:
            res = request.data.get('password')
            imap = imaplib.IMAP4_SSL('imap.naver.com')
            try:
                imap.login(tmp, res)
                if serializer.is_valid():
                    serializer.validated_data['email'] = request.data.get('email')
                    serializer.validated_data['password'] = request.data.get('password')
                    serializer.save(user=request.user)
                    serializer.save()
                return Response({"message":"success"}, status=status.HTTP_200_OK)
            except:
                return Response({"message":"fail"}, status=status.HTTP_409_CONFLICT)
        return Response({"message":"it is not right email"}, status=status.HTTP_409_CONFLICT)
    
class ImapViewSet(viewsets.ModelViewSet):
    queryset = Emaillist2User.objects.all()
    serializer_class = Emaillist2Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#DB의 사용자 정보를 GET을 통해 조회하는 API
class ImapGetView(APIView):
    def get_object(self, pk):
        try:
            return Emaillist2User.objects.get(pk=pk)
        except Emaillist2User.DoesNotExist:
            return Response("message:do not exist id")
    
    # Blog의 detail 보기
    def get(self, request, pk, format=None):
        blog = self.get_object(pk)
        serializer = Emaillist2Serializer(blog)
        return Response(serializer.data)
#Token을 통해 유저 id 뽑아내는 API. 그 id를 통해 g_email, g_password 가져올수있다
class TokenGetView(APIView):
    def get(self, request, format=None):
        

        blogs = Emaillist2User.objects.all()
        # 여러 개의 객체를 serialization하기 위해 many=True로 설정
        serializer = Emaillist2Serializer(blogs, many=True)
        return Response(serializer.data)

        tmp = EmaillistUser.objects.get(id=request.user.id)
        tmpserializer = EmaillistSerializer(tmp)
        res = tmpserializer.data.get('g_email')
        asg = tmpserializer.data.get('g_key')
        print(res)
        print(asg)

        return Response(tmpserializer.data)

class ImapGetList(APIView):

    def get(self, request, format=None):
        tmp = Emaillist2User.objects.filter(user_id=request.user.id)
        #tmp = tmp[0].g_key
        #tmp = str(tmp)
        j=0
        emaillist = ""
        emaillists = []
        while j < len(tmp):
            resg = tmp[j].email
            asg = tmp[j].password
            had = tmp[j].g_key
            if resg.find('@gmail.com') != -1:
                imap = imaplib.IMAP4_SSL('imap.gmail.com')
                try:
                    imap.login(resg, had)
                except:
                    return Response("imap gmail information is not matcded")
                imap.select("INBOX")
                status, messages = imap.uid('search', None, 'ALL')

                messages = messages[0].split()

                r_email = messages[-1]

                res, msg = imap.uid('fetch', r_email, "(RFC822)")

                raw = msg[0][1].decode('utf-8')

                email_message = email.message_from_string(raw)
                d = datetime.now().day
                date = decode_header(email_message.get("Date"))[0]
                #print(date)
                try:
                    temp = datetime.strptime(date[0], '%a, %d %b %Y %H:%M:%S %z')
                except:
                    temp = datetime.strptime(date[0], '%a, %d %b %Y %H:%M:%S %Z')
                i = -1
                while d == temp.day:

                    r_email = messages[i]
                    # fetch 명령어로 메일 가져오기
                    res, msg = imap.uid('fetch', r_email, "(RFC822)")
                    # 사람이 읽을 수 있는 형태로 변환
                    raw = msg[0][1].decode('utf-8')
                    #print(raw)
                    # raw_readable에서 원하는 부분만 파싱하기 위해 email 모듈을 이용해 변환
                    email_message = email.message_from_string(raw)

                    # 보낸사람
                    fr = make_header(decode_header(email_message.get('From')))
                    fr = str(fr)
                    print(fr)

                    # 메일 제목
                    subject = make_header(decode_header(email_message.get('Subject')))
                    subject = str(subject)
                    print(subject)

                    #메일 시간
                    date = decode_header(email_message.get("Date"))[0]
                    #print(date)
                    try:
                        temp = datetime.strptime(date[0], '%a, %d %b %Y %H:%M:%S %z')
                    except:
                        temp = datetime.strptime(date[0], '%a, %d %b %Y %H:%M:%S %Z')
                    #print(temp.day)
            
                    if d != temp.day:
                        break

                    # 메일 내용
                    if email_message.is_multipart():
                        for part in email_message.walk():
                            ctype = part.get_content_type()
                            cdispo = str(part.get('Content-Disposition'))
                            if ctype == 'text/plain' and 'attachment' not in cdispo:
                                body = part.get_payload(decode=True)  # decode
                                break
                    
                    else:
                        body = email_message.get_payload(decode=True)
                    body = body.decode('utf-8')

                    emaillist = {"title":subject, "sender":fr, "detail":body}
                    #emaillisttt = json.dumps(emaillist, indent=2, ensure_ascii=False)
                    emaillists.append(emaillist)
                    print(emaillists)
                    i-=1

            elif resg.find('@naver.com') != -1:
                imap = imaplib.IMAP4_SSL('imap.naver.com')
                try:
                    imap.login(resg, asg)
                except:
                    return Response("imap naver information is not matcded")
            
                imap.select('INBOX')
                resp, data = imap.uid('search', None, 'All')
                all_email = data[0].split()
                last_email = all_email[-1]
                result, data = imap.uid('fetch', last_email, '(RFC822)')
                raw = data[0][1]
                email_message = email.message_from_bytes(raw, policy = policy.default)
                d = datetime.now().day
                date = email_message['Date']
                print(d)
                temp = datetime.strptime(date, '%a, %d %b %Y %H:%M:%S %z')
                print(temp.day)
                i=-1

                while d == temp.day: 
                    last_email = all_email[i]
                    result, data = imap.uid('fetch', last_email, '(RFC822)')
                    raw_email = data[0][1]
                    email_message = email.message_from_bytes(raw_email, policy = policy.default)
                
                    #보낸이
                    sender = email_message['From']
                
                    # 제목 가져오기
                    subject, encode = find_encoding_info(email_message['Subject'])
                    print('SUBJECT : ', subject)
                    print('+'*70)
    
                    #본문 내용 출력하기
                    message = ''
                    if email_message.is_multipart():
                        for part in email_message.walk():
                            ctype = part.get_content_type()
                            cdispo = str(part.get('Content-Disposition'))
                            if ctype == 'text/plain' and 'attachment' not in cdispo:
                                message = part.get_payload()  # decode
                                break
                    
                    else:
                        try:
                            message = email_message.get_payload()
                        except:
                            message = ""
                    print(message)
                    #메일의 시간
                    date = email_message['Date']
                    temp = datetime.strptime(date, '%a, %d %b %Y %H:%M:%S %z')

                    
                    emaillist = {"title":subject, "sender":sender, "detail":message}
                    emaillists.append(emaillist)

                    i-=1
            
                
            j+=1
        imap.close()
        imap.logout()
        return Response(emaillists)
    