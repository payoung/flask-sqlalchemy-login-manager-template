from database import db_session, init_db
from models import *
import datetime
import unittest

class TestCase(unittest.TestCase):

        def setUp(self):
            init_db()

        def test_input_data(self):
            u1 = User(name="Paul", email="paul.andy.young@gmail.com", 
                password="whatever")
            db_session.add(u1)
            db_session.commit()
            print "*****Data has been committed to DB*****"

        def test_query1(self):
            user1 = db_session.query(User).filter_by(name='Paul').first()
            print "User Name: ", user1.name, "User Email: ", user1.email

        def tearDown(self):
            db_session.remove()



if __name__ == '__main__':
    unittest.main() 

'''
class TestCase(unittest.TestCase):

    def setUp(self):
        pass
        
    def test_input_data(self):
        u1 = User(name="Paul", email="paul.andy.young@gmail.com", 
                    password="whatever")
        u2 = User(name="Joe", email="judojoe84@gmail.com", 
                    password="hellyeah")
    
        s1 = Search(name="guitars", string="guitars -steel", status=1, 
                    last_update=datetime.date(2013, 9, 25), user=u1)
        s2 = Search(name="banjo", string="banjo -100", status=1, 
                    last_update=datetime.date(2013, 9, 30), user=u1)
        s3 = Search(name="judo stuff", string="gee", status=1, 
                    last_update=datetime.date(2013, 5, 13), user=u2)
        s4 = Search(name="bmx bike", string="bmx -hoffman", status=0, 
                    last_update=datetime.date(2011, 3, 5), user=u2)

        r1 = Result(title="Guitar for Sale - $100", 
                    link="http://craigslist.com/12341234", search=s1)
        r2 = Result(title="Shitty Guitar for Sale - $50", 
                    link="http://craigslist.com/54325432", search=s1)
        r3 = Result(title="Even shittier Guitar for Sale - $30", 
                    link="http://craigslist.com/4672345", search=s1)

        session = Session()
        session.add_all([u1, u2, s1, s2, s3, s4, r1, r2, r3])
        session.commit()
        print "****Data Has Been Commited to DB****"

    
    def test_query1(self):
	    #Pull a user
        session = Session()
        user1 = session.query(User).filter_by(name='Paul').first()
        print "User Name: ", user1.name, "User Email: ", user1.email


    def test_query2(self):
	    #Pull a Search History
        session = Session()
        user1 = session.query(User).filter_by(name='Joe').first()
        searchhist = session.query(Search).filter_by(user=user1).all()
        for search in searchhist:
            print "Search Name: ", search.name, "Search Term: ", search.string


    def test_query3(self):
        #Pull results from a search
        session = Session()
        search1 = session.query(Search).filter_by(name='guitars').first()
        results = session.query(Result).filter_by(search=search1).all()
        for result in results:
            print "Result Title: ", result.title, "Result link: ", result.link

	
if __name__ == '__main__':
    unittest.main()	

'''


