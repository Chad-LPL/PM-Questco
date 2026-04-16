Questco - LPL: Weekly Status Check-In - April 08
VIEW RECORDING - 28 mins (No highlights): https://fathom.video/share/Fwev1sti75f5_-WVsTUz42isSgp7hHPw

---
  SCREEN SHARING: Chad started screen sharing - WATCH: https://fathom.video/share/Fwev1sti75f5_-WVsTUz42isSgp7hHPw?timestamp=12.925223

0:00 - Chad Gregory (LaunchPad Lab)
  Notes. It's awesome. All right, Chris, you're coming into a team fresh off of a big discovery session here. So everybody's just been on that.  I've got our agenda notes pulled up here. We do have some questions that we wanted to get. into here.  We touched on a little bit of this in the call that we just had, but we'll try to hit those.  I wanted to start with kind of a sense of where we are right now. So yesterday, we were able to re-sync with Anna to make sure that we had the flow correct.  So everything basically that we talked through with you, Anna, it sounded like was correct, which is good. A couple of things that we found, or like we needed to discuss, and we have these kind of in our questions here, is where we want to house like the rate book data, the reband data, and where essentially where Taylor is going to be getting that information from.  Today, we just had a deep dive on the workbook, primarily, a little bit on like what data lives where.  I guess I'm going to skip the questions for a second. Tomorrow we have a deep dive discovery on OMQ and like all the audits that have to happen in different parts of the process.  We also then around, I think, noon central is the technical architecture review. I wanted to call out that Nikki's hoping to get that sent over to Chris and Jagger and anybody else that we should send it to by the end of today so that you have it ahead of time.  And then we'll have that discussion tomorrow reviewing what they put together. Then after that call in the afternoon on Thursday, we've got a deep dive discussion on what happens with the executed workbook and how that leads to doc generation.  Friday, we've got our grooming session we're going to use to talk about alright. Thank Prism Imports, and Anna invited some other folks from Questco to help with that discussion.  And then we've also got our internal planning Friday afternoon to take everything that we've learned from all these deep dive discoveries and continue working on our plan for all of our sprints and all the work that needs to be done.  Let me stop there. Any questions from the Questco team about that or any call outs?

3:34 - Dimple.Desai
  I won't be able to make it to the Taylor Technical Architecture review meeting tomorrow. Do you guys need me or is it primarily just going to be Chris and Jagger that are needed?

3:45 - Chris Whitney (Questco Cos)
  We'll fill you in. I'll fill you in if there's any action. I'm sure there will be some Dimple action coming out of that, but I'll fill you in.

3:56 - Dimple.Desai
  I'll fill you in if there's anything. Thank you. I appreciate it.

4:00 - Chris Whitney (Questco Cos)
  Um, I do have a question on this, and the question is, for your questions, if I'm getting ahead of myself, do you have a path to get all those answers, or are you blocked on the path to get those answers?

4:17 - Chad Gregory (LaunchPad Lab)
  I was going to ask some of them here, uh, if they need to be extended into any of the, any of these other discoveries, we can definitely grab that, yeah.  Um, okay, I will start into that if there aren't any other thoughts or questions on what I've touched on.  Okay, so rate book and revanding we talked about in, in this last call. Um, it does seem like, uh, the Questco team, and correct me if I'm wrong, but it seems like you're pretty confident you can get your rates into Prism for your clients.  So, um, any rates that change in the rate book, you're able to... To get those rates updated into the client information in Prism for like the future year.  Is that correct? I'm not saying anything wrong yet. Okay. That's correct.

5:15 - Dimple.Desai
  One second.

5:17 - Chris Whitney (Questco Cos)
  I'm sorry, I'm not muted. Perfect. Dimple, Anna, is there any action, Kim action, Chris action, Kelly action for us to enable that to be so?  From any other teams?

5:32 - Dimple.Desai
  No. I checked with LaWanda to make sure that it's possible. She sent me the exact import file that's needed and the columns that we would be putting the future rates into.

5:43 - Chris Whitney (Questco Cos)
  Okay. Who owns making that happen?

5:47 - Dimple.Desai
  Correct me if I'm wrong, Anna, but I believe it's LaWanda, right?

