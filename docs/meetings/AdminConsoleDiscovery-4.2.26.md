Taylor v1 - User Story Discussion/Grooming Pt 2 - April 02
VIEW RECORDING - 42 mins (No highlights): https://fathom.video/share/ksCbrKuNMZT1u-VDBU4uUzAJBU-xvheg

---

0:30 - Chad Gregory (LaunchPad Lab)
  Hello.

0:35 - Jagger Sturdivant (Questco Cos)
  Hello. Hey, everyone.

0:58 - Chad Gregory (LaunchPad Lab)
  Books in. Howdy, Chris.

1:04 - Chris Whitney (Questco Cos)
  Howdy, Chad. A couple others joining here.

1:25 - Chad Gregory (LaunchPad Lab)
  So for those, the space fans, Nikki is down in Florida right now and got to see the Artemis rocket launch yesterday.  How cool was that?

1:40 - Chris Whitney (Questco Cos)
  Probably awesome. It was pretty cool.

1:42 - Nikki Dow
  I'm not going to lie, like, I didn't expect to, but watching it, I felt nervous. Like, I had, like, anxiety for the whole process.

1:50 - Chris Whitney (Questco Cos)
  I was following that mission since they launched it. They launched the idea, and it's so cool. Any of you seen Project Hail Mary?

2:02 - Chad Gregory (LaunchPad Lab)
  Oh my gosh, I'm seeing it on Saturday. I've been wanting to see it so bad.

2:06 - Chris Whitney (Questco Cos)
  I don't want to say anything good, bad, or indifferent. I want to say so much.

2:10 - Dimple.Desai
  It was such a good movie.

2:12 - Chris Whitney (Questco Cos)
  Yeah. Yeah.

2:13 - Chad Gregory (LaunchPad Lab)
  I read the book, so I know... Oh, you did read the book.

2:16 - Chris Whitney (Questco Cos)
  Okay, I read the book too. Did you know about the movie before you read the book?

2:21 - Chad Gregory (LaunchPad Lab)
  No. I read it like probably four or five months before the movie was announced. Okay, good.

2:27 - Chris Whitney (Questco Cos)
  Yeah, so I didn't even... I knew Ryan Gosling, which messed me up a little bit because I had that image, but I didn't want to have an image of anything.  I didn't want to have an image of Rocky, of anything, but yeah. Yeah. Have fun. I'm excited.

2:45 - Chad Gregory (LaunchPad Lab)
  I've never cried over a rock before, but...

2:48 - Chris Whitney (Questco Cos)
  It's movies.

2:50 - Chad Gregory (LaunchPad Lab)
  I keep hearing that people were crying throughout the movie. I'm interested to see that, how that impacts me, but...  Not usually a movie crier. We'll see. Oh, the book.

3:02 - Dimple.Desai
  Okay, well, when we check in next week, it'll be nice to hear. Yes, talk to me Monday whenever we're talking, yeah.

3:10 - Chris Whitney (Questco Cos)
  If you don't cry, we're going to all think you're completely emotional.

3:13 - Chad Gregory (LaunchPad Lab)
  I'm a robot. Yeah. could be. All right. So today we wanted to, or this call today, we wanted to focus on sort of the items around the vendor.  What? I keep calling it vendor. The admin console. Um, so there are six items in the scope of the SOW that are, I mean, they're not really fleshed out fully or anything, but we want to get a little bit more ideas around.  Um, and basically I'll just hit these real quick, but one is role-based access control. Two is a dashboard for the renewal status.  Um, three is rate book management. Four is the OMQ Plan Data Entry and Management. Five is audit result review and exception.  Is it notification or monitoring? I think it's monitoring. And then the last one is reporting on the renewal pipeline and workbook generation activity summaries.  So just off the bat, the thought process that we've discussed in a couple of calls is trying to keep this console to be, you know, not where the team working on the renewals is necessarily working, but more of like, yeah, that like admin tool behind the scenes.  And the first item that jumps out to me that's maybe, you tell me what you think, if this is uncomfortable.  I I'm congruous with that thought or not, but the OMQ plan data entry being there feels a little weird based on what we talked about with Natalia earlier this week, but I could be misunderstanding that or this is really the only place to enter that.  Does anybody have any thoughts on that item in particular?

