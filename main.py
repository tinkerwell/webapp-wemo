##
#
# Change IP to your machine's IP in line 802 in miranda.py
#
##

import webapp2
from wemo import * 
from time import gmtime, strftime

class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
      # Save to log
      # f = open('log.txt','a')
      # f.write("%s;%s\n" % (self.request.remote_addr,strftime("%Y-%m-%d %H:%M:%S", gmtime()))) 
      toggle()   
      if(get()):
        self.response.write("Lamp is On")
      else:
        self.response.write("Lamp is Off")
 

app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='0.0.0.0', port='8080')

if __name__ == '__main__':
    main()
