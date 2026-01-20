# products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
# searchWord = "mouse"

products = ["havana"]
searchWord = "havana"



finalResult = []

newProducts = sorted(products)

for i in range(len(searchWord)):
    # print(i, letter)
    # print("test")
    result = []
    for word in newProducts:
        # print("test2")
        if searchWord[:i + 1] == word[:i + 1]: #if letters inserted so far are the same
            result.append(word)
            if len(result) > 2:
                break

            # print(result) #print one at a time
        
    finalResult.append(result)
print(finalResult)
    
# return suggestions