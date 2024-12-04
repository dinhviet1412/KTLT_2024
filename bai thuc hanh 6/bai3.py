class Nguoi(object):
 def getGender( self ):
  return "Unknown"
class nam( Nguoi ):
 def getGender( sefl ):
  return "nam"
class nu( Nguoi ):
 def getGender( self ):
  return "nu"
anam = nam()
anu = nu()
print (anam.getGender())
print (anu.getGender())
