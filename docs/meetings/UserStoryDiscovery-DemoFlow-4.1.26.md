Taylor v1 - User Story Discovery - April 01
VIEW RECORDING - 66 mins (No highlights): https://fathom.video/share/WDdvzGDUsxjT2QnkAVFJLxan-N772cKp

---

0:00 - Dimple.Desai
  Um, my, my husband has a job in Illinois, so that's why we needed to get a house very close to the border for taxes.  Are you in like, like Kenosha? Caledonia.

0:11 - Chad Gregory (LaunchPad Lab)
  Oh, okay. Yeah, I'm in the northern suburbs in Buffalo Grove here. Uh, so pretty close to that area. Yeah, yeah.

0:21 - Dimple.Desai
  Um, I don't know too much about Illinois, but, um, my husband works in Gurney. I don't know how far that is from Buffalo Grove.

0:28 - Chad Gregory (LaunchPad Lab)
  Yeah, that's, uh, it's like in between the two, so we're probably like 30 minutes from Gurney, and I imagine you guys are probably about 30 minutes, 45 minutes from Gurney.  Yeah.

0:39 - Dimple.Desai
  Yep, exactly that.

0:41 - Chad Gregory (LaunchPad Lab)
  That's funny. Awesome.

0:44 - Dimple.Desai
  We were just talking about how nice the weather was on, um. Monday.

0:49 - Chad Gregory (LaunchPad Lab)
  Yeah, an hour. It took a really sour turn.

0:52 - Dimple.Desai
  I see you clutching that cup like you're freezing. It's primarily because my office is in our floor. Four Seasons room in our house, so there's windows all around, and so very cold.

1:06 - Chad Gregory (LaunchPad Lab)
  Yeah, you're frozen solid. Okay.

1:08 - Spencer Stringer
  Do I need to overnight you a little foot space heater for your pet?

1:14 - Dimple.Desai
  I really like one of those, have you seen one of those like table heaters that you can put over your legs under your desk?

1:21 - Spencer Stringer
  Yes, and I have one that goes over your keyboard and mouse too.

1:24 - Chad Gregory (LaunchPad Lab)
  Whoa, that's a step up. Awesome. All right, I think we've got everybody here. Yes. Just to set the stage a little bit, LaunchPad does have, LaunchPad and Questco are going to get together later this afternoon for a shorter meeting, like a weekly status check-in.  Generally on that call today, I think I want to focus on somewhat logistical stuff, where we're at. I potentially get some different questions answered, but making sure that we are able to potentially schedule additional meetings if we need to reschedule, Chris, potentially the meeting that you're not able to make tomorrow and get through some of that stuff, show you guys kind of where we're at on things.  This call this morning, the original purpose was to get into some of the kind of user story grooming and everything after the walkthrough on Monday, which was very helpful.  We kind of realized one thing that would help a ton in putting together these tickets is doing kind of a full demo walkthrough of like a real sample of this whole process that you have today and giving you guys a chance to talk about what are the areas that you are really hoping to see that improvement on with Taylor.  What areas are you expecting are going to go away when Taylor begins, either obviously in V1 or later in like a V2?  And obviously we'll want to ask questions along the way, but Dimple was able to bring in Natalia, I believe, to help with this, and I really appreciate it.

3:20 - Dimple.Desai
  Yeah, Natalia is our strategic benefits operations lead. But before we get started, I was wondering if we could just have like a couple of minutes to talk about the Azure items on this call since Chris is here.

3:34 - Chad Gregory (LaunchPad Lab)
  Yeah, we can jump into that.

3:36 - Chris Whitney (Questco Cos)
  We'll see, maybe give us five minutes, 10 at the most, and we'll see if we can answer and make sure that we can get you all working when we actually get to a point to develop.  So, do we have the right representation from the key technical team here on the call?

3:57 - Chad Gregory (LaunchPad Lab)
  Yes, we do. Between Nicky, Connor, and Jose. Okay.

4:01 - Chris Whitney (Questco Cos)
  All right. So I'll give the super top side high level on Azure. We have one environment, one subscription. And Azure subscription is the same thing as an AWS account.  I don't know what it's called in Heroku or GCP world. We essentially have a primary Azure subscription. What we would like to do is we would like to provision resource groups, which are the logical containers, and give you all full control and full access to the resource groups.  From there, you can build any object and it's self-contained into the resource group. And we can make sure that the resource group is named correctly and so on and so forth.  So the first fundamental question that we have is, if you're going to build this dev environment and a production environment, we're going to want to create two resource groups.  We're going to want to segment this with a dev and a production. So what we need from you is that answer if we're planning.  on traveling down that path. Once you have your Questco accounts, it'll be a piece of cake for us to assign you full control over those resource groups, and then you could go to town.  So before I talk about Git integration and CICD, I'll stop and see if there's any Azure questions.

5:23 - Nikki Dow
  No questions on what you just raised, but I think we do want the separate dev and production environments.

5:30 - Chris Whitney (Questco Cos)
  Okay, perfect. So the other piece that's really important, and I don't know what Sprint that is for me and for Jagger, is I really want to see what you're building and what you plan on building and what the design includes.  There's, you know, there's 10 ways to build different services, so we want to stay away from VMs, and we want to look at functions and serverless, and we want to be modern and progressive in the stack.  So when we get to that point, that piece is really important. So you guys can go to town, but at the same time, we want to understand what you're building.  The second piece is cost. The other reason we really need to understand what you're building is so that we can make sure that we're forecasting the costs correctly.
  ACTION ITEM: Create Azure dev/prod RGs; grant Nikki/Jose full control - WATCH: https://fathom.video/share/WDdvzGDUsxjT2QnkAVFJLxan-N772cKp?timestamp=367.9999  I don't think this is going to be high cost on the Azure Compute side, but yeah. Okay, so we'll take the action to get those two resource groups created and get your accounts added from there.

6:25 - Chad Gregory (LaunchPad Lab)
  That's awesome. Maybe just to give you some context on that call that I had scheduled for yet tomorrow, Chris, and maybe the Azure part of that is sort of handled now with just what you guys talked about.  But we also wanted to kind of talk through the API for and the access that is needed for Prism and client space.  Also, what we might want to do with SharePoint.

6:56 - Chris Whitney (Questco Cos)
  Okay, perfect. You don't need me on that. You should keep that. And you have with Dimple and Spencer and Jagger and the team here.  I saw your gestures. Did I catch your gestures? So, yes, you should keep that. You don't need me on the call from that.  It's great to go through. CICD, we don't have any. Help us bring this into the company. So the best that we do here is automated.  I guess we should. We do have a bit. Some automated deployments through some GitHub Actions is kind of the best that we do.
  ACTION ITEM: Grant Nikki/Jose full control to GitHub repo; they configure SSO/SSH - WATCH: https://fathom.video/share/WDdvzGDUsxjT2QnkAVFJLxan-N772cKp?timestamp=451.9999  There's no other CICD platform. So the tooling is essentially native Azure plus GitHub and GitHub Actions. So we also created a repo for you all, and we'll get you guys full control access to the repo.  You're going to have to use your Questco accounts because it's single sign-on. And then once you get in, you're going to have to create your SSH keys or work through it.  You're going to use the API to post and continue. Admit to the repo, but I think we'd like to kind of lean into GitHub where we can, instead of standing up some other third-party CICD, either GitHub or Azure DevOps is what we would prefer.

