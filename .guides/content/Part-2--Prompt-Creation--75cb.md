Now that we have our box we need to be able to fill it with a list of movies. The next step we are going to take is creating our prompt. We are going to create a function called Moreflix that will prompt the user for: 
1. The number of recommendations they want 
2. The genre they want 
3. A similar movie they have in mind.

We write the code below to take care of that. The function will prompt users and return a prompt for us to feed to our OpenAI. We want the user to be able to type 0 if they don't have an answer in mind.
```python
def Moreflix():
  # ask the user for different inputs
  print("Enter 0, if you don't have an answer in mind")
  number_recs=int(input('How many movies do you want recommended: '))
  genre=input('What genre are you looking for: ')
  similar= input('What is a similar movie: ')
```
To try it add the print statement `print(Moreflix())`  and press the button below
{Try It!|terminal}(python3 moflix.py)

From there we have all the tools needed for us to write our prompt. First of all if they add `0` to the number of recs we will default it to `5` for them.
```python
if number_recs==0:
  number_recs=5
```
{Try It!|terminal}(python3 moflix.py)
For the others if `0` is included we will generate a prompt simply asking for the number of recommendation. But first we are about to create our first prompt. A quick reminder,here are three basic guidelines to creating better results:
* **Show and tell**
* **Provide quality data**
* **Check your settings**

We are going to focus on show and tell on 3 things:
1. Giving the model clear instructions (tell)
2. Giving the model an example (show)
3. Giving the model clear instructions and an example (show and tell) 


In order for the prompt to generate more clear answers, try the following prompt in the playground in the bottom left next to your terminal. `In a python array form, give me 3 movie recommendation`

{Try it!}(python3 box.py 10)
{Reset}(python3 reset.py 10)

Now that we have a sample prompt and have an idea of what the response would look like, we can start coding. We are going to take care of edge cases where the users do not provide all the information. Base on the information that the user provides we will, create different prompts. For example here is an example where the user do not provide a genre or a similar movie. Copy and paste the code to the `moflix` file on your left.  

```python
if genre=="0" and similar=="0":
  return("In a python array form, give me " + str(number_recs) +" movie recommendation")
```
{Try It!|terminal}(python3 moflix.py)
Now we can take care of the additional scenarios

```python
if genre=="0" :
  return ("In a python array form, give me " + str(number_recs) +" movie recommendation, similar to " + similar)
if similar=="0":
  return ("In a python array form, give me "+genre + " "+ str(number_recs) +" movie recommendations")
return ("In a python array form, give me "+genre +" "+str(number_recs)+" movie recommendation similar to " + similar)
```
{Try It!|terminal}(python3 moflix.py 4)

Now run the following to make sure all the work is going well. To make our code cleaner, feel free to remove the print statements when done with it. 
`print(Moreflix())`

To increase our accuracy, of getting the AI to do what we want after our prompt we will start it off with providing it space to do what we want
`
Prompt=Moreflix() + "rec="
`

{Check It!|assessment}(multiple-choice-3296452282)
