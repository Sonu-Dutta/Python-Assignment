import random
when = ['A few days ago', 'Yesterday morning', 'Last night', 'A long back','On my birthday']
who = ['a goat', 'an elephant', 'a mouse', 'a monkey','a buffalo']
place = ['China','India', 'Germany', 'jungle', 'England']
went = ['cinema', 'university','shopping mall', 'school', 'laundry']
activity = ['made a lot of friends','did not eat anything', 'celebrated my birthday', 'made reels on instagram','solved a mistery', 'wrote a book']
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(place) + ', went to the ' + random.choice(went) + ' and ' + random.choice(activity))