5:32 - Chris Whitney (Questco Cos)
  How does it happen today? I don't know what OMQ even stands for, for the record.

5:38 - Dimple.Desai
  After, it means open market quote, and I guess after we talked to Natalia about it, I wasn't aware of it, but it seems like that process is completely outside of client space.  If a client requests an open market quote, somebody will, somebody from benefits brokerage. Which will go and get like up to eight different plan information, and then like they'll share it with the client, and then the client will decide if they want to go with an open market quote.  And then once they do that, the rest of the process just happens outside of client space. And then after, if it's a new plan that's not in PRISM, a benefits analyst will create the plan in PRISM.

6:27 - Chad Gregory (LaunchPad Lab)
  And the following year, when it's renewals time, we'll do an OBP import to then get that plan data from PRISM into client space into the benefits batch.  And so then after the first year, then the open market quote plans will be in client space. Right.

6:49 - Chris Whitney (Questco Cos)
  Jagger, what was the thought about how Taylor replaced the open market quoting?

6:54 - Jagger Sturdivant (Questco Cos)
  It doesn't replace it. We should be able to add those into the workbook. Because right now they're skipping over the workbook and manually entering those into the CBE.

7:05 - Chris Whitney (Questco Cos)
  So open market quoting happens because we can't quote them on our master for whatever reason. So we go to the open market.  And today during renewal or onboarding a client, all that happens from the agency. Goes out, gets the quotes, does all that.  And our vision here is that Taylor, when it produces a workbook, would have a mechanism of getting the open market quote data into Taylor to generate the workbook.  Right.

7:40 - Chad Gregory (LaunchPad Lab)
  And it seems to me that the scope right now is there's a place in the admin console to enter that data, whether that's like manually entering it off of the PDF or whatever they have, or like putting it into a CSV and then importing it.  Either, or there could be a form or an import, but that part does feel like it's a little bit outside of like the admin scope, but, you know, that may just be the place that it has to be, you know, for Taylor V1.

8:22 - Ifat Ribon
  I think, sorry, Chris, go ahead.

8:26 - Chris Whitney (Questco Cos)
  I don't even feel like this, this isn't, we have to solve this in this project. This is less of a Taylor problem and more of a Questco.  What are we doing? On storing the open market quotes, and there's a lot of work we're doing around that world.  So just so you all understand, I think it's irrelevant. We quote open market for benefits and we quote open market for workers comp.  And we are not effective at all as a company in that. We do it manually and we do it in Excel and it.  It hurts us on our speed to quote and our sales velocity, and it hurts us in the fact that we have errors.  And we actually have this whole other world that Kim and I are working on and others where we're trying to build a bunch of efficiencies around that.  And actually, this conversation even ties into how we use Salesforce and how we use client space as well, because it's our vision that we would be leaning in more to Salesforce because we're right there.  We're doing all of the quoting and pricing and opportunities in Salesforce already. So it's a much larger question. Yeah, my gut says I don't want to have the pricing team, the agency work in an admin portal.  I think you're right. But the question is, we still have to have it somewhere and we still have to get it.  So where is that somewhere and where would we get it right now? Now, in the last year, and for current clients coming in, just stays where, Jagger, do even know, do they even have a shared SharePoint?  Or does that all stay in Pipedrive and the agency just works on it?

10:10 - Jagger Sturdivant (Questco Cos)
  I think they upload it to client space, but I'm not 100% sure.

10:14 - Chris Whitney (Questco Cos)
  Yeah. Dimple kind of feels like there's an action for us to chase that process down and get that into client space.  And then we can grab that from Taylor. We can grab that into Taylor.

10:33 - Ifat Ribon
  I guess, or I guess if putting it into client space, like, would that still align with kind of the overall philosophy or goals around maybe reducing actual benefits data in client space?

10:46 - Chris Whitney (Questco Cos)
  We still want to keep our benefits. We still need to keep all client documents in our client collateral and client space.  So keep in mind that we are our view of the world technically. Basically is that client space is our client and operations CRM and Salesforce is our sales CRM.  Now those probably should be one, but they're not right now. And we still need to house the documents. Just like the workbook and the CBE will ultimately live there long term.  We might work on them and iterate through them at SharePoint. When they're executed, they will be stored in the client documents.  So I don't think it disrupts that plan. I don't think it disrupts that plan. Did, Jagger, was there ever a perspective on it living in client space or not?