8:16 - Chad Gregory (LaunchPad Lab)
  Okay, nice. Nikki or Conor, José, any questions for Chris on this stuff? Otherwise, we can save some of that for Jagger and Dimple tomorrow.

8:28 - José Blanco
  Not for GitHub Actions is ideal.

8:32 - Chris Whitney (Questco Cos)
  Okay. Right on. Okay. Right on. We don't have, like, GitHub Copilot. We don't have, like, any of the GitHub Copilots.  So from the AI perspective, we could talk about that in another call. We'll have to externalize your AI support, which I think you guys are already doing, but that's the one piece we don't have licenses for, which we won't buy.

8:57 - Chad Gregory (LaunchPad Lab)
  Okay. So if you're...

9:00 - Chris Whitney (Questco Cos)
  And I want to inject what you, which you will. We should also maybe talk about that when we get into it.  I don't know what you guys use for generating code. I don't know what AI you're using, but if we needed to provision a Claude license, so we use Anthropic for this chain and we use Claude.  If we need to provision that license, we can talk about that as well.

9:28 - Chad Gregory (LaunchPad Lab)
  okay.
  ACTION ITEM: Schedule tech architecture review w/ Chris + Jagger next week - WATCH: https://fathom.video/share/WDdvzGDUsxjT2QnkAVFJLxan-N772cKp?timestamp=568.9999

9:29 - Chris Whitney (Questco Cos)
  Okay, thanks for letting me take some time. But yeah, I think you're keeping that technical call tomorrow and getting through the APIs is probably, SharePoint is probably a good idea.

9:39 - Chad Gregory (LaunchPad Lab)
  And then, sorry, to go back to what may be one of your very original points, we do want to set up time probably next week to review the technical architecture that gets developed.

9:52 - Chris Whitney (Questco Cos)
  Perfect.

9:53 - Chad Gregory (LaunchPad Lab)
  Yeah, Mark, yeah, you can deliver that.

9:56 - Chris Whitney (Questco Cos)
  so, Jagger, did we already create the repo? Yeah.

10:00 - Jagger Sturdivant (Questco Cos)
  Uh, yeah, I think so.

10:02 - Chris Whitney (Questco Cos)
  Okay. Yeah, so we should probably try to, like, merge into using that repo, folks, and if you want to publish Markdown up in there, it'll be easy for us to work like that, so, or whatever format.  So the repo's there, you're just going to have to do the work of signing in SSO into GitHub to configure your keys.  I guess the last thing, technically, is just a comment on SharePoint real quick. So because you're in Azure, your authorization into SharePoint is going to be really easy for us.  We can create app registrations for the services that you build in Azure and wire those up so that we can authenticate in through the Graph API and things like that.  So leaning into SharePoint is good because we're building in Azure. It'll be easy for us to configure that authentication, and we won't have to pass, we won't have to do anything with pulling the key.  Keys out, so on and so forth.

11:02 - Chad Gregory (LaunchPad Lab)
  Okay, that's all I have. Sweet. Okay.

11:08 - Chris Whitney (Questco Cos)
  Any technical questions at all from the team? We have a big group, so thanks, everyone. Talia, thank you for bearing with that.  Jagger, can you take the action with Neil on creating the two resource groups and giving the team access?

11:24 - Jagger Sturdivant (Questco Cos)
  Sure.

11:25 - Chris Whitney (Questco Cos)
  Also, folks, I don't want to give all five of you, if you need it, we'll give it. Who really is going to be building in Azure is the other question.  So, let me know who actually needs that access into Azure. If you want to put it in the chat, you can, or send it to us offline, because I don't think you all need it.

11:45 - Chad Gregory (LaunchPad Lab)
  Yeah. Nikki, do you think it's just you, Jose, and Conor?

11:49 - Conor Hawes
  Let me start with Nikki and Jose for now.

11:52 - Chad Gregory (LaunchPad Lab)
  Nikki and Jose. Okay. Okay.

11:54 - Chris Whitney (Questco Cos)
  Great. Great, great, great. Not that we have no problem, but let's just be smart about assigning access to that.

12:00 - Conor Hawes
  Yeah. Principal, least, privilege. There you go.

12:03 - Chris Whitney (Questco Cos)
  Thank you, folks. Thanks, David.

12:06 - Nikki Dow
  Sorry, I guess my one follow-up question. When you say you're going to provision the resource groups, and then that's kind of like ours to start building in, like with your approval on certain, on the design, are there anything we should know about ahead of time where Questco already has preferences?  Because I'm thinking things like, do you strongly prefer container apps over web apps? Or like just things like that we should know before we start that design?

12:35 - Chris Whitney (Questco Cos)
  serverless is the, like, serverless would be the key. So anything where we don't have to manage the compute stacks.  So if you're going to build containers, and we're going to publish the containers, it's okay. But I'd rather use the Azure Container Services or the, I don't know what it's called, EKS or AKS, the Azure Kubernetes Service.  Right? So serverless there. And then, yeah, Azure Web Apps. Azure Web Apps is like the source container for the object for like deploying functions.  So, yeah, functions would be first. If you're going to build something that needs more robust containers, I just don't want to run this natively on infrastructure that we have to manage unless we really have to.  The other pieces we know that well are know that world really well. So if you guys need help on that, like connecting the services or the underlining VNet.  So VNet is like a VPC in the networking layer. If you need help on that, let's just talk about it.  So know you're coming into on Azure side. So, yeah, like let's work as a team on that piece. But to answer your question directly, serverless, light administration to the best that we can.  Once you have the resource groups, when you log in. Azure, you're going to be able to essentially have full control over them.  So you'll be able to download the CLI and work with the CLI and so on and so forth. And you can configure and sandbox in the dev, absolutely.  Like I said, just all that stuff comes at a cost. So use your discretion. But if you're going to be building something that's substantial in cost, over $500 a month, over a couple hundred dollars a month, we really need to talk.  So just be, just, I'll be watching it too, not in a bad way. We have another project going on there and it's spiked out of control.  So I just need your help to make sure you keep us all posted as to what you're building.

14:42 - Nikki Dow
  Yeah, for sure. That all sounds good.

14:44 - Chris Whitney (Questco Cos)
  Cool. Thanks, Nikki.

14:49 - Nikki Dow
  Thank you.