5:51 - Anna.Fiske
  Yeah. LaWanda would be in charge of doing that import after Kelly does the rebanding. Kelly and Kim will do the rebanding first.  it. it. it. it. And that's Final file will be imported through Lawanda.

6:04 - Chris Whitney (Questco Cos)
  What's in my perspective here is there's requirements for us piloting and getting ready for Taylor for incoming clients. And then there is the OE requirements for when all that has to be loaded.  So I just would like us to have dates specifically for OE on like when that all needs to be in prism, because the risk when that's not is the scrambling.  Right. So we should understand those dates.

6:37 - Anna.Fiske
  That was something that Chad had hit on a good bit in our last meeting also to get a really good time frame for as far as our CSP renewals and then what the time frame really looks like for our year-end open enrollment.

6:47 - Chris Whitney (Questco Cos)
  So we're all over. So we're already all over the dates.

6:50 - Anna.Fiske
  Okay, right.

6:51 - Chris Whitney (Questco Cos)
  should have been there. My bad. That's what I get for not coming to that meeting.

6:54 - Anna.Fiske
  Right. I agree. Yeah.

6:56 - Chad Gregory (LaunchPad Lab)
  Totally fine. Let's see. In Prism. This leads us to the rebanding, which it doesn't seem like rebanding can live in Prism.  And the band, because there's not like a band identifier in Prism, essentially. Um, we, for Taylor, need to have that band identified, um, not because it's going to tell us, like, the rate for, uh, yeah.  Basically, sorry, the, the approach that we talked about today for rebanding is if that rebanding file can live in SharePoint, and then we can grab it.  This all leads to this last question on this list about, do we need an admin console? So, this is, like, one step in not needing the admin console, I guess, is if somebody is able to put this file.  into SharePoint and update it in SharePoint if they need to at any time. And then whenever Taylor is running through, Taylor can grab the rebanding file and associate bands with the clients.  How does that sound? I know we just talked about this, but does it feel like that's going to work?  Or what thoughts do you guys have on the Questco side about that?

8:28 - Anna.Fiske
  I'm pro SharePoint, only because it does prevent a bottleneck as far as somebody going in, doing the import into Prism to update those rate bands if they change.  Because the rebanding, it's only really redone once, maybe two times, maybe three times. It just kind of depends. It's not touched often, but it is critical when it does change.

8:50 - Chad Gregory (LaunchPad Lab)
  So I think having it live in SharePoint is ideal. When does it change, Anna?

8:56 - Anna.Fiske
  It's before we would create the workbook, so it would be in August.

9:01 - Chad Gregory (LaunchPad Lab)
  Okay, and it happens like once a year then is what you're saying, or are you saying?

9:06 - Anna.Fiske
  For the 1-1 renewals, yeah. So once we get all of our rate bands assigned by the carrier for our clients for 1-1, we will sometimes change those depending on the client.  And if, you know, we want to do some negotiation there and we'll re-band it. And that's when those bands will change according to Questco.  And then we have that new file, the re-banding file.

9:26 - Dimple.Desai
  So this may be a dumb question, but do we need to put anything into SharePoint for clients that are starting halfway through the year or something like that, that have different rates?

9:39 - Anna.Fiske
  What do think different rates?

9:41 - Dimple.Desai
  Or not rates. What's the right word?

9:44 - Chad Gregory (LaunchPad Lab)
  Like they need to be assigned a band.

9:47 - Dimple.Desai
  Yeah.

9:48 - Chad Gregory (LaunchPad Lab)
  Yeah.

9:49 - Dimple.Desai
  Yeah. Thank you.

9:49 - Anna.Fiske
  So if they start, if a client starts mid-year, let's just use Aetna, for example. So they start with Aetna in July and they have their rate band as a new client if they get rebanned.  So they get a new rate ban for 1-1, a renewal with Aetna, they'll be on that list. And we as Questco, we're like, hey, we promised them a rate cap and they can't go above this amount of an increase.  Then we'll re-ban that client, but they should be listed on the Aetna rate book if they're renewing for 1-1, no matter when they join.  Now, if they join during September, October, November, usually they don't get a renewal. They stick with the rate ban that they have going through 1-1 into the new year.