11:39 - Jagger Sturdivant (Questco Cos)
  Well, I don't know, honestly. But it makes sense to me that they would be in client space. It's a Betty ask, right?

11:48 - Chris Whitney (Questco Cos)
  It's a Betty discussion. Betty runs the, so we call the, Bennett, we call the world, the business function that is in charge.  of both quoting, open market, and underwriting. So underwriting would be after we've got the quote and it's good, we actually implement.  We have to underwrite that to make sure that's all accurate when we go into implement. We call that the benefits agency.
  ACTION ITEM: Align w/ Betty on OMQ docs in Client Space; then sync w/ Conor on Taylor pull - WATCH: https://fathom.video/share/ksCbrKuNMZT1u-VDBU4uUzAJBU-xvheg?timestamp=738.9999  And the business stakeholder that's above the benefits agency is Betty. And I'll give you her last name in a second.  Somebody has it.

12:23 - Dimple.Desai
  It's Lee, L-E-E. Thank you.

12:29 - Chris Whitney (Questco Cos)
  This feels like, this feels like a critical item, table for this discussion, Questco takes the action, has a discussion with Betty, and figures out what we think the right positioning is on this.

12:44 - Chad Gregory (LaunchPad Lab)
  Okay. That's totally fine with us.

12:47 - Chris Whitney (Questco Cos)
  Does anyone disagree with that? Questco's team?

12:55 - Dimple.Desai
  No disagreement here. Me either.

12:57 - Jagger Sturdivant (Questco Cos)
  So like a...

12:59 - Conor Hawes
  Okay. A tenet of date that we should put on that in terms of like a target for resolution.

13:06 - Chris Whitney (Questco Cos)
  Every time that you ask me that, I'm just training you on the way I work. Every single time you ask me that question, I'm going to come back and say, when do we need it by so that we can stay on track of the current schedule?  So that's my question back on that, Conor. When do you need it to turn it back?

13:26 - Chad Gregory (LaunchPad Lab)
  That's good.

13:27 - Chris Whitney (Questco Cos)
  And that's going to be my answer every time.

13:32 - Conor Hawes
  That's a fair question. Why don't we, we can chat about that as a, like, We'll work on it quickly.

13:40 - Chris Whitney (Questco Cos)
  That answer might dictate how we solve this too. So that's my follow-up to that. Okay.

13:48 - Conor Hawes
  Yeah, we'll communicate that async.

13:53 - Chris Whitney (Questco Cos)
  Awesome.

13:54 - Chad Gregory (LaunchPad Lab)
  And I'm just putting it in our board so we have an item for it. Okay. Okay. Maybe the next place to start on the admin console is, in general, the roles that we expect to be in here, given the different pieces to this console.  And maybe OMQ could be, like, a separate thing, potentially, I guess, here. But being able to, you know, see a dashboard of the renewal status of everything, being able to tackle rate book management, which is something I want to talk about.  And then generally, kind of, like, the audit and exception monitoring and the pipeline reporting. Do we see maybe that there's, like, I don't know, maybe there's, like, three roles there.  There's, like, an overall admin. There's, like, somebody who might be doing rate book stuff. And then there's... Like the technical person who could be helping sort of debug or manage anything that gets stuck or something like that.  Are there any others that I'm not thinking about or do any of those kind of not really make sense?  Or is that too hard to think about right now?

15:28 - Chris Whitney (Questco Cos)
  I have a perspective, but I'd love to hear my team's perspective. First of all, my perspective is we need to talk about each one of those to make sure we're aligned, that those should go in the dashboard.  And I think that probably has to happen first. And then I think it's probably easier to talk about what the rules should actually be.  It'll be really easy. Do we do anything in client space today, team, to differentiate who in operations can see what or...  Is client space pretty much wide open? You're in benefits, you're in tech, you're CSM, you can poke around all day long to see everything in client space, right?

16:10 - Dimple.Desai
  No, we have different user roles that lock down access for specific people. Okay.

16:16 - Chris Whitney (Questco Cos)
  Is it access to view or is it access to be able to do stuff? I know we have admins and things like that, but is there some view access to Dimple?  There is.

