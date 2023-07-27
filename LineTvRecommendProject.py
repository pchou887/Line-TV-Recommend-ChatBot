import pymongo
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import FlexSendMessage, TextSendMessage, ImageSendMessage
import random
import requests as req
from bs4 import BeautifulSoup
import json

line_bot_api = LineBotApi('BXylMToBBy0xf0N6OZI9sYk8Itc6VB513OV9jzkPZ2y32H0FfGh0Bd9opczT31CHtiApwmzCdZAgm92HDIrT9L36VSsxVc5t1X1M3tTxupL4VzCBgFJc25L7kDe4BplND1YdIVXPwVp0FHo2Ke+6wgdB04t89/1O/w1cDnyilFU=')
client = pymongo.MongoClient("mongodb+srv://chou1998:king1998@cluster0.h9aoseu.mongodb.net/?retryWrites=true&w=majority")

def top10(tk):
    res = req.get("https://www.linetv.tw/")
    soup = BeautifulSoup(res.text)
    j = json.loads(soup.find("script").text[27:])
    count = 0
    bk = 0
    r = []
    for search in j['ssrData']['https://api.linetv.tw/v2/index']:
        if search["title"] == "熱播排行榜":
            for d in search["datas"]:
                r.append([d["data"]["posterUrl"], "https://www.linetv.tw/drama/"+ str(d["data"]["id"]), d["data"]["name"]]) #圖片網址 網址 劇名
                count += 1
                if count == 10:
                    bk = 1
                    break
        elif bk == 1:
            break
    line_bot_api.reply_message(tk, FlexSendMessage(alt_text='你有一則新訊息',contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": r[0][0],
        "size": "full",
        "aspectRatio": "30:20",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Line",
          "uri": r[0][1]
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "No.1",
            "contents": []
          },
          {
            "type": "text",
            "text": r[0][2],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "速速看劇去",
              "uri": r[0][1]
            },
            "height": "sm",
            "style": "link"
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": r[1][0],
        "size": "full",
        "aspectRatio": "30:20",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Line",
          "uri": r[1][1]
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "No.2",
            "contents": []
          },
          {
            "type": "text",
            "text": r[1][2],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "速速看劇去",
              "uri": r[1][1]
            },
            "height": "sm",
            "style": "link"
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": r[2][0],
        "size": "full",
        "aspectRatio": "30:20",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Line",
          "uri": r[2][1]
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "No.3",
            "contents": []
          },
          {
            "type": "text",
            "text": r[2][2],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "速速看劇去",
              "uri": r[2][1]
            },
            "height": "sm",
            "style": "link"
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": r[3][0],
        "size": "full",
        "aspectRatio": "30:20",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Line",
          "uri": r[3][1]
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "No.4",
            "contents": []
          },
          {
            "type": "text",
            "text": r[3][2],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "速速看劇去",
              "uri": r[3][1]
            },
            "height": "sm",
            "style": "link"
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": r[4][0],
        "size": "full",
        "aspectRatio": "30:20",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Line",
          "uri": r[4][1]
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "No.5",
            "contents": []
          },
          {
            "type": "text",
            "text": r[4][2],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "速速看劇去",
              "uri": r[4][1]
            },
            "height": "sm",
            "style": "link"
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": r[5][0],
        "size": "full",
        "aspectRatio": "30:20",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Line",
          "uri": r[5][1]
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "No.6",
            "contents": []
          },
          {
            "type": "text",
            "text": r[5][2],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "速速看劇去",
              "uri": r[5][1]
            },
            "height": "sm",
            "style": "link"
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": r[6][0],
        "size": "full",
        "aspectRatio": "30:20",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Line",
          "uri": r[6][1]
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "No.7",
            "contents": []
          },
          {
            "type": "text",
            "text": r[6][2],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "速速看劇去",
              "uri": r[6][1]
            },
            "height": "sm",
            "style": "link"
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": r[7][0],
        "size": "full",
        "aspectRatio": "30:20",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Line",
          "uri": r[7][1]
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "No.8",
            "contents": []
          },
          {
            "type": "text",
            "text": r[7][2],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "速速看劇去",
              "uri": r[7][1]
            },
            "height": "sm",
            "style": "link"
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": r[8][0],
        "size": "full",
        "aspectRatio": "30:20",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Line",
          "uri": r[8][1]
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "No.9",
            "contents": []
          },
          {
            "type": "text",
            "text": r[8][2],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "速速看劇去",
              "uri": r[8][1]
            },
            "height": "sm",
            "style": "link"
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": r[9][0],
        "size": "full",
        "aspectRatio": "30:20",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Line",
          "uri": r[9][1]
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "No.10",
            "contents": []
          },
          {
            "type": "text",
            "text": r[9][2],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "速速看劇去",
              "uri": r[9][1]
            },
            "height": "sm",
            "style": "link"
          }
        ]
      }
    }
  ]
}
))

    
def reply(tk, rc):
    r = []
    top = 5
    down = 4.5
    results = list(rc.find(
        {"評分": {"$gt": down, "$lte": top}}
    ))
    if not len(results):
        while len(r) < 5 and top > 0:
            top -= 0.5
            down -= 0.5
            results = list(rc.find(
                {"評分": {"$gt": down, "$lte": top}}
            ))
            if len(results):
                for t in results:
                    r.append([t["劇照"], t["url"], t["劇名"]])
    else :
        for t in results:
            r.append([t["劇照"], t["url"], t["劇名"]])
        while len(r) < 5 and top > 0:
            top -= 0.5
            down -= 0.5
            results = list(rc.find(
                {"評分": {"$gt": down, "$lte": top}}
            ))
            if len(results):
                for t in results:
                    r.append([t["劇照"], t["url"], t["劇名"]])
    r = random.sample(r, len(r))
    if len(r) >= 5:
        r = r[:5]
        line_bot_api.reply_message(tk, FlexSendMessage(alt_text='你有一則新訊息',contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": r[0][0],
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Line",
          "uri": r[0][1]
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": r[0][2],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "迫不及待追起來",
              "uri": r[0][1]
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": r[1][0],
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Line",
          "uri": r[1][1]
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": r[1][2],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "迫不及待追起來",
              "uri": r[1][1]
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": r[2][0],
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Line",
          "uri": r[2][1]
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": r[2][2],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "迫不及待追起來",
              "uri": r[2][1]
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": r[3][0],
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Line",
          "uri": r[3][1]
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": r[3][2],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "迫不及待追起來",
              "uri": r[3][1]
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": r[4][0],
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Line",
          "uri": r[4][1]
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": r[4][2],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "迫不及待追起來",
              "uri": r[4][1]
            }
          }
        ]
      }
    }
  ]
}))
    elif len(r) == 4:
        r = r[:4]
        line_bot_api.reply_message(tk, FlexSendMessage(alt_text='你有一則新訊息',contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": r[0][0],
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Line",
          "uri": r[0][1]
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": r[0][2],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "迫不及待追起來",
              "uri": r[0][1]
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": r[1][0],
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Line",
          "uri": r[1][1]
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": r[1][2],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "迫不及待追起來",
              "uri": r[1][1]
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": r[2][0],
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Line",
          "uri": r[2][1]
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": r[2][2],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "迫不及待追起來",
              "uri": r[2][1]
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": r[3][0],
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Line",
          "uri": r[3][1]
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": r[3][2],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "迫不及待追起來",
              "uri": r[3][1]
            }
          }
        ]
      }
    }
  ]
}))
    elif len(r) == 3:
        r = r[:3]
        line_bot_api.reply_message(tk, FlexSendMessage(alt_text='你有一則新訊息',contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": r[0][0],
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Line",
          "uri": r[0][1]
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": r[0][2],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "迫不及待追起來",
              "uri": r[0][1]
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": r[1][0],
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Line",
          "uri": r[1][1]
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": r[1][2],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "迫不及待追起來",
              "uri": r[1][1]
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": r[2][0],
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Line",
          "uri": r[2][1]
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": r[2][2],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "迫不及待追起來",
              "uri": r[2][1]
            }
          }
        ]
      }
    }
  ]
}))
    elif len(r) == 2:
        r = r[:2]
        line_bot_api.reply_message(tk, FlexSendMessage(alt_text='你有一則新訊息',contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": r[0][0],
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Line",
          "uri": r[0][1]
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": r[0][2],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "迫不及待追起來",
              "uri": r[0][1]
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": r[1][0],
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Line",
          "uri": r[1][1]
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": r[1][2],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "迫不及待追起來",
              "uri": r[1][1]
            }
          }
        ]
      }
    }
  ]
}))
    elif len(r) == 1:
        line_bot_api.reply_message(tk, FlexSendMessage(alt_text='你有一則新訊息',contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": r[0][0],
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Line",
          "uri": r[0][1]
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": r[0][2],
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "flex": 0,
        "spacing": "sm",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "迫不及待追起來",
              "uri": r[0][1]
            }
          }
        ]
      }
    }
  ]
}))
    else:
        line_bot_api.reply_message(tk, TextSendMessage("很抱歉！目前此種類沒有影片！"))
    
    
