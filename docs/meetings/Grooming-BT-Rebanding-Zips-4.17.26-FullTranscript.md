# Taylor - Weekly Grooming/Office Hours - April 17, 2026 (Full Transcript)

**Duration:** 56 mins
**Attendees:** Chad Gregory (LaunchPad Lab), Jagger Sturdivant (Questco), Nikki Dow (LaunchPad Lab), Nico Zubía (LaunchPad Lab — briefly)

**Note:** A Fathom-style summary of this meeting exists as `Grooming-BT-Rebanding-Zips-4.17.26.md`. This file contains the full word-for-word transcript.

---

## Transcript

**@0:00 — Chad Gregory (LaunchPad Lab):** You could probably skip this one if you want. This will be very undesigned focused.

**@0:11 — Nico Zubía:** You're discriminating with that.

**@0:14 — Chad Gregory (LaunchPad Lab):** I discriminate against designers, yep.

**@0:17 — Nico Zubía:** Yeah, yeah.

**@0:19 — Chad Gregory (LaunchPad Lab):** All right. Okay, guys.

**@0:20 — Nico Zubía:** Thank you, sir.

**@0:21 — Chad Gregory (LaunchPad Lab):** See you.

*[SCREEN SHARING: Chad started screen sharing]*

**@0:21 — Nico Zubía:** I know you got other stuff to focus on. Perfect. All right.

**@0:27 — Chad Gregory (LaunchPad Lab):** Okay. Yeah, I talked about talking a lot about Baby Taylor. I don't know if it'll be exactly like super Baby Taylor focused, but I wrote down kind of a flow for Baby Taylor. Maybe we go through it a little bit and then there are like parts of it that we can focus on a little bit more. But maybe, Nikki, we could start with your questions on this since it's something you're working on right now. Oh, and I guess Connor discussed some of this with you earlier, so Nikki, did you want to lead these three questions?

**@1:11 — Nikki Dow:** If Connor got the answers, I can just connect with him. Okay. Unless, Jagger, do you think we still have to go through these items?

**@1:19 — Jagger Sturdivant (Questco):** I don't remember number two. I know we did go through one and three.

**@1:24 — Chad Gregory (LaunchPad Lab):** Okay.

**@1:26 — Nikki Dow:** Yeah, let's touch on that. Let me just pull up the right file. I'll read this for the transcript.

**@1:41 — Chad Gregory (LaunchPad Lab):** Number two is confirm that readiness gate will no longer be needed with Taylor. And this is for generating the workbook sheet CS export.

*[SCREEN SHARING: Nikki started screen sharing]*

And wasn't that in like, yeah, like row 10 or something? Go ahead. Yeah.

**@2:03 — Nikki Dow:** Yeah. So I guess I just wanted to confirm, we have this like ready for client call out here. My understanding is that's related to like the macro running and the formatting having been done, which Taylor is going to do automatically. So I guess I'm just wondering, like, should we just omit this?

**@2:26 — Jagger Sturdivant (Questco):** Yeah, because we'll only have one version of the workbook. We won't have a pre-macro and a post-macro. So yeah, I can just delete it. Okay.

**@2:35 — Nikki Dow:** That's what I thought. I just wasn't sure if people would open it and be like, oh, it's not ready because it doesn't have the call out there. No, that's more for internal use anyway.

**@2:46 — Jagger Sturdivant (Questco):** So most people wouldn't have seen that regardless. Okay.

**@2:49 — Nikki Dow:** Gotcha.

*[SCREEN SHARING: Chad started screen sharing]*

**@2:55 — Chad Gregory (LaunchPad Lab):** Easy. Okay. I'll get back in here real quick. So then on BabyTaylor, maybe you can help me confirm this flow a little bit. I'll try to run through it kind of quickly, and then we'll jump back to the areas to talk about a little bit more.

So obviously, right now in client space, the batch gets created. There are a few steps to do that. But then the workbook is generated in client space as well. And it seems like you're taking that workbook and like adding it to your local to run BabyTaylor. Is that right?

**@3:38 — Jagger Sturdivant (Questco):** Yeah. Okay.

**@3:40 — Chad Gregory (LaunchPad Lab):** And then BabyTaylor will actually open up that workbook and validate different things like the rates versus the carrier rate book. Do the plans exist? Mappings for certain things. Comparing the previous year in client space. Just to make sure there's like, I guess that's kind of like, like a sanity check. And then it uses those census zip codes, and then it flags for whether or not any regional plans are going to be needed. That's an area that we want to talk through a little bit more. Maybe you can walk through how it's handling that and how we can talk about how should Taylor handle those.

Um, but then BabyTaylor also runs those, those, um, macros in Excel. Um, I was curious, like, how, like, it sounds like Excel, Excel is still doing that, but BabyTaylor, like, triggers it. Obviously, I think for Taylor, that's, like, probably not relevant at all, because we'll just generate the file with the macros already being run, having been run, essentially.

Um. Then there's additional baby-tailored-driven content, the Census tab from Prism, which I guess was already, like, I'm kind of bumping these, I guess, but column L on the class sheets gets prefilled to align with the current plan column, the columns T through Z for the buy-downs, which I'm curious how that works. The renewal increase percentage on the summary sheets, you mentioned some formulas there, which maybe it would make sense to go through since you, I think you called out that those were complex at some point. Adds more of the detail on, like, the bottom sections of the class sheets, and then runs some validations. The one that was called out was, like, that dental vision carrier planning, like, if they have MetLife for dental, then they have to have it for vision.

**@5:59 — Jagger Sturdivant (Questco):** I'm curious. I'm

**@6:00 — Chad Gregory (LaunchPad Lab):** Is there other validations there that are important?

**@6:04 — Jagger Sturdivant (Questco):** The other one I can think of is the contributions being filled out.

**@6:09 — Chad Gregory (LaunchPad Lab):** Okay. I think I had that somewhere else for some reason. Oh, missing contributions. Is that at this step, like when you're generating the workbook itself, or is it maybe done in multiple times?

