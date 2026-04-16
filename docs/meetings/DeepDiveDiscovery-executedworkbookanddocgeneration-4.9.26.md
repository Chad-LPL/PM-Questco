Taylor Deep Dive on Executed Workbook and Document Generation - April 09
VIEW RECORDING - 62 mins (No highlights): https://fathom.video/share/TnPSDgSApSmzzSZFz71SpvrzEbwH7EEE

---

0:00 - Anna.Fiske
  Hi, how are you?

0:02 - Chad Gregory (LaunchPad Lab)
  Doing all right. How about yourself?

0:06 - Anna.Fiske
  I'm good. I'm good.

0:09 - Chad Gregory (LaunchPad Lab)
  Sorry to drag you into so many calls.

0:12 - Anna.Fiske
  No, I think it's worth it.

0:14 - Chad Gregory (LaunchPad Lab)
  Yeah, it definitely helps. Hey, Dimple. Yeah, we're trying to get our hands around everything and definitely appreciate all the time, especially this week.  Um, tomorrow is going to be a big day for me and Nikki and Jose to really, like, try to put all our tickets together into the plan.  Um, I think we're realizing that the SOW items themselves are not really going to make the best tickets, unfortunately.  So, there's There's probably some reorganization on the Asana board that you'll see and everything, but we've got some good sessions tomorrow, and I don't know that we're going to have the full plan figured out tomorrow, although that was my goal, but I just wanted to be transparent and let you guys know.  So obviously it's something that we're working on pretty hard, and fortunately we did get the thumbs up from Chris on the technical architecture, so we can move forward on all of that, and that's good.  Yes. Oh, you got this. This going here. Yeah.

1:43 - Dimple Desai (Questco Cos)
  Chris showed me those, but I've never been able to, do I need to enable something?

1:46 - Chad Gregory (LaunchPad Lab)
  You have to click the, are you on a Mac?

1:49 - Dimple Desai (Questco Cos)
  No. Oh, I don't know if you can do it on a PC, actually. Okay.

1:57 - Chad Gregory (LaunchPad Lab)
  Awesome. Okay, so we can get into things. On this call. Let me pull up my notes again. So we wanted to figure out, talk more about the executed workbook and generating these documents.  So I think part of this will be like kind of looking at the workbook and part of this will be looking at the documents.  We have templates. I don't know if we have like final versions of like the CBE benefit guide or cost sheet, to my knowledge.  You might have put those in Dimple, but I've seen so many different things. I could be missing them. But starting with the executed worksheet, her workbook, I guess my first question is, what is it that makes the workbook executed, quote unquote?  Is that just the client says that it's good? And like their selections?

2:58 - Anna.Fiske
  Yeah, that'll be that. Everything is elected in column L. So they have their plans filled out and the contribution is filled out.  So if they pick a plan, but they don't put a contribution in, we kick it back because we won't assume anything on the client's behalf, as well as the bottom part.  As it sits today, that bottom part of the workbook has all the employer paid. You saw like the disability and the life down there and the EAP.  All of that has to be filled out as well.

3:27 - Chad Gregory (LaunchPad Lab)
  Let me open this guy. So I think this was the example we had that was like the executed version.
  SCREEN SHARING: Chad started screen sharing - WATCH: https://fathom.video/share/TnPSDgSApSmzzSZFz71SpvrzEbwH7EEE?timestamp=221.188988  If I go to primary. So what should I be looking for? So here are these, these are the contributions you're saying.

4:00 - Anna.Fiske
  That's the right. So over in column N, that should be filled out the contribution method. So if you click on that orange box, it's a dropdown.  And that's when you put in what kind of contribution you want to do, whether you want to keep it the same percentage or dollar amount wise, or you want to key it in.

4:17 - Chad Gregory (LaunchPad Lab)
  Okay. So for some reason, we saw this sheet dropped into SharePoint and like these fields were not filled out.  Right.

4:28 - Anna.Fiske
  is a, so Claymore University, that 107 client, this is a demo client. So it doesn't have any employer contributions because we don't run payrolls off of it.  Oh, I see. So we wanted to give you the demo information instead of real client information.

4:41 - Chad Gregory (LaunchPad Lab)
  Yeah, that makes sense. Mm-hmm. Do you think that would ever be the case that something would be missed like that when it got into SharePoint?

4:53 - Anna.Fiske
  Baby Taylor audits that now. So it is done a lot, but yeah, Baby Taylor will. Flag that and we'll kick it back.  To say, hey, you need to fill out the contribution. And that's for all for medical, dental, and vision.

5:05 - Chad Gregory (LaunchPad Lab)
  Yeah. In terms of column L, like, they're pretty much always going to have something in there, right? Chosen? Yes.

5:16 - Anna.Fiske
  Usually, yeah.

5:18 - Chad Gregory (LaunchPad Lab)
  Like, that's not going to be, unless it's one of these new plan fields, we wouldn't be able to know.  Would we be able to know if something was missing there?

5:33 - Anna.Fiske
  Only if it was empty, yeah. Kind of like you said, because BabyTaylor now will make sure that column is filled out, column L, and that it's the same plan as column D, to show the true renewal.  And then that's before the client gets it. So then after the client gets it, like you said, there will always be something in there, because we pre-select it for them.  And then whatever they return in that column is what we're going to install as a renewal.

5:57 - Chad Gregory (LaunchPad Lab)
  Really, we should be looking at P and Q. I guess. Is that right?

6:03 - Anna.Fiske
  Yeah.

6:04 - Chad Gregory (LaunchPad Lab)
  Yeah.

6:05 - Anna.Fiske
  Either O or P. Yeah.

6:07 - Chad Gregory (LaunchPad Lab)
  Oh, O or P. Okay.

6:10 - Jagger Sturdivant (Questco Cos)
  You just have to make sure that they picked a contribution method. If it's stuck in that bracketed contribution methods, then they didn't pick anything, and you'll have to flag that.

6:22 - Chad Gregory (LaunchPad Lab)
  Okay. I see these different options are. Yeah. So we could look at column N in the top header for each of these to see if something was picked.  Okay.

6:50 - Nikki Dow
  If Baby Taylor checks this and there's places they're supposed to make a selection and they didn't, what happens then?  Like, does the batch code? Into a certain status.

7:02 - Jagger Sturdivant (Questco Cos)
  No, there's a separate application that, it does it when it's importing the workbook data back into client space, and that's a separate application.  So that application just flags it then and there and tells you that you need to go back and fix it.  There's no like status update for that.

7:20 - Anna.Fiske
  So it flags it for you then, Jagger?