def drama(text, rtk):
    drama_list = ["職場","校園","家庭","古裝","愛情","都會","改編","甜寵","懸疑","喜劇","勵志","BL","奇幻","在地","驚悚","療癒","仙俠","穿越","時代"]
    if text not in drama_list:
        line_bot_api.reply_message(rtk, TextSendMessage("請輸入正確選單格式！"))
    else:
        db = client.drama
        if text == "職場":
            c = db.drama_workplace
        elif text == "校園":
            c = db.drama_school
        elif text == "家庭":
            c = db.drama_family
        elif text == "古裝":
            c = db.drama_costume
        elif text == "愛情":
            c = db.drama_love
        elif text == "都會":
            c = db.drama_city
        elif text == "改編":
            c = db.drama_adaptation
        elif text == "甜寵":
            c = db.drama_sweet
        elif text == "懸疑":
            c = db.drama_suspenseful
        elif text == "喜劇":
            c = db.drama_comedy
        elif text == "勵志":
            c = db.drama_inspirational
        elif text == "BL":
            c = db.drama_bl
        elif text == "奇幻":
            c = db.drama_fantasy
        elif text == "在地":
            c = db.drama_local
        elif text == "驚悚":
            c = db.drama_thriller
        elif text == "療癒":
            c = db.drama_heal
        elif text == "仙俠":
            c = db.drama_chivalrous
        elif text == "穿越":
            c = db.drama_time_travel
        elif text == "時代":
            c = db.drama_period
        reply(rtk, c)