**@6:27 — Jagger Sturdivant (Questco):** That, those are both done after the client executes the workbook.

**@6:34 — Chad Gregory (LaunchPad Lab):** Oh, yeah, that's true. So these are, what, that's a good point. So, so then, are there any other validations that you're doing on the first workbook generation?

**@6:53 — Jagger Sturdivant (Questco):** Not that you didn't already mention, I don't because you already said that.

**@6:57 — Chad Gregory (LaunchPad Lab):** yeah, because you're doing like the validation.

**@7:00 — Jagger Sturdivant (Questco):** Yeah.

**@7:01 — Chad Gregory (LaunchPad Lab):** Okay. That's good. So then after the consultation, BabyTaylor can take the executed workbook, parse that data for the Prism imports, which everything's getting sent to ClientSpace today so that those can be generated there, right? And then when the imports are generated in ClientSpace, then you can give those back to BabyTaylor to take these files and clean them up with another macro. I was curious if there were like any tricky parts to this cleanup that we could maybe expect to be tricky with Taylor. Like obviously we're going to build like ClientSpace isn't going to make these files anymore. So maybe again, this is like not something to worry about, but I'm wondering if there are like tricky parts that like, is there a reason that ClientSpace can't access the data or BabyTaylor needs to be cleaning them up.

**@8:05 — Jagger Sturdivant (Questco):** I don't think so. We put together a file. don't think we've sent it to you yet. But for the imports, we've mapped each column to where it would be in the workbook or where it would be in Prism.

**@8:17 — Chad Gregory (LaunchPad Lab):** Great. So you guys will have that soon.

**@8:20 — Jagger Sturdivant (Questco):** And I don't think there was any super tricky parts. You'll have to make some Prism calls for some of that stuff. And maybe some stuff needs to be added to the workbook.

**@8:31 — Chad Gregory (LaunchPad Lab):** We'd have access to it.

**@8:33 — Jagger Sturdivant (Questco):** But other than that, I don't think it'll be too bad.

**@8:37 — Chad Gregory (LaunchPad Lab):** Okay, great. Then maybe we should jump back to the zips and census file. Because essentially, that's the end of the process, right? Is cleaning up the Prism import. Because then they're doing it.

**@8:56 — Jagger Sturdivant (Questco):** You are missing one thing here is the CBEs.

**@9:00 — Chad Gregory (LaunchPad Lab):** Oh, yeah. So this is like all workbook, basically. Or, yeah, workbook and then prism. So at the same time, no, not at the same time, here.

**@9:12 — Jagger Sturdivant (Questco):** it would, yeah.

**@9:14 — Chad Gregory (LaunchPad Lab):** Like, this is kind of net, yeah, I don't know. Before the prism import files, the CBE gets, the CBE and Kashi get generated. What do you do there? So, again, those are both actually generated in Client Space. And does, what level of, like, cleanup does BabyTaylor do on those?

**@9:48 — Jagger Sturdivant (Questco):** BabyTaylor doesn't touch those. As long as everything has been done correct up to that point, Client Space generates those properly. Okay. The only thing BabyTaylor does does is... It takes the workbook and imports everything back into client space for those to be made.

**@10:06 — Chad Gregory (LaunchPad Lab):** Yeah, got it. That's right. Nikki, I'm curious if you want to talk a little bit about the zips here. These questions came from you, but Jagger, don't know how easy it is for you to kind of show us what's going on with the zip file or anything.

**@10:47 — Jagger Sturdivant (Questco):** Yeah. Do you have it open by chance?

**@10:50 — Chad Gregory (LaunchPad Lab):** Let me see. I do.

**@10:52 — Nikki Dow:** I can share.

**@10:53 — Jagger Sturdivant (Questco):** And I did go through this with Connor earlier as well, but I don't mind going through it again.

**@10:58 — Chad Gregory (LaunchPad Lab):** Nice. Connor's on top of it. He is.

*[SCREEN SHARING: Nikki started screen sharing]*

**@11:08 — Nikki Dow:** Yeah, he gets a lot done. Okay, no, sorry, that's a great book. Okay, so I think I understand at a high level things we're validating, like Arizona, North Carolina, and Texas, I believe, you have to have regional plans. Um, but I'm a little lost on, like, what the columns in this zip code spreadsheet, like, are indicating, and, like, how they tell you there's a plan that you need to include, if that makes sense.

**@11:51 — Jagger Sturdivant (Questco):** So, it really doesn't. So, this is, this is really a client-facing file, and we're kind of just hijacking it and reusing it for Taylor. So the only column you really care about is the zip code column. All the rest of those columns don't matter for us. Connor and I were talking about this earlier, and this wasn't designed for the workbook, but we can create a custom version of this that works for Taylor. So we can rename the sheets to be just the state codes instead of being what they are now. And we can add another sheet that maps the states to the plans that need to be added. So like for Arizona, we would have Arizona, and then we would have the three or however many Arizona plans. And so if they matched the zip code on that in column A, we would know, okay, we need Arizona. These are the three plans they need to add, and we go from there.

**@12:55 — Chad Gregory (LaunchPad Lab):** Is there a reason it has to be zip code, or is it just like state-based?

**@13:00 — Jagger Sturdivant (Questco):** No, it is zip code, because not all of the zip codes in Arizona are covered, necessarily.

**@13:06 — Chad Gregory (LaunchPad Lab):** Okay. So what do we think that that custom, I guess, resource that Taylor would use would look like zip code, state, plan, basically?

**@13:30 — Jagger Sturdivant (Questco):** You could do it that way. You'd need to have multiple lines, because you'd have more than one plan. So it'd be a really long file if you did it that way.

**@13:45 — Chad Gregory (LaunchPad Lab):** What do you think the, sorry, maybe I'm just not understanding exactly.

