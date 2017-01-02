import urllib2

TEXT = ["This text is a test", "This text is bullshit", "This text is a wrinkled dinkle winkle"]
ADD  = ["", "wrinkled dinkle winkle, potato, wine"]
FILL = ["", "[censored]"]
CHAR = ["", "_"]

TEXT_N = [TEXT[0], ""]
ADD_N  = [ADD[0], "a,b,c,d,e,f,g,h,i,j,k", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque purus tellus, suscipit eu iaculis in, finibus eget ex. Suspendisse id nisi tempor dui rhoncus suscipit. Maecenas ac orci imperdiet..."]
FILL_N = [FILL[0], "123456789012345678901", "$$$$$$"]
CHAR_N = [CHAR[0], "$"]

TC = [
    #TC_01
    {"TEXT" : TEXT[0], "ADD" : ADD[0], "FILL" : FILL[0], "CHAR" : CHAR[0], "EXPECTED" : "{\"result\":\"This text is a test\"}"},
    #TC_02
    {"TEXT" : TEXT[1], "ADD" : ADD[0], "FILL" : FILL[1], "CHAR" : CHAR[0], "EXPECTED" : "{\"result\":\"This text is bull [censored]\"}"},
    #TC_03
    {"TEXT" : TEXT[2], "ADD" : ADD[1], "FILL" : FILL[0], "CHAR" : CHAR[1], "EXPECTED" : "{\"result\":\"This text is a ______________________\"}"},
    ]

TC_N = [
    #TC_N01
    {"TEXT" : TEXT_N[1], "ADD" : ADD_N[0], "FILL" : FILL_N[0], "CHAR" : CHAR_N[0], "EXPECTED" : "{\"error\":\"No Input\"}"},
    #TC_N02
    {"TEXT" : TEXT_N[0], "ADD" : ADD_N[1], "FILL" : FILL_N[0], "CHAR" : CHAR_N[0], "EXPECTED" : "{\"error\":\"User Black List Exceeds Limit of 10 Words.\"}"},
    #TC_N03
    {"TEXT" : TEXT_N[0], "ADD" : ADD_N[2], "FILL" : FILL_N[0], "CHAR" : CHAR_N[0], "EXPECTED" : "{\"error\":\"Invalid Characters in User Black List\"}"},
    #TC_N04
    {"TEXT" : TEXT_N[0], "ADD" : ADD_N[0], "FILL" : FILL_N[1], "CHAR" : CHAR_N[0], "EXPECTED" : "{\"error\":\"User Replacement Text Exceeds Limit of 20 Characters.\"}"},
    #TC_N05
    {"TEXT" : TEXT_N[0], "ADD" : ADD_N[0], "FILL" : FILL_N[2], "CHAR" : CHAR_N[0], "EXPECTED" : "{\"error\":\"Invalid User Replacement Text\"}"},
    #TC_N06
    {"TEXT" : TEXT_N[0], "ADD" : ADD_N[0], "FILL" : FILL_N[0], "CHAR" : CHAR_N[1], "EXPECTED" : "{\"error\":\"Invalid User Replacement Characters\"}"},
    ]


def makeRequest(text, add, fill_text, fill_char):
    #print 'http://www.purgomalum.com/service/json?text='+text+'&add='+add+'&fill_text='+fill_text+'&fill_char='+fill_char
    request = "http://www.purgomalum.com/service/json?text="+urllib2.quote(text)
    if add != "":
        request += "&add="+urllib2.quote(add)
    if fill_text != "":
        request += "&fill_text="+urllib2.quote(fill_text)
    if fill_char != "":
        request += "&fill_char="+urllib2.quote(fill_char)
    #print request
    response = urllib2.urlopen(request)
    return response.read()


#POSITIVE TEST CASES
print "EXECUTING POSITIVE TEST CASES:"
for i, case in enumerate(TC):
    print "TC_0"+str(i+1),
    response = makeRequest(case["TEXT"], case["ADD"], case["FILL"], case["CHAR"])
    if response == case["EXPECTED"]:
        print "\t[PASSED] Got response: "+response
    else:
        print "\t[FAILED] Got response: "+response

#NEGATIVE TEST CASES
print "\nEXECUTING NEGATIVE TEST CASES:"
for i, case in enumerate(TC_N):
    print "TC_N0"+str(i+1),
    response = makeRequest(case["TEXT"], case["ADD"], case["FILL"], case["CHAR"])
    if response == case["EXPECTED"]:
        print "\t[PASSED] Got response: "+response
    else:
        print "\t[FAILED] Got response: "+response