16:26 - Dimple.Desai
  Okay. Okay, right on.

16:27 - Chris Whitney (Questco Cos)
  Yeah, we should probably talk about each one of those items and make sure we're relying on what those actually are.  And then I think that's an easier question. Great. Okay.

16:39 - Chad Gregory (LaunchPad Lab)
  Okay, so thinking about the general dashboard, this is probably where the people land when they log into the admin console.  It's got essentially in my vision, in my head, it's a table of all of the renewals that have come through.  Maybe. There's like a filter to filter out just to just show active ones that by default, but I imagine there are different columns for things like the client name, the batch ID, the status of things, maybe like the last step that it hit, and then a way to get into each of those items to do like the other detailed items for those.  In general, how does that sound in terms of what you were thinking dashboard-wise?

17:38 - Chris Whitney (Questco Cos)
  Did Spend, Dimple, is this what we developed that didn't get used last OE in Spencer's dashboard?

17:48 - Dimple.Desai
  Yeah, yeah. We had a full dashboard we developed that differentiated between Questco Master Medical and client-sponsored plan. That showed every single batch with its status and a bunch of other information like client-specific information, what state the client was in, that kind of stuff.  We have that available and we built that off of a Questco master tracker that they ended up using instead.

18:24 - Chris Whitney (Questco Cos)
  But you have to think that we're not going to be using the module, so there's not going to be imports and the plan where the CBE, well, we'll know when the CBE is getting issued for signature, but where the steps of the CBE are will be done in Taylor.  So how we'd have to either A, integrate back to client space, which we are everywhere on this project, not a problem, or that would be something externalized and we would manage it natively and tailor, i.e.  admin dashboard. Do you have a perspective? Jagger, you have a perspective on where that should be?

19:12 - Jagger Sturdivant (Questco Cos)
  I mean, I feel like Taylor should be updating client space, what the status is anyway. So if client space knows what the status is, we could also just add in any other information, just reuse the dashboard in client space.

19:25 - Dimple.Desai
  And isn't the goal to have all client specific information stored into client space?

19:29 - Chris Whitney (Questco Cos)
  I'm kind of there too. I'm of under the, I think, I know for me, when we scoped the project, I put the admin dashboard for me in a very distinct box.  And I also know that being very candid, Karen, who's no longer with us, she had the admin dashboard very much in, I need some reporting.  And there's a lot of like visibility in reporting, but I think we feel we could get that from. Client space.  Yeah, I would imagine. I'm kind of on the same token with the team here that says it'd be better for us to develop your input into that and develop the workflow and orchestration and have us build the dashboards and feed and update the status for that and not put that in an admin dashboard.  So can I ask, is the purpose of this admin dashboard just to basically have visibility on every single batch throughout the renewals process?

20:33 - Chad Gregory (LaunchPad Lab)
  Mostly. your primary purpose? And then the other two pieces were rate book management and OMQ plan data entry. But basically everything else was being able to see all the renewals, being able to audit how those were going and essentially, yeah, like get reporting on where everything was.

20:59 - Chris Whitney (Questco Cos)
  So. So, OMQ, we talked about a path to an answer there that we need two weeks ago. We talked about the enrollment status, and we have a perspective, which we think.  And the third one was rate books. Yep.

21:20 - Chad Gregory (LaunchPad Lab)
  What's that? What does that mean? This is my biggest question of the day, I think. What does that mean to Dimple and to Jeff?  I don't know.

21:31 - Dimple.Desai
  I do know.

21:33 - Jagger Sturdivant (Questco Cos)
  So, every year we get new rates from Aetna, from Blue Choice, from Kaiser, and Taylor needs to know what those rates are so that it can display those to the client.  We also have bands for each client, and those are assigned by the carriers as well.

21:49 - Chad Gregory (LaunchPad Lab)
  Those are not in Prism, though?

21:52 - Jagger Sturdivant (Questco Cos)
  Not yet, because those are the new rates that they're going to be doing active the year that they're renewing for.  You have to like do it.

22:00 - Chad Gregory (LaunchPad Lab)
  Annually. Go, go. Exactly.

22:02 - Jagger Sturdivant (Questco Cos)
  Yeah, those are signed annually.

