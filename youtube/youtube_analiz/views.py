import re

from django.shortcuts import redirect, render
import pandas as pd
from pyparsing import DebugExceptionAction
import requests
import json
import joblib
from django.contrib.auth.models import User
from youtube_analiz.models import Video
from youtube_analiz.models import Comment
key="ENTER YOUR GOOGLE DEVELOPER KEY" 


import requests

API_URL = "https://api-inference.huggingface.co/models/nanelimon/bert-base-turkish-bullying"
headers = {"Authorization": f"Bearer YOUR_HUGGING_FACE_KEY"}



def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	

def get_comments(video_id):
    url="https://www.googleapis.com/youtube/v3/commentThreads"
    params={
        'part':'snippet',
        'video_id':video_id,
        'key':key,
        "maxResults":500,
    }
    r=requests.get(url,params)
    data=r.json()

    yorum_listesi=[]
    author_list=[]
    like_count_list=[]
    reply_count_list=[]
    author_profile_list=[]
    author_url_list=[]
    zorbalık_list=[]
    comment_id_list=[]
    for item in data['items']:
        yorum=item['snippet']['topLevelComment']['snippet']['textOriginal']
        author=item['snippet']['topLevelComment']['snippet']['authorDisplayName']
        like_count=item['snippet']['topLevelComment']['snippet']['likeCount']
        reply_count=item['snippet']['totalReplyCount']
        author_profile=item['snippet']['topLevelComment']['snippet']['authorProfileImageUrl']
        author_url=item['snippet']['topLevelComment']['snippet']['authorChannelUrl']
        zorbalık=query({"inputs":yorum})#same_pipe(yorum)[0]['label']
        zorbalık=zorbalık[0][0]['label']
        comment_id=item['id']

        if Comment.objects.filter(comment=comment_id).exists():
            print("")
        else:
            video=Video.objects.filter(video=video_id).first()
            db_video=Comment(video=video,comment=comment_id,text=yorum,writer=author,like_count=int(like_count),reply_count=int(reply_count),writer_url=author_url,writer_image=author_profile,zorbalık=zorbalık)
            db_video.save()

        yorum_listesi.append(yorum)
        author_list.append(author)
        like_count_list.append(like_count)
        reply_count_list.append(reply_count)
        author_profile_list.append(author_profile)
        author_url_list.append(author_url)
        zorbalık_list.append(zorbalık)
        comment_id_list.append(comment_id)


    return  yorum_listesi,author_list,like_count_list, reply_count_list,author_profile_list,author_url_list,zorbalık_list,comment_id_list



def get_video(video_id,username):
    user=User.objects.filter(username=username).first()
        
    url="https://www.googleapis.com/youtube/v3/videos"
    params={
        'part':'snippet',
        'id':video_id,
        'key':key,
        "maxResults":500,
    }
    r=requests.get(url,params)
    data=r.json()
    title=data['items'][0]['snippet']['title']
    channel_title=data['items'][0]['snippet']['channelTitle']
    video_image=data['items'][0]['snippet']['thumbnails']['medium']['url']
    description=data['items'][0]['snippet']['description']
    if Video.objects.filter(user=user,video=video_id).exists():
        print("")
    else:
        Video.objects.create(user=user,video=video_id,title=title,channel_title=channel_title,video_image=video_image,description=description)
        
        


    #return title,channel_title,video_image,description



# Create your views here.
def anasayfa_view(request):

    return render(request,"index.html")


    

def comment_detail(request):

   
    username=request.user.username
    link= request.POST['link']
    
    link=link.split("v=")[1]
    link=link[0:11]
    print(link)
    get_video(link,username)
    get_comments(link)
    output = query({
    })
    

    return redirect('video')
    
    

def video(request):


    title_list=[]
    channel_title_list=[]
    video_image_list=[]
    description_list=[]
    
    videos=Video.objects.filter(user=request.user)
    for video in videos:
        
        title_list.append(video.title)
        channel_title_list.append(video.channel_title)
        video_image_list.append(video.video_image)
        description_list.append(video.description)

    title_list.reverse()
    channel_title_list.reverse()
    video_image_list.reverse()
    description_list.reverse()
    videos=reversed(videos)

    data = {"videos":videos,"title":title_list,"channel_title":channel_title_list,"video_image":video_image_list,"description":description_list}
    df = pd.DataFrame(data)
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    return render(request,"video.html",context)


def video_details(request,videoId):
    
    yorum_listesi=[]
    author_list=[]
    like_count_list=[]
    reply_count_list=[]
    author_profile_list=[]
    author_url_list=[]
    zorbalık_list=[]
    comment_id_list=[]

    video=Video.objects.filter(video=videoId).first()
    videos=Comment.objects.filter(video=video)
    print(videos)


    
    for video in videos:
        
        yorum_listesi.append(video.text)
        author_list.append(video.writer)
        like_count_list.append(video.like_count)
        reply_count_list.append(video.reply_count)
        author_profile_list.append(video.writer_image)
        author_url_list.append(video.writer_url)
        zorbalık_list.append(video.zorbalık)
        comment_id_list.append(video.comment)

    yorum_listesi.reverse()
    author_list.reverse()
    like_count_list.reverse()
    reply_count_list.reverse()
    author_profile_list.reverse()
    author_url_list.reverse()
    zorbalık_list.reverse()
    comment_id_list.reverse()
    #videos=reversed(videos)
  
    #yorum_listesi,author_list,like_count_list, reply_count_list,author_profile_list,author_url_list,zorbalık_list,comment_id_list= get_comments(videoId)


    
    counter=len(yorum_listesi)
    data = {
    "yorum": yorum_listesi,
    "author": author_list,
    "like":like_count_list,
    "reply":reply_count_list,
    "profile":author_profile_list,
    "url":author_url_list,
    "zorbalik":zorbalık_list,
    "comment_id":comment_id_list,

    }
    df = pd.DataFrame(data)
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data,"counter":counter,"video":videoId}
    return render(request,"video_detail.html",context)
   


def comment_detail_2(request,videoId,commentId):

    video=Video.objects.filter(video=videoId).first()
    comment=Comment.objects.filter(video=video,comment=commentId)
    print(comment.first().text)

    output = query({
	"inputs": comment.first().text
    })
    
    context = {'d': output,"text":comment.first().text}
    return render(request,"comment_detail.html",context)

def deletevideo_confirm(request,videoId):
    video=Video.objects.filter(video=videoId)
    return render(request,"video_confirm_delete.html",{"video":video.first()})

def deletevideo(request,videoId):
    Video.objects.filter(user=request.user,video=videoId).delete()
    return redirect('video')

def hakkinda(request):
    
    return render(request,"hakkında.html")
