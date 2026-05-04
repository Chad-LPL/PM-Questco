# Benefit Guide - SBC Approach Discussion - April 29

[VIEW RECORDING - 31 mins (No highlights)](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj)

**Attendees:** Chad Gregory (LaunchPad Lab), Dimple Desai, Anna Fiske, Nikki Dow, Conor Hawes, José Blanco, Scott Brittain

---

[@0:00](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=0.0) - Chad Gregory (LaunchPad Lab)
I'm you to that tomorrow. Yes, please.

[@0:05](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=5.02) - Dimple Desai
That would be wonderful. If I don't have any conflicts, I will try my best to make it.

[@0:10](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=10.75) - Chad Gregory (LaunchPad Lab)
Yeah, that'll just be us three and Nico. But today, so maybe to lay some groundwork and Dimple, you didn't get to join us last Friday when we were going over all the benefit guide stuff.
But essentially, what we realized was that there is this other source for data that needs to be populated in the benefit guides, which is these SBC documents.
And they just come in PDF form, and there's one for every plan for every carrier. So on Friday, we essentially, we were going through all of the benefit guide pages and looking at all the different fields and making sure that we knew where to map to the workbook to get that information, the executed workbook.
And we came across these SPC items or items that would come from the SPC. which definitely brought up a fork in the road or something, something like that.
What was great was Anna was able to send us those examples so that we could look at them. We have looked at them at this point and wanted to figure out what we should do because it is...
It does diverge from the statement of work, but also we just need to figure out what's best for Questco and Taylor.
So, like I said, there's a document for every plan for every carrier. They're only available in PDF format. What's good is that, and I'll pull one up here.
Where's my, hold on up so we can look at it. Here. Oh no, where did I leave? Sorry about that.
I had, I know I have this open on one of my tabs. I'm just having trouble with my, with my tabs.
Oh, here we go. I think this is it. Now let me find. Here we go. Okay, I'm going to open this Kaiser one.
What is great is obviously they all come in a similar format or essentially identical format, I will say, where you have a table with the questions and it looks like all the questions are the same on these documents.

SCREEN SHARING: Chad started screen sharing - [WATCH](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=201.985203)

And then they've got columns for the answers. What is not the same is where the actual information that we're looking for kind of shows up and how it how it shows up.
So for example, just looking at like this. Deductible example, for Kaiser, says 2,500 individual, 5,000 family, and on the, let's just go to Aetna, it'll tell us like in network, 2,000 family, 4,000 out of network, 6,000, 12,000.
Additionally, there's like certain things like virtual visits, those don't necessarily show up like in the like what you will pay sections or anything, they're kind of over here in like the notes essentially.
So it's, it's just a little tricky. And I know like another factor to this was that we were seeing, and I'll let, I'll let Jose show like all of his examples.
But I know that today the way that the benefit guide is getting generated is handing off all of these to the third party along with the workbook and having them generate everything and that they do use AI or like an LLM to kind of pull it all in.
And when we were looking at the benefit guide together on Friday, we did notice some areas where that was causing issues.
I don't know if I'm going to be able to find it immediately, but... It was a vision page.

[@5:48](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=348.49) - Anna.Fiske
The vision was really inaccurate. Yeah.

[@5:52](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=352.11) - Chad Gregory (LaunchPad Lab)
And I think based on what I was seeing here, Anna, like it does need to make some guesses. So not guesses, but like there, for example, the Teladoc, it needs to find that.
And then it's doing like a normalization to say, yeah, that's $0. And if preventative care isn't on here, for example, then it needs to say NA or like hospital expenses, it needs to say NA.
Let's see, I've got Kaiser here. Let me go back to Kaiser. I think that this one didn't have or did have preventative care.
Why is this not working? Maybe it didn't have it. I thought it did. Oh, yeah, preventative care. So it says like no charge.
So it changes that to zero. Or no, it said NA, but I think it should have said zero, right?
Right.

[@6:57](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=417.39) - Anna.Fiske
Yeah. Yep.

[@6:58](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=418.89) - Chad Gregory (LaunchPad Lab)
Yep. So that would have been a mistake, actually. Well, actually, I don't know if this is the exact right plan.
Well, it's an inconsistency.

[@7:12](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=432.06) - Anna.Fiske
Like it should be $0 or NA for similar answers.

[@7:16](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=436.58) - Chad Gregory (LaunchPad Lab)
So I guess there's like a couple of things rattling around in my head is one, what is the actual best way to get this data into the benefit guide?
And two, what are the implications of that? I think our recommendation to make sure that the benefit guide is as accurate as possible is getting the data from these documents out of these documents into a structured format, whether that's, I mean,
In a super ideal world, think it would also be added to the workbook.

