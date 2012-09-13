import urllib2
import json
class WeatherFetcher:
    def wundergroundFetch(self):
        page = urllib2.urlopen('http://api.wunderground.com/api/2ca02f07b8a1e20a/conditions/q/IL/Warrenville.json')
        if page == None:
            return None
        json_string = page.read()
        parsed_json = json.loads(json_string)
        return (parsed_json['current_observation'])
    def tempFetch(self):
        parsed_page = self.wundergroundFetch()
        if parsed_page == None:
            return None
        else:
            return parsed_page['temp_f']
    def whichTempLevel(self):
        temp  = self.tempFetch()
        if temp == None:
            return 0
        if temp <= 32:
            return 1
        if temp <= 50 and temp > 32:
            return 2
        if temp <= 70 and temp > 50:
            return 3
        if temp <= 90 and temp > 70:
            return 4
        if temp > 90:
            return 5
        
    