7:23 - Chad Gregory (LaunchPad Lab)
  Is that what you're saying? Yeah, whoever's importing it in a client space will see it. Do you have another question on that, Nikki?

7:37 - Nikki Dow
  No, I'm just thinking about like, so we're going to generate the Prism import files based on the selection, right?  And I think that is when we would see these selections work made. So I guess, I don't know, maybe we need to think about like.  Would we see it when the.

8:01 - Chad Gregory (LaunchPad Lab)
  The documents were generated.

8:04 - Jagger Sturdivant (Questco Cos)
  Yeah, you would see it when the documents are generated, which I guess you could generate the Prism import files then as well.  Yeah, we could.

8:13 - Chad Gregory (LaunchPad Lab)
  Yeah. Okay. I wanted to ask, yeah, so we should be looking at more than just column L here, because we need to pay attention to column L, but we need to grab all of this data in L through R.  Is that everything that's going to be needed for generating the documents?

8:49 - Anna.Fiske
  Yes.

8:50 - Chad Gregory (LaunchPad Lab)
  Okay.

8:51 - Jagger Sturdivant (Questco Cos)
  Well, for medical, dental, and vision, yes. But for like the other ER plans, you'll have to go to the bottom.

9:00 - Chad Gregory (LaunchPad Lab)
  Yeah, that's true. And then obviously there'll be some other like client data to include. And we need to look at each of the classes.  How do you break up the, this may be a question that I'm getting ahead of myself a little bit, but how do these classes differ in like the documents and everything that we, that you end up sending?  Are there like different sections for each class or different documents for each class or?

9:40 - Anna.Fiske
  It would be different cost sheets for each class because that's kind of why we have classes is because they'll contribute differently to those, but they'll all get the same benefit guide and the CBE will show them together.  Yeah. So it'll say primary and then owner's right underneath it for each benefit. So if somebody only had one class, does that mean they only...  I have one cost sheet? Correct.

10:02 - Chad Gregory (LaunchPad Lab)
  So what does it typically, or what does it look like today when you get the executed worksheet? Does that already go straight into SharePoint for somebody to pick it up?

10:22 - Anna.Fiske
  The executed workbook, it's uploaded in client space. We have a dedicated field. And then they push consultation complete button, which will then push the batch status forward to client election updates.  And that's when me and Jagger will get a task at client space to say, create their CBE.

10:42 - Chad Gregory (LaunchPad Lab)
  So nothing is it, like this does not end up in SharePoint today. Not today. We don't currently use SharePoint for anything.  Okay.

10:52 - Jagger Sturdivant (Questco Cos)
  It's a new thing. Okay.

10:54 - Chad Gregory (LaunchPad Lab)
  So then in the world of using SharePoint, we kind I need to think about like a structure for that.  Like does each client have a folder and then there's a folder structure within that for all the documents that we need for that client, which would be where this ends up.  Do you envision the person that would typically be putting that into client space still putting it in a client space or just like changing their process to put it into SharePoint?  Then I think it would be okay to do the latter because Taylor would pick up the task that was, yeah, Taylor would pick up the task that you guys had assigned to start generating the CBE and everything.  Does that make sense what I'm saying? It does.

11:59 - Anna.Fiske
  I'm not sure, Jagger. I think we had talked about dropping it in SharePoint, right?

12:02 - Jagger Sturdivant (Questco Cos)
  Yeah, and I think the reason for that is because of the webhook problem that ClientSpace has. Because you can listen to SharePoint, and so you'll know that it's there.

12:12 - Chad Gregory (LaunchPad Lab)
  Yeah.

12:12 - Jagger Sturdivant (Questco Cos)
  And then Taylor can, yeah, just move it to ClientSpace.

12:17 - Chad Gregory (LaunchPad Lab)
  Connor, what are you thinking?

12:20 - Conor Hawes
  I'm just thinking about access control. Like, if individuals are tied to different, like, certain companies in ClientSpace, then, but all of the documents move to SharePoint, like, how would we make sure that that user is authorized to download that file?  We don't need an answer right now. It's just, maybe just thinking out loud.

12:56 - Chad Gregory (LaunchPad Lab)
  I'm wondering if they are not. Given access to download anything in SharePoint.

13:07 - Conor Hawes
  That's an interesting alternative to explore. I guess the business question would be when that document is added to client space, is it being viewed for a manual review step?  Do they need to be able to see it or do they just need to be able to see this executed workbook has been uploaded to SharePoint and it's there, but I can't view it.

13:36 - Jagger Sturdivant (Questco Cos)
  Who is they? Like, who are we talking about here?

13:45 - Conor Hawes
  Anyone with access to that company in client space.

13:52 - Jagger Sturdivant (Questco Cos)
  Dimple, doesn't everybody have access to every client?

13:56 - José Blanco
  Don't be the CSP team, I believe you call it.

14:03 - Dimple Desai (Questco Cos)
  I'm talking and I'm muted. Yes, everybody has access to every client and client space currently. We do have the ability to configure that if we wanted to.  I don't know if, I think Connor had to step away too. I don't know if this is answering the question though, but I think the renewal reps are reviewing the executed workbook before they send it out for DocuSign.  Like they're supposed to be opening it, opening it up, looking at it, and then sending it via DocuSign.

14:34 - Chad Gregory (LaunchPad Lab)
  Is that before they, before it gets put into client space or before, or after, like somebody is putting it into client space, then that person, that other person's reviewing it while Jagger and Anna are putting together the CBE?

14:51 - Jagger Sturdivant (Questco Cos)
  No, it's the same person. Because usually it's the rep that's putting it in the client space right now, and they're the ones that are meeting with the client.  Usually they had their hands in that workbook anyway, so there's no review because they already are saying, like, them uploading it into client spaces, them saying this is ready to be made.

15:11 - Dimple Desai (Questco Cos)
  I'm going to pull this up because I know that you've had this stuff in here, Dimple.

15:21 - Conor Hawes
  Okay, I mean, it might be a non-issue then.

15:23 - Chad Gregory (LaunchPad Lab)
  Yeah.

15:24 - Conor Hawes
  We can, I think we can move forward.

15:29 - Chad Gregory (LaunchPad Lab)
  Where am I? I'll look at that again, but.

15:43 - Dimple Desai (Questco Cos)
  It might be, also, it might be in the BSR workflow. So, not sure. They, they kind of coincide.

15:51 - Chad Gregory (LaunchPad Lab)
  Yeah.

15:52 - Dimple Desai (Questco Cos)
  Good luck looking in there.