[@8:06](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=486.16) - Anna.Fiske
Yeah, that's not a bad idea.

[@8:09](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=489.33) - Chad Gregory (LaunchPad Lab)
Or Prism. But probably, I don't know if it could get into Prism. I don't think the amount that we need.
Too much. We would have the fields, yeah, for Prism. Yeah.

[@8:22](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=502.26) - Anna.Fiske
But the workbook would be ideal, and then you're just calling from the workbook for everything.

[@8:26](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=506.36) - Chad Gregory (LaunchPad Lab)
Mm-hmm. Right, exactly. Um, now, how to do that is a question. I know on Friday we talked about that a little bit, where it was, I think, Anna, you were worried that getting, having people go through all of these documents and doing that would be a massive task.

[@8:52](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=532.48) - Anna.Fiske
Mm-hmm.

[@8:54](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=534.48) - Chad Gregory (LaunchPad Lab)
I agree. I also think that if we... Tried to run all of the documents through an LLM, or if you guys did, and then reviewed it, reviewing would still be a pretty massive task, because you would want to make sure that it's all accurate.

[@9:16](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=556.761) - Anna.Fiske
Correct, but auditing that is something we already do today. So with our third party, they're doing that. They're taking these SBCs, running it through AI, and then we're having to validate that on our side.
Obviously, things are going to get missed here and there, but...

[@9:29](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=569.681) - Chad Gregory (LaunchPad Lab)
You validate it once it's in the benefit guide?

[@9:33](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=573.421) - Anna.Fiske
Yeah, we're supposed to be checking it once it's in the benefit guide. And again, the guide that I presented to you guys was a fresh one that they just made.

[@9:41](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=581.881) - Chad Gregory (LaunchPad Lab)
Yeah, and you didn't.

[@9:42](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=582.721) - Anna.Fiske
I didn't take the time to review every single page, yeah. Got it.

[@9:46](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=586.341) - Chad Gregory (LaunchPad Lab)
So how often are you catching stuff?

[@9:49](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=589.221) - Anna.Fiske
In the very beginning, we caught a lot, just because this was a new company to us, the third party was.
That was their first year doing open enrollment with us last year. So we caught... Yeah, fair amount. But I mean, it was kind of what we're seeing today.
Like the HSA page was missing completely in our guide. We would catch things like that.

[@10:07](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=607.321) - Chad Gregory (LaunchPad Lab)
The vision page being messed up. would catch things like that. Yeah. So we would send it back to them.

[@10:12](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=612.681) - Anna.Fiske
And I think they just manually corrected it. I don't think they re-ran or re-trained their AI.

[@10:17](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=617.141) - Chad Gregory (LaunchPad Lab)
Yeah.

[@10:19](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=619.021) - Anna.Fiske
But that's something I would kind of vote for is that we plug all of this into a utility. It puts all of these rows into Excel.
And then we have the benefits department verify that. And just, it's easier to look at an SBC that you kind of know by heart and you're checking the lines.
Like, yeah, I know it's 25 and 5,000. I know preventative is always going to say no charge. You know, it's kind of easier on the benefits department to do that.
Because we almost know this by heart.

[@10:48](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=648.501) - Chad Gregory (LaunchPad Lab)
Yeah. If they reviewed that, then it got put into the workbooks that we were just using the work. I mean, we could use that other document too, potentially, but.
Then, they review that. It does take, like, they're still going to want to look at the benefit guide before they send it to people, but it should be a lot more accurate, if not 100% accurate, in terms of those things, because we're literally, we would literally just be programmatically taking from a spot in the workbook versus, you know, generating it or, you know, having LLM parse it and pull it in.
Um, and make decisions. So, they would have, like, a yearly kind of big task of reviewing, reviewing it all, but their regular tasks, or, yeah, sort of regular, but also very heavy at a certain time of the year, um, would be less bad.

[@12:00](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=720.731) - Anna.Fiske
This would be better, though, because what they're doing currently is reviewing every single benefit guide against the SBC. So I'm going to get my benefit guides.
I'm going to check the Aetna Vision. Same as Chad, you're going to get all 20 of your benefit guides.
You're checking the same benefit that I am. They would have to check the benefit once. So we'd break up all the benefits between all of our individual people.
They would check it once and give it a thumbs up or give it a thumbs down. And then we move on and they don't have to check it again.
We're not having 20 people check Vision.

[@12:30](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=750.731) - Chad Gregory (LaunchPad Lab)
20 times. So it would be better. So like it's better for you.

