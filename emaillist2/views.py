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
from myfolders.models import Folder
from email.utils import parsedate_to_datetime

def find_encoding_info(txt):
    info = email.header.decode_header(txt)
    subject, encode = info[0]
    return subject, encode

def arrayfilter(txt):
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
# a = resg, b = asg, c = had
def gmaillists(a,c,gmailres):
    if a.find('gmail') != -1:
        imap = imaplib.IMAP4_SSL('imap.gmail.com')
        try:
            imap.login(a, c)
        except:
            return False
        imap.select("INBOX")
        status, messages = imap.uid('search', None, 'ALL')

        messages = messages[0].split()

        r_email = messages[-1]

        res, msg = imap.uid('fetch', r_email, "(RFC822)")

        raw = msg[0][1].decode('utf-8')

        email_message = email.message_from_string(raw)
        d = datetime.now().date()
        date_string = email_message.get("Date")
        temp = parsedate_to_datetime(date_string)
        tempday = temp.date()

        '''
        d = datetime.now().day
        date = decode_header(email_message.get("Date"))[0]
        #print(date)
        try:
            temp = datetime.strptime(date[0], '%a, %d %b %Y %H:%M:%S %z')
        except:
            temp = datetime.strptime(date[0], '%a, %d %b %Y %H:%M:%S %Z')
        '''
        i = -1
        while d == tempday:

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
            d = datetime.now().date()
            date_string = email_message.get("Date")
            temp = parsedate_to_datetime(date_string)
            tempday = temp.date()

            '''
            d = datetime.now().day
            date = decode_header(email_message.get("Date"))[0]
            #print(date)
            try:
                temp = datetime.strptime(date[0], '%a, %d %b %Y %H:%M:%S %z')
            except:
                temp = datetime.strptime(date[0], '%a, %d %b %Y %H:%M:%S %Z')
            '''
            
            if d != tempday:
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
            emaillist = {"title":subject, "sender":fr, "detail":body, "date":temp}
            gmailres.append(emaillist)
            i-=1    
            
    return gmailres

def naverlists(a,b,naverres):
    if a.find("naver") != -1:
        imap = imaplib.IMAP4_SSL('imap.naver.com')
        try:
            imap.login(a,b)
        except:
            return False
        imap.select("INBOX")
        status, messages = imap.uid('search', None, 'ALL')

        messages = messages[0].split()

        r_email = messages[-1]

        res, msg = imap.uid('fetch', r_email, "(RFC822)")

        raw = msg[0][1].decode('utf-8')

        email_message = email.message_from_string(raw)
        d = datetime.now().date()
        date_string = email_message.get("Date")
        temp = parsedate_to_datetime(date_string)
        tempday = temp.date()

        '''
        d = datetime.now().day
        date = decode_header(email_message.get("Date"))[0]
        #print(date)
        try:
            temp = datetime.strptime(date[0], '%a, %d %b %Y %H:%M:%S %z')
        except:
            temp = datetime.strptime(date[0], '%a, %d %b %Y %H:%M:%S %Z')
        '''
        i = -1
        while d == tempday:

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
            d = datetime.now().date()
            date_string = email_message.get("Date")
            temp = parsedate_to_datetime(date_string)
            tempday = temp.date()

            '''
            d = datetime.now().day
            date = decode_header(email_message.get("Date"))[0]
            #print(date)
            try:
                temp = datetime.strptime(date[0], '%a, %d %b %Y %H:%M:%S %z')
            except:
                temp = datetime.strptime(date[0], '%a, %d %b %Y %H:%M:%S %Z')
            '''
            
            if d != tempday:
                break

            # 메일 내용
            body = ""
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
            
            emaillist = {"title":subject, "sender":fr, "detail":body, "date":temp}
            #emaillisttt = json.dumps(emaillist, indent=2, ensure_ascii=False)
            naverres.append(emaillist)
            
            i-=1
    return naverres

