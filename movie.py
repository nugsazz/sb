import lineX
from lineX import *
from akad.ttypes import *
from thrift.Thrift import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift.protocol import TCompactProtocol
from thrift import transport, protocol, server
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess,asyncio
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, urllib, urllib.parse,youtube_dl,pafy,timeit,atexit,traceback,ffmpy,humanize
_session = requests.session()
botStart = time.time()
movieOp = codecs.open("movie.json","r","utf-8")
sett = codecs.open("set.json","r","utf-8")
menu = codecs.open("help.json","r","utf-8")
mengirim = json.load(movieOp)
set = json.load(sett)
plate = json.load(menu)
print("___________[SELFBOT ONLY]___________")
#me = LINE() # INI LOGIN LANGSUNG
#me = LINE("gmail.com", "passwd") #ini kalo mau pake gmail
me = LINE("EFbnMivO7Xm9Xwv1esp2.eZ9Xen0a5JxWD2LxG3bvOG.auEST/V7kVkknXieXhKxm9xeuL0nn80PI1mMmGaev3E=")
print("___________[LOGIN SUCCESS]___________")
oepoll = OEPoll(me)
# BATAS MID

meM = me.getProfile().mid
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
    
jakaProfile = me.getProfile()
myProfile["displayName"] = jakaProfile.displayName
myProfile["statusMessage"] = jakaProfile.statusMessage
myProfile["pictureStatus"] = jakaProfile.pictureStatus
meSettings = me.getSettings()

set = {
  "Key": False,
  "text": "acil:"
}
def Comt(text):
  pesan = text.lower()
  if set["Key"] == True:
    if pesan.startswith(set["text"]):
      Pbot = pesan.replace(set["text"],"")
    else:
      Pbot = "Undefined command"
  else:
    Pbot = text.lower()
  return Pbot
def backupData():
  try:
    backup = set
    f = codecs.open('set.json','w','utf-8')
    json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
    return True
  except Exception as e:
    print(e)
    return False

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "╭━━━━━━━━━━━━━━━━━━━━╮\n├ ☠ MENTION [ {} ] MEMBER\n├━━━━━━━━━━━━━━━━━━━━\n├[1.]☠".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@InexBots\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "├[%i.]☠ " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚☠•➤[ {} ]".format(str(me.getGroup(to).name))
                except:
                    no = "\n╚☠•➤[ Success ]"
        me.sendMessage(to, textx+"╰━━━━━━━━━━━━━━━━━━━━╯", {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)

def sendTextTemplate(to, text):
    warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
    warnanya1 = random.choice(warna1)
    data = {
        "type": "flex",
        "altText": "InexBots",
        "contents": {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": text,
                        "color": "#3800E0",
                        "wrap": True
                    }
                ]
            }
        }
    }
    me.sendFlex(to, data)

def sendTextTemplate1(to, text):
    warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
    warnanya1 = random.choice(warna1)
    data = {
            "type": "flex",
            "altText": "HELP XTC INEX",
            "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "sm",
            "weight": "bold",
            "wrap": True,
            "color": "#40ff00"
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#03f5f1"
    },
    "header": {
      "backgroundColor": "#03f5f1"
    }
    },  
     "hero": {
     "type": "image",
     "aspectRatio": "20:13",
     "aspectMode": "cover",
     "url": "https://media.giphy.com/media/67pVlH3LSLDjTBikzf/giphy.gif",
     "size": "full",
     "margin": "xl"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#ff0a3b",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "OFFICIAL",
                  "uri": "https://line.me/R/ti/p/%40bvb1195k"
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#310dff",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "CREATOR",
                  "uri": "http://line.me/ti/p/~denjaka-inexx"
              }
          }]
      }]
  }
}
}
    me.sendFlex(to, data)

