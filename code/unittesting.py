import unittest
# import account
# import googlexml
# import mongo
# import searchlight


### Search

def isItSearch(self):
    print "it's a search page"
    return True

def isItCaptcha(self):
    print "it's not a captcha"
    return False


### Tests

## Check if it's a google search page

class SearchTests(unittest.TestCase):

    def test_isItSearch(self):
        self.assertTrue


## Check if it's a captcha page

class CaptchaTests(unittest.TestCase):

    def test_isItCaptcha(self):
        self.assertFalse


## tests for mongo.py

# class MongoTests(unittest.TestCase):


## tests for googlexml.py

# class XMLTests(unittest.TestCase):


## tests for account.py

# class AccountTests(unittest.TestCase):


## tests for searchlight.py

# class SearchlightTests(unittest.TestCase):


def main():
    unittest.main()

if __name__ == '__main__':
    main()