10:32 - Chad Gregory (LaunchPad Lab)
  Oh, does the rate ban file only have clients who have had changes to their bans? Is that what I was hearing you say, Hannah?  It'll have every client.

10:48 - Anna.Fiske
  It'll have every client.

10:49 - Chad Gregory (LaunchPad Lab)
  You will have every client. So every client, when I get assigned, then I'll be added to that file with a band.

10:55 - Anna.Fiske
  Right, and your rate ban could not change. That's very rare, but it could not change. So you They'll have the same rate ban as a renewal rate ban, but yeah, usually.

11:04 - José Blanco
  It'll be there.

11:06 - Ifat Ribon
  I guess I don't know if you find this in your answer to Dimple's question, which I think is maybe related to mine.  I don't know if it's the same. Is there any scenario in which that rate ban file or changes to it would happen in flight of any given client batch, aka a workbook has been generated and then a rate ban changes?

11:25 - Anna.Fiske
  Yes, that can happen.

11:28 - Ifat Ribon
  Okay, so then if that file were to be updated and re-uploaded to SharePoint, Taylor would have to know about that and regenerate it, or we could reset the status or something like that.  It'd have to get regenerated, right, the workbook?

11:41 - Anna.Fiske
  Yeah, that's kind of why we were asking for Taylor to be able to do big batches of workbooks, but also run one-offs for that exact reason.

11:47 - Chad Gregory (LaunchPad Lab)
  you would just rerun it?

11:49 - Anna.Fiske
  Yeah, we would just go in and rerun that one client because we know their rates have changed.

11:53 - Ifat Ribon
  Okay, that's I was trying to confirm. Thanks.

11:55 - Chris Whitney (Questco Cos)
  It feels like when we were... Thinking about this before, like Taylor running over and over and over again and processing and just skipping steps that it already needs is like the path, I think, for success, if that makes sense.  So just run it again. You've already got the workbook, check the rate bands, make adjustments. If something's changed, if not, then you skip it.  Same thing because Taylor's going to generate the import files. Same thing, right? If anything changes, make a change. If not, skip it.  This is why we were looking at it before. Did the rate bands change for taking OE out just during the year?  How does that work for like new incoming clients during the year? Does it frequently change?

12:41 - Dimple.Desai
  You should have been on the last call, Chris.

12:43 - Chris Whitney (Questco Cos)
  That answer's already there. I don't know if I was invited, by the way.

12:48 - Chad Gregory (LaunchPad Lab)
  You might not. I think I made you optional on all this.

12:52 - Chris Whitney (Questco Cos)
  Okay.

12:53 - Chad Gregory (LaunchPad Lab)
  All right.

12:54 - Anna.Fiske
  All right, then. If you all feel good about that, if those answers are there, I'll leave it to the team.

13:00 - Chris Whitney (Questco Cos)
  I'll leave it to the team. You all know what you're doing. Cool.

13:07 - Chad Gregory (LaunchPad Lab)
  Okay, regionalized plan mapping, we also talked about. We need to figure out the mapping of all those zip codes.  And I think you said, Anna, that you had, well, I know you gave us a zip code file. Is that the file that we should use to do this mapping already?  Or did you have something else that you've been talking about? Yeah.

13:29 - Anna.Fiske
  It is the zip code file, but Jagger doesn't, BabyTaylor, have something as a key for those as well? The zip code file will only tell you if they need a regionalized, like if they're in a regionalized area, but it won't tell you what plans to add.

13:44 - Jagger Sturdivant (Questco Cos)
  There's another remapping that's like, if it's this state, then you need these plans.

13:52 - Anna.Fiske
  But you have that for BabyTaylor?

13:54 - Jagger Sturdivant (Questco Cos)
  Yes.

13:55 - Anna.Fiske
  Okay.

13:58 - Chad Gregory (LaunchPad Lab)
  Okay. Um, I think, Conor, did you ask this question in the last call about denial, the denialist?

14:11 - Conor Hawes
  Yeah.

14:13 - Chad Gregory (LaunchPad Lab)
  Are you good there? Do you need anything else?

14:17 - Conor Hawes
  Um, I think there was, like, uh, some open questions that Ifai posted around, uh, determining, like, terminated plans as well as test plans, grandfathering gap plans, like, if there's anything within prison, whether it's used today or not, um, where that could be.  Like, deterministically identified or versus, like, keeping it as a, like, hard-coded list.