def template(op):
  global threading
  global groupParam
  global rsa
  try:
    if op.type == 0:
      return
    if op.type == 25 or op.type == 26: # INI PUBLIK SAMA SELF JALAN KABEH
      self = op.message
      to = self.to
      Id = self.id
      text = self.text
      if self.toType == 0 or self.toType == 1 or self.toType == 2:
        if self.toType == 0:
          if self._from != me.profile.mid:
            to = self._from
          else:
            to = self.to
        elif self.toType == 1:
          to = self.to
        elif self.toType == 2:
          to = self.to
        elif self.contentType == 16:
             if set["Timeline"] == True:
                     ret_ = "☠•➤ Detail Postingan☠•➤"
                     if self.contentMetadata["serviceType"] == "GB":
                         contact = me.getContact(self._from)
                         auth = "\n☠•➤  Penulis : {}".format(str(contact.displayName))
                     else:
                         auth = "\n☠•➤  Penulis : {}".format(str(self.contentMetadata["serviceName"]))
                     ret_ += auth
                     if "stickerId" in self.contentMetadata:
                         stck = "\n☠•➤  Stiker : https://line.me/R/shop/detail/{}".format(str(self.contentMetadata["packageId"]))
                         ret_ += stck
                     if "mediaOid" in self.contentMetadata:
                         object_ = self.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                         if self.contentMetadata["mediaType"] == "V":
                             if self.contentMetadata["serviceType"] == "GB":
                                 ourl = "\n☠•➤  Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(self.contentMetadata["mediaOid"]))
                                 murl = "\n☠•➤  Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(self.contentMetadata["mediaOid"]))
                             else:
                                 ourl = "\n☠•➤  Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                 murl = "\n☠•➤  Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                             ret_ += murl
                         else:
                             if self.contentMetadata["serviceType"] == "GB":
                                 ourl = "\n☠•➤  Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(self.contentMetadata["mediaOid"]))
                             else:
                                 ourl = "\n☠•➤  Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                         ret_ += ourl
                     if "text" in self.contentMetadata:
                         text = "\n☠•➤  Tulisan : {}".format(str(self.contentMetadata["text"]))
                         purl = "\n☠•➤  Post URL : {}".format(str(self.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                         ret_ += purl
                         ret_ += text
                     me.sendMessage(to, "Done")
                     me.likePost(url[25:58], url[66:], likeType=1001)                                                        
                     me.createComment(url[25:58], url[66:], "╭━━━━━━━━━━━━━━━━━━━━━━━━\n┃ ╔══════════════════━━━━╮\n┃ ║   ❀     BY BOT : INEXBOTS    ❀\n┃ ╚══════════════════━━━━╯\n├━━━━━━━━━━━━━━━━━━━━━━━━\n┃ ╔══════════════════━━━━╮\n┃ ║  ❀ LIKE DONE \n┃ ║  ❀ COMMENT DONE \n┃ ║  ❀ INEXBOTS_TEAM\n┃ ╚══════════════════━━━━╯\n├━━━━━━━━━━━━━━━━━━━━━━━━\n┃ ╔══════════════════━━━━╮\n┃ ║  http://line.me/ti/p/~denjaka-inexx\n┃ ╚══════════════════━━━━╯\n╰━━━━━━━━━━━━━━━━━━━━━━━━")
                     me.sendMessage(to, "Like done")
                     if self.toType in (2,1,0):
                         purl = self.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
                         adw = me.likePost(purl[0], purl[1], random.choice([1001,1002,1003,1004,1005]))
                         adws = me.createComment(purl[0], purl[1], "╭━━━━━━━━━━━━━━━━━━━━━━━━\n┃ ╔══════════════════━━━━╮\n┃ ║   ❀     BY BOT : INEXBOTS    ❀\n┃ ╚══════════════════━━━━╯\n├━━━━━━━━━━━━━━━━━━━━━━━━\n┃ ╔══════════════════━━━━╮\n┃ ║  ❀ LIKE DONE \n┃ ║  ❀ COMMENT DONE \n┃ ║  ❀ INEXBOTS_TEAM\n┃ ╚══════════════════━━━━╯\n├━━━━━━━━━━━━━━━━━━━━━━━━\n┃ ╔══════════════════━━━━╮\n┃ ║  http://line.me/ti/p/~denjaka-inexx\n┃ ╚══════════════════━━━━╯\n╰━━━━━━━━━━━━━━━━━━━━━━━━")
                         data = {
        "type": "template",
        "altText": "AUTO LIKE",
        "template": {
            "type": "carousel",
            "actions": [],
            "columns": [
                {
                    "thumbnailImageUrl": "https://scontent.fcgk8-1.fna.fbcdn.net/v/t1.0-9/fr/cp0/e15/q65/51689146_2326064860750957_3568131342002552832_o.jpg?_nc_cat=100&efg=eyJpIjoiYiJ9&_nc_eui2=AeEKUakDYnXikuMkE8vPPZhxEuKQRqPyo08BbWoruGL-DN9mYH2NmCnik886MGJCiMS8D7ZSUmabSAcRk7S3_GwwhAIKCVBmiq32OaYa0XaV-w&_nc_ht=scontent.fcgk8-1.fna&oh=18937dc8439c5fdf7c9de33c6f00fad6&oe=5D0231F5",
                    "title": "{}".format(me.getContact(srlf._from).displayName),
                    "text": "ᴀᴜᴛᴏ ʟɪᴋᴇ ɴ ᴄᴏᴍᴍᴇɴᴛ ᴅᴏɴᴇ\nвʏ.ᴛᴇᴀᴍ ⊶ ɪɴᴇxʙᴏᴛs ⊷",
                    "actions": [
                        {
                            "type": "uri",
                            "label": "CREATOR",
                            "uri": "http://line.me/ti/p/~denjaka-inexx"
                        }
                      ]
                    }
                  ]
                }
               }
                         me.sendFlex(to, data)
        if self.contentType == 0:
          if text is None:
            return
          else:
            Pbot = Comt(text)
            if Pbot == "movie":
              me.sendFlex(to, mengirim["movie"])
            if Pbot == "sepi":
              sendTextTemplate1(to, "╔════╗╔════\n║▓▓▓█║║▓▓▓█\n║▓▓▓█║║▓▓▓█\n║▓▓▓█╚╝▓▓▓█\n║▓▓▓▓▓▓▓▓▓█\n║▓▓▓▓▓▓▓▓▓█\n║▓▓▓█╔╗▓▓▓█\n║▓▓▓█║║▓▓▓█\n║▓▓▓█║║▓▓▓█\n╚╦═══╝╚═══\n╔╝▓▓▓▓▓▓▓█\n║▓▓▓▓▓▓▓▓▓█\n║▓▓▓█╔╗▓▓▓█\n║▓▓▓█╚╝▓▓▓█\n║▓▓▓▓▓▓▓▓▓█\n║▓▓▓▓▓▓▓▓▓█\n║▓▓▓█╔╗▓▓▓█\n║▓▓▓█║║▓▓▓█\n╠════╝╚══\n║▓▓▓▓▓▓▓█\n║▓▓▓▓▓▓▓▓█\n║▓▓▓█║▓▓▓▓█\n║▓▓▓█╚╗▓▓▓█\n║▓▓▓█╔╝▓▓▓█\n║▓▓▓█║▓▓▓▓█\n║▓▓▓▓▓▓▓▓█\n║▓▓▓▓▓▓▓█\n╩╦══════\n═║▓▓▓▓▓█\n═║▓▓▓▓▓█\n═╚╗▓▓▓█\n══║▓▓▓█\n══║▓▓▓█\n═╔╝▓▓▓█\n═║▓▓▓▓▓█\n═║▓▓▓▓▓█\n╔╩══════\n║▓▓▓▓▓▓▓▓█\n║▓▓▓█║▓▓▓▓█\n║▓▓▓█╠═▓▓▓█\n║▓▓▓█║▓▓▓█\n║▓▓▓▓▓▓▓█\n║▓▓▓█▓▓▓█\n║▓▓▓█║▓▓▓█\n║▓▓▓█╠╗▓▓▓█\n╚════╝╚═══")
            if Pbot == "help":
              me.sendFlex(to, plate["help"])
            if Pbot == "price":
              me.sendFlex(to, plate["pricelist"])
            if Pbot == "galeri":
              me.sendFlex(to, plate["galery"])
            if Pbot == "memberpict":
              kontak = me.getGroup(to)
              group = kontak.members
              picall = []
              for ids in group:
                if len(picall) >= 400:
                  pass
                else:
                  picall.append({
                                  "imageUrl": "https://os.line.naver.jp/os/p/{}".format(ids.mid),
                                  "action": {
                                    "type": "uri",
                                    "uri": "http://line.me/ti/p/~denjaka-inexx"
                                   }
                                 }
                               )
                  k = len(picall)//10
                  for aa in range(k+1):
                    data = {
                                "type": "template",
                                "altText": "{} Membagikan janda geratis".format(jakaProfile.displayName),
                                "template": {
                                  "type": "image_carousel",
                                  "columns": picall[aa*10 : (aa+1)*10]
                                }
                              }
                    me.sendFlex(to, data)
            if Pbot == "me":
              h = me.getContact(self._from)
              cover = me.getProfileCoverURL(self._from)
              me.reissueUserTicket()
              data = {
                             "type": "flex",
                             "altText": "{} Berak di celana".format(str(h.displayName)),
                             "contents": {
                              "type": "bubble",
                              "styles": {
                                "header": {
                                  "backgroundColor": "#0000FF",
                                },
                                "body": {
                                  "backgroundColor": "#000080",
                                  "separator": True,
                                  "separatorColor": "#ffffff"
                                },
                                "footer": {
                                  "backgroundColor": "#0000FF",
                                  "separator": True
                                }
                              },
                              "header": {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": "  ɪɴᴅᴏɴᴇsɪᴀ_ᴡᴀʀs",
                                    "weight": "bold",
                                    "color": "#00ffff",
                                    "size": "xxl"
                                  }
                                ]
                              },
                              "hero": {
                                "type": "image",
                                "url": "https://os.line.naver.jp/os/p/{}".format(self._from),
                                "size": "full",
                                "aspectRatio": "20:13",
                                "aspectMode": "cover",
                                "action": {
                                  "type": "uri",
                                  "uri": "https://line.me/ti/p/~denjaka-inexx"
                                }
                              },
                              "body": {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "md",
                                "action": {
                                  "type": "uri",
                                  "uri": "https://line.me/ti/p/~denjaka-inexx"
                                },
                                "contents": [
                                  {
                                    "type": "text",
                                    "text": h.displayName,
                                    "size": "md",
                                    "color": "#00ffff"
                                  },
                                  {
                                    "type": "box",
                                    "layout": "vertical",
                                    "spacing": "sm",
                                    "contents": [
                                      {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                          {
                                            "type": "icon",
                                            "url": "https://scontent.fcgk8-1.fna.fbcdn.net/v/t1.0-9/fr/cp0/e15/q65/51689146_2326064860750957_3568131342002552832_o.jpg?_nc_cat=100&efg=eyJpIjoiYiJ9&_nc_eui2=AeEKUakDYnXikuMkE8vPPZhxEuKQRqPyo08BbWoruGL-DN9mYH2NmCnik886MGJCiMS8D7ZSUmabSAcRk7S3_GwwhAIKCVBmiq32OaYa0XaV-w&_nc_ht=scontent.fcgk8-1.fna&oh=18937dc8439c5fdf7c9de33c6f00fad6&oe=5D0231F5",
                                            "size": "5xl"
                                          },
                                          {
                                          "type": "icon",
                                            "url": cover,
                                            "size": "5xl"
                                            },
                                          {
                                          "type": "icon",
                                            "url": "https://scontent.fcgk9-2.fna.fbcdn.net/v/t1.0-9/fr/cp0/e15/q65/51890364_2326064870750956_7074549303951228928_o.jpg?_nc_cat=101&efg=eyJpIjoiYiJ9&_nc_eui2=AeEc5YaEyHcma96fQknN77Ts31Vr9tB56EhCg-oA5nemHcUDHDJVLdsSRS60nE-ufyQ7xv-MfMuTt-wlw8hXtAdUltq0Wf_75ALi3hFg3rvvtw&_nc_ht=scontent.fcgk9-2.fna&oh=6f2ad391c533b3533c3533ccefb5839d&oe=5D734262",
                                            "size": "5xl"
                                          }
                                        ]
                                      }
                                    ]
                                  },
                                  {
                                    "type": "text",
                                    "text": "_________________________________________________\nɬɧąŋƙʂ ɬơ ąƖƖąɧ \nɬɧąŋƙʂ ɬơ ℘ཞąŋƙცơɬʂ,\nąŋɖ ɬɧąŋƙʂ ɬơ ıŋɛҳ ɬɛąɱ.",
                                    "wrap": True,
                                    "color": "#aaaaaa",
                                    "size": "xxs"
                                  }
                                ]
                              },
                              "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                  {
                                    "type": "spacer",
                                    "size": "sm"
                                  },
                                  {
                                    "type": "button",
                                    "style": "primary",
                                    "color": "#10CF08",
                                    "action": {
                                      "type": "uri",
                                      "label": "CONTACT",
                                      "uri": "https://line.me/ti/p/"+me.getUserTicket().id
                                    }
                                  }
                                ]
                              }
                             }
                            }
              me.sendFlex(to, data)
            if Pbot == "mention":
              group = me.getGroup(self.to)
              nama = [contact.mid for contact in group.members]
              k = len(nama)//20
              for a in range(k+1):
                  txt = u''
                  s=0
                  b=[]
                  for i in group.members[a*20 : (a+1)*20]:
                      b.append(i.mid)
                  mentionMembers(to, b)
            if Pbot == "speed":
              start = time.time()
              sendTextTemplate(to, "Speed Ngaciiirrr...")
              elapsed_time = time.time() - start
              sendTextTemplate(to, "{} detik".format(str(elapsed_time)))
            if Pbot == "cek":
              try:me.inviteIntoGroup(to, ["u45882d0ead1703855dbc60d40e37bec7"]);has = "OK"
              except:has = "NOT"
              try:me.kickoutFromGroup(to, ["u45882d0ead1703855dbc60d40e37bec7"]);has1 = "OK"
              except:has1 = "NOT"
              if has == "OK":sil = "ś̵̢̨͕̋̽͛̇̿̚e̷̗͍̩͚͚̗͔̾ḩ̴̛̞̬̝̟̘̭̾̊͑́͛̒̓̈́͒ͅȃ̴̞͇̗̭̪͖̦̜̫̞͗͑́̈́̀͘t̶̮͕͉̂̉̐̀́͜"
              else:sil = "ֆǟӄɨȶ"
              if has1 == "OK":sil1 = "ś̵̢̨͕̋̽͛̇̿̚e̷̗͍̩͚͚̗͔̾ḩ̴̛̞̬̝̟̘̭̾̊͑́͛̒̓̈́͒ͅȃ̴̞͇̗̭̪͖̦̜̫̞͗͑́̈́̀͘t̶̮͕͉̂̉̐̀́͜"
              else:sil1 = "ֆǟӄɨȶ"
              sendTextTemplate(to, "🄺🄸🄲🄺 : {} \n🄸🄽🅅🄸🅃🄴 : {}".format(sil1,sil))
            if Pbot == "profile":
              contact = me.getContact(self._from)
              cover = me.getProfileCoverURL(self._from)
              me.reissueUserTicket()
              res = "╭━━━━━━━━━━━━━━━━━━━━╮\n├ ☠ Profile info\n├━━━━━━━━━━━━━━━━━━━━\n"
              res += "├ ☠ Display Name :{}\n".format(contact.displayName)
              res += "├ ☠ Mid: {}\n".format(contact.mid)
              res += "├ ☠ Status Message\n├ ☠ {}\n".format(contact.statusMessage)
              res += "╰━━━━━━━━━━━━━━━━━━━━╯"
              sendTextTemplate(to, res)
              try:
                poto = "https://os.line.naver.jp/os/p/{}".format(self._from)
              except:
                poto = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQcNdUbC8kEeVWqgR9qMX66lQ_hQPM8ScNY30x4nqpYaKY2jt02"
              dax = {
                "type": "template",
                "altText": "berak di celana",
                "template": {
                  "type": "image_carousel",
                  "columns": [
                    {
                      "imageUrl": poto,
                      "layout": "horizontal",
                      "action": {
                        "type": "uri",
                        "label": "PROFILE",
                        "uri": poto,
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    },
                    {
                      "imageUrl": cover,
                      "layout": "horizontal",
                      "action": {
                        "type": "uri",
                        "label": "COVER",
                        "uri": cover,
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    },
                    {
                      "imageUrl": "https://qr-official.line.me/L/"+me.getUserTicket().id+".png",
                      "layout": "horizontal",
                      "action": {
                        "type": "uri",
                        "label": "CONTACT",
                        "uri": "https://line.me/ti/p/"+me.getUserTicket().id,
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    }
                  ]
                }
              }
              me.sendFlex(to, dax)

            if Pbot == "memberlist":
              group = me.getGroup(to)
              ret_ = "╭━━━══[ Member List ]"
              no = 0 + 1
              for mem in group.members:
                ret_ += "\n{}. {}".format(str(no), str(mem.displayName))
                no += 1
              ret_ += "\n╰━━━══[ Total {} member]".format(str(len(group.members)))
              sendTextTemplate1(to, ret_)
              
  except Exception as e:
    print(e)
    if op.type == 59:
      print(op)
while True:
  try:
    ops=oepoll.singleTrace(count=50)
    if ops != None:
      for op in ops: 
        template(op)
        oepoll.setRevision(op.revision)       
  except Exception as e:
    me.log("ERROR\n IN [ " + " ] == " + str(e) + "INI HARUS DI PERBAIKI")
