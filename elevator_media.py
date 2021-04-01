import requests

class ElevatorMedia:
    class Streamer:
        def __init__(self):
            self.game = "<iframe width='100%' height='100%' src=https://www.addictinggames.com/embed/html5-games/23635 scrolling=no></iframe>"
            self.ada = "<div class=nomics-ticker-widget data-name=Cardano data-base=ADA data-quote=USD></div><script src=https://widget.nomics.com/embed.js></script>"
            
        def getContent(self, data):
            if data == "game":
                self.formating(self.game)
            elif data == "ada":
                self.formating(self.ada)
            elif data == "quote status":
                return self.quote().status_code
            elif data == "quote body":
                return self.formating(self.quote().text)
            
        def formating(self, data):
            return "<div> {} </div>".format(data)
        
        def quote(self):
            r = requests.get('http://getmeaquote.designedbyaturtle.com/')
            # print(r.text)
            return r