**@13:52 — Jagger Sturdivant (Questco):** So I think really what we should do is, using this Arizona one as an example, we would rename this sheet to just AZ, just Arizona. And then we pull the census from Prism, we get the employee's zip code, and we check if that zip code is in this sheet for Arizona.

**@14:15 — Chad Gregory (LaunchPad Lab):** Yeah.

**@14:17 — Jagger Sturdivant (Questco):** And if one of them matches, then we know, okay, we need the Arizona plans. So then we would have another sheet that we create that maps Arizona to the three plans that are needed.

**@14:31 — Chad Gregory (LaunchPad Lab):** I see.

**@14:33 — Nikki Dow:** That makes sense. I guess maybe like in the new scenario, this doesn't matter, but is like this, does this have like a tie to the plan you need to include?

**@14:47 — Jagger Sturdivant (Questco):** Or is that just. I'm not going to lie, have no idea what that even is. Okay.

**@14:51 — Nikki Dow:** I don't think it does. Okay. Okay, but really all we need is a list of zip codes.

**@15:00 — Jagger Sturdivant (Questco):** Yeah.

**@15:00 — Nikki Dow:** Because not all Arizona zip codes are going to have specifically required plans.

**@15:05 — Jagger Sturdivant (Questco):** Right.

**@15:06 — Nikki Dow:** And then for each zip code, we just need plans A, B, C are required.

**@15:12 — Jagger Sturdivant (Questco):** Yeah. For each state, the zip codes will all map to a state and then the states map to plans.

**@15:21 — Chad Gregory (LaunchPad Lab):** Got it. Oh, okay.

**@15:22 — Nikki Dow:** The plans are based on the state. It's just not all zip codes. Right.

**@15:26 — Jagger Sturdivant (Questco):** Yep. Okay.

**@15:27 — Nikki Dow:** I see. Yeah.

**@15:28 — Chad Gregory (LaunchPad Lab):** Okay. And do the zip codes that are represented? Change. And I'm sure the plans change. Like, so each of those files could be edited whenever they need to be.

**@15:46 — Jagger Sturdivant (Questco):** Yeah. I think they only change, like, once per year. Like, and it doesn't update this often, I don't think. But, yeah, it can change.

**@15:54 — Chad Gregory (LaunchPad Lab):** And they can't add new ones.

**@15:55 — Jagger Sturdivant (Questco):** Like, that Texas one, that's new from last year. So they add states as well.

**@16:05 — Chad Gregory (LaunchPad Lab):** Oh, yeah. It's in the same.

**@16:11 — Jagger Sturdivant (Questco):** Yeah, that one's new. Oh, okay.

**@16:16 — Chad Gregory (LaunchPad Lab):** And there would be a different one for Aetna, and, like, does Kaiser do the same thing?

**@16:27 — Jagger Sturdivant (Questco):** No, this is just Aetna does this for now. I think Anna said that MetLife Dental is going to start doing it, but we don't have the zip code file for that.

**@16:37 — Chad Gregory (LaunchPad Lab):** Okay, maybe that's a road to cross later. But, like, having to check multiple, you would only check the zip code, oh, wait, you would only check the zip code to state matcher once, but then depending on the state, then you would need to check multiple like state to plan, or I guess both plan, the plans could be on the same state files or something.

**@17:12 — Jagger Sturdivant (Questco):** Yeah, they could. We don't have to make a new sheet.

**@17:14 — Chad Gregory (LaunchPad Lab):** Yeah. We could put them in column O or something.

**@17:17 — Jagger Sturdivant (Questco):** mean, it doesn't really matter.

**@17:18 — Chad Gregory (LaunchPad Lab):** Whatever's easiest. I'm reading our questions here.

**@17:26 — Nikki Dow:** Yeah, I'm just thinking if MetLife is going to also add that, we should probably just build from the get-go, like being able to do the same validation. It might be against like, I don't know, like dummy data that we set up, but it's probably worth including.

**@17:53 — Chad Gregory (LaunchPad Lab):** Interesting.

**@17:54 — Nikki Dow:** And so then the rules about New York, New Jersey, Connecticut. Um, that's like a totally separate thing, right? Like, you're just checking the zip code. Is it in one of those three states?

**@18:10 — Jagger Sturdivant (Questco):** That one is in your zip code. Go ahead. Oh, sorry.

**@18:15 — Nikki Dow:** I think I misspoke. It's based on the headquarters of the company, not the employee, right? Yeah. Yep. So if they're in New York, New Jersey, Connecticut, you only offer plans for those three states, right? Yep.

**@18:34 — Jagger Sturdivant (Questco):** Even like our national Aetna plans, you don't offer those either. It's just like they have a whole separate book for those three states.

**@18:42 — Chad Gregory (LaunchPad Lab):** So we always should check the zip code of the company headquarters and always, well, check that first, basically. If it is in one of those three states, then we have to go that route. If it's not in one of those three states, then we check the zip code of all the employees to see if we need to offer any of these other regional things for the other state. Exactly.

**@19:15 — Nikki Dow:** And when you say there's a separate, I think you said a separate book for New York, New Jersey, Connecticut, is that a separate book?

**@19:28 — Jagger Sturdivant (Questco):** No, it'll be in the Aetna rate book still, but it's just like they only offer those plans. don't offer any of the national plans. They don't offer any of these regionalized plans. It's only those 15 or whatever tri-state plans is what we call them.

**@19:43 — Nikki Dow:** Okay. And that's, I don't know if this would ever happen, but even if they have an employee in this zip code, it doesn't matter. Like that doesn't mean they're offering.

**@19:55 — Jagger Sturdivant (Questco):** Yeah. need to offer that plan.

**@19:57 — Nikki Dow:** We would have to ask Anna, but I'm pretty sure, yeah.

**@19:59 — Jagger Sturdivant (Questco):** Yeah. Doesn't matter.

**@20:02 — Nikki Dow:** Okay. Yeah, we should, I guess, confirm, but I guess that would make sense.