[@12:35](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=755.741) - Anna.Fiske
I think so, yeah.

[@12:37](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=757.781) - Chad Gregory (LaunchPad Lab)
Okay. Let me ask the dev team, as we're talking about this, what thoughts do you have that are cropping up?
I mean, it sounds like we still want to run an LLM process to generate the review. Reviewable version, and then we want to take that reviewable version and get it into the workbook somehow, but that's not as bad as like building a part of the process to go find the SBC that we need and look up the information and pop it in.

[@13:34](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=814.681) - Nikki Dow
Yeah, it definitely sounds preferable to that latter option. I guess that, so this would have to be done each year.
We'd basically, everyone would be like generating and validating an updated SBC sheet that's going to go in the workbook.
So that basically means. We have like a new version of the workbook template every year.

[@14:08](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=848.231) - Anna.Fiske
Yes. Right.

[@14:12](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=852.951) - Conor Hawes
Well, guess, sorry, one quick question for clarification. This is for, like this information is used for chosen plans.

[@14:25](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=865.211) - Anna.Fiske
In the benefit guide, yes. Yeah.

[@14:29](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=869.511) - Conor Hawes
So, Nikki, is the proposal to have the SBC for every single plan in the workbook and then draw from the, you know, six or nine or 12 that are taken?

[@14:49](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=889.541) - Anna.Fiske
Oh, that's a good point. So if they're only offering Aetna, they wouldn't see the blue choice SBC information in their workbook.

[@14:58](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=898.231) - Chad Gregory (LaunchPad Lab)
Well, I wonder if the SBC. The is actually hidden, a hidden sheet in the workflow.

[@15:04](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=904.561) - Anna.Fiske
yeah, that's great, you can do that. I guess I was envisioning, because like the SPC is per plan, right?

[@15:11](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=911.381) - Nikki Dow
So I guess I was envisioning a hidden sheet or hidden sheets where like the rows are plans and then the columns are values that we need for the benefit guide.
And then that's hidden, but, you know, we can read it when we're benefit, when we're generating the benefit guide.

[@15:32](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=932.481) - Chad Gregory (LaunchPad Lab)
It's either that or that is a separate sheet that we have to read that one too every time. But, yeah, I mean, what were you thinking, Connor, of like, were you thinking that other option so that we were, yeah, I don't know.

[@15:56](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=956.401) - Conor Hawes
Yeah, mean, like, if we're not, if, like, size of the word. Workbook is not a constraint. Hidden sheets aren't really hidden, right?
So they can be opened up. So I guess it would be more of a question of like, I mean, I suppose all this information is available publicly?
Maybe or not? Yeah. I mean, I guess my kind of like intuition or preference would be that the workbook has only the information that's relevant for like the client's workbook has what's relevant for the client.
So maybe that could mean that the template has all of them and then we like delete some of the rows in the hidden sheet during the generation process.
Like that's also an option. That's not, I would say, too different from referencing a different Excel. It would also help with the side of the workbook and all that for it to actually get sent to the client.
So yeah, maybe that's something that we would start with and then decide if we need to pull it out into its own thing.

[@17:25](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1045.94) - Chad Gregory (LaunchPad Lab)
Yeah, almost like the current plans and renewal plans lists. We have to generate those, and those would be the same plans that we would need to show the SPC information for, right?
So it could be pared down to that, because they already see those on the summary pages, right, Anna? Like all that information.

[@17:49](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1069.69) - Anna.Fiske
Yep.

[@17:53](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1073.14) - Chad Gregory (LaunchPad Lab)
Okay, go ahead.

[@17:55](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1075.26) - José Blanco
Yeah, I was going to say, unless you're... We're going to be using the information to display to the client and the executed version of it, where only the pages that are visible to clients are available.
It doesn't really need to be in the workbook. It could be a separate file if it's not going to be referenced by any other sheets.
And that said, it would be preferable to have all the information in one place. And this would only need to be updated once a year.

[@18:39](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1119.36) - Nikki Dow
Yeah, I think it's a good point that it doesn't have to be in the workbook. I guess maybe one other thing we should think about, if the ultimate plan for the future is to move away from the workbook, do we really want to add to it now?

[@18:56](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1136.72) - Anna.Fiske
That's a good point. So then maybe it's more like...

[@19:01](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1141.91) - Nikki Dow
I don't know, it's still some kind of sheet that maybe we import or reference like outside of the workbook.

[@19:11](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1151.96) - José Blanco
Could be a good first step to moving away from it.