22:04 - Chris Whitney (Questco Cos)
  How did those get added to, in the benefits module world, how did those get added into the workbooks?

22:12 - Dimple.Desai
  We had to import them into space. Because we imported all of them. And Chris, if this gives you context, this is what caused such a delay last year was because we weren't receiving rates from carriers until, I think, beginning of September.

22:28 - Chris Whitney (Questco Cos)
  But that was, was it that problem plus client space choked on the rates when they got them, Dimple? Or was it pretty much that was the primary source of the challenge, was just the delay in getting the rates?

22:43 - Dimple.Desai
  You're going to ask me. I think that that was the primary delay. The secondary delay was that we were doing our OVP import process backwards.

22:54 - Chris Whitney (Questco Cos)
  Did those, if we hadn't made the decision to stay with client space, did we now... Would that make us have to do an OBP import because we're bringing those in?  We don't want to do that, right? We would have to do an OBP import every single year before we renew batches.  We don't want to do that. We don't want to do OBP import and we don't want to do batches, right?

23:20 - Dimple.Desai
  We don't want to do OBP import. That's correct. Batches we have to.

23:26 - Chris Whitney (Questco Cos)
  Is that the status? Is it batch the workflow and the status? So batches we have to do because it's keeping track of where we are in OE.

23:34 - Dimple.Desai
  It's keeping track of like if the client's in consultation status, if the docusign has been sent, if it's pending activation in Prism, that kind of stuff.  And that's also where, well, right now where the workbook gets generated. And I think Anna's goal is to have everything still housed in the batch and primarily use Taylor to just help automate all of the.  processes that occur inside the batch. Now, is that different from the conversations that you guys have had before?

24:16 - Chris Whitney (Questco Cos)
  I don't think we were in the depths of this, which is a good conversation. I don't think we were this detailed, which is okay.  Yeah.

24:26 - Chad Gregory (LaunchPad Lab)
  I think Dimple, I don't.

24:29 - Dimple.Desai
  So the visualizations that I created, there's one for the BSR, and then there's one for the batch. I got in touch with Anna before she went out of office, and it includes specific parts of the batch process that she's hoping that Taylor will help automate.  Does that help at all? Or is there something else that I can do to help?

24:55 - Chris Whitney (Questco Cos)
  I think for me, I feel like that. What would help the team in terms of understanding more than the rate book question we're asking?  Absolutely, 100% yes, right? I don't know. I looked at the batches differently. Don't think what I'm saying on the batches shouldn't use the batches.
  SCREEN SHARING: Chad started screen sharing - WATCH: https://fathom.video/share/ksCbrKuNMZT1u-VDBU4uUzAJBU-xvheg?timestamp=1511.595927  So sure, that would help. The question on the rate books is, do we want to leverage client space or do we want to create an externalized process for Taylor to collect the rate books?

25:26 - Chad Gregory (LaunchPad Lab)
  Yeah. And I think, like, extrapolating on that, is that the only externalized piece for Taylor that we need based on some of the other conversations or thoughts earlier about, like, seems like everything else might just be in client space?

25:45 - Chris Whitney (Questco Cos)
  OMQ. Except for, yeah, OMQ.

25:48 - Chad Gregory (LaunchPad Lab)
  OMQ and the rate books.

25:53 - Dimple.Desai
  In terms of the imports that we used to do in client space for the benefits model, of telemetry only theuccane kelp, and  For outside data that may not have existed in PRISM, if there's any kinds of new benefit plans, we would have to import the benefit plan information along with the rates into client space.  I think that's the part we want to skip, though.

26:16 - Jagger Sturdivant (Questco Cos)
  We don't want to have do that.

26:18 - Dimple.Desai
  Okay.

26:18 - Chris Whitney (Questco Cos)
  Have it come from PRISM. So that, for the plan detail, it'd have to be in PRISM and take it from PRISM on new plans?

26:26 - Jagger Sturdivant (Questco Cos)
  Right. Or no. No, that's right. Yeah.

26:31 - Chad Gregory (LaunchPad Lab)
  Sorry, that's for new plans only. Otherwise, like, it exists in PRISM, you're just changing the rates on those plans, right?

