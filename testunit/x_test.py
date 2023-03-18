import unittest, xmlrunner



if __name__ == '__main__':

   with open('resultats_tests.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)
