{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [],
   "source": [
    "#擷取套件\n",
    "import requests\n",
    "#requests.請求方式\n",
    "url = requests.get(\"https://zh.wikipedia.org/wiki/%E8%B6%85%E6%96%87%E6%9C%AC%E4%BC%A0%E8%BE%93%E5%8D%8F%E8%AE%AE\")\n",
    "#印(文本)\n",
    "#print (url.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  hello world This is Iink1 This is Iink2   \n",
      "[<html> <body> <h1 id=\"title\">hello world</h1> <a class=\"link\" hrefe=\"#\">This is Iink1</a> <a class=\"link\" hrefe=\"# link2\">This is Iink2</a> </body> </html>, ' ']\n",
      "<a class=\"link\" hrefe=\"# link2\">This is Iink2</a>\n",
      "<h1 id=\"title\">hello world</h1>\n",
      "[<a class=\"link\" hrefe=\"#\">This is Iink1</a>, <a class=\"link\" hrefe=\"# link2\">This is Iink2</a>]\n"
     ]
    }
   ],
   "source": [
    "#資料剖析\n",
    "from bs4 import BeautifulSoup\n",
    "#樣本\n",
    "sample='\\\n",
    "<html> \\\n",
    "  <body> \\\n",
    "  <h1 id=\"title\">hello world</h1> \\\n",
    "  <a hrefe=\"#\" class=\"link\">This is Iink1</a> \\\n",
    "  <a hrefe=\"# link2\" class=\"link\">This is Iink2</a> \\\n",
    "  </body> \\\n",
    "</html>  '\n",
    "#裝載\n",
    "soup = BeautifulSoup(sample)\n",
    "print (soup.text)\n",
    "#全部丟出\n",
    "print (soup.contents)\n",
    "#標籤抽取 id:要加# class要加.\n",
    "#select(標籤)[第幾個元素]\n",
    "print (soup.select('a')[1])\n",
    "print (soup.select('#title')[0])\n",
    "print (soup.select('.link'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unexpected EOF while parsing (<ipython-input-2-0a575b30de7c>, line 7)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-2-0a575b30de7c>\"\u001b[1;36m, line \u001b[1;32m7\u001b[0m\n\u001b[1;33m    #print (item.select('.price')[0].text,item.select('.item-desc')[0].text.strip())\u001b[0m\n\u001b[1;37m                                                                                    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m unexpected EOF while parsing\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "url = requests.get(\"https://world.taobao.com/product/%E8%87%BA%E7%81%A3%E6%B7%98%E5%AF%B6.htm\")\n",
    "soup = BeautifulSoup(url.text)\n",
    "for item in soup.select('.item-box'):\n",
    "    #item.select('標籤,id,class')[0].文字.刪除空白()\n",
    "    #print (item.select('.price')[0].text,item.select('.item-desc')[0].text.strip())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"\\nimport requests\\nfrom bs4 import BeautifulSoup\\npayload ={\\n    'responsive': 'true',\\n    'packageType': 'fh',\\n    'c': '91ed89b5-db35-476e-91ea-6e1d6390fc1f',\\n    'ttla': 'TYO',\\n    'ftla':'TPE',\\n    'tripType': 'ROUND_TRIP',\\n    'origin': '台北, 台灣  (TPE-桃園國際機場)',\\n    'destination': '成田, 日本',\\n    'startDate': '2019/3/4',\\n    'endDate': '2019/3/11',\\n    'checkInDate': '2019/3/4',\\n    'checkOutDate': '2019/3/11',\\n    'adults':' 1',\\n    'infantsInSeats':'0',\\n    'cabinClass':' e',\\n    'Direct':' 1',\\n    'regionId': '8900',\\n    'star': '50',\\n    'guestRating': '45',\\n    'sort': 'price',\\n    'timezoneOffset': '28800000',\\n    'langid': '1028',\\n    'hsrIdentifier': 'HSR',\\n    '?1543880218772': ''\\n}\\n\\nurl = requests.post('https://www.expedia.com.tw/Hotel-Search-Data?responsive=true&packageType=fh&c=91ed89b5-db35-476e-91ea-6e1d6390fc1f&ttla=TYO&ftla=TPE&tripType=ROUND_TRIP&origin=%E5%8F%B0%E5%8C%97,+%E5%8F%B0%E7%81%A3++(TPE-%E6%A1%83%E5%9C%92%E5%9C%8B%E9%9A%9B%E6%A9%9F%E5%A0%B4)&destination=%E6%88%90%E7%94%B0,+%E6%97%A5%E6%9C%AC&startDate=2019/3/4&endDate=2019/3/11&checkInDate=2019/3/4&checkOutDate=2019/3/11&adults=1&infantsInSeats=0&cabinClass=e&Direct=1&regionId=8900&star=50&guestRating=45&sort=price&timezoneOffset=28800000&langid=1028&hsrIdentifier=HSR&?1543880218772', data =payload)\\nsoup = BeautifulSoup(url.text)\\nprint (soup.text)\\n\""
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''\n",
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "payload ={\n",
    "    'responsive': 'true',\n",
    "    'packageType': 'fh',\n",
    "    'c': '91ed89b5-db35-476e-91ea-6e1d6390fc1f',\n",
    "    'ttla': 'TYO',\n",
    "    'ftla':'TPE',\n",
    "    'tripType': 'ROUND_TRIP',\n",
    "    'origin': '台北, 台灣  (TPE-桃園國際機場)',\n",
    "    'destination': '成田, 日本',\n",
    "    'startDate': '2019/3/4',\n",
    "    'endDate': '2019/3/11',\n",
    "    'checkInDate': '2019/3/4',\n",
    "    'checkOutDate': '2019/3/11',\n",
    "    'adults':' 1',\n",
    "    'infantsInSeats':'0',\n",
    "    'cabinClass':' e',\n",
    "    'Direct':' 1',\n",
    "    'regionId': '8900',\n",
    "    'star': '50',\n",
    "    'guestRating': '45',\n",
    "    'sort': 'price',\n",
    "    'timezoneOffset': '28800000',\n",
    "    'langid': '1028',\n",
    "    'hsrIdentifier': 'HSR',\n",
    "    '?1543880218772': ''\n",
    "}\n",
    "\n",
    "url = requests.post('https://www.expedia.com.tw/Hotel-Search-Data?responsive=true&packageType=fh&c=91ed89b5-db35-476e-91ea-6e1d6390fc1f&ttla=TYO&ftla=TPE&tripType=ROUND_TRIP&origin=%E5%8F%B0%E5%8C%97,+%E5%8F%B0%E7%81%A3++(TPE-%E6%A1%83%E5%9C%92%E5%9C%8B%E9%9A%9B%E6%A9%9F%E5%A0%B4)&destination=%E6%88%90%E7%94%B0,+%E6%97%A5%E6%9C%AC&startDate=2019/3/4&endDate=2019/3/11&checkInDate=2019/3/4&checkOutDate=2019/3/11&adults=1&infantsInSeats=0&cabinClass=e&Direct=1&regionId=8900&star=50&guestRating=45&sort=price&timezoneOffset=28800000&langid=1028&hsrIdentifier=HSR&?1543880218772', data =payload)\n",
    "soup = BeautifulSoup(url.text)\n",
    "print (soup.text)\n",
    "'''#多行註解"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