14:50 - Chris Whitney (Questco Cos)
  You really won't be able to break anything. Well, , I don't want to jinx this.

14:54 - Chad Gregory (LaunchPad Lab)
  Yeah, don't jinx it.

14:56 - Chris Whitney (Questco Cos)
  Oh no, what happened here? Remember this conversation. You're going to be. So your full control to those two resource groups is going to really put you, but you're going to like, once you get to like wiring up authorization against SharePoint and stuff like that, you're going to need all of our help with that, but you should be able to, to like get to work quickly.

15:14 - Chad Gregory (LaunchPad Lab)
  Nice. Okay.

15:15 - Chris Whitney (Questco Cos)
  That kind of sounds like in the movies when people say, what's the worst that can happen? Careful here. No, no, we'll be, we'll be good with this resource group approach.

15:26 - Chad Gregory (LaunchPad Lab)
  All right. Perfect. Perfect.

15:28 - Dimple.Desai
  Thank you. Okay.

15:31 - Chad Gregory (LaunchPad Lab)
  Dimple, do you want to set the stage for Natalia?

15:34 - Dimple.Desai
  I do. I do. Yes. Natalia, thank you again for joining the call today. We really needed a benefits perspective on the renewals process.  For some context for you, I have already mapped out all of the client space workflows for the benefits batch and for the benefits setup and renewals data forms.  And then I've also provided some tangos that Anna had created that involve information. you. much. Thank Informations such as like how to create a benefits batch, how to start a benefits setup and renewals data form, how to process a renewal and stuff like that.  But having a clear step-by-step walkthrough in order would be super helpful for the team. So we were wondering if you would be able to walk us through kind of like the full benefits renewal process from start to finish.  It would be really nice to see each step in sequence, starting with like setting up the BSR data form, then creating the batch, and like wherever cost sheets, benefit guides, like any other key steps along the way.  Also, I guess if it's possible, it would also be helpful to understand like where the majority of the work is happening, whether or not that's in PRISM, in client space, or if there's like a manual tracker.  And like if we're going through Teams or email or any kinds of like other systems to get information or feedback from anybody.
  SCREEN SHARING: Natalia.norena started screen sharing - WATCH: https://fathom.video/share/WDdvzGDUsxjT2QnkAVFJLxan-N772cKp?timestamp=1024.348965

17:00 - Natalia.Norena
  Let me know if that makes sense. Yeah, that makes sense. So I'm going to share my screen. Can you guys see my client space?

17:08 - Chad Gregory (LaunchPad Lab)
  Yes.

17:09 - Natalia.Norena
  Okay, so I'm going to just put up a test client, and I'm going to create a batch, pretending that this client renews on the month of June.  So I'm going to select the client. I'm going to go through the benefits and create a benefits batch. So go to the benefits batch, and I'm going to, let me move my screen.  I'm going to add the batch, reflecting the month that they're going to renew. So the effective day, I'm going to say it's June 1st, so it's like an only type.  And the type is a renewal. So implementation. implementation. Implementation. Implementation. Implementation. Implementation. Implementation. Implementation. Implementation. Implementation. Implementation. Implementation. Thank  We use when there's new clients, renewal when it's an existing client, and we need to identify those plans that renew.  And the expiration date is the day that those benefits expire, or the renewal, because I'm going to pretend that they are going to expire on the 31st of the following year.  It's usually a year. So we will see this a lot through open enrollment. So most likely it's going to be from 1-1 to 12-1.  So for training purposes, we just pretend. On the renewal representative, this information we pull from PRISM. Or you can't, no, you don't see it here.  So if I go to the client 105, I'm going to see on the client details that on their account, that the benefit specialist is going to be listed here.  So I'm just going to name Jagger, because he's one of my favorite Pips and Benefits. I'm to going I'm I'm I'm I'm  So I'm going to pretend that it's Jagger, and I'm going to apply. So once the batch is created, I'm going to go to Benefit Setup and Renewal, and by going through the batch, it's going to link the Setup and Renewal page to the batch that I just created.  So I'm going to go to the Benefit Setup and Renewal, and it's going to take me automatically to the batch that I created.  If you happen to create the renewal first, you just have to make sure that it's linked to the batch that we want to work that renewal from.  The enrollment type is going to be renewal, and the effective date is going to be June 1st. And this is where we identify or we mark what kind of benefits the client has.  We can... We the import before or we can, this information is pulled from PRISM. The broker type, we get this information from a spreadsheet that we have in SharePoint.  We don't have this information in PRISM. So if it's something that you need me to grant access to it, I'd be more than happy to send it to you, Dimple, so you can share with the team.

20:22 - Dimple.Desai
  Thank you. Do you mind also showing us where in PRISM they would go to see what kinds of benefits they need to check off on the BSR?  Would it be the benefits overview?

20:36 - Natalia.Norena
  It will be the benefits overview, but once we complete this step, we can import the benefits from PRISM. So, I'll show you PRISM really quick, so I can go to type benefits overview.
  ACTION ITEM: Confirm broker-type source w/ LaWanda; decide PRISM vs SharePoint - WATCH: https://fathom.video/share/WDdvzGDUsxjT2QnkAVFJLxan-N772cKp?timestamp=1251.9999  Hold on, I have a shortcut, so let me see how it is spelled. Okay. It's client benefits.

21:02 - Chris Whitney (Questco Cos)
  Natalia, quick question on the broker type. What's the rationale with not having the broker type in PRISM?

21:11 - Natalia.Norena
  I really don't know, Chris.

21:12 - Chris Whitney (Questco Cos)
  Okay. Maybe Dimple, let's take that because I wonder if we're going to have to, if Taylor's going to have to go get that, be more effective for us not to have to go do a call to SharePoint and PRISM so we could see if there's an efficiency that we could take offline.  So that's an item to track.

21:32 - Dimple.Desai
  Yeah, that might be a question for LaWanda. I'll get in touch with her.

21:36 - Natalia.Norena
  Okay. If you go to the client information, like if you go through the workspace and their benefits and carrier logins, you can also find the broker information here.  But this is a process that we just implemented last year. So for existing clients older than a year, that information might not be here or might not be accurate.  But this is where the implementation team is including the brokered information from July 2025, 2026 on. So that's another way to find it.  And if it's something that you're going to discuss with Wanda, under the client details, that information is usually listed under the client account.  So you will find that information here. I do not know the story why Questco hides it. But that would be...  So like the broker type would be under the account information? Correct. Under the client account information.

22:43 - Chad Gregory (LaunchPad Lab)
  So I see that down there, there's a broker line under account assignments.

22:48 - Natalia.Norena
  Is that what you mean? Correct. So once you edit this information and you go to the client details, that information reflects under the client account.

22:57 - Chad Gregory (LaunchPad Lab)
  Okay. Or you can either...

22:59 - Natalia.Norena
  Or you can either... I do it here, but once you grant access to PRISM, it will show in both ways.

