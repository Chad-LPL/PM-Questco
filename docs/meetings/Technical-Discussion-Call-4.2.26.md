Taylor v1 - Technical Discussions - April 02
VIEW RECORDING - 22 mins (No highlights): https://fathom.video/share/yd87eoYQH9kG_y3pxhu8tz37sXJBcqHL

---

0:00 - Chad Gregory (LaunchPad Lab)
  Timbal did send a thing asking about it. So, José, you're only available the first half of this?

0:12 - José Blanco
  No, wasn't available the second half, but I was able to talk with Juan to figure it out, and I'm going to be here the whole time.

0:19 - Chad Gregory (LaunchPad Lab)
  Oh, yeah. Oh, yeah. Digital Dental, did you guys move that call? Or is he just taking it?

0:27 - José Blanco
  Yeah, we're just going to be asking for, like, some quick questions. So he's going to take care of it.

0:33 - Chad Gregory (LaunchPad Lab)
  Sounds good. Hey, Jagger. Sorry about the link. Spencer, same to you. We'll give Timbal a second. Everything on here has gone so slow.  I know that Ifat's just going to tell me to get rid of all of my tabs. She says that to me every few months.

1:29 - Ifat Ribon
  Do you ever do a tab cleanup while housekeeping? Yeah, I do every time you tell me to. Well, go clean up your tabs.

1:39 - Chad Gregory (LaunchPad Lab)
  How many tabs do you open? Honestly, I feel like I'm in good shape right now. I think it's Cursor also in the background now is like killing me.  But yeah, all right. Hey, Dimple, sorry about that. Thanks for hopping on. Okie doke. So yeah, the goal of...  This call this morning is to go over essentially what we need to know and how we need to get access to the API for Prism and Client Space, and then also touch on, I guess, any other questions that we might have around Azure and SharePoint, I suppose, as well.  But I guess from the dev team, and maybe we start with Prism, Connor, since we kind of started down that road a little bit yesterday, is there a spot that you would want to start there?  Or maybe it makes sense to ask, like, Jagger, maybe how you're using these today and, like, what to look out for as we...  We start to get access.

3:09 - Jagger Sturdivant (Questco Cos)
  Maybe that's too vague.

3:11 - Conor Hawes
  Well, yeah, I think the latter would be better. know that Jagger had mentioned Asana, like going under the covers of the client that he created on the Java side.
  ACTION ITEM: Send Prism API docs to Chad/Conor/Nikki; include Create PEO Session + token, GetClientMaster, benefits endpoints, GetData - WATCH: https://fathom.video/share/yd87eoYQH9kG_y3pxhu8tz37sXJBcqHL?timestamp=195.9999  And then, yeah, I don't necessarily know that we need to talk about like endpoints in detail in this call, but yeah, having documentation around that or creating that documentation to send over async would be great.

3:44 - Jagger Sturdivant (Questco Cos)
  I think there is one endpoint we should talk about, and that's the create PEO session. I don't know if you've seen that one, but that one is required to make any call to the API at all.

3:55 - Conor Hawes
  Yeah, yeah, I've seen it. Yeah, so that's the only one you have to use.

4:00 - Jagger Sturdivant (Questco Cos)
  You have to pass that token in the headers for every call. Other than that, you just have some important ones that you may use often, like GetClientMaster gives you all of the data about the client.  In the benefits categories, there's a lot of GetBenefits plans, GetBenefit rules, that's where you're going to get most of your benefits data.  And then if you're ever doing, like, bulk actions, in the system category, there's a GetData, and you pass in, like, Client, ClientMaster, and it'll give you every ClientMaster possible, instead of having to iterate that client list and requesting them one by one.

4:45 - Conor Hawes
  Oh, interesting. Okay. But other than that, like, that's kind of the gist of it.

4:51 - Jagger Sturdivant (Questco Cos)
  I can show you the Java Client if you want to see it, but really all it's doing is calling...  Great PEO session, attaching the link, and then hitting the endpoints.

5:03 - Conor Hawes
  Yeah, yeah, okay.

5:10 - Chad Gregory (LaunchPad Lab)
  That's fine.

5:10 - Conor Hawes
  Do you know the difference between, so I think one of the comments I left was there's like four or five endpoints that all sound the exact same to me regarding benefits.  So I'm just trying to pull up the comment that I left.

5:33 - Jagger Sturdivant (Questco Cos)
  Oh, I see it.

5:34 - Conor Hawes
  Yeah, so there's, where did it go? Get active benefit plans, get available benefit plans, get benefit plans, and get client benefit plans.

