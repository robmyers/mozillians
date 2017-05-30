import logging

try:
    from xml.etree import ElementTree
except ImportError:
    from elementtree import ElementTree

from django.contrib.auth.models import User

#logger = logging.getLogger(__name__)

def callbackfunction(tree):

    email = tree.findall('*/{http://www.yale.edu/tp/cas}user')[0].text
#    global_name = tree.findall('*/{http://www.yale.edu/tp/cas}attributes/{http://www.yale.edu/tp/cas}global')[0].text
     
    user, user_created = User.objects.get_or_create(email=email,
                                                    username=email)
    user.save()