**@20:13 — Chad Gregory (LaunchPad Lab):** Okay.

**@20:17 — Nikki Dow:** And I assume, like, there's some, like, Prism API call that makes it easy to, you the headquarters of a company, right? That shouldn't. Oh, yeah.

**@20:26 — Jagger Sturdivant (Questco):** It's in their adams. Okay.

**@20:32 — Chad Gregory (LaunchPad Lab):** Hmm. I feel better about this, Nikki. How do we move forward with getting those, like, new files created or whatever we need to do there? Or actually, oh, yeah, go ahead. I know you had one more question on this PBO column.

**@20:56 — Nikki Dow:** I did. I saw this column here on the screen. And I was just wondering if it had any effect on like plans we need to make sure are offered.

**@21:05 — Jagger Sturdivant (Questco):** It doesn't. It's used for the renewal reps. They just kind of have to know. I talked to Connor about this too. There is an enhancement we can make where it does check that they have a PPO plan, but I don't know how you check if a plan is a PPO or not. I don't know if PRISM has that information, so I don't know that it's possible. But what we did last year is, yeah, just the renewal rep, just use this as a reference to know if they need to offer a PPO or not.

**@21:37 — Nikki Dow:** Gotcha.

**@21:44 — Chad Gregory (LaunchPad Lab):** Who came up with all the names for these people? I just realized like how many of them, like there's so many and like, I don't know if any of them are just like Mark Twain. Yeah, Hershey Ballmer, Clay Aikens in there. Mickey Mouse, Super Duper, Deep Duper, like, King Ducks. don't know. It's a mix.

Anyway, does it make sense? Nikki, what do you think about, like, getting the, like, do we just need somebody to go through the existing zip code file and, like, actually, I don't know. Can we just use that how it is? And then we need to make the state files?

**@22:41 — Nikki Dow:** I mean, the zip code file, like, I think works for us to just know when we need to, like, check plans that are offered. But, yeah, we still will need some kind of a... File that, like, maps the plans to that state.

**@23:07 — Jagger Sturdivant (Questco):** Yeah, I think it's easiest to just build that into this sheet somewhere.

**@23:12 — Nikki Dow:** Yeah.

**@23:13 — Chad Gregory (LaunchPad Lab):** It doesn't really matter where. Yeah. Is that, like, an Anna question, Jagger, to get all the plans for the states?

**@23:26 — Jagger Sturdivant (Questco):** No, I think I, I mean, unless they've changed them. I have them from last year.

**@23:31 — Chad Gregory (LaunchPad Lab):** Okay. Yeah. We would have to ask them if they changed them or not, though. Okay. How would we, I mean, we could add additional sheets on here that's just, like, Texas, California, blah, blah, blah. Maybe that's easiest.

**@23:51 — Nikki Dow:** Yeah. It could be really simple. Just, like.

**@23:53 — Chad Gregory (LaunchPad Lab):** Yeah.

**@23:54 — Nikki Dow:** A sheet for Arizona required plans, and then all in column A. And then same. For the other states.

**@24:03 — Chad Gregory (LaunchPad Lab):** Yeah.

**@24:04 — Jagger Sturdivant (Questco):** I mean, if you wanted to do one sheet, you could have two columns and just have state and then plan and then just duplicate the state for each plan. So you don't have. That's true.

**@24:14 — Nikki Dow:** You don't have like five sheets.

**@24:16 — Jagger Sturdivant (Questco):** One for each state.

**@24:20 — Chad Gregory (LaunchPad Lab):** Yeah. Yeah, that's true. Okay. We'll follow up with you and Anna on that then next week, just to be sure that one, they haven't changed, but two, it seems like it's going to be pretty easy to update this to accommodate for that. Okay. Any other questions on that front, Nikki or José?

**@24:53 — Nikki Dow:** I don't think so. I think I got my zip code questions answered.

**@24:58 — Chad Gregory (LaunchPad Lab):** Maybe you can... Oh. I was going to ask, so the next one I wanted to ask about was kind of the formulas on the renewal increase percentage on the summary sheets. guess you weren't on the worksheet actually, so let see if I can pull, I guess I should open like the Claymore one.

**@25:32 — Jagger Sturdivant (Questco):** Are you talking about the renewal percentage that shows up on total cost?

**@25:36 — Chad Gregory (LaunchPad Lab):** Yeah.

**@25:38 — Jagger Sturdivant (Questco):** Yeah, that formula is a doozy.

**@25:42 — Chad Gregory (LaunchPad Lab):** Renewal percentage. Oh yeah, and total cost, that's where it is. Wait, why is there a renewal increase? Okay, there it is.

*[SCREEN SHARING: Chad started screen sharing]*

Um. Come on. Feels like my screen is froze. What's going on here?

**@26:09 — Jagger Sturdivant (Questco):** It might be locked.

**@26:11 — Chad Gregory (LaunchPad Lab):** Oh, it's locked. Yeah.

**@26:13 — Jagger Sturdivant (Questco):** I can put the password in the chat. It's fine. If want to unlock it with that. I actually do that. Yeah. Unprotect sheet.

**@26:38 — Chad Gregory (LaunchPad Lab):** Okay. There we go. Let's make this. So, I mean, I'm assuming, well, I guess my assumption previously was that it is looking at, okay, so it's going sum of primary.

**@27:04 — Jagger Sturdivant (Questco):** So I think it's multiplying, I know it's the enrollment count times the, what's L, if you've got a primary?

**@27:18 — Chad Gregory (LaunchPad Lab):** L is the selection. rate, yeah, the rates.

**@27:25 — Jagger Sturdivant (Questco):** Yeah, so it's the enrollment count times the rate, and then you sum that up for each class, for each plan.

**@27:31 — Chad Gregory (LaunchPad Lab):** Yeah, E is the enrollment count.

**@27:33 — Jagger Sturdivant (Questco):** Yeah.