26:39 - Jagger Sturdivant (Questco Cos)
  Right. Yeah. Okay. I feel like even the rates don't need to be in client space, because even if they were in client space and we pulled from there, we still need to audit them.
  ACTION ITEM: Align w/ Anna on PRISM as rate source; then sync w/ Conor on Taylor pull - WATCH: https://fathom.video/share/ksCbrKuNMZT1u-VDBU4uUzAJBU-xvheg?timestamp=1609.9999  So Taylor still has to know what the right rates are.

26:53 - Chad Gregory (LaunchPad Lab)
  Yeah.

26:53 - Jagger Sturdivant (Questco Cos)
  So you might as well just have Taylor do the rates. Why aren't the rates...

26:57 - Chris Whitney (Questco Cos)
  Why aren't the rates... Something... know. price... you. Why don't we solve that problem in PRISM? If the PRISM houses the plans and we get new rates, why don't we solve that problem in updating PRISM with the rates and then having Taylor go get the right plans with the right rates?  Is that what they're doing today, Jagger?

27:18 - Jagger Sturdivant (Questco Cos)
  Could be doing. Yeah.

27:21 - Chad Gregory (LaunchPad Lab)
  That is the right way to do it, I think.

27:25 - Chris Whitney (Questco Cos)
  Right. You're saying, because we could absolutely, we haven't had them in Portland Scope, we could absolutely build whatever we want to build to house rates.  Right. We can build a NoSQL or we can build a SQL or we can build a backend or like talk about these paths.  But like the question is like, if we're housing the rate, if the source of truth for the plan data is PRISM and we're talking about updating rates for PRISM for those same plans, it seems like that needs to be a dependency for us to have Taylor even more congenerate.  The rates, generate the workbooks.

28:04 - Jagger Sturdivant (Questco Cos)
  Yeah.

28:09 - Chris Whitney (Questco Cos)
  Does this have to be validated with Anna?

28:15 - Chad Gregory (LaunchPad Lab)
  Probably a good idea. does, because I currently don't really know how Benefits puts plan data information on when they receive new plans.

28:22 - Chris Whitney (Questco Cos)
  Let's take the OMQ action and the rate book action. Yeah.

28:37 - Chad Gregory (LaunchPad Lab)
  Browser's frozen up, apparently. Come on. That is helpful, though. I mean, I think this has been a good thought process on the admin console.  don't think we have answers on any of this, but it's a good discussion.

28:54 - Chris Whitney (Questco Cos)
  It is pushing us in the right direction.

28:58 - Chad Gregory (LaunchPad Lab)
  So you all didn't see the admin.

29:00 - Chris Whitney (Questco Cos)
  Console as a cue for if Taylor coughs up, if Taylor doesn't process a workbook, if there is an error in generating an input or generate processing for signature or API calls, you did not see the admin portal as an area for that.

29:27 - Nikki Dow
  Yeah, actually, I wanted to ask about that because that was like my read on some of the requirements we had.  If I recall correctly, there were maybe also some call outs to like create remediation tasks in client space based off of like a failed run in Taylor.  So I guess that to me, that kind of like poses the question, like, do we need to see those failed runs in an admin portal at all?  Or like, should we just be relying on them? Those tasks in client space.

30:06 - Chris Whitney (Questco Cos)
  Well, we need to see them somewhere because they failed them. We need to have somebody action, right? So we need to know how Taylor's processing.  The question is, I think your question is, do we feel that that should be an admin portal? Or do we feel that that should be in client space?  Or do we feel that that should be somewhere else, natively, Azure, GitHub, wherever, right?

30:31 - Conor Hawes
  Yeah. Yeah, think that's a valid question. And I think there might need to be a distinction made where it's not necessarily like everything would go to client space, like kind of making the distinction between like a server error and a client error.  Like if there's an issue with rates, then like someone would need to go in and review those rates. But if the job failed because...  Because... The client space was down. Like that's, there's nothing within like someone on the benefits team could do to troubleshoot that.  Like that feels to me, just like coming in a little bit more green on this project, more like an admin console or potentially, as we mentioned last week, like an Azure DevOps, you know, like ticketing kind of support flow.  So that would be more like tech administration of the platform of Taylor versus like administration of the process of renewal.