14:58 - Chad Gregory (LaunchPad Lab)
  Okay, this kind of leads to. So OMQ, and I'm not sure if, did you guys get a chance to talk about OMQ with Betty in the last few days?

15:11 - Dimple.Desai
  Yes, and I sent you a couple of proposals. Yeah, so I took a brief look at all of them.  They're all very, very different, Anna was correct, but I'm not really sure. Yeah, I think the best approach would be to have a template for open market plans, but let us know if that's possible after you look at the proposals, if you guys see any commonalities.

15:45 - Anna.Fiske
  And I don't know, Chris, if this has been ran by you or not before, but for the open market quotes that we get, because they come from carriers and such different templates, and they're usually PDFs, we were asking LPL to look at those and then make.  Yeah. A unified template, like a global template, and we have temps on that agency, get those open market quotes in and key those into that template so that we can then plug it into Taylor and it can read it and put it into the workbook.  So that's what we're thinking for version one for open market quotes. Okay.

16:18 - Chris Whitney (Questco Cos)
  The takeaway for you and I on that is that when we had built, just very transparent, when we had built the business case for Taylor, we had taken and had some offset funding for temps, which we can absolutely get in front of Anna.  But when we get closer to what the success is looking like and how we're tracking on Taylor, you and I should talk about the plan for temps there and make sure we're fully aligned, and then I can help work on the budget to make sure we're set.  But there is an assumption that we're saving on temp workload this year that we had spent last year, and we're gaining that efficiencies through...  Taylor. Does that make sense? It does, yeah.

17:03 - Anna.Fiske
  And I remember that being in your business case, and that's why I wanted to bring it up here.

17:08 - Chris Whitney (Questco Cos)
  It's fine. We'll adjust. We could talk and adjust because we're going to need what we're going to need for OE, but we just have to get in front of that, and I will absolutely 100% help shepherd those discussions through.

17:20 - Anna.Fiske
  Okay, thank you.

17:21 - Chad Gregory (LaunchPad Lab)
  We have a bigger discussion on OMQ tomorrow, but it sounds like maybe there's a world where if you needed a template in like a file, you could use that, and maybe there's like a SharePoint world like we were talking about with the rate books, or sorry, the banding.  But I know that you had also mentioned there being a previously started and not finished or not used version of that in Client Space 2.  Does it Seem like that's not a good approach to like having that updated in client space where somebody could drop that information in?

18:10 - Anna.Fiske
  What's in client space would just be for tracking purposes. So it's only going to be checkboxes as far as the client requested open market.  Who's taking it on the agency? Is it received? Was it presented? Are they going with it? So it's more of tracking.

18:22 - Chad Gregory (LaunchPad Lab)
  that. Yeah, you don't have like fields for all the information.

18:25 - Anna.Fiske
  We don't. We do not.

18:32 - Chad Gregory (LaunchPad Lab)
  Okay. The goal is that OMQ gets added into the work, like you would generate the workbook, go through with the client, they would see things, they would want to go to open market, you would get those quotes, you would get them back, you would fill them out into this template, the template would feed into Taylor, and Taylor, you could then hit the regenerate button.  So that Taylor regenerated with the OMQ there in the workbook as well. Did I miss anything with that?

19:09 - Anna.Fiske
  Well, that's perfect. then ideally, if the process could be the same after that. So as far as like the import files to go into Prism, if there's that open market plan, everything would be the same following that point because it's plugged into Taylor at that point.  So plan design, all the rates, all that information. I see what you mean.

19:29 - Chad Gregory (LaunchPad Lab)
  Yeah. I have a question.

19:33 - Dimple.Desai
  The status could be brought back as well when a client, when we inject the plans back into the workbook.

19:41 - Anna.Fiske
  Are you asking me?

19:43 - Dimple.Desai
  No, I was just adding on to.

19:46 - Anna.Fiske
  Oh, yeah. If we can move the batch status.

19:48 - Chad Gregory (LaunchPad Lab)
  Which status would it need? Which status would it be? It would be in consulting, right? then consultation. And then it needs to go back to what at what point?  okay. Okay. Okay. Thank Thank