23:06 - Chad Gregory (LaunchPad Lab)
  And a broker is just a piece of information that needs to be in the workbook? Like that's who is assigned to the client?

23:16 - Natalia.Norena
  It's not that it needs to be on the workbook. It's for us to know who to contact when it's an external broker or who to contact for renewal purposes to get the information, the rates, rate band, all the renewal information from them.  It's not something that reflects on the workbook. The workbook is something that we work to send the client the details of reflecting the plans and the rates that they are going to be renewing with.

23:46 - Chad Gregory (LaunchPad Lab)
  Got it.

23:47 - Natalia.Norena
  So let me just go back. I'm going to go back to the setup and read. going to delete it by mistake.  So I'm going to select Renewal. I'm going to say that it's in June. And since this is one of our clients, I'm going to say that we are the broker.  And we track the commissions. That's something the agency does. So how much are displayed with that particular broker, if it's us.  And if we do the eligibility and the reconciliation.

24:30 - Dimple.Desai
  Do you happen to know where the commission information would be pulled from?

24:39 - Natalia.Norena
  I do not. That is a better question.

24:42 - Dimple.Desai
  Okay.

24:43 - Natalia.Norena
  I think that's a new process for client space too. But it was something that it just started. This feels here.  Go ahead.

24:54 - Spencer Stringer
  We were working on how to get the commissions in there. Um, and then. And life got busy. So we never actually finalized it.  So it's still kind of up for discussion on if we have a better way to do it, I guess.

25:15 - Natalia.Norena
  Yeah, these fields here are new. It does not reflect, it does not affect on the workbook creation at all either.  So that's something that we can circle back, but it won't affect your process. And once we create that, so then I'm just going to click apply.  So once the batch is created, I can go ahead and I'm going to go back to the workbook that I just, the batch that I just created, and I'm going to import the benefits that they currently offer.  That information is pulled from Prism. So every time you create a batch, there's not going to. And the results, because we just created, so I'm going to go to OBP import, and I'm going to go to actions, and we're going to select both.  This is like, if it's a client that renews, like client-sponsored plans, they renew on the monthly basis, like off-cycle, not necessarily January, where our master main clients renew.  So we're always going to, if it's up for open enrollment purposes, we're going to select both, and we're going to import.  Of course, it's going to be a lot of plans, because this is a test client, so all the plan, all the benefits that we offer rates are a bit reflected in there, so it's not as crowded.
  ACTION ITEM: Send OBP import error troubleshooting doc to LPL - WATCH: https://fathom.video/share/WDdvzGDUsxjT2QnkAVFJLxan-N772cKp?timestamp=1609.9999

26:55 - Chad Gregory (LaunchPad Lab)
  And then sometimes when we do the OBP import, there will be some errors that we'll need to.

27:00 - Dimple.Desai
  The Resolve, I think I have a document that has troubleshooting steps for certain OBP import errors. I can send it over to you guys as well.

27:09 - Chad Gregory (LaunchPad Lab)
  Okay.

27:17 - Dimple.Desai
  And typically the errors occur if there is something like there's a rate group in PRISM for a specific plan, but the rate group doesn't exist in client space, then like the plan will not, won't know like what rate group to match it up with or if basically like the rate group title, the plan ID, and the amount of benefit group codes all need to match up in both PRISM and client space for the OBP import to work.

27:48 - Natalia.Norena
  Correct.

27:52 - Chris Whitney (Questco Cos)
  Hence the rigidness of the system. Yeah. Hence the rigidness of the system and some of the challenges. Challenges when we're processing these at scale.

28:04 - Dimple.Desai
  Yeah.

28:05 - Chad Gregory (LaunchPad Lab)
  So you basically have all of these options kind of in the library in client space, but what we're doing here from Prism is like matching up what is actually a viable option for that client, right?

28:20 - Dimple.Desai
  Yes. Yes. So the OBP import should technically bring over whatever is in the client benefits overview screen.

28:28 - Natalia.Norena
  Correct. Only the current benefits that they offer is what the workbook will reflect. Should have picked another client.

28:42 - Chad Gregory (LaunchPad Lab)
  We're seeing some of those errors, right? The red. Correct.

28:46 - Natalia.Norena
  So once you import them, so all the benefits that that client offers are going to show on, you know, under the offer plans.  So that's how you create a botch. And then that's when John- Jagger comes and he does his magic creating the workbooks.

29:04 - Chad Gregory (LaunchPad Lab)
  Okay, so it's at this point, Jagger, that BabyTaylor's taking over today?

29:09 - Jagger Sturdivant (Questco Cos)
  Yes.

29:10 - Chad Gregory (LaunchPad Lab)
  For a bit, okay.

29:12 - Jagger Sturdivant (Questco Cos)
  Yeah, that's when that workbook gets generated by ClientSpace and then BabyTaylor does her pass over it and then it gets re-uploaded into the batch.

29:20 - Natalia.Norena
  And, yeah, so once Jagger creates the workbook, this automatically gets changed to a consultation once he uploads it. And so the workbook will be, sorry, my ClientSpace is super slow today for whatever reason.  So once the workbook is created, he uploads them here and it starts creating different tasks. So, yeah.

29:57 - Chad Gregory (LaunchPad Lab)
  So, yeah, so that's what, well.

30:00 - Natalia.Norena
  Once the workbook is ready, all the tasks, that's the graphic that you showed them step-by-step while you stand there.  So every time you complete one, it generates the, it follows the path.

30:15 - Dimple.Desai
  So you'll see in the visualization that basically all of the stuff that Natalia just showed you happens right before the benefit batch process begins.  Um, the statuses start, or like the, the tasks start when the batch status is in consultation status.

30:31 - Chad Gregory (LaunchPad Lab)
  Yeah. So, sorry, I don't know if there was actual, um, contradiction here or not, but it sounded like, Jagger, you might have said that, uh, the workbook got generated and then BabyTaylor's taking over, but I thought I also heard that BabyTaylor was doing the generation, or you were.

30:50 - Jagger Sturdivant (Questco Cos)
  Um, so it's both, you see the, on the right-hand side, there's a renewal work button. Yeah.

30:55 - Chad Gregory (LaunchPad Lab)
  Yeah.

30:55 - Jagger Sturdivant (Questco Cos)
  So that's client-based version of the workbook. And then. BabyTaylor goes in and modifies that one that it generates.

31:03 - Chad Gregory (LaunchPad Lab)
  Okay. So, yeah, what does this look like when we first generate it now? Is it, I assume, like pretty unusable?  And that's the purpose of a baby.

31:13 - Jagger Sturdivant (Questco Cos)
  There's like a macro that has to be run, and then we add a bunch of features with BabyTaylor.

31:20 - Chad Gregory (LaunchPad Lab)
  Okay. I think in the project files I sent, I sent a BabyTaylor version and one that comes out of client space.  Oh, nice. Okay.