15:53 - Chad Gregory (LaunchPad Lab)
  I was having a hard time with it yesterday with Nikki. It was like, and Miro was, like, messing stuff up, so.  Um, anyway. Um, okay. So today it's getting put into client space. You guys are picking it up and running with it.  In the world of SharePoint, we would expect somebody's going to drop it into SharePoint and then we'll do what we need to do with it.  Um, we need to figure this out. This question is kind of maybe.

16:27 - Dimple Desai (Questco Cos)
  Sorry to cut you off. Do we need a person to drop it into SharePoint or can somebody, I know like the purpose is to get away from client space, but maybe can somebody drop the file into client space if we're trying to limit access to SharePoint and have that file be automatically put in?

16:45 - Chad Gregory (LaunchPad Lab)
  That's what Jagger was talking about. Like with the webhook situation on client space, doesn't seem like it's going to be a good way to like know that it's there.

16:55 - Dimple Desai (Questco Cos)
  I see.

16:57 - Chad Gregory (LaunchPad Lab)
  Um, were you going to say something else, Jagger?

17:01 - Jagger Sturdivant (Questco Cos)
  No, don't remember what I was going to say.

17:04 - Chad Gregory (LaunchPad Lab)
  Sorry.

17:05 - Jagger Sturdivant (Questco Cos)
  No, you're good.

17:06 - Ifat Ribon
  I guess based on what you were saying, Dimple, guess we, I don't know if I missed the first time of your question, but is that just a more familiar, easier workflow for people to put in client space or you want in client space anyway?

17:22 - Dimple Desai (Questco Cos)
  It is a more familiar workflow, but I'm also not sure if we want to try to limit access to SharePoint should, I don't know, anybody mess anything up on accident or like accidentally put a file into the wrong folder, that kind of stuff.

17:37 - Ifat Ribon
  Yeah, that's what I, maybe I thought where you were headed. And I do wonder, let me know, this kind of sounds silly, but is there any connectors or any automations you can include in client space to direct it exactly to a SharePoint folder?

17:52 - Chad Gregory (LaunchPad Lab)
  Or that could be something to explore.

17:57 - Dimple Desai (Questco Cos)
  Yeah.

17:58 - Ifat Ribon
  And again, yeah, to repeat. What Jagger was saying, all this is just to solve for the lack of a webhook, but if ClientSpace has other automation options, we can maybe close the gap around manual and authorization questions.

18:10 - Dimple Desai (Questco Cos)
  I can take a look into that.

18:14 - Chad Gregory (LaunchPad Lab)
  Essentially, ifat, what you're kind of pushing or talking about there would be somebody puts it into ClientSpace and ClientSpace knows, I got this executed workbook, I need to send it to SharePoint.  And we have some sort of rules in that automation that put it into the right folder, or I guess the alternative would be they all go into one folder, and then we, Taylor, has rules about knowing, based on the file name or something, which client it belongs to, I guess.

18:54 - Ifat Ribon
  Yeah, I think that's a good summary. Yeah, and how that actually works out, I have no idea. I don't know what clients are.

19:01 - Dimple Desai (Questco Cos)
  I'm going to be honest, not very much.

19:05 - Ifat Ribon
  All right. Maybe I was getting a little lofty because I know they have DocuSign and other things you guys have built in, right?  The ability to even generate the workbook to begin with. So I'm also happy to take away and look at that.  But Dimple, if you happen to know where to look first, then you can get an answer on that.

19:19 - Jagger Sturdivant (Questco Cos)
  Dimple, do you know if Client Space can hit another endpoint? Like it can make an HTTP call or anything like that?

19:27 - Dimple Desai (Questco Cos)
  I'm pretty sure it can. But I can send you a link to the Help Center if you want to take a look and confirm.

19:36 - Jagger Sturdivant (Questco Cos)
  Okay. Because that might be a way to do it. It's just we can call an endpoint that Taylor hosts when it gets uploaded.

19:47 - Dimple Desai (Questco Cos)
  Here.

19:49 - Jagger Sturdivant (Questco Cos)
  And then we probably don't even need SharePoint at all because that solves the trigger problem.

19:54 - Chad Gregory (LaunchPad Lab)
  Yeah.

19:55 - Ifat Ribon
  So you're saying, Jagger, like while Client Client Space doesn't outright offer a formal webhook pattern. They might still offer the option to...

20:07 - Jagger Sturdivant (Questco Cos)
  We might be able to set it up in the data form so that the data form does that on its own.  But I don't think we can programmatically set up a webhook.

20:19 - Ifat Ribon
  Sure, but that would essentially achieve what we were trying to do with the webhook, right?

20:23 - Jagger Sturdivant (Questco Cos)
  Exactly. Yeah.

20:26 - Dimple Desai (Questco Cos)
  You guys are more techie than I am, so I just sent you a link to the Client Space extranet.

20:38 - Chad Gregory (LaunchPad Lab)
  I think we'll have to look through this. It might actually be the API documentation about... What are they called?  Data sources?

20:53 - Ifat Ribon
  Data Data forms? Data forms.

20:56 - Chad Gregory (LaunchPad Lab)
  I wonder if there's anything... I about it in there, but I know Connor came across some copy in there that was like, oh, get ready for a wild ride.  Okay, I think that's kind of something to still figure out. But maybe Anna, now that you're back, I am curious if you want to weigh in on, would it actually be better to have somebody just continue to drop it into client space if we're able to figure that out?  And, or, are there any, I guess this is just a second question, are there any like restrictions we need to make on who has access to these?

21:44 - Anna.Fiske
  I'm not opposed to staying in client space as far as dropping the executed workbook in. I can't remember who said it, but that was a very good point that if people have access to SharePoint, they might upload one workbook into the incorrect client.  then the confusion just gets out of control by then.

22:00 - Chad Gregory (LaunchPad Lab)
  Yeah.

22:02 - Dimple Desai (Questco Cos)
  I see a lot of potential for human error.

22:05 - Anna.Fiske
  Yeah. And our team is pretty familiar with the client space process as it is. So that would help.

22:12 - Jagger Sturdivant (Questco Cos)
  I think there's ways to solve that problem with them dropping in the wrong folder. Like we could have just a global folder that they put it in and then Taylor could delegate it to the right folder so that you don't have to search and put it in the right spot.

22:25 - Anna.Fiske
  That's true.

22:26 - Dimple Desai (Questco Cos)
  And will we just have like a standard naming convention for all of the files and then Taylor could categorize all of the files and put them where they need to go?

22:34 - Jagger Sturdivant (Questco Cos)
  Yeah. You don't even need a naming convention because the client ID is in the workbook so it could figure it out that way.

