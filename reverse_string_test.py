def solution(some_string):
    
    ar=some_string.split(" ")
    result= [x[::-1] for x in ar]
    string_return= ' '.join(result)

    return string_return
    
def main():
    str= "we are coding"
    return
