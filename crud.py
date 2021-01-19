from basic import db, Puppy

##create##

my_puppy = Puppy('Rufus', 5)
db.session.add(my_puppy)
db.session.commit()