22:46 - Dimple Desai (Questco Cos)
  And then could we give like all the renewal reps access to just like this global folder and then remove access for all the other ones that Taylor's putting files into?

22:57 - Jagger Sturdivant (Questco Cos)
  Yep. That way they can't delete stuff. Because they will.

23:05 - Chad Gregory (LaunchPad Lab)
  Okay. That, I mean, I'll leave it up to our dev team. Like, maybe there's a couple different options to explore there.  But if we went that route that Jagger just described, that would solve both problems, I think, in general. So the problem of the webhook and client space and the problem of potential user error in SharePoint.

23:32 - Dimple Desai (Questco Cos)
  Additional question. With that global folder, is it possible to give a certain subset of people access to only upload documentation and not delete?

23:42 - Chad Gregory (LaunchPad Lab)
  I think SharePoint does let you do stuff like that. We would have to look at that. Or they just might not have access to the client.  Folders. Although, I guess this gets back to the earlier question. Do people, are there any users that need to get access to those?  Or would they be different than the people that are uploading?

24:22 - Dimple Desai (Questco Cos)
  I would say if there are people that need to get access to the other folders, they certainly would be different from the people that don't need the access.  I don't know if that answers your question. Sort of does.

24:34 - Chad Gregory (LaunchPad Lab)
  Yeah. I think, I guess, like if we used SharePoint to house other documents after they were generated or something, and people wanted to have access to those to review them for some reason, and like we weren't sending them back to clients, I'm not sure if this is true or not, but just trying to think if it's different people and we're able to control the access that way.  Anyway, I think that's fine. The last question here on this one, from me at least, was what should trigger the process to grab this file?  And I think basically, the assumption is the file exists in SharePoint. Does that sound right to everybody?

25:29 - Jagger Sturdivant (Questco Cos)
  Yeah, like there's a trigger when the file gets uploaded and then...

25:32 - Chad Gregory (LaunchPad Lab)
  Right. Yeah.

25:34 - Anna.Fiske
  Yeah. Okay.

25:42 - Chad Gregory (LaunchPad Lab)
  Would there ever be a case where somebody uploaded it and it wasn't ready? Like, I guess that's kind of getting back to what we talked about earlier, where we would have some validations that it was actually filled out right.  So, I guess... That's fine.

26:03 - Nikki Dow
  Yeah, I guess one thing I'm worried about is, I think this is what Chad was getting at, is there any situation where the workbook was uploaded and then maybe it gets like deleted and re-uploaded because they uploaded the wrong workbook, named it wrong, something like that?  That could happen.

26:29 - Anna.Fiske
  Also, it could happen as far as like they fill out the workbook and then the client changes their mind and we need to redo it.  So that happens a lot, a lot.

26:40 - Chad Gregory (LaunchPad Lab)
  I think the more, the worst, or a worse option, I don't know if this would actually happen, would be like somebody has the initial version of the workbook and the executed version of the workbook on their computer.  They upload the... They the... upload upload... upload... upload... Executed one, and then for some reason upload the blank one again afterwards or something like that and it undoes the work that was already generated.  I guess they're going to know to like regenerate it, but.

27:21 - Jagger Sturdivant (Questco Cos)
  They shouldn't generate the blank one.

27:23 - Chad Gregory (LaunchPad Lab)
  Yeah, it'll get blocked. Yeah. All right. Maybe we're safe on all these. I'm just trying to think of edge cases, but.

27:31 - Nikki Dow
  Yeah, I guess I was kind of asking, I think the naming convention for the files is probably a route we could go down, but maybe we just need to like keep in mind what that looks like for like a mistake and then a new version is uploaded.

27:50 - Chad Gregory (LaunchPad Lab)
  Okay. Something to think about. I have these templates here for these. Well, sorry, let me. me stop first. Are there any other questions on the executed workbook side?  Nikki, José, José, thumbs up?

28:15 - Nikki Dow
  Maybe I missed this, but if the executed workbook is being uploaded into SharePoint, does that mean that the batch in client space, it won't have a reference to that file?  Or is the intent to put that link to the SharePoint file somewhere in the batch?

28:37 - Chad Gregory (LaunchPad Lab)
  Yes, I believe we wanted to put the link in. Is that right, Jagger? Yeah, I think the link was right.  Yeah. And the person who uploaded it is going to do that?

28:51 - Nikki Dow
  Or is that, like, how's that going to happen?

28:55 - Jagger Sturdivant (Questco Cos)
  Taylor should put the link in client space.

28:58 - Nikki Dow
  Okay.

29:00 - Jagger Sturdivant (Questco Cos)
  should try to like limit the amount of steps that the renewal rep has to take, but they're already putting it in SharePoint.

29:05 - Chad Gregory (LaunchPad Lab)
  They shouldn't have to go back into client space and do something there as well. They shouldn't do both.

29:10 - Nikki Dow
  Okay, that makes sense.

29:17 - Chad Gregory (LaunchPad Lab)
  I wanted to look at each of the documents, and we may need other like individual calls on each of these documents later on when I think Jose is going to tackle these for us.  Do you guys have a thought on which one we should start with? Should we start with the CBE?

29:44 - Anna.Fiske
  Yeah, I would say the CBE, if you're asking, Questo.

29:47 - Chad Gregory (LaunchPad Lab)
  Yeah. Okay. Could you maybe walk through, this is just, I think you did walk through. This previously, so that is the CBE always just these two, two tabs, one is for the signature, does anything ever change about the signature page?

30:19 - Anna.Fiske
  The fees and commission, all these disclosures, those are updated every year.

30:24 - Chad Gregory (LaunchPad Lab)
  Every year, okay, but not like per client.

30:27 - Anna.Fiske
  Correct, yeah, that's just a blanket disclaimer for Questco.

30:31 - Jagger Sturdivant (Questco Cos)
  The only thing that changes on that page is the notes, that blank box at the top.

30:34 - Chad Gregory (LaunchPad Lab)
  Oh, okay. Yeah, there's a notes field in client space, and that gets filled in from there. Oh, I see, okay.  What typically, like how big does that typically get? Or I guess that doesn't really matter, but.

30:54 - Anna.Fiske
  It's usually just a few short sentences at most.

30:58 - Chad Gregory (LaunchPad Lab)
  Okay. And there's no, like, formatting expectations or anything like that. We're just dropping in the text. Yep, that's literally it.

31:09 - Anna.Fiske
  Yep, it's just going to be a call-out that the client specifically requests us put in there because they're wanting to see their signature next to the HSA contribution or, I know I bring up the vets a lot, but, like, they want it in there that we don't offer pet benefits.

