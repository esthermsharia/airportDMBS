
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class Employee(UserMixin, db.Model):
    """
    Create an Employee table
    """

   

    __tablename__ = 'employees'

    enumber= db.Column(db.Integer, index=True,primary_key=True)
    id=enumber#This is attribute must be identified in every python application as it identifies the current user.
    email = db.Column(db.String(60), index=True, unique=True)
    union_no= db.Column(db.Integer, index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    address = db.Column(db.String(60), index=True)
    phone_no= db.Column(db.Integer, index=True)
    role_id = db.Column(db.String(60), db.ForeignKey('roles.role_id'))
    is_admin = db.Column(db.Boolean, default=False)
    salary= db.Column(db.Integer)

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Employee: {}>'.format(self.username)



# Set up user_loader
@login_manager.user_loader

def load_user(user_id):
    return Employee.query.get(int(user_id))


class airplane(db.Model):
    """
    Create a airplanes table.
    """

    __tablename__ = 'airplanes'

    reg_no= db.Column(db.String(60), primary_key=True)
    model_no=db.Column(db.String(60), db.ForeignKey('models.model_no'))

    def __repr__(self):
        return '<airplane: {}>'.format(self.reg_no)

class planemodel(db.Model):
    """
    Create a airplanes table.
    """

    __tablename__ = 'models'
    model_no=db.Column(db.String(60),index=True,primary_key=True)
    capacity=db.Column(db.Integer)
    weight=db.Column(db.Integer)


    def __repr__(self):
        return '<planemodel: {}>'.format(self.model_no)


class traffic_controller(db.Model):
    """
    Create traffic_controller table.
    """

    __tablename__ = 'traffic_controllers'

    enumber=db.Column(db.Integer, db.ForeignKey('employees.enumber'),primary_key=True)
    med_exam_date=db.Column(db.String(60))

    def __repr__(self):
        return '<traffic_controller: {}>'.format(self.enumber)

class test(db.Model):
    """
    Create tests table.
    """

    __tablename__ = 'tests'

    KAA_test_no=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(60),unique=True)
    max_score=db.Column(db.Integer)

    def __repr__(self):
        return '<test: {}>'.format(self.KAA_test_no)

class testing_event(db.Model):
    """
    Create testing_events table.
    """

    __tablename__ = 'testing_events'

    KAA_test_no=db.Column(db.Integer,db.ForeignKey('tests.KAA_test_no'),primary_key=True)
    reg_no = db.Column(db.String(60),db.ForeignKey('airplanes.reg_no'))
    Tnumber= db.Column(db.Integer,db.ForeignKey('technicians.Tnumber'))
    hrs_spent=db.Column(db.Integer)
    score=db.Column(db.Integer)
    date=db.Column(db.String(60))
  

    def __repr__(self):
        return '<testing_event: {}>'.format(self.KAA_test_no)



class Role(db.Model):
    """
    Create a Role table
    """

    __tablename__ = 'roles'

    role_id = db.Column(db.String(60), primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='role',
                                lazy='dynamic')

    def __repr__(self):
         return '<Role: {}>'.format(self.name)


class technician(db.Model):
    """
    Create technicians table.
    """

    __tablename__ = 'technicians'

    Tnumber= db.Column(db.Integer, primary_key=True)
    enumber=db.Column(db.Integer, db.ForeignKey('employees.enumber'))
    expert_model_no=db.Column(db.String(60), db.ForeignKey('models.model_no'))
    planemodels = db.relationship('planemodel', backref='technician',
                                lazy='select')
   

    def __repr__(self):
        return '<airplane: {}>'.format(self.reg_no)



