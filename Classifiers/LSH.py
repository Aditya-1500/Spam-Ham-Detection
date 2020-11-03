# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:33:57 2020

@author: Aditya
"""

# from datasketch import MinHash

# hamCl = [
#     "Go until jurong point, crazy.. Available only in bugis n great world la e buffet... Cine there got amore wat...",
#     "Ok lar... Joking wif u oni...",
#     "U dun say so early hor... U c already then say...",
#     "Nah I don't think he goes to usf, he lives around here though",
#     "Even my brother is not like to speak with me. They treat me like aids patent.",
#     "I'm gonna be home soon and i don't want to talk about this stuff anymore tonight, k? I've cried enough today.",
#     "Oh k...i'm watching here:)",
#     "Is that seriously how you spell his name?",
#     "Lol your always so convincing.",
#     "Did you catch the bus ? Are you frying an egg ? Did you make a tea? Are you eating your mom's left over dinner ? Do you feel my Love ?",
#     "I'm back &amp; we're packing the car now, I'll let you know if there's room",
#     "Ahhh. Work. I vaguely remember that! What does it feel like? Lol",
#     "K tell me anything about you.",
#     "Oops, I'll let you know when my roommate's done",
#     "I see the letter B on my car",
#     "Pls go ahead with watts. I just wanted to be sure. Do have a great weekend. Abiola",
#     "Great! I hope you like your man well endowed. I am  &lt;#&gt;  inches...",
#     "No calls..messages..missed calls",
#     "Fair enough, anything going on?",
#     "Yeah hopefully, if tyler can't do it I could maybe ask around a bit",
#     "What you thinked about me. First time you saw me in class.",
#     "A gram usually runs like  &lt;#&gt; , a half eighth is smarter though and gets you almost a whole second gram for  &lt;#&gt;",
#     "Wow. I never realized that you were so embarassed by your accomodations. I thought you liked it, since i was doing the best i could and you always seemed so happy about 'the cave'. I'm sorry I didn't and don't have more to give. I'm sorry i offered. I'm sorry your room was so embarassing.",
#     "Sorry, I'll call later in meeting.",
#     "Tell where you reached"
#     ]

# spamCl = [
#     "Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121 to receive entry question(std txt rate)T&C's apply 08452810075over18's",
#     "FreeMsg Hey there darling it's been 3 week's now and no word back! I'd like some fun you up for it still? Tb ok! XxX std chgs to send, £1.50 to rcv",
#     "WINNER!! As a valued network customer you have been selected to receivea £900 prize reward! To claim call 09061701461. Claim code KL341. Valid 12 hours only.",
#     "Had your mobile 11 months or more? U R entitled to Update to the latest colour mobiles with camera for Free! Call The Mobile Update Co FREE on 08002986030",
#     "SIX chances to win CASH! From 100 to 20,000 pounds txt> CSH11 and send to 87575. Cost 150p/day, 6days, 16+ TsandCs apply Reply HL 4 info",
#     "XXXMobileMovieClub: To use your credit, click the WAP link in the next txt message or click here>> http://wap. xxxmobilemovieclub.com?n=QJKGIGHJJGCBL",
#     "England v Macedonia - dont miss the goals/team news. Txt ur national team to 87077 eg ENGLAND to 87077 Try:WALES, SCOTLAND 4txt/ú1.20 POBOXox36504W45WQ 16+",
#     "Thanks for your subscription to Ringtone UK your mobile will be charged £5/month Please confirm by replying YES or NO. If you reply NO you will not be charged",
#     "SMS. ac Sptv: The New Jersey Devils and the Detroit Red Wings play Ice Hockey. Correct or Incorrect? End? Reply END SPTV",
#     "Congrats! 1 year special cinema pass for 2 is yours. call 09061209465 now! C Suprman V, Matrix3, StarWars3, etc all 4 FREE! bx420-ip4-5we. 150pm. Dont miss out! ",
#     "As a valued customer, I am pleased to advise you that following recent review of your Mob No. you are awarded with a £1500 Bonus Prize, call 09066364589",
#     "Urgent UR awarded a complimentary trip to EuroDisinc Trav, Aco&Entry41 Or £1000. To claim txt DIS to 87121 18+6*£1.50(moreFrmMob. ShrAcomOrSglSuplt)10, LS1 3AJ",
#     "Did you hear about the new 'Divorce Barbie'? It comes with all of Ken's stuff!",
#     "Please call our customer service representative on 0800 169 6031 between 10am-9pm as you have WON a guaranteed £1000 cash or £5000 prize!",
#     "Your free ringtone is waiting to be collected. Simply text the password 'MIX' to 85069 to verify. Get Usher and Britney. FML, PO Box 5249, MK17 92H. 450Ppw 16",
#     "GENT! We are trying to contact you. Last weekends draw shows that you won a £1000 prize GUARANTEED. Call 09064012160. Claim Code K52. Valid 12hrs only. 150ppm",
#     "You are a winner U have been specially selected 2 receive £1000 or a 4* holiday (flights inc) speak to a live operator 2 claim 0871277810910p/min (18+) ",
#     "PRIVATE! Your 2004 Account Statement for 07742676969 shows 786 unredeemed Bonus Points. To claim call 08719180248 Identifier Code: 45239 Expires",
#     "Todays Voda numbers ending 7548 are selected to receive a $350 award. If you have a match please call 08712300220 quoting claim code 4041 standard rates app",
#     "Sunshine Quiz Wkly Q! Win a top Sony DVD player if u know which country the Algarve is in? Txt ansr to 82277. £1.50 SP:Tyrone",
#     "You'll not rcv any more msgs from the chat svc. For FREE Hardcore services text GO to: 69988 If u get nothing u must Age Verify with yr network & try again",
#     ]



# mh,ms = MinHash(),MinHash()
# for ham in hamCl:
#     for h in set(ham.split()):
#         mh.update(h.encode('utf-8'))
# for spam in spamCl:
#     for s in set(spam.split()):
#         ms.update(h.encode('utf-8'))
        
# queries = [
#     "Pls i wont belive god.not only jesus.",
#     "This is my number by vivek..",
#     "sorry brah, just finished the last of my exams, what up",
#     "I agree. So i can stop thinkin about ipad. Can you please ask macho the same question.",
#     "I had askd u a question some hours before. Its answer",
#     "Congratulations U can claim 2 VIP row A Tickets 2 C Blu in concert in November or Blu gift guaranteed Call 09061104276 to claim TS&Cs www.smsco.net cost£3.75max ",
#     "Fantasy Football is back on your TV. Go to Sky Gamestar on Sky Active and play £250k Dream Team. Scoring starts on Saturday, so register now!SKY OPT OUT to 88088",
#     "Free msg: Single? Find a partner in your area! 1000s of real people are waiting to chat now!Send CHAT to 62220Cncl send STOPCS 08717890890£1.50 per msg",
#     "Free Msg: Ringtone!From: http://tms. widelive.com/index. wml?id=1b6a5ecef91ff9*37819&first=true18:0430-JUL-05",
#     "Oh my god! I've found your number again! I'm so glad, text me back xafter this msgs cst std ntwk chg £1.50",
#     "A link to your picture has been sent. You can also use http://alto18.co.uk/wave/wave.asp?o=44345"
#     ]

# for query in queries:
#     q = MinHash()
#     for t in set(query.split()):
#         q.update(t.encode('utf-8'))
#     jh = q.jaccard(mh)
#     js = q.jaccard(ms)
#     if jh > js:
#         print("Ham")
#         print(jh)
#     else:
#         print("Spam")
#         print(js)

import pandas as pd
from datasketch import MinHash
import random

messages = pd.read_csv('smsspamcollection/SMSSpamCollection', sep='\t',names=["label", "message"])
hamCl = []
spamCl = []

for m in messages[messages['label']=='ham']['message']:
    hamCl.append(m)

for m in messages[messages['label']=='spam']['message']:
    spamCl.append(m)

hamTest = hamCl[-5:]
spamTest = spamCl[-5:]

hamCl = hamCl[:-5]
spamCl = spamCl[:-5]

rd_rangeH = random.sample(range(1,len(hamCl)),50)
rd_rangeS = random.sample(range(1,len(spamCl)),50)

# print(rd_range)
hCl = [hamCl[i] for i in rd_rangeH]
sCl = [spamCl[i] for i in rd_rangeS]

mh,ms = MinHash(num_perm=512),MinHash(num_perm=512)
for ham in hCl:
    for h in ham.split():
        mh.update(h.encode('utf-8'))
for spam in sCl:
    for s in spam.split():
        ms.update(s.encode('utf-8'))
        
queries = hamTest+spamTest

for query in queries:
    q = MinHash(num_perm=512)
    for t in query.split():
        q.update(t.encode('utf-8'))
    jh = q.jaccard(mh)
    js = q.jaccard(ms)
    if jh > js:
        print("Ham")
        # print(jh)
    else:
        print("Spam")
        # print(js)