20:01 - Anna.Fiske
  I think it would kind of just stay in consultation because we would then move to the BSR to do the open market quote process to get it and then redo the workbook and then re-consult.

20:13 - Chad Gregory (LaunchPad Lab)
  Oh, yeah. Is there a status that it goes to when you are getting the open market quote?

20:20 - Anna.Fiske
  Okay. Not in the batch currently, no.

20:22 - Chad Gregory (LaunchPad Lab)
  Okay.

20:24 - Anna.Fiske
  Should we make one?

20:25 - Dimple.Desai
  I can always do when the client requests open market quote, when that checkbox is checked, the batch status changes back to consultation or something.

20:34 - Anna.Fiske
  It should stay in consultation, though, even if they ask for an open market quote, because the next step is plan election updates, which would be they made a selection, so they have it at that point.  So would you want a new status to say open market quote requested? And then we bump it back? I'd vote just keep it in consultation.

20:52 - Dimple.Desai
  I'm also fine with keeping it in consultation. Okay.

20:56 - Chad Gregory (LaunchPad Lab)
  Then I, okay, that's good.

20:57 - Dimple.Desai
  I think somebody had a question from...

21:00 - Ifat Ribon
  Yeah, I did. And maybe it's better for tomorrow morning when we dive in. But in terms of like defining that template, Anna, you mentioned, then Dimple, mentioned, you know, confirmed that, yes, all these documents look wildly different.  I think the assumption we had going into this is that the template we defined would be essentially informed by like the PRISM schema so that they look like those things, right?  So then Taylor can adjust it in a similar way and output them in a similar way. I guess I want to maybe try to validate that assumption.  And if there are any like edge cases to that, like there's something unique about these OMQ plans that we want to make sure we're capturing extra metadata field or something like that, which will lead us to believe, you know, we need to slightly adjust what that schema or template could look like.  And you don't have to have an answer now, you we could talk about it tomorrow morning too, but that's like an assumption we kind of had going into this.

21:52 - Anna.Fiske
  That's a good thing to bring up because some open market quotes won't have static rates like what we've been seeing so far in this project.  which is employee, employee-child, employee-spouse. Sometimes I'll have age-branded rates and that can't be reflected in the workbook. That would just be way too many rates.  I mean, it's zero to 99 as far as the rates go. So that's a good thing to bring up that we should talk about tomorrow too of like how we would want that captured and not required in the template for Taylor to read.  Because if they have it, great. not, great.

22:22 - Chad Gregory (LaunchPad Lab)
  All right.

22:23 - Ifat Ribon
  Yeah, spot on. That's like a great first example and, you know, other things like that and diving deeper into that one.

22:28 - Anna.Fiske
  I wonder if Betty's available tomorrow morning. So we can add her in.

22:32 - Dimple.Desai
  Be the best person to include.

22:34 - Anna.Fiske
  Yeah.

22:36 - Dimple.Desai
  And if not, Anna, would you want to meet right before to take a look at the proposals that I sent over to Chad to see if there's anything that like we definitely need to have added to the template at least so that they have a starting point?

22:51 - Anna.Fiske
  Yeah. If Betty can't attend, then I'll probably try to grab her before then. So I might try to bring it up then.  Okay.

23:01 - Chad Gregory (LaunchPad Lab)
  That'd be great. It's available.

23:05 - Anna.Fiske
  We're going to invite them.

23:07 - Chad Gregory (LaunchPad Lab)
  The one last question I think that will help us determine if we need this admin console is the reporting aspect.  And we talked about this a little bit with you, Anna, yesterday. Dimple brought up a note that Chris mentioned last week about Q Insights.  Have we landed on a thought around reporting?

23:31 - Dimple.Desai
  That's kind of still a work in progress. I sent over all of the data points from Prism and Client Space that we would need for the admin console over to our Q Insights team.  So they're taking a look at that right now to see if that request could be accommodated. And if not, then we would like to proceed with the admin console.

23:51 - Chris Whitney (Questco Cos)
  Oh, is that gate, that decision gates whether or not we need the admin console or not?

23:58 - Dimple.Desai
  Yes. Ooh.

24:00 - Chris Whitney (Questco Cos)
  Okay. Kind of a high priority ask.

24:04 - Anna.Fiske
  Okay.