5:50 - Jagger Sturdivant (Questco Cos)
  They don't name them very well.

5:53 - Conor Hawes
  Do you know, does one of those stand out to you as one that you're, you typically use? I know I've used Get Benefit Plans, Get Client Benefit Plans, and Get Active Benefit Plans.

6:04 - Jagger Sturdivant (Questco Cos)
  I don't think you'll need Get Available Benefit Plans. Okay.

6:09 - Conor Hawes
  I was thinking that maybe, just reflecting on the call that we had yesterday, that Get Available Benefit Plans would possibly be what came over in the OBP import.  Oh. But, that being said, like, you know, it's all new to me, so I'm just trying to wrap my head around it.

6:36 - Jagger Sturdivant (Questco Cos)
  And maybe that one is related to an employee. Hold on. Oh, they're both related to an employee. Honestly, I don't know what the difference between those two things are.

6:52 - Conor Hawes
  All right. Well, we'll find out. Yeah.

6:54 - Jagger Sturdivant (Questco Cos)
  I've only ever used Get Active Benefit Plans. I don't think I've ever called Get Available Benefit Plans. Plans.

7:00 - Conor Hawes
  Okay. I mean, that is, that's definitely helpful context.

7:03 - Chad Gregory (LaunchPad Lab)
  Yeah.
  ACTION ITEM: Set up Prism/Client Space web service users (sandbox) + dev logins; limit to 102,104,105,107; send creds/links to Chad/Conor/Nikki/José - WATCH: https://fathom.video/share/yd87eoYQH9kG_y3pxhu8tz37sXJBcqHL?timestamp=423.9999

7:05 - Conor Hawes
  I guess, like, I mean, without being able to, like, get into it, you know, there's only, like, so many questions to ask.  So I guess the, like, main ask that I have right now is just trying to get that web service user set up for the sandbox and if you're, like, if you have any influence there.

7:28 - Jagger Sturdivant (Questco Cos)
  I do not. That is Dimple. Yeah.

7:30 - Dimple.Desai
  I am currently still waiting on corporate IT to free up some licenses for you guys. I pinged them again this morning.  And so I'm hoping that it's going to be sometime today. But, yeah, so I can't set up your web service users until they have some licenses for you guys.  And so once I have that, I will be setting up your Prism and client-based accesses and then sending you links for both of them.

7:58 - Chad Gregory (LaunchPad Lab)
  Okay. Okay, and is that like a quick question for the web service user?

8:03 - Conor Hawes
  Like that would be one user per environment, right? Not one user per developer?

8:13 - Dimple.Desai
  We're currently, I think the way that Anna sent out the access form, she asked for one user per developer, but do we just need one user?

8:21 - Conor Hawes
  Well, I guess there's like, maybe there's a distinction between like an account that I can use to log into Prism.  That would be associated to Connor. But then like this web service user is, is like how the servers communicate together.  And so that's like, that's app to app. So I don't, unless like you guys have specific like auditing in place where you want to be able to see like which developer is using their local development environment to speak to the sandbox environment.  If that's the case, then we would need. Individual, like, web service users created, but if it's just, like, we need a different account for the development environment to speak to the sandbox, and we need a different account for the production app to speak to the production Prism API, then I think it would just be, like, one for the team per each environment.  But I don't, like, I can't, I don't think I can make that decision. would say, like, typically I've seen it more on the end of, like, having one service account created per app environment, but your corporate IT policies may differ from my experience.

9:40 - Dimple.Desai
  Yeah, so, um, I think one of the other reasons why we're doing one account per developer is because we, we've rolled out this, um, new authentication method for Prism, it's called Prism 1ID, where, um, every single account, it has to be associated with a specific email address, and the person signing in, they.  They to either send a code to their text message or through an authentication app. So if we did just one account for all of you guys, every time you log in or anything like that, if you are trying to log in, you would have to either send a text message code to one of the phone numbers associated with you guys or authenticate via an app on one of your cell phones.

10:24 - Conor Hawes
  I think that's maybe like where there's still a little bit of confusion because like this service account, like the servers communicating with each other, like you won't be able to use a text message base flow for that.  Or like I wouldn't expect that like security protocol to be in place for the web service user as opposed to like the actual user account.

10:50 - Jagger Sturdivant (Questco Cos)
  Yeah, the web service. don't know, Jagger, like are you able, maybe I'm just, maybe I'm not explaining it well.  Yeah, so the web service user doesn't have that security. Security feature. It's just a username and password. So you'll each have your own Prism account that you log into, which is what Dimple's referring to.  That's the one you'll have to authenticate with Prism 1. And then I don't know if we're going to assign one web service user for each environment.  We probably will. And it'll just be called like Taylor API or whatever.