31:22 - Chad Gregory (LaunchPad Lab)
  Yeah, okay. So they want to see it there. So this comes from client space only. Okay. And then these renewal plans here, these are just the ones that they chose, and so they could have many in each of these rows or sections, I guess I'll call them section rows.  And that first column that says benefit groups, that's going to be the classes. The class. The classes. Primary, Owners, that kind of stuff, that's where you're going to see that.  So you'll have, if you have three classes, you could have, you know, three or four.

32:10 - Anna.Fiske
  in everything. Yeah.

32:11 - Chad Gregory (LaunchPad Lab)
  Yeah, okay.

32:12 - Anna.Fiske
  So if they have two medical plans and three classes, you're going to see the medical twice for each class.  So you're going to see it three times.

32:20 - Chad Gregory (LaunchPad Lab)
  Yeah, okay. That makes sense. Basically, you would just be grabbing those from the workbook itself. Is there an order that those need to show up in?  Or is it just order of the sheet on the workbook and then top to bottom?

32:44 - Anna.Fiske
  They're usually done cheapest to most expensive. I don't know if that's built into client space to do it on purpose, but that's how we normally see them come out.

32:57 - José Blanco
  Like cheapest to most expensive. So the same group, like within health, the cheapest of the four classes at the top?

33:07 - Anna.Fiske
  Right.

33:09 - José Blanco
  Okay, within their group.

33:10 - Anna.Fiske
  Yes. Okay. So it would be primary, and then it would be the cheapest, middle, most expensive, and then elders, cheapest, middle, most expensive, listed that way.

33:18 - Chad Gregory (LaunchPad Lab)
  And that does make sense that that would want to be how the client sees it here. So if we can accomplish that, I think we should.  But I'm sure ClientSpace is trying to do that on purpose. Is there anything on this page that, like, is not from the workbook?  Or is this is all from the workbook, right? Like, even all this stuff is going to be in there?

33:51 - Anna.Fiske
  Right. And at the bottom, that other section, the very last section towards the bottom, Baby Taylor fills that out with all the voluntary products that are in the workbook today.

34:00 - Chad Gregory (LaunchPad Lab)
  Oh, yeah. Okay. Remind me, where does BabyTaylor get that from?

34:09 - Jagger Sturdivant (Questco Cos)
  It does it when it uploads back into ClientSpace. So ClientSpace does actually put them there, but BabyTaylor is the one telling ClientSpace, hey, you need to add these.

34:19 - Chad Gregory (LaunchPad Lab)
  So BabyTaylor takes everything out of the workbook, puts it in a ClientSpace, and then when you hit the, that makes sense, when you hit the button for this, it takes everything out of ClientSpace.

34:29 - Jagger Sturdivant (Questco Cos)
  Yep, exactly.

34:31 - Chad Gregory (LaunchPad Lab)
  Okay. But for us, we are just going to take it from the workbook and from ClientSpace all at once, really.  Unless it makes sense to do it the same way BabyTaylor's doing it for some reason.

34:47 - Jagger Sturdivant (Questco Cos)
  Nope. ClientSpace, I don't even think you'll need it. It won't know any of that.

34:52 - Chad Gregory (LaunchPad Lab)
  It'll know just these notes, I mean, over here. Oh, yeah.

34:55 - Jagger Sturdivant (Questco Cos)
  It'll just know the notes, and that is it, I think. Yeah.

35:01 - Chad Gregory (LaunchPad Lab)
  Okay.

35:04 - Jagger Sturdivant (Questco Cos)
  And honestly, maybe we even add a field for notes in the workbook so you don't have to do it in client space?

35:09 - Chad Gregory (LaunchPad Lab)
  We're already going to adjust the workbook, I think, for those voluntaries. So that might save José some heartache. What do you think, José?

35:21 - José Blanco
  Yeah, that could work.

35:24 - Chad Gregory (LaunchPad Lab)
  Let's just take a peek at that again. I don't know, Anna, do we need the notes in client space?

35:31 - Anna.Fiske
  Not sure. People reference client space throughout the year for those notes, but that doesn't mean we can't make it a field.  That Taylor fills in because it's sitting in the workbook. know what I mean? Taylor will read it from the workbook and plug that into client space for future reference.  I do like the idea of it being in the workbook because that's a one-stop shop for the client just to fill everything out in one go.  That gives us a really good chance of getting. Creating one consultation to a full completion.

36:04 - Chad Gregory (LaunchPad Lab)
  So the client would fill out the notes?

36:07 - Anna.Fiske
  Ideally, yeah. Our clients do like to take this workbook with them and play with it, but if you're having the consultation, you can always fill it out.

36:13 - Chad Gregory (LaunchPad Lab)
  You can fill it out, give it back to them.

36:17 - Anna.Fiske
  Where do you think those notes should go? I'd kind of like it on the total cost page, because it's like a summary.

36:26 - Chad Gregory (LaunchPad Lab)
  it's like plenty of space here. Yeah. Okay, just thinking. Do we do anything with this total cost page otherwise?  No, right? the renewal increase that's floating there at the bottom.

36:48 - Anna.Fiske
  Baby Taylor plugs that in.

36:49 - Chad Gregory (LaunchPad Lab)
  Where does that go? Is that on here?

36:55 - Jagger Sturdivant (Questco Cos)
  No, it's just a field that needs to be added to the workbook when we tweak it.

37:01 - Chad Gregory (LaunchPad Lab)
  Oh yeah, sorry, I was asking, do we, are we using anything on this page for any of it? the CBE?

37:10 - Anna.Fiske
  No. Yeah, okay.

37:13 - Chad Gregory (LaunchPad Lab)
  Okay, what else do we need to know about the CBE? Obviously, this is going to be the important one that we make sure can be signed in DocuSign still.  Maybe we move on to the next one. Should I go to the cost sheet next?

37:59 - Anna.Fiske
  Yes.

38:02 - Chad Gregory (LaunchPad Lab)
  Okay. Okay. Maybe walk me through these.

38:14 - Anna.Fiske
  So this one that we're looking at, does it have the macro ran, which is that format button? And does it come out of ClientSpace like this, Jagger?  And then we run the macro? Or BabyTaylor runs the macro?

38:29 - Jagger Sturdivant (Questco Cos)
  I think it comes out like that of ClientSpace, and then we have to run it.

38:33 - Anna.Fiske
  Okay. So then we run the macro. So it just pulls out all that raw data from ClientSpace. We run the macro, and it'll just show the third tab, the cost sheet itself.  But it'll be a lot prettier. I'm sure you could run it, possibly.

