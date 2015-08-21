__author__ = 'SuturkinAA'

import unittest
import json
import pycurl
from io import BytesIO
import csv

class TestStringMethods(unittest.TestCase):

#resource counnt change is not tested

    def test_emptyList(self):
        print('>empltyList')
        self.curlRequest('allocate/saa')
        self.curlRequest('reset')

        self.curlRequest('list')
        self.assertEqual(self.jsonParse(), [{"allocated": {}, "deallocated": ["r1", "r2", "r3"]}])
        self.assertEqual(self.status, 200)

    def test_allocate(self):
        print('>allocate')
        self.curlRequest('reset')

        self.curlRequest('allocate/saa')
        self.assertEqual(self.answer,'r1')
        self.assertEqual(self.status, 201)

        status = self.curlRequest('list')
        self.assertEqual(self.jsonParse(), [{"allocated": {"r1": "saa"}, "deallocated": ["r2", "r3"]}])
        self.assertEqual(self.status, 200)

    def test_allocateAll(self):
        print('>allocateAll')
        self.curlRequest('reset')

        self.curlRequest('allocate/saa')
        self.curlRequest('allocate/rob')
        self.curlRequest('allocate/GordonFreeman')

        self.curlRequest('allocate/latecomer')
        self.assertEqual(self.answer,'Out of resources.')
        self.assertEqual(self.status, 503)

        self.curlRequest('list')
        self.assertEqual(self.jsonParse(), [{"allocated": {"r1": "saa", "r3": "GordonFreeman", "r2": "rob"}, "deallocated": []}])
        self.assertEqual(self.status, 200)

    def test_deallocateByName(self):
        print('>deallocateByName')
        self.curlRequest('reset')

        self.curlRequest('allocate/saa')
        self.curlRequest('allocate/rob')
        self.curlRequest('allocate/saa')

        self.curlRequest('deallocate/saa')
        status = self.curlRequest('list')
        self.assertEqual(self.jsonParse(), [{"allocated": {"r2": "rob"}, "deallocated": ["r1", "r3"]}])
        self.assertEqual(self.status, 200)

        self.curlRequest('deallocate/WrongName')
        self.assertEqual(self.answer,'Not allocated.')
        self.assertEqual(self.status, 404)

#json used ' odinarnie kovichiki, v intnete napisano, what imenno tak
#error texzadanie deallocate/r2 = 404, r1 = 204
    def test_deallocateByRes(self):
        print('>deallocateByRes')
        self.curlRequest('reset')

        self.curlRequest('allocate/saa')
        self.curlRequest('allocate/rob')
        self.curlRequest('allocate/jcup')

        self.curlRequest('deallocate/r1')
        self.assertEqual(self.answer,'Not allocated.')
        self.assertEqual(self.status, 404)

        self.curlRequest('deallocate/r1')
        self.assertEqual(self.status, 204)

        self.curlRequest('deallocate/r666')
        self.assertEqual(self.status, 204)

    def test_listByname(self):
        print('>listByName')
        self.curlRequest('reset')
        self.curlRequest('allocate/saa')
        self.curlRequest('allocate/rob')
        self.curlRequest('allocate/saa')

        self.curlRequest('list/saa')
        data = csv.reader(self.answer)
        self.assertEqual(self.answer, "['r1', 'r3']")
        self.assertEqual(self.status, 200)

        self.curlRequest('list/SaaStudio')
        self.assertEqual(self.answer, "[]")
        self.assertEqual(self.status, 200)

    def test_reset(self):
        print('>reset')
        self.curlRequest('reset')
        self.curlRequest('allocate/saa')
        self.curlRequest('allocate/rob')

        self.curlRequest('reset')
        self.curlRequest('list')
        self.assertEqual(self.jsonParse(), [{"allocated": {}, "deallocated": ["r1", "r2", "r3"]}])
        self.assertEqual(self.status, 200)

    def test_badRequest(self):
        print('>badRequest')
        self.curlRequest('abracadabra')
        self.assertEqual(self.answer,'Bad request.')
        self.assertEqual(self.status, 400)

        self.curlRequest('allocate/jcup.ru')
        self.assertEqual(self.answer,'Bad request.')
        self.assertEqual(self.status, 400)

        self.curlRequest('reset/fantastic')
        self.assertEqual(self.answer,'Bad request.')
        self.assertEqual(self.status, 400)


    service = 'http://localhost:8000/'
    status = -1
    answer = ''

    def curlRequest(self, request):
        #print('-->'+request)
        self.answer = ''
        self.status = -1
        buffer = BytesIO()
        curl = pycurl.Curl()
        curl.setopt(curl.URL, self.service+request)
        curl.setopt(curl.WRITEDATA, buffer)
        curl.perform()

        self.status = curl.getinfo(curl.RESPONSE_CODE)
        answer = str(buffer.getvalue())
        self.answer = answer[2:len(answer)-1]
        curl.close()
        return self.status

    def getStatus(self):
        return self.status

    def getAnswer(self):
        return self.answer

    def jsonParse(self):
        #print ('<--'+self.answer)
        return json.loads(self.answer)

if __name__ == '__main__':
    unittest.main()