31:29 - Chris Whitney (Questco Cos)
  Sure. I just might not have known the difference. You can imagine troubleshooting those import issues. We're stuck. We have to go back to client space, and we're like, this is another fundamental thing.  We're controlling it, and Taylor is going to give us that control when we actually have issues. Jagger, in BabyTaylor, when you process to get the workbooks to a good place, do you do other API calls back, or are you just...  To process some of the data that was missing that didn't come over on the workbook generation?

32:06 - Jagger Sturdivant (Questco Cos)
  I mean, there are Prism API calls that it makes. It injects a census for the client, so it makes a new sheet in the workbook and injects that.  So, mean, yeah, it is making calls to Prism. is, right?

32:21 - Chris Whitney (Questco Cos)
  You are going and correcting it, and some of those instances make calls always to Prism? Or do you go to, do you go look at the commission sheet in Excel, or do you go look anywhere else besides Prism?

32:33 - Jagger Sturdivant (Questco Cos)
  Yeah, not a commission sheet. There's a, like, our rate sheet that we get from the carriers, it checks against that to make sure that the rates are right.  And then it checks the zip code file for, like, if there's an employee that needs to have regional plans, it's checking that sheet as well.
  ACTION ITEM: Send last year's carrier rate sheets to Dimple; she forwards to LPL - WATCH: https://fathom.video/share/WDdvzGDUsxjT2QnkAVFJLxan-N772cKp?timestamp=1967.9999  Okay.

32:58 - Dimple.Desai
  Gregor, can you potentially... Please send me the zip code file and like the rate files from last year, just so we can maybe send it over to LPL.

33:08 - Jagger Sturdivant (Questco Cos)
  They do have the zip code file, but yes, I can send you the rate sheets.

33:12 - Dimple.Desai
  Okay, thank you.

33:17 - Natalia.Norena
  Anything else you want me to go over, Dimple? So just for you, like when we do have the errors, so we go to the plan and this is where we go to the plan code, and this is where we edit the information, whether it is to change the rates or the premiums, anything that has to do with that particular plan, this is where we will make the edits.

33:56 - Chad Gregory (LaunchPad Lab)
  You would make these edits before the work? Sheet is generated? After. After? After, yeah.

34:04 - Natalia.Norena
  So when we have those errors, and then we have, like, let's say there is a rate group that we need to correct, that was the error we received the information.  So we select the plan that we need to correct, whether it's the rate ban or the premium, whatever the case is, and this is the screen where we make the changes.  Okay, so after the import from Prism, but is it, is, are you also saying after the workbook is generated too?  Or is it? Either, either or. So we did, we did a both ways. Ideally, will be prior the workbook is created that we can make the corrections.

34:42 - Chad Gregory (LaunchPad Lab)
  Yes, But if you saw the error later for some reason or something, you could obviously, okay.

34:47 - Natalia.Norena
  Correct.

34:49 - Chad Gregory (LaunchPad Lab)
  If the workbook was created and then you guys needed to, what would be situations in which you guys would need to, to adjust, like, premiums or anything like that, would that be, like, after you have a concert?

35:00 - Dimple.Desai
  With the client, and then they express some kind of discontent with the rates or something, would you adjust the rates here and then regenerate the workbook?

35:10 - Natalia.Norena
  Correct.

35:11 - Dimple.Desai
  Would you be putting the batch status back to like a prior status?

35:16 - Natalia.Norena
  Correct. Yes. So if we need to create a workbook again, then we just go to the status and change it back to workbook prep.  It can be like both ways, depending on how the consultation goes. you know, because once you update the plan, you can generate the CBE.  So the workbook would not really be that much involved if you had that first consultation and you had that discussion with the client.  So it's something that we can manually update and just create the CBE after that.

36:00 - Chad Gregory (LaunchPad Lab)
  So maybe this is not exactly, it's definitely not like the happiest path, but can you talk to me more about the, gosh, I lost my train of thought on, is it called OBQ?  Yeah, like how does that come into this process? I assume they are looking at, they get the, they get, the client gets a chance to see, OMQ, sorry, the client gets a chance to see the rates and the plan options, and if they're not happy or if they think, you know, oh, I might be more competitive in the market.  Westco is able to go and get those different market quotes for them. And how does that work today in terms of like going out and getting those, pulling them in?

37:16 - Natalia.Norena
  Well, if the renewal comes high and the client say, I don't, I want to go out and shop for different plans, we create a case.  So we create a case for our agency.

37:31 - Chad Gregory (LaunchPad Lab)
  Okay.

37:31 - Natalia.Norena
  So, wait, I want to go to the client and I'm going to create a case. So I'm going to add a case and then we go to benefits and then we just create.  let's just say, okay, Oh. Okay. So benefit court request. So this, the agency team gets the notification, and then we include how, on the subject, we include the client name and open market court request, and then we include, depending on the conversation that we have with the client, why they want to go out to market, was it because they're renewal, because they're not happy with the plan.  And so we include all those details in there, and once you save it, it goes through the agency queue to go out to market.

38:41 - Chad Gregory (LaunchPad Lab)
  Oh, so it like, gets sent out somewhere, where all of the different, um.

38:48 - Natalia.Norena
  So the case has nothing to do with the renewal batch. So, this is like, a separate case for them, it has, it's not related.  On the batch, we... We will just enter the notes that, so on the, hold on, let me show you, on this phase, on phase five, this is where we track the notes.  So we met with the client, the client wants, so this is where we track. So in this section, we will enter a comment saying, client was not satisfied with the renewal and requested an open market quote, and create that case.  So we had to, when we entered the case number, to follow up with agency and just track that trajectory, you know, we follow up like three to five business days later with agency to see what the status of the open market is.  But those two are not linked.

39:50 - Chad Gregory (LaunchPad Lab)
  They're not linked in the, like that is not technically a part of the flow, is that what you're saying?

39:57 - Natalia.Norena
  Notommating, but if If I.

40:01 - Chad Gregory (LaunchPad Lab)
  If I was a client trying to go through and go through my enrollment or re-enrollment and I'm not satisfied, is it kind of part of my, I thought I understood this correctly, but I may just be wrong.  If I'm not satisfied with what I see in that workbook and I ask for, I ask to go through open, the open market, and you all are able to provide me those quotes, I thought I was hearing like, you know, sometimes you're giving two or three quotes, maybe up to eight if it makes sense for some reason, and that those would get included in the workbook for the client to then review that and see kind of how either they are or are not a competitive, they're like not actually getting competitive rates?

40:56 - Natalia.Norena
  So if they kind of, if we are going to print, the workbook has nothing. to do with presenting quotes.  So the purpose of the workbook is to present them their renewals with their current plans. If they are not satisfied, then we go out and so the workbook will not play for open market quotes.  when we are shopping for different plans.