[@19:19](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1159.38) - Chad Gregory (LaunchPad Lab)
Okay, so then I think the steps here are one, we need to create a sheet that will be able to house the plans for all of the carriers, all of the plans for all of the carriers, and have columns, I think, for each of the items that we need out of the SPC to populate into the benefit guides.
Then, then, We'll need all of the SPC documents so that we can run them through a process to generate data into that template.
And then we would need the Questco team to review it. And then once it's reviewed, it would be ready to be used to generate the benefit guides.
Although we could, we wouldn't necessarily be, like, once we had the template and had the data in it, we wouldn't necessarily, like, be blocked development-wise to, like, use that to start generating, like, working on generating the benefit guides.
But obviously you would want it to be accurate when we were done. Does that sound right?

[@20:52](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1252.5) - Anna.Fiske
Mm-hmm. It does to me.

[@21:00](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1260.63) - Chad Gregory (LaunchPad Lab)
As I mentioned, there's definitely some scope creep there, but I think that gets you to the point where benefit guides will be generated more accurately, and you will have one for each benefit class, and it'll happen without the third-party vendor.
It'll happen immediately with everything else. So I think that is a pretty good bonus. I'm curious, I know you don't know this, Anna, because we don't have a real estimate on this work for you, but...
Like, do you, it seems in some conversations I was having with Chris a couple weeks ago, like, he might be interested in figuring out where to trade off scope for what's going, what's been going on with the benefit guides.
I don't think he knows. Well, Scott, did you get to talk to him about the SBC stuff?

[@22:24](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1344.93) - Scott Brittain
No, we never connected yesterday. Okay.

[@22:27](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1347.29) - Chad Gregory (LaunchPad Lab)
Yeah, I don't think he knows about this SBC piece, but he does know about multiple benefit guides per renewal for the different classes.
Is there any area from your vantage point, Anna, that maybe we should think about cutting back on a little bit more to make some room on that?
Or, because I feel like we're already pretty trying to be. you. As lean as possible with what the V1 is, but I'm curious if there was any area that you were thinking maybe you could live with more manual effort or scaled back scope or something like that.

[@23:18](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1398.62) - Anna.Fiske
I can't think of anything off the top of my head. I'd like to go through Asana and just kind of see what we've done so far.
And maybe something will jump out at me. Because I know we went back and forth on the admin console on whether that was needed or not.

[@23:31](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1411.26) - Chad Gregory (LaunchPad Lab)
But we decided it was.

[@23:33](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1413.06) - Anna.Fiske
But I still think we're being, like you said, kind of lean on everything we've done so far.

[@23:36](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1416.64) - Chad Gregory (LaunchPad Lab)
I know. And tomorrow you'll see more of that admin console stuff like I was mentioning on the designs. I think the biggest thing that we should cover there is just making sure that we have all the right information that you want to actually be able to see there.
I'm thinking like maybe one area which like we haven't. dug into a ton yet is like the post-enrollment validation stuff.
I know we just haven't really touched on that. But with this approach that we've talked about today, I want to give this as maybe like a preview for the status call.
With this approach that we've talked about today, Scott and I can work through building out the change order, getting estimates from the devs.
And I don't know that we will have everything in place by Friday. But I actually think we can have a decent plan built out in Asana.
And it may just be like a couple days after that to have like the change order fully ready to go.
And like, Make sure that we know the timeline super well. That's something that we've been working on this week is trying to get all of the tickets planned out at this point.
And we're through, I think I'm through Sprint 3. We just started Sprint 2. And so I've got a couple, like three more sprints to go.
I've got a ton of time to work on this tomorrow. But yeah, hopefully that feels decent to you.

[@25:32](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1532.31) - Anna.Fiske
Yeah, I'm good with that. That's the first thing Chris is going to ask is numbers, like what the quote looks like.

[@25:38](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1538.67) - Chad Gregory (LaunchPad Lab)
So I think we'd rather dig into dollars than scale back on the project. Yeah. That's my opinion.

[@25:45](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1545.47) - Anna.Fiske
I don't deal with the money though. Yeah, I know.

[@25:48](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1548.09) - Chad Gregory (LaunchPad Lab)
And I think it's just, you know, you never know exactly what you don't know until you get in there.

[@25:57](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1557.38) - Anna.Fiske
Right, right. Do you think that there are any...

[@26:00](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1560.0) - Chad Gregory (LaunchPad Lab)
Are other aspects like the SBC that we need to consider? I guess that was, I think, José, an open question that you had was like, is there any other source that we need to consider for the benefit guides before we kind of lock that in?

[@26:17](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1577.84) - José Blanco
Yeah, for the time being, and given like the samples that we had, it was only the Teladoc field, which wasn't present in one of the values.