31:31 - Chris Whitney (Questco Cos)
  I'll tell you, I'll tell you this for sure. If we're not going to do the rate books in an admin portal and we're not going to do OMQ, then we 100% won't just build a separate portal for that problem.  You're absolutely correct. Totally correct on that. And I think you're right that there has to be a distinction between issues that can be addressed by the operations team and issues that need to be addressed that are technical issues as a result of Taylor not being able to process.

32:00 - Nikki Dow
  Yeah, and for those, like, technical issues, we also could, rather than an admin console, just be looking into, like, Azure Monitor Alerts.

32:10 - Chris Whitney (Questco Cos)
  I don't know what you think about that as a solution. Yeah, I'm going with you on that. I'd rather do, I'd rather do technical in the tooling that we're going to use, Azure or GitHub, right?  Like, we should be, or there's a million ways to do observability in Azure, right? We 100% should probably do that for the work queue on the technical issues over an admin portal for that.  Okay.

32:43 - Chad Gregory (LaunchPad Lab)
  Jagger, what do you think about that?

32:45 - Chris Whitney (Questco Cos)
  Does that make sense, what we're saying here? Yeah, that does make sense. Do you have a perspective on if you think that that should live in client space?  I think that who's going to be solving those issues? It's going to be you. It's going to be our team, our technical team solving.  And those issues. And I don't need that. I don't, I almost kind of feel like we should take out client space in that technical side so we don't have to deal with the development for that thing when we could just do it natively right in Azure.

33:14 - Jagger Sturdivant (Questco Cos)
  Yeah, because I don't look at my client space tasks. I'm not going to see those.

33:26 - Chris Whitney (Questco Cos)
  It's just a waste of time to develop against that when we can be right there, right in Azure, firing off what's happening with the service, with all of the out-of-the-box functionality that we get in Azure.

33:38 - Chad Gregory (LaunchPad Lab)
  Do you think, this is kind of moving on, but do you think like all the other reporting that Karen was referencing is already there in client space or would, would be buildable there in client space?

34:03 - Chris Whitney (Questco Cos)
  Uh, I will tell you what, uh, I think it has, I think it has to be, I don't, I don't see if there was a nuanced report that we were struggling in client space, I don't see us, I don't see the value in creating an admin portal just for that.  We have another reporting solution, by the way, uh, we have another reporting platform, which we have, which, which we have called Q Insights and it's a new platform, but I do not think it's wise of us to solve reporting in another tool.  should live somewhere in an existing Questco world. So client space first and second being our Q Insights platform.

34:52 - Chad Gregory (LaunchPad Lab)
  Got it. Based on this, and I know we need answers from Anna and Ben. Ready next week, but it feels like there's probably kind of a high bar to clear for Rapebooks and OMQ to get their own admin console as well.

35:16 - Chris Whitney (Questco Cos)
  I think we need to answer the Rapebooks and OMQ question because I know that there's scope and sprints in the statement of work and time and designers here for this very thing.

35:28 - Chad Gregory (LaunchPad Lab)
  And we might be repurposing, we might be making a call to repurpose that elsewhere.

35:33 - Chris Whitney (Questco Cos)
  So I think it feels to me like the admin tech issues is the easiest thing. feels like Questco has to answer the OMQ and Rapebooks and what our position is, where that's going to be.  And then we can repurp on the right way to take the admin console forward or do a change order and put this money back into the right development.  Yeah.

36:00 - Chad Gregory (LaunchPad Lab)
  That makes a lot of sense to me.

36:02 - Chris Whitney (Questco Cos)
  Okay.

36:06 - Chad Gregory (LaunchPad Lab)
  One more thing before we put a pin on that. Jagger, is there anything else that we're missing on the vision there that you think we need to get from Anna or that we originally had scoped out for the admin portal concept?
  ACTION ITEM: Define error routing (Azure vs Client Space) w/ Conor; then set Azure Monitor alerts - WATCH: https://fathom.video/share/ksCbrKuNMZT1u-VDBU4uUzAJBU-xvheg?timestamp=2180.9999  That was literally my next question. Not that I can think of off the top of my head.

36:26 - Chris Whitney (Questco Cos)
  Yeah. Yeah. Yeah. Well, there'll still be work, even if we didn't do an admin consult, there will still be work to determine, like, the approach to those different exceptions or errors.  Oh, yeah.