41:21 - Dimple.Desai
  I guess it's different from how I was understanding it as well. So if a client decides to, they want to be presented with open market quotes, what, where do the rates go?  Like how, how do the rates get presented to the client?

41:39 - Natalia.Norena
  That's an agency and the rates are on there. Like when you go out to market and the carrier sends how the, like all the, all the plan details, including the rates.  If they decide to go with one of those plans, we just create the CBE. We don't create another workbook.

42:00 - Dimple.Desai
  So it's like the workbook and then the open market quotes, the rates and everything, they're separate on a like separate PDF or Excel spreadsheet.

42:08 - Natalia.Norena
  Correct, yep. That gets presented to the client.

42:11 - Dimple.Desai
  And then if they decide that they want to go with the open market quote, that gets put onto the CBE.

42:17 - Natalia.Norena
  Correct. Not in a workbook. And is somebody manually like typing in all of the changes on the CBE? Correct.

42:29 - Chad Gregory (LaunchPad Lab)
  Okay.

42:29 - Ifat Ribon
  And then that also, does it also like manually make its way back to PRISM so that it shows up for their employee elections or employee enrollment?  Right.

42:39 - Natalia.Norena
  So we complete the client election form manually with their new plans that they elected, send it to the client for a signature.  Once they sign it, then our analyst team enter all that information in PRISM.

42:53 - Chad Gregory (LaunchPad Lab)
  So the next time, you know, the next time they are due for a renewal, we are going to complete.

43:00 - Natalia.Norena
  It's same process that we just did with the current plans.

43:04 - Dimple.Desai
  So then if the plan that the client decided to go with through open market, if that one doesn't exist in PRISM, and they're signing off on the CBE, would the analysts be creating the benefit plan and everything and assigning the rates in PRISM?

43:22 - Chad Gregory (LaunchPad Lab)
  Correct.

43:23 - Natalia.Norena
  And then for the upcoming renewal, we will be able to import that with those rates because that information is already in PRISM and that's where we pull it from.

43:31 - Chad Gregory (LaunchPad Lab)
  You mean for the following year?

43:33 - Natalia.Norena
  For the following year, yes.

43:35 - Chad Gregory (LaunchPad Lab)
  Okay. And you don't even care about the other plans or options that they didn't choose, right? You're not like capturing those anywhere or anything?

43:45 - Natalia.Norena
  If it's an off-mine. So once you import that in client space, you can manually update the medical portion. Instead of, like, if they currently have Aetna and they want to go, like, with UnitedHealthcare, we just override the information on the medical section, deleting Aetna with the new medical that they elected, and all the supplementals and the rest of the benefits that they currently offer will show on the CVE.

44:20 - Chad Gregory (LaunchPad Lab)
  Conor, do you want to ask your question? I can read it. Conor asked, how do you track enrollment if it's not in the workbook, Natalia?  Yeah.

44:38 - Natalia.Norena
  Like, how do we track enrollments, like, when we open the portals for the employees to make their elections?

44:47 - Chad Gregory (LaunchPad Lab)
  I'm not sure, like, I understand the question.

44:49 - Natalia.Norena
  Like, enrollments, to me, is when the employees make their elections.

44:54 - Chad Gregory (LaunchPad Lab)
  And they're actually doing that in PRISM, right?

44:56 - Natalia.Norena
  Correct. Yeah.

44:58 - Chad Gregory (LaunchPad Lab)
  And I think that that would be...

45:00 - Dimple.Desai
  pulled in the final enrollment census after open enrollment.

45:03 - Chad Gregory (LaunchPad Lab)
  Yeah, okay.

45:05 - Natalia.Norena
  Does that answer your question, Conor?

45:07 - Chad Gregory (LaunchPad Lab)
  I just want to make sure.

45:08 - Ifat Ribon
  Maybe related to that, or I don't know if this is what you're asking, Conor, but if the open market steps are today kind of outside the flow because you can't use the workbook with them, maybe where does like client space kind of come back in to get updated?  Is someone kind of just like manually updating the steps and saying, you know, they did select this open market quo and then I'm, you know, setting the status to the next status or how does it go?

45:34 - Natalia.Norena
  Yeah, that will be, those notes, those, those updates will be listed in notes and, but if that client space does not get updated, only press them.  When the renewal comes, that's when client space come into place.

45:51 - Chad Gregory (LaunchPad Lab)
  Because you get it back in that OPQ or whatever it was.

45:56 - Natalia.Norena
  OVP.

45:57 - Chad Gregory (LaunchPad Lab)
  OVP import. Yeah, okay. Correct.

46:01 - Natalia.Norena
  So the client will not be on the picture because we don't have plans to import because they just making the decision to change plans, if that makes sense.

46:11 - Dimple.Desai
  So if a client is going with an open market quote, are we not moving the batch forward at all?

46:21 - Natalia.Norena
  Not for the medical portion, no. So we complete the process like creating the CBE, but again, we manually override the changes or the carrier that they change in.
  ACTION ITEM: Collect last year's OMQ templates; share w/ LPL to define schema - WATCH: https://fathom.video/share/WDdvzGDUsxjT2QnkAVFJLxan-N772cKp?timestamp=2797.9999  Everything else stays except that. So when we go to the step of creating the CBE, yes, we generate it from client space, but we override the information with the open market.

46:47 - Dimple.Desai
  Okay. So I think that there's a major opportunity for improvement here with open market quotes. If we could potentially find a way to get open market quotes added into the workbook.  So this year, so if a client requests an open market quote, I can look and see if I can find the different open market quote templates that we got last year so that you can see if there's any kinds of consistencies in terms of column headers and all that kind of stuff.  If we could create just like a general template where if a client does decide to go with an open market quote, our team could maybe fill out all of that relevant information and then have that injected into the workbook and then maybe have the batch status moved back up to consultation so that we can actually have the open market quote reflected in the workbook.  And we can see like this is these are the Questco master plans. These are the rates. And then these are the open market quote plans and then their rates.  And then the client can make their decisions. And then maybe that can be tracked through the workbook and client space now.

47:52 - Chad Gregory (LaunchPad Lab)
  And probably important then is like, ideally, if that if one of those plans gets selected. Did then through the workbook that the team doesn't have to then add it in PRISM, but it gets added in PRISM when it is imported to PRISM, when the workbook is imported to PRISM, right?

48:13 - Dimple.Desai
  That would be wonderful.

48:14 - Chad Gregory (LaunchPad Lab)
  Yeah.

48:15 - Ifat Ribon
  Yeah, I think that's generally how we were thinking about it. I think that that is in scope to be able to somehow get those open market quotes into the workbook so that you can use the rest of your process kind of in the same way, exactly like you described.  I think what we'll probably want to do some discovery on is exactly what you just listed, Dimple, is examples of those PDFs, those plans, and then, you know, working on how do we get, like, the data schema aligned.  Ideally, it's aligned to, like, how PRISM thinks about it so that, you know, Taylor is kind of working with that same schema.

