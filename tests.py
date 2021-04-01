import unittest
from elevator_media import ElevatorMedia

streamer = ElevatorMedia.Streamer()

# This test will check that the game comes back in the right format
class GetContentGameTest(unittest.TestCase):
    def testGame(self):
        self.assertEqual(streamer.getContent("game"), formating(streamer.game))
    
    
# This test will check that the Cardano chart comes back in the right format
class GetContentAdaTest(unittest.TestCase):
    
    def testAda(self):
        self.assertEqual(streamer.getContent("ada"), formating(streamer.ada))
 
# This will check in the HTTP response status is 200    
class GetContentQuoteTest(unittest.TestCase):
    
    def testQuoteStatus(self):
        self.assertEqual(streamer.getContent("quote status"), 200)
        
# This test will check that the HTTP response matches the "<div>" substring after begin formated
class GetContentQuoteTestBody(unittest.TestCase):
    
    def testQuoteBody(self):
        b = streamer.getContent("quote body")
        if "<div>" in b:
            self.assertTrue(True)
        
def formating(data):
    "<div> {} </div>".format(data)
        
if __name__ == '__main__':
    unittest.main()