38:50 - Chad Gregory (LaunchPad Lab)
  Yeah.

38:53 - Anna.Fiske
  Yeah, there was no benefits, because this is our demo client, so there's no contribution. So what it's going to show for the...  The cost sheet only is going to be what it costs the employee to enroll in that benefit. So it'll just show their per pay period cost.

39:10 - Chad Gregory (LaunchPad Lab)
  Okay. So they would see something like this, I assume.

39:18 - Anna.Fiske
  Right. So it would have the carrier. So Aetna, the plan description would be the plan name. And then your employee only, employee, spouse, child, family, what it would cost per pay period.  So it would have those listed out. And we have one of these for each benefit class.

39:32 - Chad Gregory (LaunchPad Lab)
  Yes.

39:32 - Anna.Fiske
  So even if it, because this is a demo, so it doesn't, it won't show us anything. How is that different than, is it just because this is the pay period and this is monthly?  It is. And this will show the employer contribution for everybody. So we don't want the primary staff to see if a different class is getting a higher contribution or not.  Like they may not disclose. also So, what Oh, is that to everybody? So that's why we just hand out a cost sheet per class so they see one cost that's relevant to them and they don't see other people's cost.

40:10 - Chad Gregory (LaunchPad Lab)
  Okay. But are we getting all this information still just from the worksheet?

40:16 - Anna.Fiske
  From the workbook, yeah. I keep calling it workbook, yeah.

40:20 - Chad Gregory (LaunchPad Lab)
  That's right.

40:21 - Anna.Fiske
  And it's through the OBP.

40:29 - Chad Gregory (LaunchPad Lab)
  Oh, yeah. You're saying client space gets this information from the OBP. Maybe we would have that information from PRISM already into the workbook.  And is this information in the workbook or is it not?

40:51 - Jagger Sturdivant (Questco Cos)
  Yeah, everything that is in the workbook. It is in there. Maybe with the exception of the pay period.

41:00 - Chad Gregory (LaunchPad Lab)
  That's just calculated.

41:04 - Jagger Sturdivant (Questco Cos)
  It's in prison somewhere. I don't know where it is, but it's there, but it's not in the workbook.

41:13 - Anna.Fiske
  It's on the CBE, I think, also. No, I lied. It's not there. Just kidding.

41:23 - Jagger Sturdivant (Questco Cos)
  Well, even if it wasn't, it would get it from client space, which is what we want to avoid.

41:29 - Dimple Desai (Questco Cos)
  What is it that you guys are looking for?

41:32 - Anna.Fiske
  The pay group, like the pay frequency. That is in prison for sure. I just don't know where.

41:36 - Dimple Desai (Questco Cos)
  It's in both. So it's in the client master and client space, and then it's on the client details in prism.

41:45 - Chad Gregory (LaunchPad Lab)
  Ah, yeah. And then these get calculated based on... Based on which column here?

42:04 - Jagger Sturdivant (Questco Cos)
  Q. Q. Yeah, employee contribution.

42:08 - Chad Gregory (LaunchPad Lab)
  Yeah. But I guess that's, yeah, Q, so each of these divided by, is that, well, are these, is this annual?

42:24 - Anna.Fiske
  That would be a monthly amount that's sitting in column Q.

42:27 - Chad Gregory (LaunchPad Lab)
  Okay, so you would do like the, it's like this amount times 12 divided by this. Yep.

42:37 - Anna.Fiske
  Essentially, okay.

42:38 - Chad Gregory (LaunchPad Lab)
  One of these per class. And there, when we generate it, really, we would just generate this tab, right? Because you wouldn't need to have the macro or this renewal plans thing anymore.  Right.

43:15 - Anna.Fiske
  Yeah.

43:16 - Chad Gregory (LaunchPad Lab)
  Yeah, if we can remove all the macros from the workbooks, that'd be great. Because it'll take forever to run, especially for the workbook.  Yeah. What are the questions rattling around in our heads, José, Nikki?

43:46 - José Blanco
  What should happen to the cost sheet when they're not renewing? Should we generate the file or? How should we go about it if they choose not renewing in the workbook?

44:09 - Anna.Fiske
  You mean the client's not renewing as in they're a new client or they're not renewing benefits at all?

44:15 - José Blanco
  They're not renewing benefits at all.

44:18 - Anna.Fiske
  Then we wouldn't even upload a workbook.

44:20 - Chad Gregory (LaunchPad Lab)
  Nothing would happen. Yeah.

44:22 - Anna.Fiske
  Yeah, we have a whole separate workflow in client space to say benefits terminating, and we have other steps with other departments for that.

44:29 - José Blanco
  So we wouldn't get a trigger. Okay.

44:32 - Chad Gregory (LaunchPad Lab)
  So in a case like that, Taylor would generate the workbook, and then everything would be, yeah, like just stopped after that, basically, after the consultation.  Okay. You did make me think something, José, but I think it's all, like basically, assuming O&Q. can be in the own queue, would handle the same, like we would just pop that in here as one of the carriers then.  Yeah. Okay. I think that makes sense. So then the last one is the benefit guide. think I already. Okay.

45:27 - José Blanco
  You might want to open it in like another app because it's kind of difficult to navigate in the browser.

45:35 - Chad Gregory (LaunchPad Lab)
  Do you have a recommendation?

45:38 - José Blanco
  Any PDF viewer should do a trick. I was using, let me see.

45:51 - Chad Gregory (LaunchPad Lab)
  Here we go.

45:53 - José Blanco
  Let's see.

45:58 - Chad Gregory (LaunchPad Lab)
  Okay. Okay. So. This was the question I was trying to figure out with you in Asana yesterday, Anna. It sounded like you were saying basically that there are going to be pages that depending on what selections are made, we just are including or not including.

46:25 - Anna.Fiske
  Correct. So based off the workbook, we'll include the pages of the benefits that they select. Correct.

46:33 - Chad Gregory (LaunchPad Lab)
  Okay. So does this then have, like, does this version have everything?

46:41 - Anna.Fiske
  For Aetna, yeah. So it's not going to show like our blue choice for Kaiser in this one. I tried to get you the beefiest one I could find.  But yeah, it's going to have all of our voluntary plans and the medical dental vision.

46:54 - Chad Gregory (LaunchPad Lab)
  Okay. So what we need are all the pages, period. I guess, and like what order they should be dropped in.  Yeah, and the conditions as well for each page. Yeah, like which selection maps to those pages.

47:17 - Anna.Fiske
  Okay, can we talk about the medical page also? It's like one of the first ones.

