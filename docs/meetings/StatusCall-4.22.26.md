# Questco - LPL: Weekly Status Check-In - April 22, 2026

**Duration:** 34 mins
**Attendees:** Chad Gregory (LaunchPad Lab), Anna Fiske (Questco), Dimple Desai (Questco), Jagger Sturdivant (Questco), Chris Whitney (Questco), Conor Hawes (LaunchPad Lab)

---

## Transcript

**@0:00 — Dimple Desai (Questco):** It a lot of fun. Yeah, my sister looked beautiful.

**@0:05 — Chad Gregory (LaunchPad Lab):** Love to hear it. Perfect. Hey, Anna, how are you doing?

**@0:11 — Anna Fiske:** Good, how are you doing?

**@0:13 — Chad Gregory (LaunchPad Lab):** Doing good. Busy, keeping busy. You can tell maybe from my voice that I'm nursing this cold, blaming the nephews for getting my daughter sick and then me sick, but we will make it through it.

*[SCREEN SHARING: Chad started screen sharing]*

Let's see. Pull this up. Okay. I want to get through kind of a lot today, if we can. First, a couple notes on work progress.

Chris gave the approval on the documentation that Nikki sent over, which was great. Set up the application stack. GitHub repository is ready. Almost. Almost. Almost. Almost. Almost. We're done with the Azure hosting environment setup, which if we have a little bit of time, we can demo at the end of this, but also Nikki can send over a recording.

We're in progress on the Prism HR API integration, the Prism to workbook mapping. We're essentially done with the benefit guide spike to determine that whole approach. We want to talk with you guys about that as soon as possible, whether that's on our grooming session Friday or if we have other time, which meant also that Jose has moved forward on one of the parsing tickets for the CBE and also the cost sheets. I think you started today, Jose, which I didn't include here, and then Nico's been working on the admin console designs, which you saw a little bit of on Monday, and we're continuing to adjust based on feedback there.

And some of the questions that we have below, we have a number of questions here for you all. So let me just hit on the rest of the agenda and then we'll jump back up to this.

So these questions are mostly around like the process of replacing the apply plan group process that's in client space and how that kind of fits into the flow of Taylor. But then beyond those questions, I wanted to prep us on a little bit of the admin console scope discussion that we've been having, which I think leads into a separate call. But if we can discuss a little bit of this, we will today. And then I think in general, we've got like three big discussions open right now that we need to have and we can use the grooming session on Friday for maybe one or maybe multiple.

These, if you all have the ability to extend that call, we have an extra hour. It looks like we also have eight o'clock central tomorrow morning open if we want to grab that for one of these, but we'll get into these in a second.

And I think the biggest thing to talk about today is, are these questions here? And again, essentially the discussion here is, how do we get the list of renewal plans that need to be offered to a client? And like, you know, replacing the apply plan group process that is, is there in client space. And Connor, you wrote out all of these like specifics. So I don't know if there's a place you want to start or a document you want to pull up to get into this, these questions.

**@3:57 — Conor Hawes:** I mean, I think maybe the first place to start is just understanding if the intent is to have the list curated by an employee or filtered by some sort of rule set.

**@4:15 — Anna Fiske:** When you say employee, mean somebody at Questco or like a renewal rep deciding what goes in? Yeah, like someone responsible for that particular client. Okay, Jagger, were you going to say something?

**@4:29 — Jagger Sturdivant (Questco):** I mean, I think it should be a combination of both. I think we just have like a very generic rule set that every client follows, and then an employee can go in and override certain things if they need to.

**@4:46 — Anna Fiske:** That's how BabyTaylor is now, right? They can select what gets added? Well, we did that in Client Space. Oh, right. I'm thinking after that, yeah.

**@5:05 — Chad Gregory (LaunchPad Lab):** So today with Client Space, there's like the apply, what's it called? The apply plan group, which they get a list and then they curate that a little bit after it's on Client Space. Is that what you said?

**@5:25 — Jagger Sturdivant (Questco):** Well, yeah. I mean, right now we would curate it and then, because we would generate the workbook and then the renewal rep would just have it right. And if something was wrong, they would have to come back to us so that we could edit it.