**@27:36 — Chad Gregory (LaunchPad Lab):** So you said the sum, so it is, you said it's the enrollment rate times the rate, the enrollment count times the rate for each thing.

**@27:51 — Jagger Sturdivant (Questco):** Yeah, and then you sum those together, and then you do that for each class, and then sum those together, and then that's your percentage.

**@28:00 — Chad Gregory (LaunchPad Lab):** And then, yeah, divide by whatever. I'm sure there's a divide here somewhere.

**@28:05 — Jagger Sturdivant (Questco):** Yeah, I think it's the minus one or something.

**@28:07 — Chad Gregory (LaunchPad Lab):** There it is. Oh, yeah. Actually, that isn't that. I mean, it's complicated because it's a lot of numbers that you're grabbing, but it's not that bad. It makes sense because you're just trying to find, wait, oh, wait, F? Oh, yeah.

**@28:32 — Jagger Sturdivant (Questco):** Yeah, because you have to do the same thing for the current internet.

**@28:35 — Chad Gregory (LaunchPad Lab):** So, yeah, it's the total cost, basically, of the current or the new rate divided by the total cost of the rate this past year turned into a percentage.

**@28:54 — Jagger Sturdivant (Questco):** Yeah, pretty much.

**@28:58 — Chad Gregory (LaunchPad Lab):** Okay, that's not that. Yeah, that's not that crazy. And if we had, oh wait, yeah, why is it?

**@29:09 — Jagger Sturdivant (Questco):** There may not be any plans in owners, maybe.

**@29:11 — Chad Gregory (LaunchPad Lab):** That's right. So like if I added some plans, does that automatically happen?

**@29:18 — Jagger Sturdivant (Questco):** I don't think so.

**@29:19 — Chad Gregory (LaunchPad Lab):** Oh, but these weren't filled out.

**@29:21 — Jagger Sturdivant (Questco):** Yeah. Right, yeah.

**@29:23 — Chad Gregory (LaunchPad Lab):** Okay, so that's probably part of the macro is deciding.

**@29:27 — Jagger Sturdivant (Questco):** Well, BabyTaylor adds this formula, actually.

**@29:30 — Chad Gregory (LaunchPad Lab):** So BabyTaylor looks at what all classes are there and what all is filled out.

**@29:38 — Jagger Sturdivant (Questco):** Yep. And then just puts that formula there.

**@29:41 — Chad Gregory (LaunchPad Lab):** Okay. Nikki, how does that sound to you? Does that make sense?

**@29:52 — Nikki Dow:** At a high level, yeah.

**@29:54 — Chad Gregory (LaunchPad Lab):** Yeah, okay. It's a lot of numbers, but it makes sense. Into one formula, but it does make sense.

**@30:02 — Jagger Sturdivant (Questco):** Well, and you have to be careful too, because there's a character limit in a formula.

**@30:11 — Chad Gregory (LaunchPad Lab):** Interesting.

**@30:16 — Jagger Sturdivant (Questco):** So I don't know if you, I mean, you could like assign variables and stuff and reference those. That might be the best way to do it.

**@30:24 — Chad Gregory (LaunchPad Lab):** But I don't, we would have to modify the workbook for that. Yeah, like, could you do each one, like, each class and then separately and then pull them together, basically?

**@30:45 — Jagger Sturdivant (Questco):** Something like that.

**@30:46 — Chad Gregory (LaunchPad Lab):** I think so, yeah.

**@30:47 — Jagger Sturdivant (Questco):** You probably could.

**@30:49 — Chad Gregory (LaunchPad Lab):** Okay. Do you, do you actually know, are there any plan or any clients that have? Like seven classes? There's a few, yeah. Okay. There's some that have more than seven and that breaks. Yeah. Why do they have so many or like in those scenarios, what is it that's awesome?

**@31:15 — Jagger Sturdivant (Questco):** I don't even think they know why they have so many.

**@31:18 — Chad Gregory (LaunchPad Lab):** The owners are just like, we want to. Okay.

**@31:23 — Jagger Sturdivant (Questco):** There's one that has a bunch of them and they're all marked do not use. It's like, okay, why do you have them then?

**@31:29 — Chad Gregory (LaunchPad Lab):** Yeah. Maybe it's like one single person is still using that and they're like a special case. Yeah.

**@31:37 — Nikki Dow:** Is that like something we need to exclude from the workbook?

**@31:44 — Jagger Sturdivant (Questco):** What do you mean?

**@31:45 — Chad Gregory (LaunchPad Lab):** Like those ones marked do not use?

**@31:47 — Jagger Sturdivant (Questco):** Oh, no, no, no. No, we'll still put them in.

**@31:51 — Chad Gregory (LaunchPad Lab):** Their mark do not use so that an employee when they go into prison to actually elect doesn't touch it, right? In that case, I no idea.

**@32:01 — Jagger Sturdivant (Questco):** Like in the actual class name has dash do not use in it. So like it would be like primary dash do not use. I don't know why they do that.

**@32:09 — Chad Gregory (LaunchPad Lab):** But okay, I think it's only one client that has that. Yeah. Okay. So that makes sense here then. Oh yeah, we wanted to ask about the rebanding file and BabyTaylor. Today, how does that come into play for BabyTaylor and this whole process?

**@32:43 — Jagger Sturdivant (Questco):** The only thing BabyTaylor does with the rebanding file is it's checking that the band that's in the workbook that ClientSpace generated matches the rebanding file. So it's just making sure that ClientSpace has the right assigned band for every band. The validation. Yeah, that's all it is.

**@33:05 — Nikki Dow:** Maybe a silly question, but where in the workbook would we look to see that band that was applied?

**@33:14 — Jagger Sturdivant (Questco):** If you have the pre-macro one open, the one that doesn't have all the sheets hidden, it's in current plans and renewal plans. The risk tier column is the rate band.

**@33:28 — Chad Gregory (LaunchPad Lab):** Risk tier.

**@33:29 — Nikki Dow:** Okay. I did see that. Trying to open.

