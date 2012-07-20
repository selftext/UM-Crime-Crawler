import urllib
from BeautifulSoup import BeautifulSoup
import re

fhand = open('urls.txt')
for line in fhand:
    html = urllib.urlopen(line)
    soup = BeautifulSoup(html)

    count = -1
    countList = list()

    datesList = list()
    typesList = list()
    casesList = list()
    addressesList = list()

    for date in soup('table')[1]:
        try:
            dates = date.find('td', width="150").string
            datesList.append(dates)
            count = count + 1
            countList.append(count)
        except: continue
    
    for type in soup('table')[1]:
        try:
            types = type.find('font').b.string
            typesList.append(types)
        except: continue
    
    for case in soup('table')[1]:
        try:
            cases = case.find('td', width="100").string
            casesList.append(cases)
        except: continue
    
    for address in soup('table')[1]:
        try:
            addresses = address.find('td', colspan="3").font.string
            addressesList.append(addresses)
        except: continue
    
    tableTags = str(soup('table')[1])

    for desc in tableTags:
        try:
            descs = re.findall('td colspan="3">([a-zA-Z0-9].+?)</td>', tableTags)
        except: continue
        
    if countList == -1 : continue

    else:
        file = open("crimedata.txt", "a")

        for i in countList:
            try:
                x = datesList[i], typesList[i], casesList[i], addressesList[i], descs[i]
                file.write('\t'.join(x)+'\n')
            except:
                print 'Weird error. Ignoring....'
                continue

        print 'Success!'

        file.close()
    
print 'All done'