# CP1404 Assignment 2: Travel Tracker 2.0 by Cooper Plath

> The project reflection is complete and describes development and learning well, shows careful thought, highlights insights made during code development.


## 1. How long did the entire project (assignment 2) take you?
  I currently have spent, after viewing wakatime, close to 16 hours in the last week working on this assessment. I think my time was mostly spent watching over previous 
    pre-recorded lectures as well as collaborate lectures from this semester. This on reflection was the most time consuming element as I couldn't progress my project
    any further until I found the necessary information to apply within the code.


## 2. What are you most satisfied with?
  I think during the write up of this reflection and reviewing the final project, I found the comparison between the two assessments interesting. The use of classes 
  for the second assessment helped immensely with organising locations in the list as well as adding new entries. This was one of the main problems I had with 
  Assessment 1 beginning was importing from the place.csv file and being able to select components like .name or .location instead of [0][0]. This always 
  caused me drama and time fixing mis-placed numbers or colons. Additionally, I did find the use of kivy to be somewhat more enjoyable compared to watching
  the console display my program. Being able to see an application pop on screen and interact with buttons and text fields changed the dynamic somewhat. However,
  since only just beginning to code kivy applications, I did encounter road blocks from not implementing correct indention and box layouts.

## 3. What are you least satisfied with?
  There is a number of functions that I wish I had more time to implement into the final project for sure. Error checking for the most part worked exactly as planned
  however I wasn't able to code correctly the priority text input with it asking for an integer if a string was typed. This always caused a crash even after 
  using a Try/Except: ValueError. Additionally, implementing pushed down buttons was something that I was disappointed in. Using instance.state = 'down' worked
  up until locations.box.clear_widget was inserted. This pretty much caused the code to become obsolete so I used the little time remaining on polishing off other
  functions. Lastly, total_unvisited_places became faulty towards the end of the project (len([1 for place in self.file_places if place.is_visited == False])). This 
  was one of the first functions that worked correctly on the project but every new entry that is added to the main self.file_places list doesn't update. 

## 4. What worked well in your development process?
  On recollection, I found the Kivy demos to be a tremendous help in understanding and aiding in the development process of the assessment. Having working examples of
  demos as well as reviewing previous practicals I've done, it really did help me in understanding the task sheet and the requirements needed. Since doing uni from
  home, I'm unable able really to meet with other classmates and tutors to discuss and problem solve each section of the assignment. So having these tools readily available
  was great 
...

## 5. What about your process could be improved the next time you do a project like this?
  Like with anything, starting as soon as possible to get the maximum amount of time to research and problem solve each part of the project. Re-watching lectures as
  I said before took more time than I thought and thus showed in the end result. Also, I would have liked to have gone to campus and meet with the lectures face to face
  as its always a quick method of learning materials and hints as to what each function requires.

## 6. Describe what learning resources you used and how you used them.
  The only resources I used consisted of Github practicals, mainly kivy and classes with the solutions, as well as a number of powerpoint/recorded lectures from
  the last couple weeks that aided in me processing the assessment and understanding the task sheet. Without these, I truly would have been dead in the water.
  The practicals as I was saying before were tremendous in me understanding how kivy functions. Being able to input text into an app.kv and outputing that information
  into a python file was interesting. The assistance of google was underwhelming, even though we as the student aren't recommended to use outside resources. Not much 
  information was online for kivy code that I could find for my level of schooling. 

## 7. Describe the main challenges or obstacles you faced and how you overcame them.
   For some reason I found the most confusing section of the assessment was implementing dynamic widgets into the program from the place.csv file and outputting the correct
   string formatting. There was only a tiny section on lecture 12 I believe that showed almost a step by step on how to create this code. The kivy powerpoints I found on
   learnJCU didn't help whatsoever and this caused the biggest headache. Considering it was such a core function of the code, on reflection it shouldn't have taken me 
   so long as it did.

## 8. Briefly describe your experience using classes and if/how they improved your code.
   I found classes to be quite confusing to begin with especially when inheritance came into play. However after sometime learning and testing, I found classes to be
   important in effectively organising and displaying information. Being able to .add_place or .save_place quickly was instrumental in me building this project. 