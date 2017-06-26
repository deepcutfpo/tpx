#Luke Parker
#Formatting Conference Information from Perl Output.
import os
import re
_instring = []
userprofile = os.environ.get('USERPROFILE')
Perl_Output = userprofile + "\\" + input(userprofile+"\\" + r"")
with open(Perl_Output,'r+') as pos:
    for line in pos:
        _instring.append(line.split())
line = None
ofile = []
for i,j in enumerate(_instring):
    if _instring[i][0] == 'Working' and _instring[i+1][0] == 'Existing':
        oput = _instring[i][3]+","
        for k in _instring[i+1][2:]:
            if not '@' in k:
                oput += k + ","
            else:
                oput += k.split("@")[0] + ","
        try:
            oput = oput.replace('Conf,Bridge,','').replace('Meet-Me,Bridge,','').replace('BR_','')[:-1]
            print(oput)
            line.append(oput)
        except:
            next
