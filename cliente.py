import urllib2
import json
import matplotlib.pyplot as plt
import math

i = 1
while 1:
  if(raw_input() == 'save'):
    response = urllib2.urlopen('http://192.168.100.141:8888/ecg')
    print response.info()
    html = json.loads(response.read())
    print html
    response.close()
    plt.plot(html['valor'])
    plt.ylabel('ECG')
    plt.savefig('temp' + str(i) + '.png')
    plt.close()
    i += 1
  if(raw_input() == 'req'):
    response = urllib2.urlopen('http://192.168.100.141:8888/ecg')
    print response.info()
    html = json.loads(response.read())
    print html
    response.close()
    plt.plot(html['valor'])
    plt.ylabel('ECG')
    plt.show()
  if(raw_input() == 'q'):
    break