[@26:32](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1592.88) - Chad Gregory (LaunchPad Lab)
I just wanted to make sure that there's this like, sometimes it shows up in different places. But basically, like, Anna, is the approach, if it doesn't mention virtual care, then we just put NA or something like that?

[@26:50](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1610.61) - Anna.Fiske
Yeah, that'd be ideal. Like, if it isn't mentioned, NA would be what we'd want there. But if it's no charge, like a zero dollar would be preferable.

[@27:00](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1620.0) - Chad Gregory (LaunchPad Lab)
So that we know it's included, it's just at no cost. Okay. José, was there anything else on the benefit guide itself that you were worried about or had a question on?

[@27:15](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1635.15) - José Blanco
Not for the time being.

[@27:16](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1636.99) - Chad Gregory (LaunchPad Lab)
That's good. Okay. Well, we handled this pretty quickly. know I had scheduled extra time, but I feel okay if everybody else does on this topic.

[@27:31](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1651.64) - Anna.Fiske
Yeah, I'm good on this one. I do have one thing that I want to talk about if we had time, but you go first and do something.

[@27:38](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1658.42) - Chad Gregory (LaunchPad Lab)
No, it sounds like we do. And I know we're going to talk more in a couple hours. So we've got some more notes and progress updates and everything for you then.
But I'll let you go ahead.

[@27:50](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1670.58) - Anna.Fiske
Something that I wanted to get scheduled probably next week is for you guys to sit with our implementation team.

[@27:56](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1676.24) - Chad Gregory (LaunchPad Lab)
And I want to make sure that so far we've captured everything that they need.

[@27:59](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1679.74) - Anna.Fiske
And I... Sat with them last week, and I felt like we had captured everything, but I kind of, I don't do implementation, so I don't know all the nuances, such as this SBC thing coming to light for us.
So I just wanted to schedule a meeting with you guys, with our implementation team, for them to go over the process.

[@28:18](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1698.72) - Chad Gregory (LaunchPad Lab)
And ask for their new clients, what happens in that process, and when are we ready to bring them into Taylor?

[@28:26](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1706.58) - Anna.Fiske
Right, yeah, and just to make sure that we're accounting for everything they have to do on their end, is being accounted for in Taylor.

[@28:34](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1714.8) - Chad Gregory (LaunchPad Lab)
Okay, that does touch on one of the tickets, Connor's taking this sprint, to make sure that we have all the possible, oh wait, actually, sorry, we bumped, I was thinking about the scheduling job, so it's not the sprint.
But, um, yeah, I think next week would be good then. Um. Do you have a time in mind, or do you want me to throw out sometimes?

[@29:06](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1746.22) - Anna.Fiske
I didn't look at the calendar yet. I didn't know if next week was too early, though. Like, if you want to finish up what we're kind of focusing on now, and we push it out a little bit further, we can do that, too.
I still want to forget that that's something I wanted you guys to, like, meet with them and just hear them go through their process.

[@29:23](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1763.34) - Chad Gregory (LaunchPad Lab)
See you, Dimple. Thanks. I don't think it's too early. I think it's better to get the information.

[@29:34](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1774.64) - Anna.Fiske
Okay, let me pull up their calendars, then. I'll just, I'll email sometimes over to you. I've got to pull up their calendars and see when they're available, and give you some time slots next week.

[@29:44](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1784.0) - Chad Gregory (LaunchPad Lab)
Yeah, that'd be perfect. Okay, then, did you have anything else?

[@29:50](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1790.2) - Anna.Fiske
Nope, that was it for me.

[@29:51](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1791.76) - Chad Gregory (LaunchPad Lab)
Okay, then we will hop off. We'll talk to you in, what, I guess? Two and a half hours. And then that'll mostly be focused on progress updates.
Nikki's going to give a little demo because she's got a couple of sheets that she can generate now. And we've got a couple of questions maybe for Jagger.
wanted, based on Chris's note last week, I wanted to try to keep things as like status oriented as possible.
But there were a couple of questions that popped up for one of the tickets that we're working on now.
And, you know, we can pop them into Asana for Jagger too, but it might just be helpful to at least talk over what we're seeing so that he has some context before he looks at it.
Sweet. Thank you so much. We'll talk to you soon.

[@30:55](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1855.08) - Anna.Fiske
All right. Thank you guys. Bye.

[@30:56](https://fathom.video/share/xX5-Yg_xvTY7ozvidvZVDLs1SVezp2Sj?timestamp=1856.44) - Chad Gregory (LaunchPad Lab)
Yeah.