47:22 - Chad Gregory (LaunchPad Lab)
  Yeah.

47:24 - Anna.Fiske
  Especially for this one because it's Aetna, which all of them are like this. It's going be that one, yeah.  you see how they're side by side. So that's like a 5,000, a 1,000, and a 4,000. So we have them, so our third party does this for us currently where they put these plans on a template for us to create the guide.  I don't know how Taylor, if Taylor's able to do this. Otherwise, we would have to have one page for every single medical plan.  And that can be thousands of variations depending on what they offer because Aetna alone has 99 plans.

47:57 - Chad Gregory (LaunchPad Lab)
  Yeah.

47:58 - Anna.Fiske
  I don't know. We can solve for that, but Taylor, if we have a template like this, and Taylor's able to fill it in based off the medical, that's the only thing, everything else has its own dedicated page.  Medical is the only one that's combined like this, depending on their offerings.

48:13 - Chad Gregory (LaunchPad Lab)
  That's interesting. So there would be, that's like the only page that would need generation, like within the page of, of data in the pages.  Basically, you have like boilerplate pages all across the document for everything else. So it's definitely possible, uh, Ifat and I were just talking about this, because it's, does get tricky to generate PDFs like this.  Uh, yeah.

49:00 - José Blanco
  So right now, you're getting this from a third party, right? Are they providing you with the values for three plans that you decide, or are they deciding which three plans they're going to compare?

49:17 - Chad Gregory (LaunchPad Lab)
  My understanding is that the third party is given the workbook or the information from the workbook of what the client picked.  And then they're just adding those three things here, right?

49:32 - Anna.Fiske
  Right. So currently, as it says, they won't create a workbook until we have a signed CBE. So they get that more compact.  Instead of the whole workbook, they'll just get the CBE and the cost sheet that we create, and we send that to them, and that's how they build the guide.  So then they have people, I think, or AI, I can't remember, but they have it to read the CBE and build the guide for us.

49:59 - Jagger Sturdivant (Questco Cos)
  Does it also... also... Put them all on the same page if there's like seven Aetna plans?

50:03 - Chad Gregory (LaunchPad Lab)
  was just thinking about it.

50:04 - Anna.Fiske
  It'll three at time. Yeah, we decided there was three at most. So if they have two, it'll space it out for two.  If it's one, but if it's three, then we'll have seven. We'll have a second page with three, and then a third page with just one on it.

50:16 - Chad Gregory (LaunchPad Lab)
  Yeah.

50:18 - Conor Hawes
  And does it like the header and this all just repeat?

50:23 - Chad Gregory (LaunchPad Lab)
  It does.

50:24 - Anna.Fiske
  Okay.

50:25 - José Blanco
  That makes that easier. Except for like things like the year, which they obviously change.

50:33 - Anna.Fiske
  Yeah, we'll change that kind of stuff.

50:38 - Dimple Desai (Questco Cos)
  Does anything else change every year?

50:42 - Anna.Fiske
  For the pages? Yeah, it'll be the HSA, FSA. Those amounts are changed by the IRS every year. It depends if the plan designs change.  Those will change.

50:56 - Conor Hawes
  And sorry, where did you say like all this, these templates? Their pages are stored.

51:03 - Anna.Fiske
  We just have this master guide that was provided to us. Our third party stores all of it. So they're the ones who created this.

51:10 - Chad Gregory (LaunchPad Lab)
  So you would need to get all those pages from them for us to use?

51:15 - Anna.Fiske
  Yeah, or I would just remake this one for us for 2027.

51:21 - Chad Gregory (LaunchPad Lab)
  But when we're talking about like all of the different variations, or like all the different pages that are not included here?

51:32 - Anna.Fiske
  Right, yeah, which we have those in other client guides that I could pull. Okay, okay.

51:37 - Chad Gregory (LaunchPad Lab)
  Yeah. Hmm. I don't want to get like too cocky. It's the thing. Like, I know that. There's a lot to unpack on this one.

51:56 - José Blanco
  Yeah. Yeah.

51:58 - Chad Gregory (LaunchPad Lab)
  I mean, this is like. Fairly straightforward in terms of doing what you're asking, I think, Anna, but I just have like PTSD from when we were doing that last time and it became like super difficult to ensure that the formatting was like always looking nice when you have like different lengths of plans and all this stuff.  But this is like generally going to be pretty much the same, right?

52:36 - José Blanco
  Content-wise, yeah, maybe like the digits will change, but the number of characters should remain mostly the same.

52:42 - Chad Gregory (LaunchPad Lab)
  Yeah, like you're not going to have something crazy.

52:47 - Nikki Dow
  But like if there's more than, sorry, if there's more than three plans, like if there's nine, there's going to be three pages of the same plan.  Yeah, yeah, following this one. Say that again, Nikki? So if there were like nine plans, there's going to be two additional pages here between five and six.  Yep. So that means the table of contents has to also change.

53:19 - Chad Gregory (LaunchPad Lab)
  Just flagging that. You're right.

53:27 - Conor Hawes
  And is there anything, so does this also, if they, for the vets that elect out of pet insurance, like does that also get removed from this guide?

53:38 - Anna.Fiske
  It will. So, like, it shouldn't be generated to start with because it wouldn't be on the CBE.

53:44 - Conor Hawes
  Yeah. Any other, like, client-specific things? Like, is there, is a client's name in this or their logo or anything like that?

53:52 - Anna.Fiske
  Not their logo, but their name would be on the front page where it says Master Guide. It would say.

54:04 - Nikki Dow
  I also saw on the medical page, there's an Aetna logo. I assume that's because they chose to go with Aetna for their medical insurance.  And then if their dental insurance was another company, I assume that logo would also have to be updated.

54:22 - José Blanco
  Yeah, I saw a different logo on another page here.

54:25 - Chad Gregory (LaunchPad Lab)
  But think these are like those pages that we would associate with a selection. Like it's not a, it's not quote unquote dynamically being added into the page itself or like generating that page.  It's like pulling that page into.

54:44 - Nikki Dow
  I see. So there's like a.

54:46 - Chad Gregory (LaunchPad Lab)
  There'll be like a library of pages that we can choose from.

54:51 - Conor Hawes
  Where?

54:54 - José Blanco
  That's not how I was envisioning it. I was thinking that we will need the logos for like. Like groups of plans and we'll replace the appropriate logo.

55:08 - Anna.Fiske
  I think currently it sits with our third party. just have a big library of pages and they just pull the pages that they need because everything will be pretty static throughout the workbook page-wise.  Like this APL page will never change. They can't offer one option over option two. If they're offering it, this is the page they'll get.  They don't offer it, they don't get the page. The only thing that has to be customizable would be the medical page with the side-by-sides.

