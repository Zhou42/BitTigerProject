import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.urlencode({'sensor': 'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved', len(data), 'characters'
    print data
    tree = ET.fromstring(data)

    counts = tree.findall('.//count')
    '''lat = results[0].find('comment').find('name').text
    lng = results[0].find('comment').find('count').text
    location = results[0].find('formatted_address').text'''
    print counts