def naverbytes(a,b,naverbyte):
    if a.find('naver') != -1:
        imap = imaplib.IMAP4_SSL('imap.naver.com')
        try:
            imap.login(a,b)
        except:
            return False
        imap.select('INBOX')
        resp, data = imap.uid('search', None, 'All')
        all_email = data[0].split()
        last_email = all_email[-1]
        result, data = imap.uid('fetch', last_email, '(RFC822)')
        raw = data[0][1]
        email_message = email.message_from_bytes(raw, policy = policy.default)

        d = datetime.now().date()
        date_string = email_message.get("Date")
        temp = parsedate_to_datetime(date_string)
        tempday = temp.date()

        '''
        d = datetime.now().day
        date = decode_header(email_message.get("Date"))[0]
        #print(date)
        try:
            temp = datetime.strptime(date[0], '%a, %d %b %Y %H:%M:%S %z')
        except:
            temp = datetime.strptime(date[0], '%a, %d %b %Y %H:%M:%S %Z')
        '''

        i=-1
        while d == tempday: 
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

            #메일의 시간
            d = datetime.now().date()
            date_string = email_message.get("Date")
            temp = parsedate_to_datetime(date_string)
            tempday = temp.date()

            '''
            d = datetime.now().day
            date = decode_header(email_message.get("Date"))[0]
            #print(date)
            try:
                temp = datetime.strptime(date[0], '%a, %d %b %Y %H:%M:%S %z')
            except:
                temp = datetime.strptime(date[0], '%a, %d %b %Y %H:%M:%S %Z')
            '''

            if d != tempday:
                print("break문 실행")
                break
            
            #본문 내용 출력하기
            message = ''
            try:
                if email_message.is_multipart():
                    for part in email_message.walk():
                        ctype = part.get_content_type()
                        cdispo = str(part.get('Content-Disposition'))
                        if ctype == 'text/plain' and 'attachment' not in cdispo:
                            message = part.get_payload(decode=True)  # decode
                            message = message.decode('utf-8')
                            break
                    
                else:
                    message = email_message.get_payload(decode=True)
                #print(message)
            except:
                message = message    

                    
            emaillist = {"title":subject, "sender":sender, "detail":message, "date":temp}
            naverbyte.append(emaillist)

            i-=1

        return naverbyte

def foldergmaillists(a,c,gmailres,q,p):
    if a.find('gmail') != -1:
        imap = imaplib.IMAP4_SSL('imap.gmail.com')
        try:
            imap.login(a, c)
        except:
            return False
        imap.select("INBOX")
        status, messages = imap.uid('search', None, 'ALL')

        messages = messages[0].split()

        r_email = messages[-1]

        res, msg = imap.uid('fetch', r_email, "(RFC822)")

        raw = msg[0][1].decode('utf-8')

        email_message = email.message_from_string(raw)
        d = datetime.now().date()
        date_string = email_message.get("Date")
        temp = parsedate_to_datetime(date_string)
        tempday = temp.date()

        '''
        d = datetime.now().day
        date = decode_header(email_message.get("Date"))[0]
        #print(date)
        try:
            temp = datetime.strptime(date[0], '%a, %d %b %Y %H:%M:%S %z')
        except:
            temp = datetime.strptime(date[0], '%a, %d %b %Y %H:%M:%S %Z')
        '''

        i = -1
        while d == tempday:

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
            d = datetime.now().date()
            date_string = email_message.get("Date")
            temp = parsedate_to_datetime(date_string)
            tempday = temp.date()

            '''
            d = datetime.now().day
            date = decode_header(email_message.get("Date"))[0]
            #print(date)
            try:
                temp = datetime.strptime(date[0], '%a, %d %b %Y %H:%M:%S %z')
            except:
                temp = datetime.strptime(date[0], '%a, %d %b %Y %H:%M:%S %Z')
            '''
            
            if d != tempday:
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
            emaillist = {"title":subject, "sender":fr, "detail":body, "date":temp}
            folderemaillist = subject + fr + body
            right = False
            ii = 0
            qq = arrayfilter(q)
            pp = arrayfilter(p)
            nn = len(qq)
            while ii < nn:
                if folderemaillist.find(qq[ii]) != -1:
                    rigth = True
                    break
                ii+=1
            jj = 0
            mm = len(pp)
            while jj < mm:
                if folderemaillist.find(pp[jj]) != -1:
                    right = True
                    break
                jj+=1
            
            if right == False:
                i-=1
                continue
            gmailres.append(emaillist)

            i-=1    
            
    return gmailres