**@33:34 — Jagger Sturdivant (Questco):** ideally, we should probably remove that column if we can, because it's not really necessary. The only thing you're getting from it is the rates, and the client really shouldn't know that they have a rate band.

**@33:46 — Chad Gregory (LaunchPad Lab):** Yeah. Wait, which one did you say was on?

**@33:50 — Jagger Sturdivant (Questco):** Scroll over.

**@33:54 — Chad Gregory (LaunchPad Lab):** Oh, in the summaries?

**@33:56 — Jagger Sturdivant (Questco):** No, in the sheet itself.

**@33:58 — Chad Gregory (LaunchPad Lab):** Oh, scroll over here.

**@34:00 — Jagger Sturdivant (Questco):** To the left. I don't know why it's to the right already.

**@34:02 — Chad Gregory (LaunchPad Lab):** Okay.

**@34:03 — Jagger Sturdivant (Questco):** Yeah, G. Risk tier.

**@34:06 — Chad Gregory (LaunchPad Lab):** So, I did see that. So let me see if I can open up a rebanding sheet now. I was looking at this yesterday. This is the BCBS. Clicked it wrong. I don't know if it's going to do something now.

**@34:29 — Jagger Sturdivant (Questco):** Okay.

**@34:30 — Chad Gregory (LaunchPad Lab):** Sel, don't care about updating right now, please. Okay. So, my understanding, this tier. Is that what we're looking at then?

**@34:49 — Jagger Sturdivant (Questco):** That's their, that was their current one for 2025. The new one is Z.

**@34:55 — Chad Gregory (LaunchPad Lab):** Yeah. And... So this, let's say that the client on this workbook is Metro Machine Works. They would have 10 here, but this is BCBS, so this would just be for health. There would be a different rebanding file for dental and vision and all the others, right?

**@35:27 — Jagger Sturdivant (Questco):** No, the dental vision don't have bands, so it would probably, it would either be blank or say global.

**@35:33 — Chad Gregory (LaunchPad Lab):** Okay, and what does that actually like do, what do we do with this risk tier here?

**@35:49 — Jagger Sturdivant (Questco):** In the workbook, it doesn't do anything. Really, all it's doing is mapping to what the rates are. So in the rate book, you have a tier. And then you have rates for each plan. And then each client is assigned a tier so that you know where to pull the rates from for each plan.

**@36:07 — Chad Gregory (LaunchPad Lab):** So really it's irrelevant, except it fills out this sheet that the client doesn't even see.

**@36:15 — Jagger Sturdivant (Questco):** Right, yeah. Which is why I think we should just remove it because...

**@36:19 — Chad Gregory (LaunchPad Lab):** Yeah. Do we even need... We need it in the admin console. And so that somebody can reference it, basically, I guess. And when Anna or whoever goes in and enters the rates into Prism, she would reference that to see what rate to put in for each client.

**@36:48 — Jagger Sturdivant (Questco):** Right. Okay.

**@36:50 — Chad Gregory (LaunchPad Lab):** I mean, that makes a lot more sense to me. Sorry if I was like... I was thinking there was more to it. That's

**@37:00 — Jagger Sturdivant (Questco):** Well, there kind of is, BlueChoice is a little bit more convenient because the risk tier and the tier that they give us is the same, like it's just the number.

**@37:09 — Chad Gregory (LaunchPad Lab):** Oh.

**@37:10 — Jagger Sturdivant (Questco):** For Aetna, that is not the case. The Aetna one.

**@37:23 — Nikki Dow:** I have the Aetna one pulled up if you want me to share.

**@37:27 — Chad Gregory (LaunchPad Lab):** Oh, sure. Or it looks like you found it. Yeah, I found it, but I'll just do it. Aetna.

**@37:54 — Jagger Sturdivant (Questco):** So, I have no idea which column it is. I guess T is their current.

**@38:00 — Chad Gregory (LaunchPad Lab):** Current and then I might just scroll over for the new one.

**@38:24 — Jagger Sturdivant (Questco):** Well, it might be hidden. It might be in one of those hidden columns.

**@38:32 — Chad Gregory (LaunchPad Lab):** I'm such a noob at Excel, so.

**@38:52 — Jagger Sturdivant (Questco):** Yeah, try those.

**@39:07 — Chad Gregory (LaunchPad Lab):** band change.

**@39:13 — Jagger Sturdivant (Questco):** Where is it? There it is, AC.

**@39:26 — Chad Gregory (LaunchPad Lab):** Final band? Yeah, okay, so this client, Z-Link Inc., they are now band 1126, they were band 1077, so these associate with a simpler band.

**@40:00 — Jagger Sturdivant (Questco):** So in the workbook, it's not going to say band 1126, because for Aetna, each plan has its own rate band for each band. So if we're working with the MC5070 plan, and we were assigning it to this client, the rate band would be QAET MC5000-70-1126.

**@40:46 — Chad Gregory (LaunchPad Lab):** I mean, I guess we don't need to know, so you're saying we would, in the work, yeah, okay, in the workbook... I guess my point is we don't really need to know what that means that much, but we would put in whatever the plan was, the risk tier would show the plan name dash 1126 is what you're saying.

**@41:17 — Jagger Sturdivant (Questco):** Right. But you do have to know what that means because you have to pull in the rates and the rates are tied to that risk tier.

**@41:30 — Chad Gregory (LaunchPad Lab):** But aren't we just going to get the rates from the PRISM, from PRISM? Right.

**@41:38 — Jagger Sturdivant (Questco):** But the rates are mapped to that rate group. So you need the rate group to know which rates to pull.

**@41:44 — Chad Gregory (LaunchPad Lab):** And diff, oh, okay. How does that show up? Or yeah, I guess maybe help me, help me walk to that. Or if you, if you even know offhand. And it seems like it's pretty complicated. Wait, so this is a four. Like with this, are you telling me, so are you saying that the rate wouldn't be actually added in Prism for the client on the, I guess, for the plan?