**@5:50 — Chad Gregory (LaunchPad Lab):** So, Conor, thinking about that and thinking about what Jagger just said, if we had a rule to generate a list, or a set of rules to generate a list, and maybe it, like, let's just say it's as simple as every plan, let's just say that for right now. So every plan shows up in the workbook, and then the rep looks at it, and they say, oh, we actually want to remove these 10 things. They would, Jagger, in the world that you're proposing, they would still have to go to you guys, right, to then go into, like, the admin console, like, this would be an admin console thing to remove plans. Right, yeah.

**@6:46 — Jagger Sturdivant (Questco):** Yeah.

**@6:49 — Anna Fiske:** And a general rule of thumb is that we want to offer everything, even if they don't currently have it, we want to show the price and the breakdown of what that benefit is, because it's a Questco-sponsored plan, we obviously won't participate. So there's going to be like a set list of like we want everybody to be offered this even if they offer it today or not and that kind of goes in flow with the workbook changes that we're making on our side as far as being able to opt out or intentionally select all the voluntary employer paid options as they go through the workbook but if they don't want it in there at all then yeah we would need that function in the admin console. I kind of agree with you and Jagger on that where we go in and we remove that as one of the drop down options in the workbook. If they're insisting on not seeing it.

**@7:41 — Chad Gregory (LaunchPad Lab):** So we would have to show that list of all the all the plans on the like renewal details screen or something like that and like let you uncheck them or something and then regenerate the workbook. Yeah.

**@8:04 — Chris Whitney (Questco):** Doesn't it feel like it'd be better to not generate the workbook and figure out a way to have the plan's decision before we generate the workbook?

**@8:22 — Anna Fiske:** Based on what they currently offer, is what you're thinking?

**@8:24 — Chris Whitney (Questco):** It's just if you're going to have tailored process, if you're going to have tailored process of workbook generation, show it, then come back and process it again based on the rules. It makes me wonder if we could remove that step for all the clients and figure out a way so that we wouldn't have to do that, if I even understand this right.

**@8:39 — Chad Gregory (LaunchPad Lab):** I think you are understanding it right, Chris. I think what I don't know right now, maybe for Anna, is like, how often would the renewal reps ask to remove stuff? Would it be like most times or like if you showed everything?

**@8:55 — Anna Fiske:** I mean, maybe we should just tell them we're not going to remove plans, just opt out of it. Yeah, that can also be an option. Because we wouldn't know ahead of time, Chris, it would be like the client. I always use the vets as an example. They hate our vets. So that would be like a good example where they don't even want to see it. But to Jagger's point, they can just physically opt out of it.

**@9:16 — Dimple Desai (Questco):** Would there be like a mass opt-out option? Because there would be so many plans for people to opt out of.

**@9:22 — Anna Fiske:** Would it be automatically opted out if they currently don't have make their selections and then don't choose the other ones?

**@9:30 — Chad Gregory (LaunchPad Lab):** Because we would show their current selections on the classes page, right, Anna? And so then you would have to either add, like they would have to either add a new line for something else, or they would just be picking from the drop-down. But typically they're just going to choose the one that they already had, unless they had a problem with it, right?

**@9:56 — Anna Fiske:** Right. The way that Jagger's reworking the workbook now is how we have them. Medical, Dental, and Vision. It's current, renewal, which is going to be the same as your current, and then your alternative is going to be empty. We're putting the employer paid and the voluntary the same way, so it's going to show current, and then it's going to show, if they have it, it'll show it as a renewal and be selected, but if they don't want it, they have to intentionally opt out of it.

**@10:20 — Chad Gregory (LaunchPad Lab):** That thing says to me that there would be no reason to remove stuff from the workbook then.

**@10:27 — Anna Fiske:** Yeah, if the client throws a huge, huge fit.

**@10:33 — Conor Hawes:** Maybe it kind of just depends on scale. I pulled from the demo environment the list of system-wide available plans, and somewhere around 5,000. And then there are some, I think, filtering rules that would have to be applied. So... Like, for example, if they, like, just for medical, maybe it would be helpful to show my screen. And if I'm totally looking at the wrong source of information, then let me know.

*[SCREEN SHARING: Conor started screen sharing]*

**@11:16 — Jagger Sturdivant (Questco):** I think you're probably looking at a lot of client-sponsored plans. And so those wouldn't be added. Yeah.

