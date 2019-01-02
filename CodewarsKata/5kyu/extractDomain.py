# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.

def domain_name(url):
   dot = url.find(".")
   secondDot = url.find(".",dot + 1)
   slash = url.find("/")
   secondSlash = url.find("/",slash + 1)
   if url.count(".") == 1:
        domain = url[secondSlash + 1:dot]
        return domain
   else:
       domain = url[dot + 1:secondDot]
       return domain


if __name__ == "__main__":

    # test case 1
    assert domain_name("http://github.com/carbonfive/raygun") == "github" 

    # test case 2
    assert domain_name("http://www.zombie-bites.com") == "zombie-bites"

    # test case 3
    assert domain_name("https://www.cnet.com") == "cnet"