**@42:37 — Jagger Sturdivant (Questco):** Now let me see if I can pull it up in Prism and that might help.

**@42:44 — Chad Gregory (LaunchPad Lab):** Nikki, let me know if you're following better than me and I don't need to be floundering.

**@42:51 — Nikki Dow:** I wouldn't say.

**@42:54 — Jagger Sturdivant (Questco):** It's super complicated, I know.

**@42:57 — Nikki Dow:** I think being in Prism maybe will like.

**@43:01 — Jagger Sturdivant (Questco):** So in PRISM, have the global, you can see my screen, right?

*[SCREEN SHARING: Jagger started screen sharing]*

**@43:20 — Chad Gregory (LaunchPad Lab):** Yeah.

**@43:21 — Jagger Sturdivant (Questco):** So we have the global plan for this Aetna plan, right? So if I go into the billing rates for this plan, and I look at its current rate groups, there's a rate group for each of those numbers. So our 1126 is right here. So it's like the plan ID dash, and then it's cut off, but it says 1126. So that's what would be in the risk tier, and you have to know this to be able to pull the rates. So like if I, and then I look at the employee rates for... Or here. So this is the rate for employee for this rate group.

**@44:09 — Chad Gregory (LaunchPad Lab):** But still, it's not like, really, we just need to match that rate group name, which is the plan plus that number, like 1126, to come back to Prism and find the rate amount, right? Right.

**@44:37 — Jagger Sturdivant (Questco):** Okay. And the same, the Blue Cross version of that is, it's just 10. Yeah, like a Blue Cross plan, I think is, the rate group is literally just 10.

**@44:49 — Chad Gregory (LaunchPad Lab):** Yeah. Okay.

**@44:50 — Nikki Dow:** So Aetna is weird because it has, like, this naming convention.

**@44:55 — Jagger Sturdivant (Questco):** Yeah, I think. Combining plan and numbers.

**@44:57 — Nikki Dow:** I think Kaiser is also a little weird.

**@45:00 — Jagger Sturdivant (Questco):** Weird. I don't remember.

**@45:03 — Chad Gregory (LaunchPad Lab):** Let see if we have one of those. We have Kaiser rebanding, yeah.

**@45:12 — Jagger Sturdivant (Questco):** Or this one. Yeah, Kaiser's also weird.

**@45:27 — Nikki Dow:** Yeah, can we maybe look at the Kaiser rebanding file and kind of go through the same sequence we just did on Aetna?

*[SCREEN SHARING: Chad started screen sharing]*

**@45:36 — Chad Gregory (LaunchPad Lab):** Yeah, if you want. Yeah, okay. Okay, so here's the Kaiser rebanding. So current rate band. Yeah, so C is the current, and then... That's the factor, right? Is there a...

**@45:56 — Jagger Sturdivant (Questco):** Yeah, those numbers are factors, so... It's just multiplying the base rate by that number, and that's the rates. Technically, you could use that, I guess, but I don't know if that's consistent.

**@46:11 — Chad Gregory (LaunchPad Lab):** You're saying that is, like, is there a rate band name here somewhere?

**@46:21 — Jagger Sturdivant (Questco):** No, they just give you the number.

**@46:27 — Chad Gregory (LaunchPad Lab):** Oh, it was there.

**@46:29 — Jagger Sturdivant (Questco):** The new one. Column Y? Yeah, Y or Z. Oh, here, yeah.

**@46:37 — Chad Gregory (LaunchPad Lab):** Z is like, this is the band itself. When we, we would look at, when Alan Smith came in, well, actually, is this, this is the new one? I don't know if the old one is somewhere, here somewhere.

**@46:54 — Jagger Sturdivant (Questco):** Yeah, it was C, I think, column C.

**@46:57 — Chad Gregory (LaunchPad Lab):** C was the new, current.

**@47:00 — Jagger Sturdivant (Questco):** Okay, and for Alan Smith, it didn't change. Yeah.

**@47:04 — Chad Gregory (LaunchPad Lab):** Or it was manually overridden or whatever. So then the renewal rate band, we would look at the plan plus that or something like that again?

**@47:19 — Jagger Sturdivant (Questco):** Mm-hmm.

**@47:20 — Chad Gregory (LaunchPad Lab):** Okay. And this is actually easier because it doesn't have band in there too.

**@47:27 — Jagger Sturdivant (Questco):** Yeah.

**@47:29 — Chad Gregory (LaunchPad Lab):** Okay.

**@47:30 — Nikki Dow:** Um, maybe just like reiterate like what this means in terms of validations that Taylor needs to do. Is it basically just, well, no, I guess I'm confused what Taylor needs to validate because this rebanding file tells us the rate band of a particular client. And then when we generate the workbook from Prism, we're pulling the rates assigned to that band.

**@48:12 — Jagger Sturdivant (Questco):** Right.

**@48:13 — Nikki Dow:** And BabyTaylor needed to check that the correct rates were pulled. But if Taylor's pulling all this from Prism, is there really a validation that needs to run still?

**@48:24 — Jagger Sturdivant (Questco):** There's not. Yeah, the only reason BabyTaylor was auditing that is because in client space, we had to manually set the rate band for each plan ourselves. And so if we missed one, that plan would have been wrong. But yeah, if we're pulling directly from Prism, there's no validation there.

**@48:42 — Nikki Dow:** Gotcha.

**@48:45 — Chad Gregory (LaunchPad Lab):** Man, client space is really a complicated thing, huh?

**@48:48 — Jagger Sturdivant (Questco):** Yes, yeah.

**@48:50 — Chad Gregory (LaunchPad Lab):** So you were checking that the rates and the rate bands were right in client space?

**@48:58 — Jagger Sturdivant (Questco):** Yep.

**@49:01 — Chad Gregory (LaunchPad Lab):** And then now we do need to get the rate based on the rate band from PRISM, but the rates will be set in PRISM for each rate band and plan. Right.