def movie(text, rtk):
    movie_list = ["愛情","情慾","驚悚","動作","歷史","喜劇","勵志","犯罪","靈異","懸疑","奇幻","影展","家庭","職場","青春","動畫","戰爭","劇情","科幻","紀錄片","LGBTQ"]
    if text not in movie_list:
        line_bot_api.reply_message(rtk, TextSendMessage("請輸入正確選單格式！"))
    else:
        db = client.movie
        if text == "愛情":
            c = db.movie_love
        elif text == "情慾":
            c = db.movie_sex
        elif text == "驚悚":
            c = db.movie_thriller
        elif text == "動作":
            c = db.movie_action
        elif text == "歷史":
            c = db.movie_history
        elif text == "喜劇":
            c = db.movie_comedy
        elif text == "勵志":
            c = db.movie_insprirational
        elif text == "犯罪":
            c = db.movie_crime
        elif text == "靈異":
            c = db.movie_supernatural
        elif text == "懸疑":
            c = db.movie_suspenseful
        elif text == "奇幻":
            c = db.movie_fantasy
        elif text == "影展":
            c = db.movie_film_festival
        elif text == "家庭":
            c = db.movie_family
        elif text == "職場":
            c = db.movie_workplace
        elif text == "青春":
            c = db.movie_young
        elif text == "動畫":
            c = db.movie_animation
        elif text == "戰爭":
            c = db.movie_war
        elif text == "劇情":
            c = db.movie_plot
        elif text == "科幻":
            c = db.movie_fiction
        elif text == "紀錄片":
            c = db.movie_documentary
        elif text == "LGBTQ":
            c = db.movie_lgbtq
        reply(rtk, c)