36:43 - Chad Gregory (LaunchPad Lab)
  Whether they get sent into Azure or whether they get, you know, which ones go to Azure, which ones go to client space to create time.  And you're going to have to build, you're going to have to build the Azure, I think it's, I think you're going to use App Insights for this.

36:58 - Chris Whitney (Questco Cos)
  I think that's the Azure service. That monitors like the failures if you built functions. But anyways, you're still going to have to do the work on Azure side and you're going to have to do the work on the stuff that has been business facing to integrate into client space.

37:13 - Chad Gregory (LaunchPad Lab)
  So there's still work here, but I don't think we're going to need to publish and host our own front end unless something comes different from OMQ and Rayplex.  I agree with that. Saves us some design time potentially here then, but okay. What other thoughts does the team have on this from my end?  Is there anything else, LPO? And that was the main purpose of this call was talking through all of that.  So I don't want to like dive into too much more if, but I was going to ask like from Connor, because you're digging into prisms.  I don't know if you have any questions that have come up through the course of the day or anybody else as you've been working while we have folks.

38:15 - Conor Hawes
  No, I'm looking at the different endpoints that Dimple said over.

38:20 - Chris Whitney (Questco Cos)
  Do you still feel like that's a great site, Conor? Yeah.

38:26 - Conor Hawes
  Yeah, it looks good to me. Right on.

38:30 - Chris Whitney (Questco Cos)
  Maybe we're just used to less.

38:33 - Jagger Sturdivant (Questco Cos)
  No, just wait until you find an endpoint that's not been updated.

38:36 - Chris Whitney (Questco Cos)
  I think we need to ask him, Jagger, that's a better question. We need to ask him after he's hammered against the actual API is the better ask.

38:47 - Chad Gregory (LaunchPad Lab)
  Good point.

38:48 - José Blanco
  Yeah, it's when you try and it doesn't work how it says it does. That's when you, you know.

38:54 - Conor Hawes
  Yeah, come Tuesday, I'll let you know.

38:58 - Jagger Sturdivant (Questco Cos)
  I think I'm just used to their old. Old swagger where you could test in the browser. And when they took that away, I was really sad.  So now I'm just salty about it.

39:08 - Chad Gregory (LaunchPad Lab)
  We have time with Anna scheduled Tuesday morning. I also scheduled next week some time for like our weekly grooming.  Hopefully that'll maybe be the spot that we use weekly. But the goal for next week will be kind of to review descriptions of or like acceptance criteria for tickets as we have determined at that point and likely kind of the plan.  Chris, I just wanted, since I have you here, I know you're aware that access to the API is delayed right now until Tuesday.
  ACTION ITEM: Prepare alternate PRISM test env w/ real client data for Conor by Apr 7 - WATCH: https://fathom.video/share/ksCbrKuNMZT1u-VDBU4uUzAJBU-xvheg?timestamp=2392.9999  So it's probably pushback or like planning of things a little bit there. So I don't know that I'll have that all figured out for you on next Wednesday's call, but definitely next week.  All of that figured out for you.

40:03 - Dimple.Desai
  So are you guys leaning towards having access to the alternate testing environment that I was talking about? I can try my best to get that environment ready by Tuesday.

40:18 - Chad Gregory (LaunchPad Lab)
  Yeah, I think that's fine with us, and I think it makes sense.

40:23 - Chris Whitney (Questco Cos)
  The story is we need real test client data, right, Dimple, not just the placeholders that we were going to give them for short term time.

40:33 - Dimple.Desai
  Yeah, because we took a look at our test clients, and their benefits information isn't the best in the test clients' databases.  So if you guys are testing out the API, you're going to get a ton of errors.

40:48 - Chad Gregory (LaunchPad Lab)
  Okay, Dimple, if you feel like it makes sense for us to help jump in and schedule time with Anna or Betty on either of these items after maybe you do  If pre-chat with them or something, let us know. We've got plenty of time, too, so happy to jump in and chat.  Thank you.

41:11 - Dimple.Desai
  I appreciate it.

41:14 - Chad Gregory (LaunchPad Lab)
  Anything else I'm forgetting or missing here? Great. Thanks, Chad. Yeah, I know you guys are out tomorrow. Have a good long weekend, and we'll see you next week.  Thanks. Bye. Bye, everybody.