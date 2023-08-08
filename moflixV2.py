import os
import openai
import secret
openai.api_key=secret.api_key
import ast
# print element of a list in nice box for the user
def InBox(x):
  x=(["Movie Recommendations"]+x)
  #this gives you the longest string
  biggest = max(x, key = len)
  #THIS GETS the len of the biggest string
  biggest=len(biggest)
  #creating our box
  print("+" + "-" * (biggest + 2) + "+")
  for i in x:
    print("| " + i + (" "*(biggest-len(i))) + " |")
    print("+" + "-" * (biggest + 2) + "+")

def Res(x):
  response = openai.Completion.create(
    model="text-davinci-002",
    prompt=x,
    temperature=0,
    top_p=1,
    max_tokens=100)
  return(response['choices'][0]['text'].strip())

def Moreflix():
  # ask the user for different inputs
  user_req=input("what recomendation type do you want? book ?song? movies? show? ")
  number_recs=input('How many '+user_req+' do you want recommended: ')
  genre=input('What genre are you looking for: ')
  similar=input('What is a similar ' + user_req +': ' )
  if number_recs=="0":
    number_recs=5
  if genre=="0" and similar=="0":
    return("In a python list form, give me " + str(number_recs) + user_req + "recommendation")
  if genre=="0" :
    return ("In a python list form, give me " +str(number_recs) + user_req + "recommendation, similar to " + similar)
  if similar=="0":
    return ("In a python list form, give me "+ str(number_recs)+ " " + genre + user_req + " recommendation")
  return ("In a python list form, give me "+str(number_recs)+" "+genre + user_req +" recommendation similar to " + similar)

Prompts=Moreflix() + "rec ="
movies=(Res(Prompts))
try:
  movie_list=ast.literal_eval(movies)
except:
  movie_list2=""
  for i in movies:
    if i=="]":
      movie_list2+=(i)
      break
    else:
      movie_list2+=(i)
  movie_list=ast.literal_eval(movie_list2)

InBox(movie_list)