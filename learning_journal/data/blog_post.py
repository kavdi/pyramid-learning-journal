"""Journal entries."""
from datetime import datetime


FMT = '%m/%d/%Y'


POSTS = [
    {
        "date": datetime.strptime("11/01/2017", FMT),
        "title": "Day 12",
        "id": 12,
        "author": "kavdi",
        "text": "Aaaaaaand... I am officially behind. haha\r\nI don't feel confident at all with the material we covered on servers today. Thankfully the data structures were not too confusing to understand or I would be crying right now lol. I did learn what a Binary heap is and the simple difference between min heap and max heap. I do need to figure out how to manage my time better so I can take more time to review the material covered during lecture and rewatch the recordings to help my understanding of it.",
    },
    {
        "date": datetime.strptime("10/30/2017", FMT),
        "title": "Day 11",
        "id": 11,
        "author": "kavdi",
        "text": "cookiecutter... pyramids...deques... It's Monday. The good thing is that we don't have to make the server, we just need to implement it for a new learning journal project we are starting. It was great following during lecture and then a bit slower trying to implement the same thing during lab. I think I get the basics of what we learned, but need to go over the notes and reading to cement what I think i know.",
    },
    {
        "date": datetime.strptime("10/27/2017", FMT),
        "title": "Day 9",
        "id": 9,
        "author": "kavdi",
        "text": "Today went relatively well. I have quite a bit of review and reading to do this weekend so I can strengthen my grasp of the material we have covered this week. I really enjoyed hearing from past python grads about their experience with the class and how they are doing now. I hope there is not too much assigned tomorrow or for this weekend.. I already have some catching up to do... but then again, I know we will definitely have more work assigned haha, looking forward to the next challenge.",
    },
    {
        "date": datetime.strptime("10/26/2017", FMT),
        "title": "Numero Ocho (Day 8)",
        "id": 8,
        "author": "kavdi",
        "text": "Today was a good day. The struggles were real and the wins were great. I feel like I am understanding most everything that we are covering so far, and have great partners for both assignments that help me with the areas  I don't feel so confident in. I am still a little blurry with how to use supers, and inheriting from a different class... we implemented it on our doubly linked list, and succeeded on one of the functions we made but not on the second. I am not very sure why, and need to do some more reading on it..... honestly I could use a good day just to read up on the http/classes/supers...etc to get some more confidence in my understanding of them. The white board challenge went really well, its amazing how things get easier when you write them down and map out what you need to do. I look forward to more of these challenges.",
    },
    {
        "date": datetime.strptime("10/25/2017", FMT),
        "title": "Day 7",
        "id": 7,
        "author": "kavdi",
        "text": "Stacks!.... soo linked lists that can only be accessed from he head? haha seemed pretty straight forward and was easy to implement since we had everything done for he linked lists. Still having a couple dumb issues with the sockets and http requests and response.. but so far i don’t feel out of depth. Keeping up with the reading helps soooooo much. Anyways back to reading and hopefully learning some more. My brain is so full rn though...",
    },
    {
        "title": "Day 6",
        "author": "kavdi",
        "date": datetime.strptime("10/24/2017", FMT),
        "id": 6,
        "text": "Web sockets and linked lists... Can't say I fully grasp the subject but I didn't know anything about them before, so I have learned quite a bit. I am going over the web sockets because it seems simple enough, but I have been having a few issues implementing what I read in the assignment. Linked lists have been a lot easier to understand, and i am  understanding how to set up classes and test them. Now back to reading...",
    },
    {
        "title": "Day 5",
        "author": "kavdi",
        "date": datetime.strptime("10/22/2017", FMT),
        "id": 4,
        "text": "Well f#$% this dis day did not go as I thought it would.. wasted too much time on difficult katas. Finally was able to get the needed points and do the testing with tox. The one good thing from today was that I understand tox much better now. Thank you Gabe! this does not feel like a weekend... no bueno.. and theres more hw to do.... bye life haha",
    },
    {
        "date": datetime.strptime("10/20/2017", FMT),
        "title": "Day 3",
        "id": 3,
        "author": "kavdi",
        "text": "So many new things, my brain is full haha. From string features to dictionaries. There is a certain similarity to js that we learned about in 301 but also lots of differences. I don't like how python2 and python3 differ and that we have to account for how code responds differently depending on which one we use. I also didn't understand the Python packaging very well and need to review it farther. Feeling a little like I did in 201 and I hear that it starts getting hard in week 2 haha. I see lots of late nights ahead.",
    },
    {
        "date": datetime.strptime("10/18/2017", FMT),
        "title": "Day 2",
        "id": 2,
        "author": "kavdi",
        "text": "Today I learned about testing our code. I made a twitter account, and I signed up for a lightning talk... not sure what I will talk about in the lightning talk or if I will use twitter that much, but who knows. \r\nLearning about testing was great, I am sure we will learn quite a bit more about it and look forward to it. I like the fact that we can write tests to make sure our code is working the way we want it to work, this will come in handy once we start working on larger projects. All in all it was a good day and I feel like I understood everything that we went over in class.",
    },
    {
        "date": datetime.strptime("10/17/2017", FMT),
        "title": "Day 1",
        "id": 1,
        "author": "kavdi",
        "text": "Python... A new journey in learning. It was interesting to learn about some of the differences between the python2 and python3, seems like we might be switching back and forth a bit.... might get confusing. Setting up different environments for every project seems like a overkill. I do wonder why there isn't a simpler way of setting it up so each project will run on the packages we want it to without making a completely different environment for it. I am excited and nervous about the weeks to come and the learning brain pain that comes with them.",
    }
]