**@11:25 — Conor Hawes:** So, like, this is a list of everything I got. And then I filtered it down by, like, payee. So I removed not. And I filtered the insurance class. And then also filtered just, like, let's just say that this client only has a rate ban for Aetna. So filtered by Aetna. So that would be around, like, I think 260-some plans that would be available in the dropdown.

**@11:55 — Dimple Desai (Questco):** Yeah. And also available on the health summary.

**@11:59 — Conor Hawes:** But I mean. Like I may not be filtering entirely, accurately, 259.

**@12:09 — Chad Gregory (LaunchPad Lab):** What were you going to say, Dimple?

**@12:10 — Dimple Desai (Questco):** I was just going to say that the plans that start with CL and have a client ID in them, those are client-sponsored plans. So those might be able to be removed. Or the ones also that just start with the client ID, for example, 3144 Aetna, online number 66.

**@12:33 — Chris Whitney (Questco):** How does it happen again, Anna? It's the rep makes the decision, or the rep and the clients have a discussion here and make the decision on this?

**@12:47 — Anna Fiske:** On what not to offer?

**@12:49 — Chris Whitney (Questco):** What plans, yeah, what plans to act, to show?

**@12:54 — Anna Fiske:** Usually it's the renewal rep seeing the workbook and knowing the client already and saying, hey, they don't want to see X, Y. This was something last year that we talked about, and they would give us that ahead of time. Or during the consultation, the client will say, don't want to see this, but they can just opt out at that point.

But to Dimple's point here, yeah, you have a lot of client-sponsored options in here, Conor, which would not be available in the dropdown for every client. So on the column A, if it has QAET, that's Questco Aetna, that's our sponsored Aetna plan. So if you filtered to those, it should be like, I think it's 92 or 90-something. That's our master, which we can give you a list of all master plan IDs and plans to know what would be in the dropdowns always.

**@13:45 — Conor Hawes:** 131. So the intent would be, so if they have like a rate. And for Kaiser, and for Aetna, you would want the workbook to start with all of these plans.

**@14:09 — Anna Fiske:** Mm-hmm. We need those to be an option, yeah.

**@14:13 — Chad Gregory (LaunchPad Lab):** Mm-hmm. And I was just thinking, it's not going to be super cumbersome for the client, because the consultation, I'm sure, one, they're going to drive them towards a few. Like, either the plan that they're currently on, or if they're looking at alternative options, like a handful of other options, they're not going to be like, yeah, go ahead and click through all hundred of these. Yeah, and also the census.

**@14:45 — Anna Fiske:** So, if you don't live in Arizona, you're not going to see the Arizona plans or North Carolina. So, it also, Taylor should be whittling away those plans that don't apply to them, based on the zip codes of the census that.

**@14:57 — Chad Gregory (LaunchPad Lab):** Oh, yeah, this has all of the regional plans in it, too. Okay. Okay, yeah, I see Arizona and North Carolina there.

**@15:03 — Anna Fiske:** Yeah, it's going have the Californias in there, all the PPOs, which sometimes people don't qualify for. So it wouldn't be the entire list always. Some companies, yeah, they have employees all over the place.

**@15:25 — Chad Gregory (LaunchPad Lab):** How does this make you feel, Conor?

**@15:30 — Conor Hawes:** What I'm thinking about is like, if we're going from offering like 60 renewal plans to offering hundreds of renewal plans, you know, it certainly increases like the number of API calls that we need to make to get the rates and the benefits for each of the individual plans. At least according to like the way that, that I've seen it working in Prism and based off of some of that work that Jagger shared. I mean, there might be alternatives in some of the GitData bulk endpoints that we could explore. But yeah, I mean, I think it also would increase, I think the, I don't know if it would be material or not, but the size of the workbook. Like if you've got 200 plans to look at, then that means you've got your health summary tab. Would have like all 200 of those, right? Like health summary. So you'd have all this information for all of those. And, you know, I don't know if we'd hit limits or anything like that. So I wouldn't say it's like a blocker or anything. But that's just my initial reaction.

**@17:04 — Chris Whitney (Questco):** What do we do again today for this? New clients coming on board?

**@17:14 — Anna Fiske:** New clients don't use the workbook.

**@17:16 — Chris Whitney (Questco):** Oh, what did we do last year for the workbook?

**@17:23 — Anna Fiske:** All the Etna plans were in there, right, Jagger?

**@17:26 — Jagger Sturdivant (Questco):** Yeah, they were all in the workbook. And we applied them with that apply plan group.