24:07 - Jagger Sturdivant (Questco Cos)
  So if we don't have the admin console, where, Chad, you mentioned like a regenerate button earlier. Where would that live?  Like where would we trigger Taylor to actually go make the workbooks?

24:26 - Anna.Fiske
  Good thinking, Jagger.

24:27 - Chad Gregory (LaunchPad Lab)
  I guess in my head it was something connected in client space, but I don't know if that actually makes sense.

24:36 - Jagger Sturdivant (Questco Cos)
  I would avoid probably using client space for that.

24:39 - Chris Whitney (Questco Cos)
  You're going to need a manual, you're going to need a procedure, Jagger, which you're thinking that says go generate workbooks for input the client details and say go?

24:49 - Jagger Sturdivant (Questco Cos)
  Yeah. We need something like that.

24:51 - Chris Whitney (Questco Cos)
  Yeah.

24:53 - Jagger Sturdivant (Questco Cos)
  Or even for the batch run, like we have to initiate that process somewhere.

25:03 - Conor Hawes
  It's like, are the, who are all the actors for that? Like, if, if some of that's like the, the BA team, then, I mean, there might just be several entry points for it, right?  Because like, would, would that, if there's a, a team that's like used to working in client space that shouldn't have access to the admin panel, like if, if the admin panel is the only way to trigger it, then that would increase the number of users that would need to go in there, right?

25:36 - Jagger Sturdivant (Questco Cos)
  Yeah, I don't, Anna, who, who is going to be generating the workbooks?

25:42 - Anna.Fiske
  Not everybody. I would say just because we're doing it ahead of time, um, it would be a limited number of people that would be generating the workbooks.

25:51 - Chris Whitney (Questco Cos)
  All, so it would be all, uh, benefits, subset of benefits team and tech would be the only ones. It wouldn't be any.  Anybody on the CS, wouldn't it be any of the reps or EOI?

26:05 - Anna.Fiske
  I don't imagine any of the renewal reps doing it. would imagine, yeah, it'd be like me, Jagger, Dimple, possibly Spencer, and then the CSP team because they'd be doing renewals every month.

26:17 - Chris Whitney (Questco Cos)
  The CSP team. Is that EOI or no? The CSP team, is that EOI?

26:24 - Anna.Fiske
  No, that's my team. Client-sponsored team, yeah. Okay.

26:28 - Chris Whitney (Questco Cos)
  That and implementation also because for new clients, they would need that.

26:32 - Dimple.Desai
  Would all of the implementation need that or just like implementation benefits? Implementation benefits, sorry.

26:38 - Anna.Fiske
  Yeah, like the benefit team. She's no longer here, so it'd be Connie and Jen.

26:46 - Chris Whitney (Questco Cos)
  Can't imagine we would create benefits, an admin site just for a button to generate workbooks. Can't imagine that. I can't imagine if we had to have one for reporting, we would tie it on there.  to comes can get be There's Can't imagine we would do it just for that. There's a million ways we can kick off flows in Office 365 as well.  That's probably an avenue that's worth pursuing here for a trigger point. Although I don't, yeah, we should talk about that.  When do we need the answer, Dimple, for the reporting? Is it a chat question?

27:23 - Dimple.Desai
  That might be a chat question. I don't know when you guys would like to get started.

27:28 - Chad Gregory (LaunchPad Lab)
  I mean, we're not going to start on the admin console right away, but it would be good to know this week if we can.  But even if the data's in QInsights, the question would be, can we deliver the report through QInsights, right, Dimple?

27:44 - Anna.Fiske
  That's a full question, right?

27:47 - Chris Whitney (Questco Cos)
  Yeah. That piece is, okay, let's regroup internally and get an answer on that. There's money on, there might be money on that piece, and now we're weighing the, we already have a scope.  We can tailor, but if it's not the right solution, we should talk about that.

28:06 - Chad Gregory (LaunchPad Lab)
  Sounds good. Thank you guys for taking that on. I know we're at time. I got to hop, but we've got a bunch of calls tomorrow, so I'll try to hit on some of these other things that we didn't quite get to in those calls.  Thanks, everybody.

28:22 - Chris Whitney (Questco Cos)
  Thanks. Thank you, guys. Bye.