55:34 - Chad Gregory (LaunchPad Lab)
  And then the table contents and the cover.

55:38 - Anna.Fiske
  Yep, yep, yep, yep.

55:41 - Conor Hawes
  So dental and vision are included here?

55:45 - Anna.Fiske
  Say it again?

55:48 - Conor Hawes
  So dental and vision aren't given the same treatment as medical?

55:53 - Anna.Fiske
  They are. That's a good call out. Yeah, so they can choose to not offer all three dentals if they choose to.  And one or two of the visions, so they can customize that also.

56:04 - Chad Gregory (LaunchPad Lab)
  So those pages would be different. Wait, what are you saying?

56:09 - Ifat Ribon
  So it would be another page like that, and now one, but like for their medical and vision elections?

56:16 - Anna.Fiske
  Their dental and vision.

56:17 - Ifat Ribon
  I'm sorry, dental. I guess it, maybe it's for my clarification, there's these pages, which are highly dynamic based on their elections.  And there could be for medical, dental and vision, something like this. And then those pages at the bottom are more standardized, maybe not, I don't know about that one, but like the other one we're just looking at, the APL one.

56:45 - Chad Gregory (LaunchPad Lab)
  Yeah. What is that exactly?

56:47 - Ifat Ribon
  I just wasn't reading all of it.

56:50 - Anna.Fiske
  It's like this is more like standardized language, right?

56:52 - Ifat Ribon
  It's not specific to their?

56:54 - Anna.Fiske
  Right, right, right. Yep. What is this?

56:57 - Ifat Ribon
  Like how would you refer to this page?

57:05 - Chad Gregory (LaunchPad Lab)
  Is it one of those voluntary benefits that would be at the bottom of the workbook? It is.

57:14 - Ifat Ribon
  Yeah, think we're all converging on, there's a distinction maybe per page, mean, you probably need to just catalog an inventory for ourselves with the naming conventions.  Some are highly dynamic, and then some are these very standard ones. And for the very standard ones, you know, where would that library of standard ones that get injected, like, where could that live?  And we don't have the answer for that today, but I think that was, maybe it was getting asked earlier.

57:45 - Chad Gregory (LaunchPad Lab)
  Would it make sense to just have them live in SharePoint after we get them created?

57:50 - Ifat Ribon
  Yeah. Probably.

57:52 - Chad Gregory (LaunchPad Lab)
  Because my follow-up question was going be like, a page like this could change, it's not itself dynamic, but it might change year to year, right?  Like as, right. Okay.

58:00 - Ifat Ribon
  Absolutely will.

58:01 - Anna.Fiske
  Yep.

58:04 - Chad Gregory (LaunchPad Lab)
  Go ahead, Ifat. I was going to say SharePoint could definitely be an option.

58:08 - Ifat Ribon
  But yeah, I think maybe those are some of the things we need to still dig into and understand, maybe like page by page.

58:14 - Anna.Fiske
  Yeah.

58:15 - Chad Gregory (LaunchPad Lab)
  Am I understanding just because I, what you just said, Ifat, about dental and vision? Is this the page that would then be dynamic for dental and this is the page that would be dynamic for vision?  Is that what you were saying? Yeah. Yeah.

58:30 - Ifat Ribon
  Okay.

58:33 - Chad Gregory (LaunchPad Lab)
  Okay. That's, same thing applies. Like, there's a low, high, and upper, I guess, or something like that. Is that, like, how does that work for dental and vision?

58:52 - Anna.Fiske
  Yeah, so it's kind of like the low, medium, and high, even though it says high for both of them.

58:59 - Chad Gregory (LaunchPad Lab)
  They can.

59:00 - Anna.Fiske
  If they don't want to offer the low plan, which is pretty common, they just want offer the two better plans, our clients aren't able to do that.

59:11 - Chad Gregory (LaunchPad Lab)
  Is it relative in that case?

59:13 - Conor Hawes
  Like, it still, would it still say high plan and high 90th plan?

59:17 - Anna.Fiske
  It will, yeah. Okay.

59:19 - Conor Hawes
  Mm-hmm.

59:20 - Chad Gregory (LaunchPad Lab)
  And do the, are you saying that the numbers don't change? Like, this stuff doesn't change, but we would just remove a whole column?

59:30 - Anna.Fiske
  Correct. Yep, yep, yep.

59:32 - Chad Gregory (LaunchPad Lab)
  That's better. Sure. And they, can they go above three options? No, that's the only three we offer.

59:39 - Anna.Fiske
  And Aetna is the same way. Aetna's three dental and two vision. So Aetna, this is MetLife that we're looking at.  So MetLife, dental vision, and Aetna dental vision play about the same roles page-wise.

59:52 - Chad Gregory (LaunchPad Lab)
  I know you said that we could, it's very unlikely to have OMQ on dental and vision, but how would that change things?

1:00:00 - Anna.Fiske
  So that would be a page provided by the carrier. So that wouldn't be something that we could anticipate and make ahead of time.  if they chose the same way with medical, though, if it was an open market medical, that page would be provided to us.

1:00:18 - Chad Gregory (LaunchPad Lab)
  Oh, and that's where we were saying like somebody would need to go and drop it in or something.

1:00:22 - Anna.Fiske
  Yeah. And that's if we wanted it in. So that would be a good like stopping point to say, do we want this in the guide or not?  Are we the broker? it would kind of put that compliance stop in place.

1:00:31 - Chad Gregory (LaunchPad Lab)
  Yeah. Do you, I know we're at time. just have one more question. Do you currently do that kind of thing?  Like when you get it back from the third party, do you still have to like drop in something or?

1:00:45 - Anna.Fiske
  Absolutely. So you're like the team is used to using like an Adobe editor or something to make those changes?  I specifically do it. So I am a bottleneck on that.

1:00:55 - Chad Gregory (LaunchPad Lab)
  Yeah. Okay. Would you still always be doing it?

1:00:58 - Anna.Fiske
  Most likely. Yeah. Adobe's not very nice to people, apparently.

1:01:04 - Chad Gregory (LaunchPad Lab)
  Yeah, okay. Well, I know that we had you guys in hours of meetings today. Really appreciate it. I think we made some good headway tomorrow.  I know we're going to talk about Prism Imports on that grooming call. Maybe we'll have some other stray questions.  And we've got a lot of planning to do. So we really appreciate it, guys. It's been good. Yeah, thank you, guys.  Thank you so much. Thank you. Thanks, guys. Bye.