**@17:32 — Chris Whitney (Questco):** So the concern Conor just raised, we dealt with last year and it wasn't a concern? I'm not saying it's not a concern with your API calls, Conor. I'm talking about the client, from a client, you brought up two points there. Brought up scaling and API calls and then you brought up just the size of the workbook. It seems like the latter wasn't a challenge last year.

**@17:57 — Jagger Sturdivant (Questco):** No, it wasn't.

**@17:59 — Anna Fiske:** Yeah. That's good.

**@18:04 — Chad Gregory (LaunchPad Lab):** You had some other questions in here too, Conor, which I don't think we've hit, which I don't think are exactly related to the same thing, but do you have anything else on this renewal plan process?

**@18:28 — Conor Hawes:** So there was mention of the regional mapping. Do we have a confirmed solution for that? Like I know that this has Texas in the name, but is there something like more official that we'd be able to use to reference to say like, these are, this plan is regional. These are all the fields that we get from the API.

**@19:00 — Chad Gregory (LaunchPad Lab):** Yeah, I think we talked last week, Nikki and Jagger and I, about another file, the regional zip code file being updated so that we can look up all of, we can look up first the, correct me if I'm wrong, Jagger and Nikki, we can look up first the corporate, like headquarters zip code on that file and find plans based on that. And then if it's outside, like that applies to the tri-state, believe, tri-state area stuff. And then if we need to, we will look up each of the employee zip codes and be able to pull in the plans based on based on that. So the new file would essentially have all of these zip codes associated to plans on it. Is that right? Is that what we said, Jagger?

**@20:03 — Jagger Sturdivant (Questco):** Yeah, that sounds right.

**@20:06 — Chad Gregory (LaunchPad Lab):** And I know I didn't give you a ticket to help put that together yet, but I know you're working in the workbook first.

**@20:15 — Conor Hawes:** Okay.

**@20:18 — Chad Gregory (LaunchPad Lab):** Go ahead, Chris. Can I just make a request?

**@20:22 — Chris Whitney (Questco):** Maybe it's already being done. There's a lot of requirements here and rules, nuances, and I just want to make sure that these are on paper so we know, like, this is how Taylor operates. It pulls in all these plans. It filters out geo, right? Like, we need to know that on paper, especially when we get into scale to help both troubleshoot. So we just have to make sure that, like, your as-built document really kind of defines the logic, the business logic for Taylor, because these are the areas where we'll get stuck in that I imagine we'll be revising post-go-live too.

**@21:00 — Chad Gregory (LaunchPad Lab):** Yeah, definitely are going to have that for us, Chris. It's not there yet at all, but it's something that we It's as long as we're tracking, we're making decisions here, which is all good. We just don't want us to make decisions to develop and then not define what decision was made.

**@21:20 — Chris Whitney (Questco):** We're going to have to make sure we have that tracker or that log.

**@21:25 — Chad Gregory (LaunchPad Lab):** Connor, you also asked about how renewal plans will be mapped to current plans, which I think is what Anna had mentioned Jagger was working on for making sure that the column L shows up with the current plan by default. I think that's okay. But then the second question you had there was kind of interesting to me. Jagger, you have a plan for what happens if the current plan that they were on is no longer available? Or something like that.

**@22:03 — Jagger Sturdivant (Questco):** Wait, are we solving this problem in the workbook?

**@22:08 — Chad Gregory (LaunchPad Lab):** Well, we will have to build that. For Taylor, we will build something for that in the workbook. But maybe the question isn't, what are you doing about it? But it's, what should we do about that situation?

**@22:24 — Jagger Sturdivant (Questco):** It should just, Anna, should it default to just select plan? Or should it try to figure out? I don't know, I feel like it should default to select plan.

**@22:33 — Anna Fiske:** Like, uh, or kind of make it more obvious where it shows that plan, but it's frozen on drop plan just to show, hey, you cannot select this plan. It's not redoing. Um, but Taylor should know that from PRISM because we'll put in a future termination date for 12-31-2026. So that's how you'll know if that plan's terminating. But what it does in the workbook, I'm up for suggestions. I mean, it can default to select plan. And the renewal rep needs to know, hey, it's not renewing. They have to go with something else.

**@23:07 — Chris Whitney (Questco):** Yeah, because select plan already won't let you move forward with that.

