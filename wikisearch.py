import wikipedia                                      #pip install wikipedia
   
name=input("enter a sring")                   #no space between words
page_object = wikipedia.page(name) 
link= wikipedia.page(name).url
print("URL Link")
print(link)
filename = "log.txt"
file = open(filename,'a')
file.write(link)
file.close()
# printing title 
print(page_object.original_title) 

print(wikipedia.summary(name))
print("HTML OF PAGE") 
# printing html of page_object 
print(page_object.html)