def foldernaverlists(a,b,naverres,q,p):
    if a.find('naver') != -1:
        imap = imaplib.IMAP4_SSL('imap.naver.com')
        try:
            imap.login(a, b)
        except:
            return False
        imap.select("INBOX")
        status, messages = imap.uid('search', None, 'ALL')

        messages = messages[0].split()

        r_email = messages[-1]

        res, msg = imap.uid('fetch', r_email, "(RFC822)")

        raw = msg[0][1].decode('utf-8')

        email_message = email.message_from_string(raw)
        d = datetime.now().date()
        date_string = email_message.get("Date")
        temp = parsedate_to_datetime(date_string)
        tempday = temp.date()

        '''
        d = datetime.now().day
        date = decode_header(email_message.get("Date"))[0]
        #print(date)
        try:
            temp = datetime.strptime(date[0], '%a, %d %b %Y %H:%M:%S %z')
        except:
            temp = datetime.strptime(date[0], '%a, %d %b %Y %H:%M:%S %Z')
        '''

        i = -1
        while d == tempday:

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
            d = datetime.now().date()
            date_string = email_message.get("Date")
            temp = parsedate_to_datetime(date_string)
            tempday = temp.date()

            '''
            d = datetime.now().day
            date = decode_header(email_message.get("Date"))[0]
            #print(date)
            try:
                temp = datetime.strptime(date[0], '%a, %d %b %Y %H:%M:%S %z')
            except:
                temp = datetime.strptime(date[0], '%a, %d %b %Y %H:%M:%S %Z')
            '''
            
            if d != tempday:
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
            emaillist = {"title":subject, "sender":fr, "detail":body, "date":temp}
            folderemaillist = subject + fr + body
            right = False
            ii = 0
            qq = arrayfilter(q)
            pp = arrayfilter(p)
            nn = len(qq)
            while ii < nn:
                if folderemaillist.find(qq[ii]) != -1:
                    rigth = True
                    break
                ii+=1
            jj = 0
            mm = len(pp)
            while jj < mm:
                if folderemaillist.find(pp[jj]) != -1:
                    right = True
                    break
                jj+=1
            
            if right == False:
                i-=1
                continue
            naverres.append(emaillist)

            i-=1    
            
    return naverres

def foldernaverbytes(a,b,naverbyte,q,p):
    if a.find('naver') != -1:
        imap = imaplib.IMAP4_SSL('imap.naver.com')
        try:
            imap.login(a,b)
        except:
            return False
        imap.select('INBOX')
        resp, data = imap.uid('search', None, 'All')
        all_email = data[0].split()
        last_email = all_email[-1]
        result, data = imap.uid('fetch', last_email, '(RFC822)')
        raw = data[0][1]
        email_message = email.message_from_bytes(raw, policy = policy.default)
        d = datetime.now().date()
        date_string = email_message.get("Date")
        temp = parsedate_to_datetime(date_string)
        tempday = temp.date()

        '''
        d = datetime.now().day
        date = decode_header(email_message.get("Date"))[0]
        #print(date)
        try:
            temp = datetime.strptime(date[0], '%a, %d %b %Y %H:%M:%S %z')
        except:
            temp = datetime.strptime(date[0], '%a, %d %b %Y %H:%M:%S %Z')
        '''

        i=-1
        while d == tempday: 
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
            #메일의 시간
            d = datetime.now().date()
            date_string = email_message.get("Date")
            temp = parsedate_to_datetime(date_string)
            tempday = temp.date()

            '''
            d = datetime.now().day
            date = decode_header(email_message.get("Date"))[0]
            #print(date)
            try:
                temp = datetime.strptime(date[0], '%a, %d %b %Y %H:%M:%S %z')
            except:
                temp = datetime.strptime(date[0], '%a, %d %b %Y %H:%M:%S %Z')
            '''

            if d != tempday:
                break
                        
            #본문 내용 출력하기
            message = ''
            if email_message.is_multipart():
                for part in email_message.walk():
                    ctype = part.get_content_type()
                    cdispo = str(part.get('Content-Disposition'))
                    if ctype == 'text/plain' and 'attachment' not in cdispo:
                        message = part.get_payload(decode=True)  # decode
                        message = message.decode('utf-8')
                        break
                    
            else:
                message = email_message.get_payload(decode=True)
            
            emaillist = {"title":subject, "sender":sender, "detail":message, "date":temp}
            folderemaillist = subject + sender + message
            right = False
            ii = 0
            qq = arrayfilter(q)
            pp = arrayfilter(p)
            nn = len(qq)
            while ii < nn:
                if folderemaillist.find(qq[ii]) != -1:
                    rigth = True
                    break
                ii+=1
            jj = 0
            mm = len(pp)
            while jj < mm:
                if folderemaillist.find(pp[jj]) != -1:
                    right = True
                    break
                jj+=1
            
            if right == False:
                i-=1
                continue
            naverbyte.append(emaillist)

            i-=1
    return naverbyte