def variety(text, rtk):
    variety_list = ["益智","選秀","美食","歌唱","文化","鄉土","實境","脫口秀","短劇","偶像","素人","紀實","新聞","外景"]
    if text not in variety_list:
        line_bot_api.reply_message(rtk, TextSendMessage("請輸入正確選單格式！"))
    else:
        db = client.variety
        if text == "益智":
            c = db.variety_puzzle
        elif text == "選秀":
            c = db.variety_talent
        elif text == "美食":
            c = db.variety_food
        elif text == "歌唱":
            c = db.variety_sing
        elif text == "文化":
            c = db.variety_culture
        elif text == "鄉土":
            c = db.variety_local
        elif text == "實境":
            c = db.variety_live
        elif text == "脫口秀":
            c = db.variety_talkshow
        elif text == "短劇":
            c = db.variety_skit
        elif text == "偶像":
            c = db.variety_idol
        elif text == "素人":
            c = db.variety_talent
        elif text == "紀實":
            c = db.variety_documentary
        elif text == "新聞":
            c = db.variety_news
        elif text == "外景":
            c = db.variety_location
        reply(rtk, c)

def edu(text, rtk):
    edu_list = ["卡通","日常","教育","喜劇","冒險","家庭","校園","友情","職場"]
    if text not in edu_list:
        line_bot_api.reply_message(rtk, TextSendMessage("請輸入正確選單格式！"))
    else:
        db = client.edu
        if text == "卡通":
            c = db.edu_cartoon
        elif text == "日常":
            c = db.edu_daily
        elif text == "教育":
            c = db.edu_educate
        elif text == "喜劇":
            c = db.edu_comedy
        elif text == "冒險":
            c = db.edu_adventure
        elif text == "家庭":
            c = db.edu_family
        elif text == "校園":
            c = db.edu_school
        elif text == "友情":
            c = db.edu_friendship
        elif text == "職場":
            c = db.edu_workplace
        reply(rtk, c)

def anime(text, rtk):
    anime_list = ["Ani-One","熱血","王道","懸疑","勵志","科幻","青春","幽默","校園","料理","格鬥","家庭","友情","愛情","運動","妖怪","恐怖","職人","耽美"]
    if text not in anime_list:
        line_bot_api.reply_message(rtk, TextSendMessage("請輸入正確選單格式！"))
    else:
        db = client.anime
        if text == "Ani-One":
            c = db.anime_ani_one
        elif text == "熱血":
            c = db.anime_passionate
        elif text == "王道":
            c = db.anime_popularity
        elif text == "懸疑":
            c = db.anime_suspenseful
        elif text == "勵志":
            c = db.anime_inspirational
        elif text == "科幻":
            c = db.anime_fiction
        elif text == "青春":
            c = db.anime_young
        elif text == "幽默":
            c = db.anime_humor
        elif text == "校園":
            c = db.anime_school
        elif text == "料理":
            c = db.anime_cook
        elif text == "格鬥":
            c = db.anime_fighting
        elif text == "家庭":
            c = db.anime_family
        elif text == "友情":
            c = db.anime_friendship
        elif text == "愛情":
            c = db.anime_love
        elif text == "運動":
            c = db.anime_sports
        elif text == "妖怪":
            c = db.anime_monster
        elif text == "恐怖":
            c = db.anime_horror
        elif text == "職人":
            c = db.anime_craftsman
        elif text == "耽美":
            c = db.anime_bl
        reply(rtk, c)