48:46 - Chad Gregory (LaunchPad Lab)
  Exactly. Oh, I did have a, I guess my next question continues on the processor. You mentioned, like, the other documents that become part of the packet, Natalia, like the CBE, do those get generated here in Client Space, too?

49:14 - Natalia.Norena
  Yes. So, let me go. So, let me see if I do. I don't know if it's going to let me do it.  Because if I change it from this. So, let me see if I.

49:28 - Dimple.Desai
  Yeah, think if you change the status of the batch, the CBE link should populate on the right-hand side.

49:34 - Natalia.Norena
  So, if I change it on the status, it doesn't generate. So, once, like they said, the consultation is complete, so I'm going to go here, consultation complete.  And then it goes to the client election update. So, this is the other task. And this is what the CBE just generated.  So, this is, so, if I know what they elected. So, I'm going. To generate the CVE, this is what we send to the client.  Let me bring it here.

50:06 - Chad Gregory (LaunchPad Lab)
  Oh, and I also see that cost sheet link there, too. Is that just a link to?

50:10 - Natalia.Norena
  Correct. Okay. So these are, like, obviously, it's showing all the plans that we imported. So it shows the rates, how much of the employee contributions.  this is what, you know, once the client agreed, this is the document that we sent, reflecting all the benefits, and they sign on the second page.

50:28 - Chad Gregory (LaunchPad Lab)
  Hmm, okay.

50:30 - Natalia.Norena
  once, you know, if they sign, so then we create the CVE, we add it with the new rates, like, we make sure that everything here is accurate, you know, with the rate band, the plans that they, that the client elected after the consultation.  After we add it, we see that the CVE was created, and then send it to the benefit specialist to review if it's, if it's correct.  Oh, it's not, I have to upload the, I have to upload the CBA here.

51:04 - Chad Gregory (LaunchPad Lab)
  Yeah. Can I take a step back? So one question I had was, first, I guess, how many like plan options would a client typically see?  Obviously, you mentioned there's a ton on this.

51:21 - Natalia.Norena
  So yeah, we try to limit it, no more than five. We do have a few exceptions. They have up to eight, but very rarely.

51:30 - Chad Gregory (LaunchPad Lab)
  And then when they make their selection, they're choosing like a subset of that. How many different options do they typically present to their employees that would show up here, right?

51:46 - Natalia.Norena
  Correct. So yeah, they, yeah, the plans that they elected, they had to offer to all the employees.

51:52 - Chad Gregory (LaunchPad Lab)
  So you would have like three here on this one? Correct.

51:56 - Natalia.Norena
  So the medical, so the help will be three. police services of And. Well, So the only difference is if we cannot offer, like they say, the managers get a better plan than the regular employees, everybody has to be offered the same plan, otherwise it will be discrimination.  The only difference will be the contribution strategy. So how much, so if they want to have like a manager, so those are, so we create a CBE for each benefit group.

52:27 - Chad Gregory (LaunchPad Lab)
  Okay.

52:28 - Natalia.Norena
  So, so to answer your question, yeah, it will be like, so the primary group offer these three plans, and then you will have three more lines with, I say, full-time employees, another three lines with managers, employees, but the, the plans and the rates are the same.

52:49 - Chad Gregory (LaunchPad Lab)
  Yeah. Okay. Um, I was going to ask, I don't know if this is real. relevant or not, but is there, are there different things happening here between like health and dental and vision and, or is it all the same?

53:15 - Natalia.Norena
  It's the same, it's the same concept for different plants. So the, the medical, they do receive a renewal rate, same for the dental, the vision.  So it's the same concept for all the plants that they offer.

53:29 - Chad Gregory (LaunchPad Lab)
  Yeah. And the flow like handles all, all of these together.

53:35 - Natalia.Norena
  It's not like different flows or something.

53:38 - Chad Gregory (LaunchPad Lab)
  Okay. Anybody else have questions about this or the generation of this at all?

53:59 - Dimple.Desai
  After. After the CBE gets signed, I guess, what happens in PRISM?

54:08 - Natalia.Norena
  So when the signed CBE is uploaded here, so within the DocuSign, when the client signs it, it generates, so it goes to PRISM setup.  So the analysts get a task that is generated once it's uploaded, and they update PRISM with the new plans and the new rates.  Do they do that with an import, or? They do it manually. that's the one that's the analyst team, Cindy, so they update PRISM with the benefits that are reflecting on the signed CBE.

54:53 - Chad Gregory (LaunchPad Lab)
  Oh, and they create the cost sheet at that point, according to this flow? So...

54:59 - Natalia.Norena
  So... No, correct. So once they decide, we create the course sheet with the plans.

55:06 - Chad Gregory (LaunchPad Lab)
  Okay. What does that look like when you're doing that? See the link there on the right.

55:16 - Natalia.Norena
  So if I go to the course sheet, I'm going to create, so on the pay frequency, I'm going to go in Prism, and I'm going to see how they payroll.  And this is also something that can be added to the batch, if I'm not mistaken. Give me one second.

55:39 - Chad Gregory (LaunchPad Lab)
  Okay.

55:43 - Natalia.Norena
  No, it's not in the batch. It's in the renewal. Hold on. Yeah, on the payroll frequency, this is something that we add as well when we completed this.  And this is imported from Prism, too. So if they... they... They have, like, weekly, and they have, like, semi-monthly.  So when we create the cost sheets, we select what benefit group are we creating that. So I'm going to say the primary, and they get paid weekly.  So, and then if there's HSA information, then we apply, and then we generate the cost sheet.

56:30 - Chad Gregory (LaunchPad Lab)
  And this is how it look like.

56:33 - Dimple.Desai
  I think Conor has a question.

56:40 - Conor Hawes
  Yeah, in terms of going back and updating prison manually after the CBE is signed, I know that you mentioned for the case of the OMQ that they might be, like, inputting that new plan data.  But if it, if they were selecting, like, available plan. And more of like the happy path scenario, would the analyst be like having to re-enter all that data into PRISM, or would they just be like making a selection to say these are the plans that were chosen?

57:14 - Natalia.Norena
  If it's a new plan, they will enter from scratch. If it's an existing plan and they just updating the rates, if they go to, I'm going to say like the dental, they just update the rules.  In the contributions here. So they will, they will enter a new rate and they will update the information here or they, uh, that is not my world.  I just know very little about this. So, uh, no, it's not here. Uh, is it in the benefit rules?  That's what I went. Spencer, do you know? I don't remember this part. I, I, I know.

57:59 - Jagger Sturdivant (Questco Cos)
  Um, If it's an existing plan, they can use those import files that we talked about the other day. So those get generated, those get modified by BabyTaylor, and then there's an import screen in Prism that they use, and that'll change all the rates for all the existing plans.

58:17 - Conor Hawes
  Okay, so it's really just an OMQ scenario that would require...