**@23:10 — Jagger Sturdivant (Questco):** So it forces them to pick something else.

**@23:13 — Anna Fiske:** Okay, well, that works too then. That's good.

**@23:17 — Chad Gregory (LaunchPad Lab):** So that would also be a filter. Well, not exactly. I guess it would be a filter. Those plans that don't hit, or that, what was the date that you mentioned, Anna? 12-31-326.

**@23:34 — Anna Fiske:** What's the field called?

**@23:35 — Chad Gregory (LaunchPad Lab):** What was the field called?

**@23:36 — Anna Fiske:** Oh, future termination date. Future termination date.

**@23:39 — Chad Gregory (LaunchPad Lab):** If the future termination date is, I guess, not in the future year that we're going into, then those plans shouldn't show up in the renewal plans list at all. Correct. They would show up in the current plans list and would be. I mean, potentially selected there.

**@24:07 — Chris Whitney (Questco):** Okay. You don't have to, like, if I understand this right, last OE, we automated as much as we can, and then we did a bunch of manual scrambling. Right, Jagger? This is how we eventually work. So one world that we live in is Taylor has its rules engine, and it processes, and then we fail because of a nuance. And you dump that as a failure, but then a human could take that and finish it up and then pick it back up on the ingestion side. So it's just, that's another reason why if you define all the rules, when we go to process a workbook, it doesn't work. You're going to have the admin console dump the failures and say, this is why. And then we can manually, like, the best bet is that we're not doing any manuals, but to say that we're not, it would be probably, that's not a fair assumption. There's got to be some nuances, so just a thought, just a thought. That's true.

**@25:08 — Chad Gregory (LaunchPad Lab):** I mean, our assumptions should try to be 100%, but that's not real world, right?

**@25:12 — Chris Whitney (Questco):** We're going to have failures, and my thought for us is how we have a process to catch those failures, still move forward, and that piece seems pretty important.

**@25:24 — Chad Gregory (LaunchPad Lab):** Mm-hmm. Conor, do we want to hit any of these last two? I wasn't sure. I was exactly aware of what you were trying to get at with these last two questions, and I can share again if you wanted.

*[SCREEN SHARING: Chad started screen sharing]*

**@25:47 — Conor Hawes:** Yeah, it was just around the, like, if we're expecting the buy-down mapping to also just be another kind of, like, manually generated CSV, or... How the team was envisioning that?

**@26:03 — Anna Fiske:** The buy-down strategy, I'll have to meet internally on that if we want to make a key or if we just want to leave it blank because it's kind of up to the client and the renewal rep's discretion on what they consider a buy-down. So we can make a key to assume their buy-down position, but that might not match up with their financial goals.

**@26:22 — Chad Gregory (LaunchPad Lab):** So I will let you know on that one.

**@26:25 — Anna Fiske:** But either way, if it needs to be filled out, then we'll provide a key on what buy-down matches up to what plan. What have you done in the past?

**@26:34 — Chad Gregory (LaunchPad Lab):** Just left it blank?

**@26:35 — Anna Fiske:** We've left it blank for the most part. Unless we know that client likes a lot of hand-holding, then we would go in and fill it out for them.

**@26:42 — Jagger Sturdivant (Questco):** BabyTaylor did have a key at some point, like midway through the year last year, and it would fill out the alternate with the key. So we do have a key already.

**@26:50 — Anna Fiske:** Perfect.

**@26:51 — Chad Gregory (LaunchPad Lab):** For some of the plans.

**@26:53 — Jagger Sturdivant (Questco):** I don't know if it's all of them. Because if it didn't have one, would just leave it blank. Or leave it on select plan.

**@27:00 — Chad Gregory (LaunchPad Lab):** Is that basically assuming if you had this plan, then you probably want this buy-down applied? Right, yeah.

**@27:07 — Anna Fiske:** If you have this deductible and it's too expensive now with your renewal, here's what a higher deductible would be to lower your premiums. That's our buy-down.

**@27:18 — Chad Gregory (LaunchPad Lab):** Sounds like we could probably get that key and just assume that's what we're using for now. And again, if nothing is in that key for a certain plan or whatever, then it would be blank. Is carrier plan CSV the go-forward approach as the source of truth for which carrier a plan is associated to? Was your last question there, Conor?