11:21 - Conor Hawes
  And that's the one you'll log into with the API.

11:24 - Jagger Sturdivant (Questco Cos)
  So you'll just get a username and password for the web service user.

11:27 - Conor Hawes
  Okay. Yeah. That's, that's what I was thinking. Yeah. If we're able to get the web service user created, that would definitely help unblock some of the spike work.

11:37 - Jagger Sturdivant (Questco Cos)
  Dimple, that is a Taryn. We'll be able to set that up.

11:41 - Dimple.Desai
  Okay. Okay. Okay. That's what we're after this call.

11:47 - Conor Hawes
  Awesome. Thank you guys. That's good.

11:50 - Chad Gregory (LaunchPad Lab)
  Is there anything that we should know? Like we're, we're a little bit focused on like the Prism side of things right now and we have that spike going, but the.  Is anything different to know about the client space side of the API? We're probably going to be jumping into spiking on that, would think, next sprint as well.  And obviously, hopefully we'll be getting access to both at the same time kind of here.

12:19 - Jagger Sturdivant (Questco Cos)
  I haven't used the client space API yet, so we'll be learning and suffering together on that one. I do have an upcoming project that I'll be using that for, so hopefully by the time you guys are getting into it, I'll have a little bit more knowledge on how it works.  But as of now, I haven't used it, so I don't know.

12:40 - Chad Gregory (LaunchPad Lab)
  Okay. And their API documentation, I think, looked like it was Swagger, like the page we got was based in Swagger.  Yeah, I just dropped the link in the chat.

12:57 - Nikki Dow
  It looks like it's going to be the same thing where there's going to be... An API user that's kind of separate from, like, users for the teammates to log in to client space.

13:09 - Chad Gregory (LaunchPad Lab)
  Okay.

13:17 - Nikki Dow
  So I would kind of say, like, the same thing we said for Prism, where that API user is probably, like, the most important thing for us to get access to.  Like, the actual login users are important, too, but the API user will let us start working.

13:35 - Dimple.Desai
  Gotcha.

13:43 - Chad Gregory (LaunchPad Lab)
  Nicky, was there anything else that you wanted to talk through, thinking through, like, your spike on technical architecture at all?  I know we don't have Chris here today, but maybe Jagger can speak to anything, any questions that you might have, too.
  ACTION ITEM: Check for Questco login email; confirm receipt to Chad/Nikki - WATCH: https://fathom.video/share/yd87eoYQH9kG_y3pxhu8tz37sXJBcqHL?timestamp=832.9999  Or even just, like...

13:59 - Nikki Dow
  that to you,'am. I guess the one question that came up yesterday, Jagger, think you mentioned that you had already added us to Azure, but we would need our Questco logins.  Should we have seen those Questco logins come through, or how are we going to be getting those? I talked to Neil yesterday, and he said that José maybe was getting his yesterday.

14:26 - Jagger Sturdivant (Questco Cos)
  I don't know, José, if he actually got it.

14:32 - José Blanco
  I don't think I saw it come in, but I'll double check. Okay.

14:38 - Conor Hawes
  I got a Mimecast message three minutes ago.

14:42 - Dimple.Desai
  Yeah, I did too. Richard from IT just said that he freed up all the licenses for you guys, like, right now.

14:50 - Chad Gregory (LaunchPad Lab)
  Nice.

14:52 - Conor Hawes
  All right, well, we've got some work to do after this call, then.

14:57 - Nikki Dow
  That's good.

15:01 - Chad Gregory (LaunchPad Lab)
  Is there anything that we need to know about, and this is maybe me just being less technical here, but is there anything we need to know about, like, accessing SharePoint?  Does that just come with the Questco login too?

15:15 - Jagger Sturdivant (Questco Cos)
  Yeah, it will. Okay.

15:22 - Chad Gregory (LaunchPad Lab)
  Just trying to think. Like, our first batch of, like, a lot of the first batch of work here is, like, getting the PrismHR API set up, client space integration, SharePoint file.  Like, a lot of this early work is, like, getting all of that stuff set up so we can move forward.  My goal, though, for this afternoon's call is to talk more about, like, what we expect for the admin console so that Nico can get rolling.  Unlike on setting up some designs for that, I'm assuming this is like out of scope of this call, guess, but something to think about for you guys for the later call is maybe around like, I'm assuming we're probably keeping that pretty simple design wise.  I guess Nico has like the style guide and all the logos and everything now. So thank you for that, Dimple.  Is there anything else for this call, Conor, Nikki, or José, that has been rattling around in your brain that you want to check in on?