**@49:23 — Jagger Sturdivant (Questco):** So there's no reason to check because if you pull it in wrong, that means it's wrong in PRISM.

**@49:27 — Chad Gregory (LaunchPad Lab):** Yeah, and is PRISM, yeah, I mean, this isn't really a Taylor question, I guess, but I wonder how Questco can like validate that they are manually entering those rates per rate band accurately.

**@49:46 — Jagger Sturdivant (Questco):** Yeah, that's, that would be a Lawanda question, because I think she does the entering for those.

**@49:53 — Chad Gregory (LaunchPad Lab):** Yeah. Okay, well. Just trying to think if I have any other thoughts.

**@50:20 — Nikki Dow:** Maybe another silly question. So we've gone through Kaiser and Aetna and how, or I guess BCVS to see how they define their rate bans. Do we basically need to be accounting for all of the carriers that are in Questco's master plans and how they define the rate bans?

**@50:50 — Jagger Sturdivant (Questco):** Those are the only three that assign rate bans. Everything else that's master is ancillary plans, which those have static rates. So they'll, they're rate bans. The rate group will be global, and it'll just map to the same rate every time for every client.

**@51:08 — Nikki Dow:** Okay.

**@51:12 — Chad Gregory (LaunchPad Lab):** And that's also how dental and vision work.

**@51:15 — Jagger Sturdivant (Questco):** Yeah, those rates are the same for every client.

**@51:17 — Chad Gregory (LaunchPad Lab):** Yeah. And what about for, like, if we get an OMQ, we're just going to get the rate, right?

**@51:26 — Jagger Sturdivant (Questco):** Yeah, you'll just have the numbers. There's no rate group.

**@51:31 — Chad Gregory (LaunchPad Lab):** Okay. Oh, this was a question. Does that rebanding file include all clients?

**@51:54 — Jagger Sturdivant (Questco):** It includes everybody who got that plan previously. Yeah, I think maybe we quote new people on it as well, but I am not sure. But like, yeah, even if their band doesn't change, they would be there. Like you saw on the Kaiser one.

**@52:14 — Chad Gregory (LaunchPad Lab):** Right. The band didn't change, but they were still there. Is that, sorry, is Questco putting together the rebanding file?

**@52:22 — Jagger Sturdivant (Questco):** No, the carriers do that.

**@52:24 — Chad Gregory (LaunchPad Lab):** Okay, but maybe Questco submits the clients to them?

**@52:28 — Jagger Sturdivant (Questco):** I believe so, yes.

**@52:30 — Chad Gregory (LaunchPad Lab):** Got it, so that's why like you could theoretically like, Questco could add some other clients on there if they were like, yeah, maybe these people will want to switch to Kaiser or whatever.

**@52:41 — Jagger Sturdivant (Questco):** Yeah, exactly.

**@52:43 — Chad Gregory (LaunchPad Lab):** Okay. What are the rebanding questions do you have, Nikki? Four questions in general. We've got five minutes. Have I broken your brains enough yet? I actually feel a lot better.

**@53:11 — Jagger Sturdivant (Questco):** Oh, that's good. Me, at least.

**@53:13 — Chad Gregory (LaunchPad Lab):** I'm not the one that has to write any code.

**@53:16 — Nikki Dow:** No, it's really nice being able to walk through it and chat about it, because it makes a lot more sense than when you're just trying to look at the workbook by yourself. So thanks, Jagger. appreciate it.

**@53:31 — Chad Gregory (LaunchPad Lab):** Yeah. I did want to, I talked with Chris right before this call, because he just wanted to kind of check in, and him and Scott will talk about the, like, change order stuff probably next week, early-ish. But I told him, like, we need to figure out a lot of the admin console stuff Monday with Anna. With that kind of in mind, Jagger, did you have any chance to think about the, like, changes to the workbook at all? Like, do you think that's still sort of doable for next week? I know Anna was out yesterday and today, so I don't know.

**@54:20 — Jagger Sturdivant (Questco):** Yeah, haven't had a chance to meet with her yet. I'll probably meet with her on Monday on that.

**@54:24 — Chad Gregory (LaunchPad Lab):** Okay.

**@54:24 — Jagger Sturdivant (Questco):** And then I'll have to let you know what we come up with to see if it's feasible to have that done at end of next week.

**@54:30 — Chad Gregory (LaunchPad Lab):** Okay. Yeah, let me know. Maybe I'll even, like, pop a ticket in there for you guys so that...

**@54:37 — Jagger Sturdivant (Questco):** Okay.

**@54:40 — Chad Gregory (LaunchPad Lab):** Let's see, workbook updates.

**@54:50 — Jagger Sturdivant (Questco):** By the way, Nikki, you're going to see another repository pop up in the GitHub. Before we started working with you guys, we had thought I that I was going to build Taylor, and so I kind of have like a preliminary, Taylor pulls all the data from Prism and builds a workbook out, and so I'm going to upload that code to a repo until you guys have access to it, because when you're rebuilding the current plans and the renewal plans, it already pulls everything that you would need. So it pulls like their plans, the rates, the plan designs, the benefit groups, it pulls all of that. So you guys will be able to see like what Prism calls you need to make, how you can pull the enrollment counts, and then you just kind of have to, you can reference that when you're rebuilding the, those two files.

**@55:44 — Nikki Dow:** That's awesome. Yeah, I'll keep an eye out for that, because that'll be really helpful to look at.

**@55:49 — Jagger Sturdivant (Questco):** Yeah, I'll send that out probably today.

**@55:52 — Chad Gregory (LaunchPad Lab):** Nice. Yeah. Okay, well, we can let you go, Jagger. Hopefully you get some good gaming in this weekend, and I don't know, Nikki, if I shortchanged you at all if you're a gamer too, but I knew that José was. So, yeah, enjoy the weekend, and we'll talk to you Monday. Sounds good. Thanks, guys. Thanks, everyone. Thank y'all.
