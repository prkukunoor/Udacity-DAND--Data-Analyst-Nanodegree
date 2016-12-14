Question 1 - Describe a data project you worked on recently?

The most recent project that I worked on was A/ be testing on Udacity "start free trial" .

In the experiment, Udacity tested a change where if the student clicked "start free trial", they
were asked how much time they had available to devote to the course. If the student indicated
5 or more hours per week, they would be taken through the checkout process as usual.
If they indicated fewer than 5 hours per week, a message would appear indicating that Udacity
courses usually require a greater time commitment for successful completion, and suggesting
that the student might like to access the course materials for free. At this point, the
student would have the option to continue enrolling in the free trial, or access the course materials
for free instead.

The hypothesis was that this might set clearer expectations for students upfront, thus reducing
the number of frustrated students who left the free trial because they didn’t have enough
time — without significantly reducing the number of students to continue past the free trial
and eventually complete the course. If this hypothesis held true, Udacity could improve the
overall student experience and improve coaches’ capacity to support students who are likely
to complete the course.

The unit of diversion is a cookie, although if the student enrolls in the free trial, they are
tracked by user-id from that point forward. The same user-id cannot enroll in the free trial
twice. For users that do not enroll, their user-id is not tracked in the experiment, even if they
were signed in when they visited the course overview page.

Finally after the Experiment Made some recommendations . 

Question 2 - You are given a ten piece box of chocolate truffles. 

You know based on the label that six of the pieces have an orange cream filling and four of the pieces have a
coconut filling. If you were to eat four pieces in a row, what is the probability that the first two pieces you 
eat have an orange cream filling and the last two have a coconut filling?

Yes the probability of eating first two choices will be orange and next two choices will be coconut

My Probability choices follows as below:

1)Probability of first orange is :6/10

2)Probability of first orange is :5/10

3)Probability of first coconut is :4/8

4)Probability of first coconut is :3/7

Total Probability you will get by multiplying all four:

P(1)*P(2)*P(3)*P(4) = 7.14%


Follow up question: If you were given an identical box of chocolates and again eat four pieces in a row, 
what is the probability that exactly two contain coconut filling?


There're 14 combinations, assuming each combinations have similar probability

so We have 6 possible combinations allowing us to get 2 coconat truffles:

Therefore, we have P(exactly 2 coconuts in 14 combinations) = 6/14 = 42.857%

Question 3 - Given the table users:

Construct a query to find the top 5 states with the highest number of active users. Include the number
for each state in the query result.

select state, count(id) as num_active_users from users
where active = 1
group by state
order by num_active_users desc
limit 5

Question 4 - Define a function first_unique that takes a string as input and returns the first non-repeated (unique) character in the input string. 
If there are no unique characters return None. Note: Your code should be in Python.

def first_unique(string):
    seen = set([])
    for i in range(len(string)):
        letter = string[i]
        if letter not in seen and letter not in string[i+1:]:
            return letter
        seen.add(letter)
    return None
    
Question 5 - What are underfitting and overfitting in the context of Machine Learning? How might you balance them?

The Underfitting is the situation in Machine Learning Concept

when the model does not capture the trend in data well, That is even on training set, performance is not good  .

The overfitting in Machine Learning Concept is when the model shows good results on training set, 
but poor results on new data.

Validation and cross-validation of the model are the usual ways to fix it.

Question 6 - If you were to start your data analyst position today, what would be your goals a year from now?

This Job is posted on linkedin

(https://www.linkedin.com/jobs/view/242733516?refId=18562ade-494e-4b47-92dd-ffc9e8a52514&trk=job_view_browse_map)


Job description
RESPONSIBILITIES
Ability to work as a member of a team assigned to design and implement customer solutions.
Data analysis – skills to conduct analysis and deliver recommendations to the team and customer.
Presentation skills – demonstrated ability to simplify complex situations and ideas and distill them into compelling and effective written and oral presentations.
Learn quickly – ability to understand and rapidly comprehend new areas – functional and technical – and apply detailed and critical thinking to customer solutions.

QUALIFICATIONS
B.S. or equivalent degree in computer science, mathematics or other relevant fields.
0 – 3 years of experience in business analytics, data science, or consulting in
these fields.
Programming skills – experience and expertise in a minimum of one of thefollowing areas: 
SQL, Java, SAS, R, Python. Experience with Agile implementation methodologies.

Within one year, my goal are:

Code fluently in Python to develop new innovative metrics to track.Develop more knowledge R Language.
Query database cold & create new assumptions/hypothesis and test it. 
data & conduct a statistical test to test if this is true, and how could we target those new emerging segment.


  
 