**@27:51 — Jagger Sturdivant (Questco):** That was something that goes with the renewal rules. So renewal rules will accept like a carrier type, like Aetna, and then the carrier plan... Fathom that if you have a carry of Aetna, here's all the plans you need to add.

**@28:05 — Chad Gregory (LaunchPad Lab):** So, I mean, you could do it that way.

**@28:07 — Jagger Sturdivant (Questco):** You could also just look at the plan ID, and if it starts with QAET, that's an Aetna plan. So there's a couple ways to approach that.

**@28:21 — Conor Hawes:** Yeah, I I was thinking in terms of this automated filtering for checking to see if a client has a rate band. We see if they have a rate band for Kaiser, then they get all the Kaiser plans. So is it, I mean, I guess if all of them start with the same prefix, then we could use that instead.

**@28:55 — Chad Gregory (LaunchPad Lab):** Is it Q-A-T or like Q-K-A-I or something? For Kaiser?

**@29:01 — Jagger Sturdivant (Questco):** No, Kaiser is ERC chi, I think. And then blue choice is Q blue. So they all have different prefixes. But I think they're all standardized. They are.

**@29:19 — Chad Gregory (LaunchPad Lab):** And so, Conor, are you saying we would still use the rate band to determine if they have that carrier available? And then just pick all the plan space off of that?

**@29:34 — Conor Hawes:** That's my interpretation of the conversation. I think so, too.

**@29:38 — Chad Gregory (LaunchPad Lab):** Okay. Does that sound right, Jagger? Still, and Anna, we still, if they have a rate band for that carrier, that's what determines that we need the plans for that carrier. Yeah.

**@29:54 — Anna Fiske:** Correct. Yeah. All right.

**@29:58 — Chad Gregory (LaunchPad Lab):** Great. We on, there's a sprint that finishes up this week.

**@30:03 — Chris Whitney (Questco):** Are we on track for that sprint?

**@30:06 — Chad Gregory (LaunchPad Lab):** I would say we're behind, Chris. I wanted to send you like the status update at the end of the sprint here with like the details of that. I mean, I don't think that we haven't made progress, which is good. It's a lot of discovery and kind of what I've mentioned to you on the phone last week, but we still need some discussions here, as I've mentioned at the top. Like, I want to review how we're doing the benefit guide. I want to get another conversation about the admin console scope. And I think we have a big discussion about like testing data. That's not like as immediate, but would be helpful to have soon. So we know how to, what's the thought on how much time you need to be able to talk to us and say, okay.

**@31:00 — Chris Whitney (Questco):** Here's where we need to revise scope, and here's if and how we're impacted by a delay. How much time do you need to answer those two questions?

**@31:15 — Chad Gregory (LaunchPad Lab):** Well, I definitely need probably an hour on each of these, but in terms of calendar, I think the goal would be to have a good idea of all of that and have a change order sort of prepared by the end of next week would be my goal. But I want to keep up with you a little bit better, Chris, on like, here's how these conversations are evolving. As I mentioned, like, one of the biggest things right now that's jumped out is the benefit guide change. So that's on top of my mind. Happy to say that this spike, like we made good progress on. So I'd really like to review the approach to that and make sure that we're right on everything. The admin console scope has changed, I think, compared to the SOW, as I also mentioned. Some things we can probably de-scope a little bit more so that we...

**@32:25 — Chris Whitney (Questco):** Listen, there's good work happening here. Let's decouple the scope and cost and budget from the progress. I need that as soon as we can. If we're talking about delays and material delays in time, and we're talking about additional funds, this is where my mind goes. So if the of next week is needed to really properly vet this, I'll totally accept this. Maybe I'll ask for an update by the end of this week to just dimple Anna and I so we can stay close, and then we can go from there. I don't want to poo-poo any of the great work that's here, just to couple the project from that.

**@33:02 — Chad Gregory (LaunchPad Lab):** Yeah, I agree with that entirely. Like, I feel very good about what the Questco team is providing and what our team is being.

**@33:14 — Chris Whitney (Questco):** Let's set a goal to try to get that answer as soon as we can, hopefully before the end of next week, but if that's what you need, that's what you need. I have to drop, Thank you so much. So do we.

**@33:24 — Chad Gregory (LaunchPad Lab):** Thank you, everybody. Thank you, guys.

**@33:26 — Anna Fiske:** Bye. Bye.
