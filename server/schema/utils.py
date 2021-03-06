import jwt
import re
import datetime
from secrets import TOKEN_SECRET as secret, INVITATION_SECRET as invitation_secret


ADMIN_GROUP_ID = 1
GUEST_GROUP_ID = 2
INSIDER_GROUP_ID = 3

PUBLIC_VISIBILITY_ID = 1
RESTRICTED_VISIBILITY_ID = 2
PRIVATE_VISIBILITY_ID = 3
DRAFT_VISIBILITY_ID = 4


class Utils:
    @classmethod
    def get_all(cls):
        return cls._meta.model.query.filter_by(deleted=False).all()


def decode(token):
    if(token is None or type(token) != str or token[:7] != 'Bearer '):
        return None, 'fail'
    try:
        return jwt.decode(token[7:], secret, algorithms=['HS256']), 'success'
    except jwt.exceptions.ExpiredSignatureError:
        return None, 'expired'
    except:
        return None, 'fail'


def is_admin(decoded):
    return decoded is not None and decoded["groupId"] == ADMIN_GROUP_ID


def get_tomorrow():
    return datetime.datetime.now() + datetime.timedelta(days=1)


def get_now():
    return datetime.datetime.utcnow()


def extract_link_info(token):
    # return email and group id
    if(token is None or type(token) != str):
        return None, None
    try:
        decoded = jwt.decode(token, invitation_secret, algorithms=['HS256'])
        return decoded.get('email'), decoded.get('groupId')
    except:
        return None, None


cleanr = re.compile('<.*?>')


def cleanhtml(raw_html):
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext
