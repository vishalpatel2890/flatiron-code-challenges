# Complete the function that accepts a string parameter, and reverses each word
#in the string. All spaces in the string should be retained.
#
# “This is an example!” ==> “sihT si na !elpmaxe”
# “double  spaces”      ==> “elbuod  secaps”

def topsy_turvy(string_list):
    words=string_list.split()
    topsy=[]
    for word in words:
        tipsy=word[::-1]
        topsy.append(tipsy)
    return ' '.join(topsy)

def sentence(sentence):
    return ' '.join([word[::-1] for word in sentence.split(' ')])

#recursive
def reverse_string(string):
   if string == ‘’:
       return string
   return reverse_string(string[1:]) + string[:1]
