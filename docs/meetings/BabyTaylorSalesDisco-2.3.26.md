Jagger Sturdivant
Jagger Sturdivant
So, I'm just gonna kind of walk you through a test client, and this is basically what we would have been doing for every single client that we were building a workbook for.
So, it all starts here in client space. So, I've kind of prepared this one a little tiny bit,
We would start out by, like, applying, like, the plan groups that we wanted to add, so if we wanted, you know, to add the dental plans or the Aetna plans, we would just apply these one at a time.
So I've already done that, so here are all, like, all the Aetna plans.
And then here we have their rate band. These are not set automatically by client space, these have to be set one by one.
So, I'll show you… I actually have a utility that will do that, because it's horrendous to do.
Manually.
But this is kind of what client space looks like.
So, what we do from here is we download the renewal workbook.
And it generates… Kind of a default document.
So this… this version is not client-ready, this is, like, a pre… preliminary thing, we haven't augmented anything yet. So it's got, like, all these default tabs, and…
I can't see the button, but…
All these tabs with, like, the backend data.
In it, this is where the new tailor, these hidden tabs, is what this will generate.
But Client Space is doing it right now.
So, we have a macro that formats the workbook, but opening this file, running the macro every time, it takes a lot of time. This macro is not quick. So, instead, we're gonna use Taylor.
So… I have a folder here. All I'm gonna do is drag that
File that we downloaded into this folder.
And then I have my IDE.
And all I do is click run, and it's gonna read that workbook, it's gonna open it, it's gonna augment it, and it's gonna run that macro and transform it into the client version of the workbook.
This is actually gonna throw an error, which is fine, because…
Almost every workbook throws an error, and we have to go back and fix something.
And then rerun it. So… We can see it's… it's auditing a bunch of information as well.
So it's making sure all those rates that were in client space are the right rates.
Okay.
It's making sure…
that plans are there, that need to be there. So all… it's making sure all these Aetna plans exist.
It's making sure that the mappings are correct. I'll show you what that means in a minute.
It's making me authenticate.
other thing it's checking for is we have regionalized Aetna plans. So, it just made me authenticate because it's pulling a census from PRISM.
And that census is attached to…
it pulls, like, employee zip codes, and then that's how it knows if we need to add regionalized plans into the workbook, so…
Right now, I can tell that I need Texas and North Carolina Aetna plans added.
So, to do that manually, We would have to go into client space, apply the plan groups, for…
Aetna, North Carolina, and Aetna, Texas.
But I don't want to do that, that's too much work. So…
they have… I have a utility here that I already have open.
So what this is gonna do is I'm just gonna give it a client ID, so 107 is the one we're working on.
And then I'm going to give it the…
plan groups as well, which I have here. So I want the North Carolina.
And I want Texas.
This utility right here actually has client space open, so I have it unhidden.
I can find which one it is… Here it is.
So, I'm not… I'm not doing anything. It's making all the clicks.
So right now, it's making sure that the previous year doesn't have anything broken about it. We had… we had problems where the…
The rates were wrong last year, which caused the workbook to be wrong, so it's making sure that that's correct in client space first.
Now it's going back, it's going to this year's.
First thing it should do is apply those two plan groups that we told it to apply.
Sometimes you gotta help it.
Oh.
Brett Hileman
Brett Hileman
05:04
While that's going, I'm curious… Was there a specific reason you went, like, computer use versus, like, API?
Jagger Sturdivant
Jagger Sturdivant
05:12
Last year, we did not have Client Space API.
Brett Hileman
Brett Hileman
05:14
Okay.
They don't have a choice. Yeah, yeah.
Jagger Sturdivant
Jagger Sturdivant
05:17
Yeah.
Brett Hileman
Brett Hileman
05:18
Okay. If you had to do it over again, do you think you would look API first? Oh, absolutely. Okay. That was my first thought, originally.
Scott Brittain
Scott Brittain
05:28
I built this last year.
This was, like, this was developed last year, this… this process.
Jagger Sturdivant
Jagger Sturdivant
05:33
Yeah, this is what we did last year.
Scott Brittain
Scott Brittain
05:35
Okay.
Ifat Ribon
Ifat Ribon
05:37
In the very first step of the scripts, where you said instead of running the macros in the workbook, you use your util, did you say that the utils are then…
grabbing the macro code and running them, or was that sort of, like, rewritten and applying it to the workbook?
Jagger Sturdivant
Jagger Sturdivant
05:53
So, no, I didn't rewrite the macro, it's opening an Excel instance and just running the macro. So Excel is still running the macro, it's just instantiating the macro to run.
Ifat Ribon
Ifat Ribon
06:03
Okay, and you said that turned out to be faster, or…
Jagger Sturdivant
Jagger Sturdivant
06:07
It's faster just because you don't have to actually go in and…
Open it. I don't know why.
Ifat Ribon
Ifat Ribon
06:12
Oh, okay. But it wasn't necessarily that it's…
The actual running of the macros isn't necessarily faster than the…
Jagger Sturdivant
Jagger Sturdivant
06:19
No, because it's still Excel doing it.
Ifat Ribon
Ifat Ribon
06:21
Okay, that's what I wanted to make sure I heard right.
Jagger Sturdivant
Jagger Sturdivant
06:27
Come on.
Ifat Ribon
Ifat Ribon
06:28
And then, in terms of those validations that it's running, is that… There's also…
you wrote… you said runs validations on rates and plans of what's entered in client space, right? Is that, also doing something similar, where it's, like, opening…
This browser and doing that? Or are there, like, other scripts that it's checking against?
Jagger Sturdivant
Jagger Sturdivant
06:47
No, it's not opening the browser. There's other files that it's… that it's had access to, so…
like, it has the rate book for Aetna, so it's looking at all the plans and then just making sure that that matches the rate book that Aetna gave us.
Just gonna apply this one manually.
Ifat Ribon
Ifat Ribon
07:04
And is that rate book something that, like, also gets added to client space? And, like, that's how you have things that pop up here that you can include in your offered plans? It doesn't get added to Client Space, it gets added into Prism, and if it's not imported properly into Client Space, that's where we get problems.
This person is meant to handle that connection, but sometimes it doesn't.
Jagger Sturdivant
Jagger Sturdivant
07:26
No, so, Client Space and Prism are owned by the same company, but they're completely separate, for some reason. They don't talk, really, at all.
The only place that they talk is the OBP import, and that just pulls in the current plans that they have in Prism.
Ifat Ribon
Ifat Ribon
07:41
Okay.
So the rate books get added to PRISM, And they…
they never make it into client space, or they end up in client space in a different way, like, through your manual steps, or…
Jagger Sturdivant
Jagger Sturdivant
07:53
I think they import them independently, so if I go into a plan here…
Like, this is where the rates are?
The problem is, this risk factor thing can sometimes be applied. So, this is just a multiplier, but if this is applied, it applies to these, even though these are already…
accounting for that risk factor. So it applies it twice, which causes the rates to be wrong.
So that's why we have it, double-check it.
Ifat Ribon
Ifat Ribon
08:22
Okay.
Jagger Sturdivant
Jagger Sturdivant
08:24
It's very… it's a lot of steps, and this is… this is why we're kind of rebuilding this, because client space is…
Getting in the way.
Ifat Ribon
Ifat Ribon
08:33
Yeah, for sure, we can start to see that here.
Jagger Sturdivant
Jagger Sturdivant
08:36
So…
This is where it's going back, and it's applying those rate groups one by one, because you can't mass update all of the plans. So those Texas and North Carolina plans we just added, it has to apply that rate band.
And this is just one workbook, so, I mean, you see how long one takes.
Ifat Ribon
Ifat Ribon
08:59
Yeah, and so after you… so you do this regional check so that you know that you have to add these other…
Plans and rate bands, and then do you have to kind of rerun the macro again, or how does that get, like, pulled back into the workbook?
Jagger Sturdivant
Jagger Sturdivant
09:11
Yeah, so we'll rerun the… we'll re-download the workbook and give it back to that utility, and then it should… when it rechecks, it'll pass, and then we should get a client-ready workbook.
Ifat Ribon
Ifat Ribon
09:22
Oh, right.
Jagger Sturdivant
Jagger Sturdivant
09:24
Okay, so it's done.
So, if we've done this correctly…
Just gotta drag it back into the folder, and then… Rerun this…
Scott Brittain
Scott Brittain
09:42
Yeager, are you doing this… are you the only one doing this for all of your clients?
Jagger Sturdivant
Jagger Sturdivant
09:48
This part of it, yes.
Scott Brittain
Scott Brittain
09:50
Okay.
Jagger Sturdivant
Jagger Sturdivant
09:52
The next step after this, we did have help, and it actually has a UI attached to it.
But… so we did… I did have help with this part of it.
Scott Brittain
Scott Brittain
10:04
So is your… is your schedule during open enrollment just like crazy? Because I'm sure that's what it is.
Just peaks for me.
Jagger Sturdivant
Jagger Sturdivant
10:10
Yeah. It was brutal.
Scott Brittain
Scott Brittain
10:14
Well, we want to make your job easier this year.
Keep your sanity.
Ifat Ribon
Ifat Ribon
10:25
I saw our… in the part where it sort of highlighted that you needed those regional plans, and then you pointed to another utility that, helped you get those added more automatically, I saw you pull the name maybe from your script, like…
Is that just for a reference point for you, or like…
Jagger Sturdivant
Jagger Sturdivant
10:43
Yeah, that's just, that's just…
Ifat Ribon
Ifat Ribon
10:44
every time.
Jagger Sturdivant
Jagger Sturdivant
10:46
That was just the easiest way, because they all… I don't want to add all of them, I want to add specific ones, and so I have to tell it which ones, so I just have them in a list to grab them super easily.
Ifat Ribon
Ifat Ribon
10:56
But does that list, like, also change pretty frequently? Frequently?
Jagger Sturdivant
Jagger Sturdivant
11:00
Oh, no, that list will never change.
Ifat Ribon
Ifat Ribon
11:02
Oh, okay, that list is more static.
Jagger Sturdivant
Jagger Sturdivant
11:07
One sec… Somehow we missed one.
Let's see…
Yeah, hopefully now we're good.
Sometimes they change the plan names and it breaks this, because it's looking for specific ones.
Ifat Ribon
Ifat Ribon
11:44
Right.
Jagger Sturdivant
Jagger Sturdivant
11:45
I may just remove it, so that it doesn't check for it.
Oops.
Just don't check that one.
Ifat Ribon
Ifat Ribon
11:58
And so currently, for all these pieces to come together, you also have it living in this, like, directory of all these other sort of reference files, right?
Jagger Sturdivant
Jagger Sturdivant
12:07
Is that right?
it's not much to look at, because, I mean…
These take forever to run sometimes, and…
It's a lot of, like, starting it, and then going to do something else for 5 minutes, and then coming back.
Ifat Ribon
Ifat Ribon
12:35
Totally.
No, I also live and breathe in sort of, like, backhand utilities, so I am impressed. I think this is very cool, what you've been able to automate here. I did want to go back to something else you said earlier.
when you… you download the Renewal Workbook, and you indicate it generates this template, but New Taylor should generate the new tabs. Can you speak a little bit more to what you're envisioning there, or what you mean by that?
Jagger Sturdivant
Jagger Sturdivant
13:00
So, by new tabs, you mean… Let me reopen it.
These tabs?
Ifat Ribon
Ifat Ribon
13:19
I think so. I think that's what you were pointing to. I was kind of jotting notes quickly. Maybe these import tabs. You mentioned something that would be different between Baby Taylor and what you see in the future, and I wanted some more clarity there.
Jagger Sturdivant
Jagger Sturdivant
13:29
So, it's not that these are different, it's that the new tailor will be creating these instead of Client Space. So, we have all the plan designs here, we need to pull that from Prism with new tailor so that we don't have to do anything with Client Space.
Ifat Ribon
Ifat Ribon
13:44
Okay, when you say don't have to do anything with client space, like, are you saying that the generation of the workbook won't happen… have to happen in client space, because we'll be able to get the data from elsewhere?
Jagger Sturdivant
Jagger Sturdivant
13:54
Correct, yes.
Ifat Ribon
Ifat Ribon
13:55
Okay.
Jagger Sturdivant
Jagger Sturdivant
14:10
Okay.
Hopefully this time it passes.
Yeah, it looks like it did. So, it saves that pre-macro workbook, and then it apparently doesn't run the macro, but…
Might have been because I opened it. Let me just… Manually run it.
Well, we don't need to. We would get the client version workbook, we would upload that in the client space.
They would execute it, they would make all their elections, and then that's where this utility comes into play.
it would be… you just drag it into here, you click run, and then it does the same thing. It has a client space instance, and it's going back in, and it's clicking through everything there to update all of
Like, what plans they picked, what the contributions they selected are.
If groups are being added or removed. All that fun stuff.
Ifat Ribon
Ifat Ribon
15:10
Just so I can say back what you just said while I was taking notes there, that utility takes the client workbook, which now has, client elections in it, and basically applies all those choices and selections into client space.
Jagger Sturdivant
Jagger Sturdivant
15:23
Yep, let me see if I can… might be able to pull up one that… is already done.
So we can kinda see what it's doing.
Cause we're not gonna mess anything up.
Yeah, it should work.
Thinking about it.
Okay
So it loaded the workbook. We can see it's kind of ready to go. We can see there are two groups. We can opt out of all of these plans if they didn't want them. So, like, if they didn't want Teladoc, they didn't want EAP, we would just uncheck those, and it would just not add them.
And then, let me just click run.
And then it's gonna
You know, search for the client, and it's gonna read that workbook and update everything in there.
It may not work because of the status being wrong, but we'll see.
It's very finicky with the window being open. Usually I have these wooden windows hidden.
Yeah, so it's setting the contribution.
And then it just… it does that for every plane.
That way, client space knows what to… to generate for the import and export files.
Brett Hileman
Brett Hileman
17:09
Guess I'm surprised how much data is going into client space. I was kind of thinking that all that data would live in Prism.
Those are two different systems, right?
Jagger Sturdivant
Jagger Sturdivant
17:19
Correct, and it eventually does. The whole reason we're putting it back into client space is so that we can import it into Prism.
Yeah, it seems very redundant, but…
Because literally, the next step after this is we download…
these two import files, so one's for, like, the plans that they picked, and then one is the rules, which is their contributions.
So I can, I can pull these.
And this is… Go ahead.
Ifat Ribon
Ifat Ribon
17:48
Oh, I was gonna say, sorry, this is a dense question, but…
in writing this script to automate entering into client space, like, why not have it go into Prism? Or do they only offer, like, an import, or are there, like, different fields, or is client space doing, like, some calculations or transformations or something?
Jagger Sturdivant
Jagger Sturdivant
18:07
As far as I know, it doesn't. It… I mean, it basically just builds that… these import files, so… hang on, let me open one.
Ifat Ribon
Ifat Ribon
18:17
I guess I have another way, like, do we need the import step, or, like, could there be a utility that, like, does this directly to Prism?
Jagger Sturdivant
Jagger Sturdivant
18:23
I think the team, they want these import files because they want to be able to see them before it gets imported into Prism.
Ifat Ribon
Ifat Ribon
18:30
Hmm.
Jagger Sturdivant
Jagger Sturdivant
18:30
Because they want to double check.
So this is… this is an actual client that made elections, so…
Client space generates this with what we put back into it.
So we can see, like, there's the Teladoc contributions amounts for each tier.
And then it adds just a ton of info. This template is given to us by Prism, so you… we can provide this.
Brett Hileman
Brett Hileman
19:00
Would you not be able to generate this, all this data from the workbook?
Ifat Ribon
Ifat Ribon
19:04
Right.
Jagger Sturdivant
Jagger Sturdivant
19:05
You can. Which I think that's what… that's what New Taylor should do.
Brett Hileman
Brett Hileman
19:09
Okay, so there's nothing… client space isn't adding any additional data that isn't in the workbook.
Jagger Sturdivant
Jagger Sturdivant
19:15
Correct, it is not.
Brett Hileman
Brett Hileman
19:17
Okay.
Jagger Sturdivant
Jagger Sturdivant
19:18
Yeah, we could have skipped it, just… we didn't. We put it back in the client space because that's what they told us we had to do.
Ifat Ribon
Ifat Ribon
19:28
Totally. So there's a world in which, like, maybe the team still wants this intermediary file so that they can run other validations, but…
I guess, like, Brett's asking, like, we could just have the utility make this file that's, like.
Jagger Sturdivant
Jagger Sturdivant
19:42
I think it should.
Ifat Ribon
Ifat Ribon
19:43
Yeah, okay. And then maybe there's a world where the team gets more and more comfortable with the success or, like, validations that this goes away too, right?
That's included.
Jagger Sturdivant
Jagger Sturdivant
19:52
Yeah, we just use the API and import it directly without this.
But this also… Prism will validate this as well, to an extent, so it's kind of double auditing to make sure that you didn't break anything when you're importing.
Ifat Ribon
Ifat Ribon
20:10
Yeah, that was something I was curious about. I… I felt like I heard a couple things on our earlier call that…
PRISM does have some validations, but maybe not all the validations the team wants.
Maybe you don't know off the top of your head, but maybe that's something we can uncover. It's like, which ones might it be missing?
Jagger Sturdivant
Jagger Sturdivant
20:30
It misses a lot. It kind of lets you do whatever you want, even if…
like, it's illegal to do at all, but it'll still let you do it. It doesn't really validate anything.
Ifat Ribon
Ifat Ribon
20:41
Okay. So I guess,
when you said a minute ago, like, it does have some of these validations, like, is that just more on, like, data types, and, like, doesn't really catch the hard stuff, or…
Jagger Sturdivant
Jagger Sturdivant
20:52
Yeah, like,
Like, if this weren't here, like, if that value was missing, it would tell you that that's missing.
Ifat Ribon
Ifat Ribon
21:00
Okay, just kind of…
Jagger Sturdivant
Jagger Sturdivant
21:01
It would not tell you if this was, like, negative 100. It would let you do that.
Ifat Ribon
Ifat Ribon
21:07
Okay.
Gotcha.
Jagger Sturdivant
Jagger Sturdivant
21:14
And then this is exported from client space. A lot of this is wrong. So there's another Taylor utility that ingests these, and…
Edits the crap out of them.
There's also another macro it runs, because of course there is.
I think it's in the other file, but…
It basically edits this to how the analysts needed it to be. We won't have to do that, because we'll just build it correctly the first time.
And then the last thing Taylor does is the audit.
Brett Hileman
Brett Hileman
21:49
I think I maybe missed that. It's saying… are you saying a macro edits the import file?
Jagger Sturdivant
Jagger Sturdivant
21:54
No, so there's another Taylor utility, let me… I don't have it open, let me see if I can get it.
Actually, I think I have it installed.
Can't find it, but… yeah, it basically just… it runs… I think the other import file has a macro attached to it as well.
Yep, it does. So…
There's another utility that takes in both of these files, it runs this macro, it edits a bunch of this data to be formatted properly, because Client Space didn't do it right.
And then you can import it into Prism.
It's very similar to how the workbook utility worked.
Same concept, just different files.
Brett Hileman
Brett Hileman
23:21
Okay.
So I'm gonna repeat that back, and I maybe have it wrong, just because I want to make sure I understand.
Jagger Sturdivant
Jagger Sturdivant
23:28
This separate util is…
Brett Hileman
Brett Hileman
23:31
Doing, like, a cleanup on the file that was exported from client space?
Jagger Sturdivant
Jagger Sturdivant
23:36
Correct, yes.
Brett Hileman
Brett Hileman
23:38
So you're putting data into client space to generate the import for Prism, but it doesn't do that properly, so you had to make a macro
to correct it.
Jagger Sturdivant
Jagger Sturdivant
23:49
You've nailed it, yeah.
No, it sounds silly, but that's what happens.
Brett Hileman
Brett Hileman
23:55
No, I mean, it's the situation you're in. I don't blame you for building anything that you've built.
Yeah, you're working with the cards that were dealt, so… Right, yep.
Jagger Sturdivant
Jagger Sturdivant
24:08
And then the last thing it does is we just have a couple of extra audits talking about the stuff that Prism doesn't check for.
Stuff like being… someone being enrolled in a plan that got terminated. Prism doesn't tell you that, so we have to go manually check to see if that happened.
Brett Hileman
Brett Hileman
24:29
Got it.
Ifat Ribon
Ifat Ribon
24:33
That, that kind of check…
Is that possible from the information at hand, or is it only possible, like, from PRISM? Because PRISM also, like, links the actual employees and their status and things like that.
Jagger Sturdivant
Jagger Sturdivant
24:43
Yeah, you have to do that one from Prism.
Ifat Ribon
Ifat Ribon
24:47
Okay.
Jagger Sturdivant
Jagger Sturdivant
24:47
Because the workbook doesn't have any, like, enrollment information attached to it.
Ifat Ribon
Ifat Ribon
24:53
I guess…
Jagger, if you kind of had all the time in the world, like, what would be your ideal flow that you would have built?
Jagger Sturdivant
Jagger Sturdivant
25:00
The one that we proposed for NewTaylor would have been my ideal flow. Kind of like, you give it a client ID, it pulls everything out of Prism, it builds the workbook for you.
And then you click a button, it goes into client space, It imports everything for you.
you're done. You don't really have to… and then it just automatically runs audits.
After the enrollment posts.
Ifat Ribon
Ifat Ribon
25:26
Well, I guess that step in terms of, like, importing a client space, like, that's still needed? Like, it needs to be in both client space and present at the end of the day, or…
Jagger Sturdivant
Jagger Sturdivant
25:33
Nope, it does not have to be in client space.
The only reason we put it back in the client space was for this file right here.
But if it builds this file.
Client space never has to be… Update it.
Ifat Ribon
Ifat Ribon
25:45
Okay, so the ideal flow that you described…
generate the workbook from the client ID.
and then generate an import file for Prism, not for Client Space.
Jagger Sturdivant
Jagger Sturdivant
25:54
Correct, yes.
Ifat Ribon
Ifat Ribon
25:55
Okay.
Scott Brittain
Scott Brittain
25:58
Do you… this maybe this is a higher level question, but, like, do other PEOs use PRISM in client space? Or are you guys… I guess, like, how's everybody else figuring this out?
Jagger Sturdivant
Jagger Sturdivant
26:10
Prison is actually owned by another PEO.
Scott Brittain
Scott Brittain
26:13
Oh, really?
Jagger Sturdivant
Jagger Sturdivant
26:14
Yep, I don't know how many other PEOs use it, but I mean, I think that's their main business, so…
Scott Brittain
Scott Brittain
26:19
That seems… so they just have, like.
people have to do this manually, right? I mean, like, I doubt anybody's…
Maybe they have, but written what you have here in terms of trying to speed it up.
Jagger Sturdivant
Jagger Sturdivant
26:29
I know there is another PEO that has it.
Like, they have, like, a whole web-based UI, and it just auto-imports everything into Prism.
But that's the only one that I know of that has anything like that.
I don't know how the rest of them are doing it.
Scott Brittain
Scott Brittain
26:43
Interesting.
Okay. I know we're coming up on time. Also been really helpful, I think, just to kind of see behind the scenes.
Jagger Sturdivant
Jagger Sturdivant
26:53
I know it's a lot.
Scott Brittain
Scott Brittain
26:55
It is. It's not an easy thing to explain over a 30.
Jagger Sturdivant
Jagger Sturdivant
26:58
No.
Scott Brittain
Scott Brittain
26:58
Even a couple discovery sessions, but, I think we're starting to wrap our heads around it.
Do you see, I guess, like, one question would be, like, do you see, like, value in moving these calculations outside of, like, the macros into its own…
like, platform, basically? Or, like, do you think there's…
enough of, like, variability or risk in, like, Prism and client space that, like, building something custom would…
ultimately, like, maybe break something in the future. I guess, like, how…
How outside of this process do you think you could push it in the future?
To even speed this up more.
Jagger Sturdivant
Jagger Sturdivant
27:32
I think you could push it pretty far. You're talking, like, get everything out of Excel?
Scott Brittain
Scott Brittain
27:37
Yeah.
Jagger Sturdivant
Jagger Sturdivant
27:38
Yeah, I think you could do everything outside of Excel.
And I think that's kind of the end goal, is to have a web-based UI, and so everything would have to be outside of Excel.
But, I mean, it's definitely doable.
But there are a lot of edge cases, like, with those regionalized plans, like.
If you don't know how to check for those, they won't be added, and you'll miss them.
Scott Brittain
Scott Brittain
28:00
Right, right.
Yeah, and I think just within the timeline that we have for this… for this scope, right, like, just making sure that we don't…
Over-commit or, you know, overbuild.
Jagger Sturdivant
Jagger Sturdivant
28:11
Right, I agree.
Scott Brittain
Scott Brittain
28:11
So get a solid first foundation built, something that we can use in the future.
that's, like, a scalable architecture, that we could build, like, a front-end UI for eventually.
Okay, cool. Anything, final thoughts from anyone?
Ifat Ribon
Ifat Ribon
28:28
No, this was super helpful, so really appreciate it.
Jagger Sturdivant
Jagger Sturdivant
28:31
Of course.
Brett Hileman
Brett Hileman
28:32
Yeah, thank you.
Jagger Sturdivant
Jagger Sturdivant
28:34
If you guys have any more questions, just… you can email me. I'll respond.
Scott Brittain
Scott Brittain
28:38
Awesome, awesome. Well, hey, good work for what you built. That's impressive. Thanks.
Okay, sounds good. Thanks for the time, Jaeger, and we'll catch you soon.
Jagger Sturdivant
Jagger Sturdivant
Alright, sounds good.