app = Flask(__name__)
@app.route("/", methods=['POST'])
def verify():
    data = request.get_json()
    try :
        temp_text = data['events'][0]['message']['text'] 
    except :
        temp_text = ""
    retoken = data['events'][0]['replyToken']
    
    if temp_text == "夯劇排行":
        top10(retoken) 
    elif temp_text == "VIP升級":
        line_bot_api.reply_message(retoken, TextSendMessage("https://www.linetv.tw/purchase/vip?source=NAVBAR")) 
    elif temp_text == "活動":
        line_bot_api.reply_message(retoken, TextSendMessage("https://www.linetv.tw/feed/campaign?source=NAVBAR")) 
    elif temp_text =="快推坑我":
        line_bot_api.reply_message(retoken, FlexSendMessage(alt_text='你有一則新訊息',contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://static-img.linetv.tw/1460a4031f02f11b31e80525bf2c7d230348a995d4637a37d91a7822ebe24b22d317424a755d1fdf28262903179909c09ab0d8e934dee8f38ed16a817017e280d551c8f370c0f207b29d099d0ddbc3df1405da500ab5ef07f17fdc531aa86e567e852e81960f0a5b2e27096f0c048f3a0a102fdc3e833e4bfff1acbaf40ccb9f508660eb0a9b36f07b03993237e16e5e3f81267475fac9a3bcc14966d3828e6234ae84645c8b1d260319196ebddfb9b7e32741e3c96fad4555fc8cfc865bc6140649eb2e9229df1d6f237cff3a31b96f67543119796978b730d5a5f85bdf40f6",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Action",
          "uri": "https://www.linetv.tw/channel/1?channel_id=1&feed_id=13&source=CHANNEL_LIST_MENU"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "action": {
          "type": "uri",
          "label": "Action",
          "uri": "https://www.linetv.tw/channel/1?channel_id=1&feed_id=13&source=CHANNEL_LIST_MENU"
        },
        "contents": [
          {
            "type": "text",
            "text": "連續劇",
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "甜死人不償命",
              "text": "連續劇 甜寵"
            },
            "gravity": "bottom"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "腎上腺素飆升",
              "text": "連續劇 懸疑"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "笑顏逐開嘿嘿嘿",
              "text": "連續劇 喜劇"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "古裝cosplay最對味",
              "text": "連續劇 古裝"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "家家有本難念的經",
              "text": "連續劇 家庭"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://static-img.linetv.tw/1460a4031f02f11b31e80525bf2c7d230348a995d4637a37d91a7822ebe24b22d317424a755d1fdf28262903179909c06b1403ea122f9874df47f627ae2c37101334fc27ca83067194bd0b5e3cc15b66db4251afdb26f5b5ddd081a816f2ada1f1080f4dac60bcd09ad7a6d653a7a6d452b07ba441200b38c28021228301e1688bf2849014762959f32bc5e48a2ac4da297c94be73fca980296b9499191314ad82ff1df0188d62453a9bfac4b0ade202e35dca39058e3740c311bf9a1713a560d5dcf6407a76ed68ec39f7f20eb5afec4f221fd884a1f4b0d78ec67204605b46",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Action",
          "uri": "https://www.linetv.tw/channel/6?channel_id=6&feed_id=18&source=CHANNEL_LIST_MENU"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "action": {
          "type": "uri",
          "label": "Action",
          "uri": "https://www.linetv.tw/channel/6?channel_id=6&feed_id=18&source=CHANNEL_LIST_MENU"
        },
        "contents": [
          {
            "type": "text",
            "text": "電影",
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "各種愛情的模樣",
              "text": "電影 愛情"
            },
            "gravity": "bottom"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "來個緊張刺激的",
              "text": "電影 驚悚"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "赫赫哈ㄏㄧˋ",
              "text": "電影 動作"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "一起開心笑一個",
              "text": "電影 喜劇"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "不要做壞事啦",
              "text": "電影 犯罪"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://static-img.linetv.tw/1460a4031f02f11b31e80525bf2c7d230348a995d4637a37d91a7822ebe24b22d317424a755d1fdf28262903179909c009f0e09b93d06158ff1490aba277a166eaa5dbbc3dd00bc52c2b6a12c7494ceb97141573be52b53c75195013f3d21d6d94ee9ec9bbd896025ff7d1069448b384d46facd146781ea1254a83253a2828305cce1218bac43c81e0537f27784e47e64781b12cbb26d8d4f391dae39bf52177af583f064d228c3ea2e8aecb41552990e6ee06710ecbc557f4fb9c41307b6bed58cf58c7972d734a75fd2944698441e516d0984ddf4042719a8cfd802677dcb8",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Action",
          "uri": "https://www.linetv.tw/channel/3?channel_id=3&feed_id=15&source=CHANNEL_LIST_MENU"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "action": {
          "type": "uri",
          "label": "Action",
          "uri": "https://www.linetv.tw/channel/3?channel_id=3&feed_id=15&source=CHANNEL_LIST_MENU"
        },
        "contents": [
          {
            "type": "text",
            "text": "綜藝",
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "不按牌理出牌",
              "text": "綜藝 實境"
            },
            "gravity": "bottom"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "充實內涵開拓視野",
              "text": "綜藝 文化"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "放屁是粉紅色的一群人",
              "text": "綜藝 偶像"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "一起上山下海",
              "text": "綜藝 外景"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "噗噗噗噗噗噗勒",
              "text": "綜藝 歌唱"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://static-img.linetv.tw/1460a4031f02f11b31e80525bf2c7d230348a995d4637a37d91a7822ebe24b22d317424a755d1fdf28262903179909c08b4271063223fb0309668e6112e072f0f160979e3542787c80e6a5bd5e92e6c216cf4449a0296ff76d241e2f4d77a8ca40935b27d8c86fe521ceff5217b3d99cc59abf86117d39620b2c0e50c3afe7952db0f057a7fa303d676c3f3a7ae21f9df1ba3496a8814c7d4e28d842e213fe522a0514d9f357458bf36de97386b10687d87bbd4f33400a2d174e8878ec923a4b10e780871dedbbb8d28df598a6ed2e7da4fcc06f629753e63e56ba5ffc36f973",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Action",
          "uri": "https://www.linetv.tw/channel/2?channel_id=2&feed_id=14&source=CHANNEL_LIST_MENU"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "action": {
          "type": "uri",
          "label": "Action",
          "uri": "https://www.linetv.tw/channel/2?channel_id=2&feed_id=14&source=CHANNEL_LIST_MENU"
        },
        "contents": [
          {
            "type": "text",
            "text": "動漫",
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "燃燒起來吧！！",
              "text": "動漫 熱血"
            },
            "gravity": "bottom"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "bui bui bui蹦蹦蹦",
              "text": "動漫 科幻"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "沒人認真唸書的地方",
              "text": "動漫 校園"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "戀愛的臭酸味",
              "text": "動漫 愛情"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "妖怪勒妖怪勒妖怪勒",
              "text": "動漫 妖怪"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://static-img.linetv.tw/1460a4031f02f11b31e80525bf2c7d230348a995d4637a37d91a7822ebe24b2266bf3b8eb7d3eb0af088eee2f0a0f5ded4ef06e1f7eb9e54f428e93bbd1a6f66468f9df19c2a2285f6a0dd46dc0b1fdd17430561c6a6461aac8f4b83159a7cb2dc99d139da0be1e7cdc76b75f13076f66b1ddb435dbfcdb2098a0c48c447b571004f1febc35ea1a89e3307d24284d1db543980134d1d8601427d88fb5a29000f9ae35fe0478086658c048908b0a235c0bd61620a1f69d548680b5481546dbbcaf94d606441f7786947ec248ef76d22271e3d6e3fb69eeb2caa67b81e6380681a",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "label": "Action",
          "uri": "https://www.linetv.tw/channel/1?channel_id=1&feed_id=13&source=CHANNEL_LIST_MENU"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "action": {
          "type": "uri",
          "label": "Action",
          "uri": "https://linecorp.com"
        },
        "contents": [
          {
            "type": "text",
            "text": "育樂",
            "weight": "bold",
            "size": "xl",
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "電腦也能教小孩",
              "text": "育樂 教育"
            },
            "gravity": "bottom"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "讓你的孩子安靜半小時",
              "text": "育樂 卡通"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "爸爸媽媽哥哥姊姊弟弟妹妹",
              "text": "育樂 家庭"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "聽老師的話",
              "text": "育樂 校園"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "一起hahaha",
              "text": "育樂 喜劇"
            }
          }
        ]
      }
    }
  ]
})
)
        
    elif temp_text.find(" ") > 0:
        temp_type = temp_text[:temp_text.find(" ")]
        temp_kind = temp_text[temp_text.find(" ") + 1:]
        if temp_type == "連續劇":
            drama(temp_kind, retoken)
        elif temp_type == "電影":
            movie(temp_kind, retoken)
        elif temp_type == "綜藝":
            variety(temp_kind, retoken)
        elif temp_type == "育樂":
            edu(temp_kind, retoken)
        elif temp_type == "動漫":
            anime(temp_kind, retoken)
        else :
            line_bot_api.reply_message(retoken, TextSendMessage("請輸入正確選單格式！")) 
    else :
        line_bot_api.reply_message(retoken, TextSendMessage("請輸入：快推坑我、夯劇排行，或是點擊選單！"))
    
    return 'OK',200

if __name__ == "__main__":
    app.run(port = 3000)