58:21 - Jagger Sturdivant (Questco Cos)
  Yeah, the manual entry, yeah, it's just the OMQ.

58:24 - Conor Hawes
  Sure, okay, thanks.

58:26 - Natalia.Norena
  Thanks, Jagger. Let's see what he's my go-to.

58:45 - Chad Gregory (LaunchPad Lab)
  One of the things that we heard on Monday, Natalia, is about, like, when the DocuSign is voided, because it expires or something.  And I think basically today you just go in, you like go in and you rerun it somehow, is that right?

59:12 - Natalia.Norena
  Correct, we just changed the status again to DocuSignSend and send it again. So we just update the status for the process to start.

59:22 - Chad Gregory (LaunchPad Lab)
  Do you have to do something else to send it to? Or does that status do it for you?

59:30 - Natalia.Norena
  No, we have to apply it. If I apply it, hold on, is it going to let me? I don't know, because I haven't uploaded a CBE.

59:37 - Chad Gregory (LaunchPad Lab)
  Yeah. You see.

59:41 - Natalia.Norena
  Yeah, it doesn't, it generates it in this, and you have the option to say, that says send DocuSign. It's not letting me because I don't have a CBE uploaded here.

59:52 - Chad Gregory (LaunchPad Lab)
  Can you send that anytime? Yes. Obviously when the CBE is.

59:57 - Natalia.Norena
  Yes. Once the CBE is. It's uploading and, you know, finalize the benefits, give us the okay that everything looks good to send to the client, and it's uploaded here, you have the options, and you can send it as many times.

1:00:13 - Dimple.Desai
  We have some display rules on the back end that determine when the Send DocuSign button populates on the right-hand side under links, but we, the Send DocuSign button shows up when the batch status is either in CBE review ready or DocuSign sent, and if the DocuSign ever gets voided, then people can just click the Send DocuSign button again to just resend the DocuSign.

1:00:37 - Chad Gregory (LaunchPad Lab)
  Okay.

1:00:40 - Ifat Ribon
  And is the cost sheet and the benefit guide, is that like sent at the same time, or when do those get sent, and is that like also through here at all?

1:00:53 - Natalia.Norena
  Correct. So once the, uh, Sign CBE is uploaded, those two tasks generate simultaneously. One goes to... The other team that creates the benefits guide, and the other one goes to the team that creates the cost sheet.  So once the CVE is signed, it triggers all, like the task for the analyst to update Prism, the task for the team to create the guide.  So those get generated simultaneously at the same time.

1:01:21 - Ifat Ribon
  And then those two documents, are they sent to the client, like via email, or like also through an automated process, or after those are created?

1:01:33 - Natalia.Norena
  It really depends on the client. Some clients prefer for them to be email, and some other ones, we just go to the client documents, on the client documents, and we upload them here.  So anything, like benefit related, so the benefit. Benefits Guide, and any document. So this is the one, this is a test.  So a real client will have the 2026 Benefit Guide, but this is where we upload them.

1:02:11 - Ifat Ribon
  Okay. And is the CBE being signed a dependency to be able to create those other two documents? Or can they be created at the same time and right now we just have them sequentially?

1:02:23 - Natalia.Norena
  I'm sorry, I don't understand your question.

1:02:25 - Ifat Ribon
  Yeah, you said that once the CBE is signed and you get that back, then there's new tasks to create the Benefit Guide and the Cost Sheet.  And I wanted to confirm that the signed CBE, like is, the CBE is required to be signed before they could get started on those tasks?

1:02:41 - Natalia.Norena
  Or could those tasks be done? No, yeah, no, we need to get the approval from the client. So because the cost sheet and the Benefit Guide will reflect the benefits that that client is going to offer.  So if they don't sign it, we don't know what they are going to go with.

1:02:59 - Ifat Ribon
  Okay.

1:03:03 - Chad Gregory (LaunchPad Lab)
  And then how do the clients get access to those when they're all said and done? Are you just sending those to them?  Does the clients be sent it to them? Is it available to certain members in PRISM?

1:03:17 - Natalia.Norena
  So, yeah, usually the clients have access to PRISM and they have access to their documents.

1:03:25 - Chad Gregory (LaunchPad Lab)
  So they would go to a page like this? Yeah, they will go to this page. Got it.

1:03:30 - Dimple.Desai
  Yeah, so in the employee portal, there is this tab on a left-hand side column called documents. And like when they click on that, there's a client document section and they can see exactly what it is that we upload to this part of PRISM as a service provider.

1:03:45 - Chad Gregory (LaunchPad Lab)
  Got it. Okay. Where is this pretty much what they would have in there always? Like they would have the benefits guide?  Which, sorry if I'm not remembering this, but does the Benefit Guide have all of the other documents within it?

1:04:10 - Natalia.Norena
  Is that right? Wow.

1:04:13 - Chad Gregory (LaunchPad Lab)
  Or is it?

1:04:14 - Natalia.Norena
  When you say like all the, like the Benefits Guide is going to show the benefits that they currently offer.  So like the medical plan details, dental, vision, agency. That they pack. Correct.

1:04:26 - Chad Gregory (LaunchPad Lab)
  So then would they also see like the cost sheet here and, um, the CBE that they signed or no?

1:04:35 - Natalia.Norena
  No. That's the Benefits Guide. No.

1:04:37 - Chad Gregory (LaunchPad Lab)
  Okay. And then what about like the Chubb Welcome Kits here?

1:04:41 - Natalia.Norena
  I don't see that. Yeah. Is that, let me go to a real client, uh, to see what they show.  Uh, so if I go to the Benefits, okay. This client, this is a new client and this is a TSB client.  So hold on, let me get on my third client. Uh.

1:05:03 - Chad Gregory (LaunchPad Lab)
  I need to drop for another call, but please let me know if we need to schedule a follow-up with Anna when she's back in office next week.  I think that would be good. Yeah, I think this was really helpful and we can probably, sorry, I just saw Natalia, you showed this one real quick.  Yeah, this is a real point. In this case, they only have like the benefits guy. Okay.

1:05:33 - Natalia.Norena
  So, yeah. So, on the test client, we just have low documents left and right to see if you like them.

1:05:40 - Chad Gregory (LaunchPad Lab)
  Okay, great. I think that's good for now. We're going to get together with some of the team later today just to do a little check-in and plan some other meetings and stuff that we need.  I don't anticipate that we'll jump and grab you for like tomorrow or anything, Natalia, but... But if you're available later, I think you were great.  So Dimple will probably ask for you if we need you. But I appreciate it.

1:06:08 - Natalia.Norena
  I'm here to help. Have a great day, guys. Thank you.

1:06:11 - Dimple.Desai
  Thank so much, everybody.

1:06:12 - Chad Gregory (LaunchPad Lab)
  We'll talk to you soon. Bye, guys.

1:06:14 - Nikki Dow
  Everyone.