16:49 - José Blanco
  I suppose if there was a preference to the database that's going to be used, if there's like any... Any requirements that may have been missed earlier, or if we can defer to our preference here?

17:10 - Jagger Sturdivant (Questco Cos)
  Yeah, I mean, I think for backend database, you can kind of pick whatever. Usually we use like SQL Server, just because that's kind of what Azure does.  But if you want to use like Postgres or something else, I mean, feel free.

17:24 - José Blanco
  Thank you.

17:29 - Chad Gregory (LaunchPad Lab)
  Okay. Well, I guess we didn't need the full hour.

17:33 - Conor Hawes
  Sorry, like one question I had, and this might be, I mean, it might be more relevant. Once we get all the licenses and logins set up, but is there any sort of instruction or guidance you guys can give us on which companies or like, I guess maybe, maybe clients might be the right word we should, or like could be using.  For, for testing. Like I know that, was it Natalia yesterday or Natalie was using like a, like a demo company.  And so I'm just wondering, basically, like, I don't want to go in there and break a bunch of things, but I also do like, want to make sure that we're like, yeah, basically like have confidence that we're, we can like, like play around as we're exploring.  And yeah, maybe just like some bumpers or guide rails to help us like mitigate the damage control there.

18:36 - Dimple.Desai
  Yeah. So when I'm creating your access in both Prism and Client Space, I'm only giving you guys access to four test, testing companies.  And their client IDs are 102, 104, 105, and 107. But that's all that you guys are going to be able to see when you log into the database.

18:56 - Conor Hawes
  Okay, perfect. And then like from there, we can go in. And then modify rates or like make updates, or is it pretty much like we should treat it read-only for now because other people might be using them?  Feel free to do whatever you want with those clients.

19:14 - Chad Gregory (LaunchPad Lab)
  Nice. Okay, you got to be careful when you tell me that.

19:18 - Nikki Dow
  Yeah, maybe, okay, well, not whatever you want.

19:22 - Dimple.Desai
  Yeah, okay, that's really helpful, though, and I'm glad that it's able to be scoped like that.

19:29 - Conor Hawes
  That's helpful.

19:30 - Chad Gregory (LaunchPad Lab)
  Mm-hmm. Nikki, were you saying something?

19:34 - Nikki Dow
  Yeah, I guess maybe like a couple of clarifications that are maybe silly to ask, but is the API user going to also be locked down to just those few clients?

19:46 - Dimple.Desai
  I think for the time being, yes, that's how I'm going to try to get it set up.

19:50 - Nikki Dow
  Okay. And is this like a staging environment separate from like the production data, or is it, okay. Yes.

20:01 - Dimple.Desai
  Gotcha. Okay, that makes me feel better. Yeah, there's plans to help you guys move into production later on, but as of right now, we're just going to be in the testing environments.

20:14 - Nikki Dow
  Yeah, totally. That makes sense. That works.

20:18 - Conor Hawes
  Yeah, I did see in the documentation for configuring the API user for Prism, you can limit it to companies.  So I guess just like include those same IDs in that request if you can, Dimple.

20:30 - Dimple.Desai
  Yep.
  ACTION ITEM: Send datesandtimes.work options for next week's workflow walkthrough w/ Anna to Chad/Conor/Nikki/José - WATCH: https://fathom.video/share/yd87eoYQH9kG_y3pxhu8tz37sXJBcqHL?timestamp=1233.9999

20:44 - Chad Gregory (LaunchPad Lab)
  I guess the only other thing maybe for you, Dimple, is if you had any thoughts on times and days for different calls next week, but I'll let you figure that out with everybody.

20:57 - Dimple.Desai
  Yeah. Even with Anna not here, I'm sure.

21:00 - Chad Gregory (LaunchPad Lab)
  It's hard to know exactly what days are best for her, so.

21:05 - Dimple.Desai
  But I will, so once we hop off of this call, I'm going to get the web service user set up, and then I will also send you datesandtimes.work for a workflow walkthrough with Anna next week.

21:18 - Chad Gregory (LaunchPad Lab)
  Okay, fantastic. I think we are good for now, and we'll talk more this afternoon about the admin console with Nico.  So, appreciate you guys, and let us know if anything else pops into your head about any of this. We appreciate it.  Thank you, guys.

21:38 - Dimple.Desai
  Thanks, guys.

21:39 - Jagger Sturdivant (Questco Cos)
  Thanks, everyone.