#메일 인증 API : post로 해당 정보로 imap 로그인이 되는지 결과 반환
class ImapView2(APIView):
    def post(self, request):
        serializer = Emaillist2Serializer(data=request.data)
        tmp = request.data.get('email')
        #gmail 인증 로직
        if tmp.find('@gmail.com') != -1:
            res = request.data.get('gmailkey')
            imap = imaplib.IMAP4_SSL('imap.gmail.com')
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
    
    def get(self, request): # 연동된 메일들 보여주는 로직
        tmp = Emaillist2User.objects.filter(user_id=request.user.id)
        a = []
        n = len(tmp)
        i = 0
        if n == 0:
            return Response({"auth mail is not exist"}, status=status.HTTP_409_CONFLICT)
        while i < n:
            a.append(tmp[i].email)
            i+=1
        return Response(a, status=status.HTTP_200_OK)



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
            return False 
    
    # Blog의 detail 보기
    def get(self, request, pk, format=None):
        blog = self.get_object(pk)
        if blog == False:
            return Response("{message : not exist id}", status=status.HTTP_409_CONFLICT)
        serializer = Emaillist2Serializer(blog)
        try:
            if serializer:
                return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("{request id not existed in database}", status=status.HTTP_409_CONFLICT)
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
        print("tmp개수 : ", len(tmp))
        #tmp = tmp[0].g_key
        #tmp = str(tmp)
        res = []
        j=0
        while j < len(tmp):
            resg = tmp[j].email
            asg = tmp[j].password
            had = tmp[j].g_key
            if resg.find("gmail") != -1:
                if gmaillists(resg,had,res) == False:
                    return Response({"gmail information not righted"},status=status.HTTP_409_CONFLICT)
                res = gmaillists(resg,had,res)

            else:
                #res = naverlists(resg,asg,res)
                try:
                    if naverlists(resg,asg,res) == False:
                        return Response({"imap naver information is not matcded"}, status=status.HTTP_409_CONFLICT)
                    res = naverlists(resg,asg,res)
                except:
                    if naverbytes(resg,asg,res) == False:
                        return Response({"imap naver information ":" is not matcded"}, status=status.HTTP_409_CONFLICT)
                    res = naverbytes(resg,asg,res)
            j+=1
        print(res)
        
        return Response(res, status=status.HTTP_200_OK)

        

class FolderGetList(APIView):
    def get(self, request, pk, format=None):
        tmp = Emaillist2User.objects.filter(user_id=request.user.id)
        #rat = Folder.objects.filter(user_id=request.user.id)

        rata = Folder.objects.get(pk=pk)
        rataq = rata.sender
        ratap = rata.keyword
        #print(type(rat[pk].sender))
        #print("id is ", rat[pk].id)
        res = []
        j=0
        while j < len(tmp):
            resg = tmp[j].email
            asg = tmp[j].password
            had = tmp[j].g_key
            if resg.find('@gmail.com') != -1:
                if foldergmaillists(resg,had,res,rataq,ratap) == False:
                    return Response({"imap gmail information":" is not matched"}, status=status.HTTP_409_CONFLICT)
                res = foldergmaillists(resg,had,res,rataq,ratap)
            else:
                try:
                    if foldernaverlists(resg,asg,res,rataq,ratap) == False:
                        return Response({"imap naver information":" is not matched"}, status=status.HTTP_409_CONFLICT)
                    res = foldernaverlists(resg,asg,res,rataq,ratap)
                except:
                    if foldernaverlists(resg,asg,res,rataq,ratap) == False:
                        return Response({"imap naver information":" is not matched"}, status=status.HTTP_409_CONFLICT)
                    res = foldernaverlists(resg,asg,res,rataq,ratap)
            j+=1


        return Response(res, status=status.HTTP_200_OK)