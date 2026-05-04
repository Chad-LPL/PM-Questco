# Taylor - Weekly Grooming/Office Hours - April 24

[VIEW RECORDING - 105 mins (No highlights)](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE)

**Attendees:** Chad Gregory (LaunchPad Lab), Anna Fiske, José Blanco, Conor Hawes, Nikki Dow, Jagger Sturdivant (Questco Cos)

---

[@0:00](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=0.0) - Chad Gregory (LaunchPad Lab)
All right. Sorry about that, folks. I was trying to get on Zoom for the last two minutes, and it wouldn't go from one Zoom to the other.
Okay. Hopefully everybody's having a good Friday, getting ready for a good weekend. Do we have any good plans on the Questco side of the fence for this coming weekend?

[@0:24](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=24.62) - Anna.Fiske
Well, I was just telling everybody that I bought a car, and it's like an old used car, but it's a 4Runner, so it's really fun.
I'm going to the DMV today to get all the stuff done so that I can go drive it this weekend.

SCREEN SHARING: Chad started screen sharing - [WATCH](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=31.806461)

that's my plan, unless I get stuck in the DMV and live there for the weekend.

[@0:41](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=41.24) - Chad Gregory (LaunchPad Lab)
Yeah, that's always the worry. I remember when I first moved to Illinois, I was going to get my license changed or whatever from Ohio to Illinois, and I showed up early to the DMV, and there was a line, literally.
Probably around the entire, like, parking lot. Like, imagine a parking lot the size that you would see at, like, a Walmart.
And it was all around, and I, like, got in line, and I waited, like, 45 minutes, and we had moved, like, 100 feet or something.
And I was like, there's no way I'm doing this today. I need to figure out, like, go to a different location or something, because this is crazy.
Um, so, my, yeah, prayer hands to you, and you don't deal with that, too. I hope not.

[@1:34](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=94.94) - Anna.Fiske
I think you win the DMV horror stories. Yeah. I guess.

[@1:39](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=99.28) - Chad Gregory (LaunchPad Lab)
Yeah. Um, all right. Well, hopefully you'll have somebody watching your daughter, too. Oh, yeah.

[@1:48](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=108.24) - Anna.Fiske
The husband's home. We'll be doing that. Perfect.

[@1:51](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=111.3) - Chad Gregory (LaunchPad Lab)
Um, okay. Let's jump into things. We've got something, we've got two hours on the, on the schedule here today.
I expect we'll probably use most of it at least. So the goals are to review the benefit guide spike documentation that José put together and primarily focus on the questions that José has after going through that process and looking at the pages that were provided and all of this so that we know, you know, how to build the benefit guide or guides for each renewal.
And then I've got some other questions that are mostly like confirmations, I think, here. I want to clean up this a little bit while José's talking and asking questions, but we will probably mostly be focused on the benefit guide.
And then we may be able to talk a little bit about the testing, I guess, concerns and think about that.
process a little bit too. So let me stop sharing and hand it over to José.

[@3:08](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=188.32) - José Blanco
Hello. So the way I'm going to go about it is I'll basically start going through the Master Benefit Guide with all the pages.

SCREEN SHARING: José started screen sharing - [WATCH](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=192.706789)

And at the same time, I'll be reading through my notes on each of the pages and ask a lot of questions about certain things.
Hopefully get some answers and note them down as we go. I think we can start with this one. We talked about, look at my notes for this.
We talked about this page having a small dynamic element, which is the number of days here. And we're supposed to be fetching this information from prison.
This number of days actually currently lives under data that is associated with a plan. So I wanted to ask, what do you guys currently do when you're building the benefit guide?
And there are multiple plans that have different number of eligible days. What number is displayed here? Or is that like a validation that you currently have that all plans must have the same number of eligible days to be able to be included in the same benefit guide?

[@4:44](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=284.84) - Anna.Fiske
Correct. Yep, that last one. So all the benefits that are going to be in that benefit guide will have the same waiting period.
So it would be that 30 days or whatever that is.

[@4:53](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=293.56) - José Blanco
Okay, let me let that down. I take it that the reps are in charge of this, of making sure that they all have the same number of days, correct?

[@5:21](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=321.11) - Anna.Fiske
Yeah, and just the way it's set up in our system, we just type it in once and it applies to all the plans within that benefit class or that benefit group.
So, yeah, we don't have the option to make it different between the plans.

[@5:34](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=334.73) - José Blanco
Okay, fair enough. We can move on. That's the only question I really have for... Oh, well, there was one more thing.
What will we replace this page with when you decide to pull it out because you're not going to be...
Owning brokerage over the plans so that we can maintain the correctness of the table of contents. Could this be still be a welcome to Questco, like a small part of this page that we always include to maintain the table of contents being correct?
Or could we move this further up and put it before the table of contents so that it doesn't change the numbering of the pages here?
We would also have to make it so that table of contents starts like at one and this wouldn't be included.
Would that be okay?

[@6:44](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=404.38) - Anna.Fiske
I think that's perfectly fine, yeah.

[@6:47](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=407.71) - José Blanco
Okay, let me let that down.

[@6:50](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=410.39) - Anna.Fiske
It's great idea.

[@6:54](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=414.88) - José Blanco
Kudos to Ifat for that one.

[@6:57](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=417.36) - Anna.Fiske
Kudos Mm-hmm.-hmm.

[@7:21](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=441.85) - José Blanco
Okay. So enrolling in benefits or have any questions page. We agreed that this is a static page and is always included.
Is that correct? Yep.

[@7:34](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=454.61) - Anna.Fiske
Perfect.

[@7:37](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=457.24) - José Blanco
Okay. So this is going to be the first page where there's a lot. The first thing is that we're going to be needing the logos so that we can have them in our code base.
And build these whichever way. You could provide those, we would be okay.

[@8:04](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=484.68) - Anna.Fiske
I'll put them in SharePoint right now so I don't forget.

[@8:08](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=488.73) - José Blanco
Okay, perfect. So my first question here is to confirm that the health summary tab doesn't expand or shrink vertically previous to where the used field starts.
So I'm going to pull up now the workbook sample, health summary. Let's see, look at some of the other ones that we had when we were having this discussion, but I've
believe there was some numbering at the top, like some sequencing on the word work that we were looking for.
Oh, it's hidden here. That's why. In rows one through four, there is some sequencing based on the plan numbers or something of the sort.
And we wanted to confirm that that doesn't expand vertically, altering the positions of these rows, basically. Is that...

[@9:35](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=575.781) - Jagger Sturdivant (Questco Cos)
So, actually in the new workbook, that sequence is gone. So those, yes, those don't grow vertically at all. It'll always be those fields for every plan.

[@9:47](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=587.521) - José Blanco
Perfect. Okay, let me note that down.

[@9:51](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=591.821) - Jagger Sturdivant (Questco Cos)
Anna, correct me if I'm wrong, but I don't think we've ever shown anything other than those.

[@9:56](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=596.101) - Anna.Fiske
Correct, yep.

[@10:09](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=609.911) - Conor Hawes
Speaking of the workbook, how's that, just a quick aside, how's that coming along, Jagger?

[@10:15](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=615.091) - Jagger Sturdivant (Questco Cos)
You should have it by the end of the day. I don't think we'll have the, like, full examples yet, because I think we're going to put the plan designs in Prism before we do that.
But you should be able to have, like, a template of the one I built, so you can at least see the layout and how all the data will be structured.

[@10:34](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=634.831) - Chad Gregory (LaunchPad Lab)
Great.

[@10:36](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=636.701) - Conor Hawes
And in terms of, that's awesome. Just one more quick question, sorry for the interruption, José. In terms of, like, I guess, the approval side, like, is that just going through you, Anna, or are you guys, is there, do you think there will be some time, like, meeting with, like, other individuals?
To make sure that they're comfortable with the changes. In the workbook?

[@11:05](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=665.601) - Anna.Fiske
Yeah. I think, no, yeah, we're good. No, because I already presented it to leadership yesterday with what Jagger had sent me, like a static image, and they loved it.

[@11:17](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=677.271) - Chad Gregory (LaunchPad Lab)
So we didn't have any changes on it.

[@11:19](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=679.211) - Anna.Fiske
So yeah, we're good on that. That's great.

[@11:23](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=683.261) - Conor Hawes
Awesome. Okay. Thank you.

[@11:25](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=685.961) - Anna.Fiske
Absolutely.

[@11:32](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=692.041) - José Blanco
Okay. If there's nothing else, I'll continue on. So some of the values used here, insurance, choices. So the first field that I'm not sure where this value is being pulled is deductible type.

[@12:01](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=721.781) - Anna.Fiske
That would be pulled from the summary of benefits and coverage, which is a pretty lengthy, detailed document. We call them SBCs, and that's something we have for every single plan to show the deductible type.
And again, the benefit guide that we have today is AI-generated through our third party. So they throw all of that material into it, the AI utility or whatever, and it generates the workbook for us.
But that would be on the SBCs, the deductible type. And the SBC is a flat PDF, and it's in extensive verbiage, I guess I want to say.
Like, it kind of spells everything out for you. So it's for people who want every detail of their coverage.

[@12:54](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=774.831) - Chad Gregory (LaunchPad Lab)
Okay.

[@12:56](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=776.731) - José Blanco
Do we have, does this information list? Somewhere else, like in PRISM or something?

[@13:02](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=782.881) - Anna.Fiske
I don't know. I'll take that as a takeaway to ask if it's in PRISM somewhere. I have a feeling it is because it reflects in their employee portal when they go in to make their elections.
It shows embedded. And the other one is aggregate. It's the other two, or the other one that you could have between the two.
So let me take that as my takeaway to double check.

[@13:31](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=811.731) - José Blanco
Okay. So I'll leave it as a follow-up question.

[@13:35](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=815.351) - Chad Gregory (LaunchPad Lab)
Yeah, I got that captured, Jose.

[@13:39](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=819.281) - José Blanco
Okay. In the meantime, I'm going to note that it currently, it lives in the SPC document.

[@13:46](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=826.821) - Anna.Fiske
Okay.

[@13:50](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=830.481) - José Blanco
Continuing within Physician Services, this And this, I wasn't sure where we're pulling this data from either.

[@14:10](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=850.581) - Anna.Fiske
That would be the SBC. So a lot of what's in the workbook, or I mean, a lot of what's in the guide might not be in the workbook, because we wanted to keep the workbook to a somewhat sensible size, because we do provide the SBCs after the fact, and it's in the guide.
So I can share what an SBC looks like, and you guys let me know if you can work with it or not.

[@14:38](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=878.611) - José Blanco
Yeah, it looks like it's going to be helpful, yeah.

[@14:42](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=882.751) - Anna.Fiske
Okay, yeah, I'll just send you one, just to look at, but they all look the same. Obviously, it's just different information, depending on the plan, but they're all the same, which is helpful.

[@14:54](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=894.211) - José Blanco
Yeah, but they have different details, right?

[@14:56](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=896.851) - Anna.Fiske
Right, yeah, but the layout's the same, even on a, like, even though it's a PDF.

[@15:00](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=900.001) - Chad Gregory (LaunchPad Lab)
Now the layouts are still the same. Okay. Okay. That's an interesting wrinkle, though, José. Maybe I don't, I just want to come, like, stick on this a little bit.

[@15:17](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=917.531) - José Blanco
Yeah, I think lives in the SVC is going to be the answer to a lot of the questions I'll have today.

[@15:23](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=923.931) - Chad Gregory (LaunchPad Lab)
Yeah, I'm sure it is. So do we need to build a document that has that information that we can, a structured document?
Kind of like a, like a spreadsheet to get that information, uh, or, like, would that exist already anywhere, Anna?
Or is it only in the PDF version?

[@15:52](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=952.701) - Anna.Fiske
Yeah, think they could have it somewhere else.

[@15:54](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=954.821) - Chad Gregory (LaunchPad Lab)
I know you said that you were going to check Prism for some of this stuff, too, but.

[@16:02](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=962.561) - Anna.Fiske
Yeah, I don't think we're going to have it in Excel format, but we will, I mean, we have every single SBC as a PDF.

[@16:09](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=969.981) - Chad Gregory (LaunchPad Lab)
Yeah, would it be crazy? Do these update every year or like every?

[@16:16](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=976.741) - Anna.Fiske
They do update every year, yeah, because the, on the SBC, it has your effective dates, so it's 1-1 to 12-31 of whatever year.
So if nothing else changes, we still have to get new ones to have that date updated.

[@16:30](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=990.961) - Chad Gregory (LaunchPad Lab)
That's for every single plan that's offered.

[@16:33](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=993.861) - Anna.Fiske
Yeah. Well, master, for every single master plan.

[@16:37](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=997.641) - Chad Gregory (LaunchPad Lab)
Every single master plan, which is still like, yeah. That's It's a lot of weird. Yeah. I don't know, I was just wondering if it is reasonable to build out that document, that structured document off of the PDFs, or.
If that's crazy. I mean, yeah, I don't know. I'm just trying to think of options. The approach that is probably crossing some minds is like, well, why don't we just do what that other third party was doing?
I just, I've, I know that then there's like a worry of accuracy and it's kind of implementing a whole other AI thing that we're not doing anywhere else yet.
That is something that we wanted to do, like OCR for other things in the future, but I'm wondering, I'm trying to think like what the best approach to that might be.
It seems a little crazy to have you create a bunch of documents.

[@18:01](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1081.04) - Anna.Fiske
I feel like a human to do that, to take all the information off the PDFs and put it into Excel, that would be a huge lift.
We'd have to have a dedicated person just doing that for like a month.

[@18:12](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1092.17) - Chad Gregory (LaunchPad Lab)
Yeah. Within so many. Even if we did a one-time or annual, I mean, hopefully it would be one-time thing where we ran them all through AI to generate these documents, then somebody needs to review all of that before we use it.

[@18:35](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1115.99) - Anna.Fiske
But that could be a team effort as far as the benefits team, because they're the experts on our medical plans.
we could say, hey, you take half of Kaiser, you take 10 of Aetna, and like, I mean, we have like 10 people in the benefits department, so we could split it up and make it a team effort to get that audited.
That would be the most reasonable way, I think, to do it.

[@18:56](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1136.59) - Chad Gregory (LaunchPad Lab)
Yeah. Yeah. If we... Probably LaunchPad, found or like had fields for all the data that we need for the benefit guide in a spreadsheet, ran through Claude or something, all of the PDFs that you have for all the plans for all the SBCs to generate that or those files, or I don't know if it would be multiple files or a single file, and then have your team review those things and edit.
Okay, let's think about it a little bit more, but José, I'm sorry if I derailed you a little bit.

[@19:51](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1191.52) - José Blanco
No, it sounds perfectly fine. It's something that we have to think about. So continuing on, like I said, it's probably going to be a lot of in the SBC, but this field as well, would this come from the SBC as well?

[@20:13](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1213.57) - Anna.Fiske
I think that's in the workbook. Okay. But the answer is going to be if it's not in the workbook, then it's in the SBC.

[@20:21](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1221.91) - Chad Gregory (LaunchPad Lab)
Okay.

[@20:23](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1223.61) - Anna.Fiske
Which one were you looking at, José? The preventative. It could also be labeled as a wellness. I don't see it.
No, it's not in the workbook. But that's always 100%, so I don't think we needed to reflect it in the workbook.

[@20:44](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1244.38) - Chad Gregory (LaunchPad Lab)
Yeah.

[@20:55](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1255.62) - José Blanco
Okay. Okay. Hospital services, inpatient hospital, would be this one?

[@21:16](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1276.0) - Chad Gregory (LaunchPad Lab)
Yeah.

[@21:26](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1286.3) - José Blanco
But outpatient hospital expenses is not here, right?

[@21:31](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1291.72) - Anna.Fiske
Correct, yeah.

[@21:48](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1308.93) - José Blanco
Outpatient surgery, also SBC?

[@21:56](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1316.58) - Conor Hawes
22 and 23.

[@21:59](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1319.24) - Chad Gregory (LaunchPad Lab)
Yeah. 23, Surgery Outpatient. Okay. Complex Medical is there, Diagnostic X-ray is there, Urgent Cares.

[@22:16](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1336.52) - José Blanco
Ambulance is the next one that I have a note on, which is over here.

[@22:24](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1344.58) - Chad Gregory (LaunchPad Lab)
That would be SBC, it seems like.

[@22:28](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1348.64) - Anna.Fiske
Yep, SBC.

[@22:33](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1353.34) - José Blanco
Preferred Brand Name and Non-Preferred Brand Name.

[@22:42](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1362.97) - Anna.Fiske
So, I wasn't sure which of these were like Formulary and Non-Formulary, which is why I have these questions. So, Pharmacy Formulary is going to be Preferred Brand Name.

[@22:54](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1374.63) - Chad Gregory (LaunchPad Lab)
Yep.

[@22:55](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1375.77) - Anna.Fiske
Non-Formulary is going to be Non-Preferred Brand Name. Yep.

[@23:00](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1380.02) - Chad Gregory (LaunchPad Lab)
Specialty is Pharmacy Specialty. Yeah.

[@23:05](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1385.28) - Anna.Fiske
They're in order, but I do see how the language is confusing.

[@23:10](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1390.82) - José Blanco
Yeah. In the previous section, Emergency Room, they're not always in order, so that's why I wasn't. But yeah, so Formulary and Non-Formulary.
Okay. After that, I have...

[@23:28](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1408.7) - Nikki Dow
Sorry if I missed this, but there's two prescription sections. The bottom one's mail order 90-day. There's something hiding my view of the one above.
Did we identify where those different figures come from?

[@23:50](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1430.62) - José Blanco
Oh, I think that's why. Wait, let me see. Because I have four or five warnings in this.

[@24:00](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1440.0) - Anna.Fiske
Yeah, those would both be from the SBC.

[@24:08](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1448.41) - José Blanco
All of the mail orders?

[@24:11](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1451.17) - Anna.Fiske
Yeah, like the retail 30-day supply and the mail order 90-day supply, that gets pulled from the SBC because those can differ.
In the pharmacy, mail order times two, that just means, I think that means, I what two times means, I think it's 60 days, like times two is, you can get mail order for two months.

[@24:38](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1478.13) - Chad Gregory (LaunchPad Lab)
I think that's what that means.

[@24:39](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1479.43) - José Blanco
Oh yeah, this is not displayed in the benefit guide, so I didn't get to worry about it, but when you said earlier that those two can't differ, are we talking about they can't differ between like
Like preferred and non-preferred, or they can't differ between 30 and 90 days?

[@25:07](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1507.32) - Anna.Fiske
Yeah, like those can be different depending on the carrier. That's something that we get to negotiate. So like blue choice, it'll be 30 days and 90 days for every single plan.
But like Aetna might not be 30 days and 90 days. Like on this side, Aetna is 60 days, two times.
I order is two months, so it's 60 days. That one says 90 days, so maybe I'm lying. I don't know if it's two times.

[@25:39](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1539.7) - José Blanco
Okay.

[@25:42](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1542.61) - Anna.Fiske
I'll have to figure out what that means.

[@25:45](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1545.17) - José Blanco
Okay, I'll add a note for that then to follow up. Let me go. This would be, I'll put it as an Aetna note.

[@26:00](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1560.5) - Anna.Fiske
Really needs to be a workbook note, like what is the two, because it's going to be in all the plans, it's going to be the blue choice in the workbook, it's going to say two times or three times, like I don't know if that's times a cost, times a time, like a length of time, I don't know what that means.

[@26:16](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1576.6) - Chad Gregory (LaunchPad Lab)
It's like follow up on the pharmacy mail order.

[@26:19](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1579.64) - Anna.Fiske
Yeah, yes, please. José, are you the one sharing? Yes. Are you okay if I just take a quick screenshot of the guide right there and just ask somebody real quick?

[@26:44](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1604.13) - José Blanco
Go for it, yeah. Okay, thank you.

[@26:49](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1609.13) - Anna.Fiske
I always like to ask if I'm screenshotting someone's screen.

[@27:15](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1635.26) - Chad Gregory (LaunchPad Lab)
What's next on your list, José?

[@27:18](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1638.56) - José Blanco
Are you done, Ed?

[@27:20](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1640.34) - Anna.Fiske
Yes, thank you.

[@27:21](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1641.52) - José Blanco
Okay. So we said that the mail order prescriptions are going to be coming from the SBC, regardless if they're like 60 or 90.

[@27:30](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1650.8) - Anna.Fiske
Correct.

[@27:31](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1651.54) - José Blanco
Except for the generic field, which is, let's have it that comes from line 32. Wait, what does it mean?
Like, pause me, don't know, let me check on that.

[@27:43](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1663.8) - Anna.Fiske
Let's just say they don't come from the SBC, because I'm not sure.

[@27:53](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1673.68) - José Blanco
Oh.

[@27:58](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1678.32) - Anna.Fiske
You know, it might be times two than just. Generic price, because the math is that it's 2 times 10, which is 20, and that's what it shows in the guide.
That might be what it is.

[@28:12](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1692.35) - José Blanco
Yeah, I have something odd here.

[@28:16](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1696.69) - Chad Gregory (LaunchPad Lab)
2 times 10, 2 times 45, 2 times 70.

[@28:22](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1702.5) - Anna.Fiske
I'm like 90% sure that's what it is, because we negotiated for 90 days, so you basically get a month free if you do the mail order, I'm pretty sure.

[@28:36](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1716.38) - Chad Gregory (LaunchPad Lab)
But I will triple check. What were you going to say, José?

[@28:39](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1719.96) - José Blanco
I had a note that prescription for 90 days generic was row 32, which doesn't make sense, because unless it's like you're saying, like this time.

[@28:54](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1734.57) - Chad Gregory (LaunchPad Lab)
Yeah, it is that. It's that times whatever it was above. See you, Conor.

[@29:02](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1742.17) - Anna.Fiske
Yep, that's what it is.

[@29:07](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1747.9) - José Blanco
Okay, so the other three values are still, those are SBC, right? For the 90 days, is that correct?

[@29:19](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1759.02) - Chad Gregory (LaunchPad Lab)
Yes, I'll double check if it's listed in the SBC.

[@29:21](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1761.84) - Anna.Fiske
If not, it's just spelled out in the guide because it's the retail 30-day supply times two. And they might have just put those numbers down there.
But let me double check one of the SBCs. I think that's right.

[@29:43](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1783.08) - José Blanco
Oh, they're just like double the other amounts? Exactly.

[@29:57](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1797.3) - Chad Gregory (LaunchPad Lab)
So maybe the, actually the workbook could be a little bit more. More descriptive about that. could say non-mail order times two, but yeah.

[@30:13](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1813.31) - Anna.Fiske
So it's not specifically laid out in the SBC for the mail order. It has to be what we're talking about then.
It says it in words, but it doesn't say it in numbers like that. It just says, you know, it's twice the premium of the retail.
Okay.

[@30:35](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1835.18) - Chad Gregory (LaunchPad Lab)
Okay, I'll add a note that it's row 32. Times the retail number.

[@30:46](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1846.0) - José Blanco
But the case for the preferred brand is times the regular formulary. Okay.

[@30:57](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1857.16) - Anna.Fiske
Okay. MultipleBT. like Thank

[@31:04](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1864.09) - José Blanco
And then this would be, oh, wait, the pharmacy specialty for, it's the exact same value, it's not two eyes.
Okay, so it's just the same as row 31?

[@31:33](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1893.58) - Anna.Fiske
Yes, because you can't get specialty drugs through the mail, I believe. That's like your GLP-1s and that kind of stuff.
I don't if you can get that through the mail.

[@31:47](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1907.89) - José Blanco
Okay, let's continue on with the next page. So, medical insurance continued. I'm going to go back a few pages back because we skipped a few.
Blue choice continued. This would be it. It's this one. Is there anything, there's nothing dynamic about this page, right?

[@32:18](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1938.63) - Anna.Fiske
Correct. Yep.

[@32:20](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1940.57) - José Blanco
And the conditional rendering for this page is if there is at least one blue choice plan being offered? Correct.
Another question that came up for us is does the blue choice logo always include South Carolina or is the logo in this master document a regional one of some sort?

[@32:54](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1974.47) - Anna.Fiske
No, it's always included in the logo because it's blue choice of South Carolina. That's where the plan is. It's in
Minister.

[@33:01](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1981.71) - José Blanco
Okay.

[@33:09](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=1989.68) - Nikki Dow
Does that mean like logos are tied to plans? Like not, not, they're not as broad as just to carriers?

[@33:21](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2001.89) - Anna.Fiske
No, they are. They're just for carriers. Yeah. So as long as you offer one blue choice plan, you're going to have this page and that logo is the logo.
South Carolina is part of that logo. So someone in Texas can have this plan and it's still going to say South Carolina.

[@33:38](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2018.23) - Chad Gregory (LaunchPad Lab)
If that's what you were asking.

[@33:43](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2023.43) - Nikki Dow
I think so. So there's not like anyone who's going to see blue choice health plan, Illinois. Correct. Correct.

[@33:52](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2032.99) - Anna.Fiske
Okay.

[@33:55](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2035.43) - José Blanco
Okay. That's all I had for that page. Kaiser, we also need this logo, it's one of the notes I have.
Yeah, the rest of the questions regarding the mappings are the same as the previous page, so we're solved for those.
This page is Kaiser number two. So this is a static page that's conditionally rendered when there's at least one Kaiser plant, correct?
Correct. Okay. Spawn, Aetna. Oh, this is the note that I just added. I was like, I've never seen this before.
Okay. Beatable. Nothing new there. Let's go to the continued page. Is this a static, conditionally rendered page as well?

[@35:59](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2159.25) - Anna.Fiske
Unfortunately, It's not, because I see the waiting periods up there.

[@36:02](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2162.34) - Chad Gregory (LaunchPad Lab)
So when would my coverage begin?

[@36:04](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2164.12) - Anna.Fiske
Coverage begins on the 1st. So I don't know why that's in there.

[@36:12](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2172.22) - José Blanco
Which line? I'm sorry.

[@36:13](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2173.94) - Anna.Fiske
It's the second blue header. When would my coverage begin? it has their wait, like first of month following your waiting period.
Oh, never mind. That's static. That's just. Okay, so we're good. That's static. Yeah.

[@36:27](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2187.21) - José Blanco
That's static. Okay.

[@36:29](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2189.91) - Chad Gregory (LaunchPad Lab)
Is the. The bolded part always the same? Yes.

[@36:35](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2195.65) - Anna.Fiske
Okay.

[@36:36](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2196.23) - Chad Gregory (LaunchPad Lab)
Yeah.

[@36:36](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2196.57) - Anna.Fiske
Our Aetna plans renew every January 1st, no matter when you come on board.

[@36:40](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2200.69) - Chad Gregory (LaunchPad Lab)
Great.

[@36:46](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2206.7) - José Blanco
Okay. So now to Aetna's network of support and access. Does this look static? And is there anything that I might have missed?
Nope.

[@36:59](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2219.84) - Anna.Fiske
That's. Okay.

[@37:15](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2235.0) - José Blanco
Is this the same?

[@37:17](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2237.53) - Anna.Fiske
Yes.

[@37:19](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2239.95) - José Blanco
Okay. There are some assets like this image that we'll be needing to be able to rebuild it. We could try pulling it from this file.
It might lower the quality. So that's just something to take into account. Do you happen to have these resources at hand?

[@37:41](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2261.61) - Anna.Fiske
I don't, and I'm kind of okay if we don't include it, to be honest.

[@37:47](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2267.47) - José Blanco
So we can remove the image?

[@37:49](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2269.29) - Anna.Fiske
Yeah, in my opinion. mean, I don't see the need for it, to be honest. I they were just filling the page.
Okay.

[@38:10](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2290.04) - José Blanco
Notices and disclosures. That's static, but we will have that updated for you guys.

[@38:17](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2297.13) - Anna.Fiske
That changes every year, but it's still static.

[@38:22](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2302.6) - Chad Gregory (LaunchPad Lab)
Okay. And so the approach I think that we're talking about, José, correct me if I'm wrong, is they would just swap this out when it changes, right?

[@38:36](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2316.03) - José Blanco
We're discussing a generational approach for the benefit guys, so it might be on our end. Could you give me like an example of what changes in this page year to year?

[@38:49](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2329.63) - Anna.Fiske
On the left column at the very bottom, the edit disclosures, sometimes that gets updated depending on what's going on with the government.
So a good example is like Obamacare. The ACA and that kind of stuff. That was a huge change to the disclosures for who's covered, why they're covered, how much they're covered at.
So that could change. But we would provide this page for you if it did change.

[@39:18](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2358.3) - José Blanco
But once we provide it to you, it would be static.

[@39:20](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2360.44) - Anna.Fiske
As far as if they offer it, they get this page, nothing changes on it. Okay, so at least it will remain static copy.
Okay. Yes. Yep, yep, yep. And nothing could change. depends on the government.

[@39:45](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2385.16) - José Blanco
So to health advocate. When is this page rendered and what are the conditions?

[@39:56](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2396.48) - Anna.Fiske
So that would be added if they're offering... A master medical plan, so Blue Choice, Aetna, or Kaiser, that's included in those master plans.
So they would get this automatically.

[@40:15](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2415.03) - José Blanco
When there is a, can repeat that for me? Sorry.

[@40:18](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2418.41) - Anna.Fiske
Yeah, when a master medical plan is being offered, so our masters are going to be Blue Choice, Aetna, or Kaiser.
If any of those are being offered, they would get this page because it's included in those medical plans.

[@40:46](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2446.48) - José Blanco
Perfect. Got that. So now we go on to compare MathsRx. Does this have any special conditions like that?

[@40:58](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2458.82) - Anna.Fiske
No. Um, Jagger, is that in the workbook to elect or no, in the new one that you just did?

[@41:05](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2465.6) - Jagger Sturdivant (Questco Cos)
Um, it's not right now, but I can add it.

[@41:08](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2468.83) - Anna.Fiske
I don't think it needs to be added. This is free, so it doesn't cost our clients anything to have it.
It's exactly like GoodRx, that little discount card that you can pick up at any pharmacy. So I think this should be included in every single guide, no matter what.

[@41:20](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2480.71) - Jagger Sturdivant (Questco Cos)
Oh, okay.

[@41:22](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2482.25) - Chad Gregory (LaunchPad Lab)
Okay.

[@41:23](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2483.13) - Anna.Fiske
Because it's free, so they should be able to use it if they want it. Now, if a client's, like, getting it out of there, how dare you?
We'll just remove it manually.

[@41:31](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2491.14) - Chad Gregory (LaunchPad Lab)
Yeah. How dare you? I know.

[@42:06](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2526.15) - José Blanco
Okay. And one question there, I suppose it follows that up. If a client asks to remove this page, how would we, where in the pipeline would we do that?

[@42:22](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2542.01) - Anna.Fiske
We would just have the benefit specialist remove it manually. They can just pop in there and delete the page.

[@42:30](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2550.98) - José Blanco
Okay. And then we have the issue of the table of contents. Don't have that stupid table of contents.

[@42:46](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2566.14) - Anna.Fiske
At that point, we'll just disclose it to the client. Like, hey, it's going to be in your table of contents, but we'll remove it.

[@42:52](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2572.24) - Chad Gregory (LaunchPad Lab)
Okay.

[@42:54](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2574.29) - Anna.Fiske
Because we haven't had one client reject it. I just don't see that happening for this page specifically.

[@43:04](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2584.75) - José Blanco
Okay, got that. So now on to walk through Medicare.

[@43:35](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2615.81) - Nikki Dow
Oh, sorry. One more question about if that gets removed. How does that fit in? How does that like manual removal process fit in when we consider DocuSign?
Like, is there a manual review and like editing happening on this benefit guide before?

[@44:00](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2640.01) - Chad Gregory (LaunchPad Lab)
We send the document to DocuSign?

[@44:02](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2642.67) - Anna.Fiske
It wouldn't. It would not be removed before they are able to sign the CDE, but it would just be something to say, hey, we don't want this page in there, can you remove it?
And we would just pull it out then.

[@44:17](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2657.4) - Chad Gregory (LaunchPad Lab)
And they're already, I think, I think I remember they're already able to do that through the current client space DocuSign process, right?
Like they, the rep would have a way to access the DocuSign configuration, swap it out. Yeah, okay. Correct, yeah.

[@44:37](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2677.85) - Nikki Dow
Okay.

[@44:40](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2680.27) - José Blanco
Any other questions regarding this page or the flow? If not, I'm going to move on to the next one.
Walk through Medicare. Is this page conditional in any regard? Or, or... No, it's just like CompareRx.

[@45:03](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2703.02) - Anna.Fiske
So it's just a service that we offer, but it doesn't cost anything.

[@45:08](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2708.04) - José Blanco
So it's free and always made available to clients?

[@45:11](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2711.93) - Anna.Fiske
Correct, yep.

[@45:14](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2714.5) - José Blanco
Okay. So now to Medlink. Is this a carrier, and these are actually going to be plans that they have templated as options on your provider at the moment?

[@46:11](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2771.8) - Anna.Fiske
So this one is they choose to offer APL, but they don't get to choose which option to offer. The employees have the option of both.
So if they select APL gap in the workbook, then this page will be static.

[@46:27](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2787.47) - Chad Gregory (LaunchPad Lab)
Okay. Okay, so the page is not dynamic, but it's conditionally rendered.

[@46:34](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2794.17) - Anna.Fiske
Yeah.

[@46:35](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2795.34) - Chad Gregory (LaunchPad Lab)
How does that work on the actual enrollment, Tanya? When they go into the, you mean in the portal? Yeah.

[@46:42](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2802.75) - Anna.Fiske
So we show both of them, option one, option two, and then they elect one or the other, and they cost different because they pay out differently, but it's still an enrollment just through APL.

[@46:52](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2812.91) - Chad Gregory (LaunchPad Lab)
Okay. Does that change anything about how Taylor needs to handle? That selection? No, because the- Client's just electing APL as a whole, and then it narrows down to the employee level of what they're electing, which Taylor's not involved in the enrollment don't have to like, we don't have to like send two things for the, for the one selection or something.

[@47:14](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2834.29) - Anna.Fiske
Correct. Yep.

[@47:15](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2835.87) - Chad Gregory (LaunchPad Lab)
Yep.

[@47:16](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2836.41) - Anna.Fiske
Yep. I thought we got rid of the gap plans. We, they, they try to, I like it. I'm bringing it back.
So. Oh, okay.

[@47:24](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2844.35) - Jagger Sturdivant (Questco Cos)
Fair enough.

[@47:25](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2845.79) - Anna.Fiske
Yeah. Okay.

[@47:28](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2848.34) - José Blanco
okay. So it's conditional based on, uh, are the plans called APL as well, or are they called gap or what?

[@47:35](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2855.62) - Anna.Fiske
They're called gap. So it'd be gap option one, option two, the company that sell, that administers the gap insurance is APL.
So the carrier's APL, the plans are gap.

[@47:48](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2868.88) - José Blanco
Okay. So yes, conditional based on the gap plan being made available. Okay. So now to hospital indemnity. Um.

[@48:01](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2881.06) - Anna.Fiske
This one's the same as the APL. It's static but conditional on the election.

[@48:06](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2886.86) - José Blanco
Okay, let me note this.

[@48:09](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2889.5) - Anna.Fiske
And that's going to be the case for the next one, two, three, four pages.

[@48:20](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2900.99) - José Blanco
And what's the name of the plan for this one?

[@48:23](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2903.83) - Anna.Fiske
Hospital Indemnity.

[@48:26](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2906.23) - José Blanco
Oh, that makes sense. Okay. Accident Insurance, it works the same then?

[@48:40](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2920.37) - Anna.Fiske
Yes. Do you guys mind if take 30 seconds to go let the dog out?

[@48:43](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2923.69) - Chad Gregory (LaunchPad Lab)
I'm going to start waiting. Anybody who needs a little bit of a break can't, since we're going to be keeping going.
But, José, yes, she said the Accident Insurance, the hospital cash. Cash, Critical Illness, and Cancer Advocate, we're all the same.

[@49:06](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2946.53) - José Blanco
Accident, Insurance, Point.

[@49:46](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2986.83) - Anna.Fiske
Thank you, guys. I'm back.

[@49:48](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2988.41) - Chad Gregory (LaunchPad Lab)
No problem. Just to confirm, you were saying Accident, Hospital Cash, Critical Illness, and Cancer Advocate are all the same.

[@49:59](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=2999.77) - Anna.Fiske
Yep. Yeah, yep, yep, yep. They're all static, but conditional on the election.

[@50:06](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3006.58) - José Blanco
Okay, and are all the plans named exactly the same as the page?

[@50:10](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3010.74) - Anna.Fiske
Yes.

[@50:12](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3012.96) - José Blanco
Okay, so hospital identity, accident insurance, hospital cash. Okay. Sorry, did you mention that this one was as well?

[@50:23](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3023.66) - Anna.Fiske
Yes. Yeah.

[@50:26](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3026.4) - José Blanco
Sorry, I'm writing a lot at the same time. Yeah, you're fine.

[@50:29](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3029.4) - Chad Gregory (LaunchPad Lab)
You're good.

[@50:30](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3030.54) - Anna.Fiske
And the next one is as well.

[@50:34](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3034.15) - Chad Gregory (LaunchPad Lab)
Then we get to dental. So now...

[@51:00](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3060.01) - José Blanco
Oh, we're in dental benefits. Okay, so first of all, is this actually dynamic, these plans, or are they just like fixed based on the carrier in some way?

[@51:26](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3086.22) - Anna.Fiske
They'll be dynamic the same way the medical page is. So it depends on what they like in the workbook as far as low, high, and high plus.
Sometimes they can not offer the low, only have two plans.

[@51:43](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3103.0) - José Blanco
Hmm, hmm, okay.

[@51:46](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3106.5) - Anna.Fiske
So the information's static, same as medical, but it is dependent on the elections. So this information is static. Yes.

[@51:57](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3117.94) - José Blanco
This, and... This, and we'll need the image here as well. Okay, and regarding mappings, I have my mappings over here.
I'm going to pull up, let me put them side to side. So we've got dental page, close over here.
I have the deductible being pulled from the plan column and rows 7 and 10. That's, yeah, that looks correct.

[@52:43](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3163.93) - Anna.Fiske
It would be rows 15 and 16. That's the deductibles.

[@52:56](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3176.69) - José Blanco
Oh. Wait a sec. Let me update that, sorry. Yeah, that's why we're checking.

[@53:19](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3199.34) - Anna.Fiske
Absolutely.

[@53:22](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3202.17) - José Blanco
I'm also not sure this was the exact document that I used to build this, but maybe it just looks different because I can't see the hidden rows over here when I was doing it initially, but they are still counted, so I can't excuse myself.
All right, so preventive services, I have it as row 17, basic services, row 17. 18, but I have a question mark on it.
Is basic restorative basic services?

[@54:11](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3251.32) - Anna.Fiske
Yes, yes.

[@54:14](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3254.93) - José Blanco
Okay. Major services is just major restorative then. Right. I can't remove these checks. Orthodontia lifetime maximum row 14. I have a question around that value.
So over here, I saw that in my sample data, have like, NA is a possible value. So I was wondering, what should I be expecting in the workbook when you want NA to come up?
Is it going to be a zero or NA tags or no value? Is it

[@55:00](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3300.01) - Anna.Fiske
Can you scroll over just a little bit? Because it should be in there.

[@55:03](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3303.55) - José Blanco
Oh, there should be at least one plan here?

[@55:05](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3305.97) - Anna.Fiske
Yeah, if you scroll over, it should be below.

[@55:08](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3308.19) - José Blanco
Oh, sorry. This is...

[@55:12](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3312.64) - Anna.Fiske
So it says any. Yep, so you'll see.

[@55:14](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3314.72) - Chad Gregory (LaunchPad Lab)
Okay, that's good.

[@55:18](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3318.34) - José Blanco
I'm still finding it. Okay. Okay, so that's the literal text.

[@55:23](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3323.22) - Chad Gregory (LaunchPad Lab)
Perfect.

[@55:28](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3328.64) - José Blanco
Actually, shouldn't have taken that away. Okay, so let me add an answer here to that.

[@55:35](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3335.48) - Chad Gregory (LaunchPad Lab)
Those last two look like they're SBC things. The in-network claim payment basis and the out-of-network.

[@55:52](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3352.11) - Anna.Fiske
Correct.

[@55:53](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3353.15) - José Blanco
Yeah, I have triple warnings that I have, like, no idea. So is SBC?

[@55:58](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3358.96) - Anna.Fiske
It is. Let me pull the SBC and see where that is. But yeah, that's definitely going to be in the SBC.

[@56:29](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3389.44) - José Blanco
Okay. That was my last question regarding this page. Is there anything else I should check into account? We need the logo, I believe, if I haven't mentioned it.
Also this. And if we're keeping the image, we'll need the image as well.

[@56:49](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3409.85) - Anna.Fiske
Okay. Can you hold it right here on the screen real quick? I just want to read it. It's negotiated fee schedule and then fee schedule.
I don't see that in the SBC. So I wonder if that's like a... Static, almost like a cop, like we don't know, it's going to be on schedule, you know what I mean?
Because we don't have the information to provide, but don't see it in the SPC. So negotiating, in that word, client base, okay, I found it, never mind, it is in the SPC.
In the teeniest, tiniest little text.

[@57:37](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3457.32) - José Blanco
Okay, so yes.

[@57:40](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3460.62) - Anna.Fiske
Let me also add the notes for the images and logos here. Yes, I uploaded all the logos that we have, but as we go through this, I'm making a list of the ones I don't have, so I can get that for you.

[@57:52](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3472.37) - José Blanco
Okay, perfect. Perfect. Okay. Moving on to, I believe, Aetna Dental Benefits here. This seems to be exactly the same page, so, okay, should work similar.
The logo should have already been provided, I believe I called it out earlier. It's the same. So now on to
The vision benefits, this one's kind of interesting because the table is built differently, I believe.

[@59:15](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3555.97) - Anna.Fiske
Yeah, we included out-of-network because vision just looks so puny without it. So to like fill the page, we put out-of-network information.

[@59:27](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3567.24) - Chad Gregory (LaunchPad Lab)
There's two plans there though, right?

[@59:30](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3570.5) - Anna.Fiske
Correct.

[@59:30](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3570.82) - José Blanco
Yes, there's two plans, but they all share the same frequency period.

[@59:41](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3581.47) - Chad Gregory (LaunchPad Lab)
Yes.

[@59:42](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3582.09) - Anna.Fiske
Yes. Oh, yes. Yeah.

[@59:44](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3584.25) - Chad Gregory (LaunchPad Lab)
Is there a better way to, like, is this the preferred way of putting vision on there twice versus like- Mixing the headers?

[@59:55](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3595.37) - José Blanco
Giving it a name or something?

[@59:57](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3597.31) - Anna.Fiske
It's supposed to have vision and vision plus.

[@1:00:00](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3600.13) - Chad Gregory (LaunchPad Lab)
Okay.

[@1:00:01](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3601.01) - Anna.Fiske
So the plus is missing on the first. okay.

[@1:00:06](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3606.53) - Chad Gregory (LaunchPad Lab)
So can you go to the vision summary on the workbook, José?

[@1:00:10](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3610.81) - José Blanco
Of course.

[@1:00:14](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3614.18) - Chad Gregory (LaunchPad Lab)
There you go. Low, do you just want it to say vision instead of vision plus? Oh, wait, that's it.
No. Okay, MetLife vision on E, and then F is probably, yeah, those are the two we're looking at here.

[@1:00:30](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3630.73) - Anna.Fiske
Yeah, it should say plus on the first one.

[@1:00:34](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3634.8) - José Blanco
Okay, so let's see, exam copay, should it be copay i-exam or copay contact exam? So either row 12 or 13.

[@1:00:53](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3653.51) - Anna.Fiske
It's going to be the 12. Sorry. I just realized the benefit guy's wrong. It's $10, but it should be zero.
I won't learn that for us.

[@1:01:10](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3670.45) - José Blanco
Okay, so 12.

[@1:01:11](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3671.95) - Anna.Fiske
Yeah, sorry, row 12.

[@1:01:14](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3674.81) - José Blanco
Answer. Out of network allowance should be 22, then, I suppose.

[@1:01:33](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3693.21) - Anna.Fiske
For you out that, guide?

[@1:01:36](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3696.51) - José Blanco
Oh, out of network.

[@1:01:37](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3697.51) - Anna.Fiske
Sorry, yes. Yep, 22. I'm sorry.

[@1:01:41](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3701.13) - José Blanco
No worries. You're the one here fixing all my wrong assumptions, so. Well, I'm also realizing that they made this page incorrectly, so I'm like, oh, that's nice.

[@1:01:57](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3717.04) - Anna.Fiske
I hope all of our guides aren't like that, because that's what Connor was talking about. It got me all upset.

[@1:02:03](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3723.7) - Chad Gregory (LaunchPad Lab)
Yeah, AI can make mistakes.

[@1:02:09](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3729.18) - José Blanco
Okay, so the next question I have here is Materials Co-Pay crossing the source for Materials Co-Pay frequency. So where's this 12 coming from, is the question.

[@1:02:25](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3745.22) - Anna.Fiske
So that 12 is going to be in the SBC, and it's saying that it'll say in language like every 12 months you're eligible for this.
So you can only get your glasses every 12 months. So you can't do it in January and then December because you're getting rid of the plan.
You know what mean? It has to be every 12 months. So that's in the SBC, but that would be the same across like for the vision with MetLife is 12 months.
So we could honestly, if you didn't want it to be a row, we could put it in text somewhere.

[@1:03:00](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3780.01) - José Blanco
Will it always be 12 for, like, everything here? It will. Yeah, I could simplify the mapping. But I was, let me see.
Oh, because I was pulling from 32, 33, and 34 based on just trying to figure it out. One more thing.
You mentioned that you could provide us with an SVC.

[@1:03:35](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3815.42) - Anna.Fiske
For, like, plan.

[@1:03:38](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3818.84) - José Blanco
Since they have a fixed structure, it's likely that later on we're going to need to go over an SVC just to basically figure out where these values are, the SVC.
If we're going to go for the approach of parsing it or anything like that. But that's for later down the road.
And I mean... Tim, I'm just writing down SVCs.

[@1:04:03](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3843.93) - Chad Gregory (LaunchPad Lab)
Actually, you know, it's really, this is interesting. Anna, do the OMQs have SVCs as well?

[@1:04:13](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3853.29) - Anna.Fiske
Yes.

[@1:04:14](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3854.03) - Chad Gregory (LaunchPad Lab)
Yeah, like, is that what you get from the OMQ process that, like, would generate, would be what we need to collect in the admin console?

[@1:04:24](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3864.01) - Anna.Fiske
Um, we would get the SVCs after the client elects that plan. Yeah, we wouldn't collect that documentation until we were, like, committed.

[@1:04:34](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3874.69) - José Blanco
So how do we generate the benefit guide if you don't have, like, the SVC?

[@1:04:44](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3884.17) - Anna.Fiske
We'd be manually just inserting those SVCs into the guide if the client wanted that. but we also have an internal person who creates medical side-by-sides for the open market quote, because we know, hold on, I'm lying.
Again, I'm sorry, my brain is fried. So we're to have a template that that person fills out for Taylor to read and create a medical page of side-by-sides, but as far as like the plan details, that's going to be an external process because we don't want our format on that because it's not our plan.
So that would be outside of Taylor.

[@1:05:21](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3921.58) - Chad Gregory (LaunchPad Lab)
Okay, so OMQs wouldn't, oh, an OMQ wouldn't be in here. Sorry, I'm just, maybe that's not what you said.

[@1:05:30](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3930.36) - Anna.Fiske
Um, it would be in here as a side-by-side.

[@1:05:33](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3933.74) - Chad Gregory (LaunchPad Lab)
Yeah. But any details that need to be pulled from the SVC would not be in here. So that would just be blank for any of the OMQs.

[@1:05:43](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3943.02) - Anna.Fiske
Mm-hmm. Okay.

[@1:05:45](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=3945.76) - Chad Gregory (LaunchPad Lab)
I was going to get to basically the template that we need to put together for the OMQ could be the same template that we make to capture all the SVC.
Okay. Mm-hmm. But it sounds like no, or maybe it is yes. And then maybe it is yes, actually, but then so that it could kind of be used for two purposes.
You could use it to, we could use it for the like process, AI process or whatever to like add all the SBC information into a structured format.
But we could also use it so that the OMQ team or whatever, the person you just talked about, could take the plan information that they get in the OMQ process, pop that into the template, then give it to you to upload into the admin console.
And then they could later use that to like, I don't know if they need to organize additional SBC information after they get it later.

[@1:06:59](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4019.11) - Anna.Fiske
I don't know.

[@1:07:00](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4020.19) - Chad Gregory (LaunchPad Lab)
I'm kind of spitballing a little bit, but maybe that helps us not have to create two different templates or something.
I don't know.

[@1:07:10](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4030.51) - Anna.Fiske
That would be helpful. And again, like, even though it's an open market quote, the SVC is still going to be the same format.

[@1:07:17](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4037.07) - Chad Gregory (LaunchPad Lab)
So all SVCs look exactly the same, just different information. So that's helpful. Okay. Sorry, José. That was kind of a tangent.

[@1:07:29](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4049.01) - José Blanco
No worries. There's a lot. Okay. So the last question was, materials copay frequency. Next in line, I have, okay, so this field right here has four values, and I could identify what the first three come from, which is these three right here.
Mm-hmm.

[@1:07:58](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4078.35) - Anna.Fiske
Lenticular.

[@1:07:58](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4078.79) - José Blanco
Lenticular. Is it frames or contact lenses or where's this value coming from, both for in-network and out-of-network?

[@1:08:11](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4091.83) - Anna.Fiske
Let me Google it. I don't know what that means.

[@1:08:16](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4096.09) - José Blanco
I Googled it and it says that it's something in a lens fashion. I was like, okay.

[@1:08:26](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4106.31) - Anna.Fiske
Lenticular. But single vision, bifocal, trifocal. Like, take it to those who think that it's like, you need UV protection, blue light protection.
Like, that's what I think that.

[@1:08:41](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4121.54) - Chad Gregory (LaunchPad Lab)
Oh, I was thinking it was the contacts.

[@1:08:45](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4125.98) - José Blanco
It's an adjective that describes objects with the shape of a lens or by convex lens.

[@1:08:55](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4135.8) - Anna.Fiske
Oh, so that's if you're, no. I don't know. I don't know where that would come from. It must be in the SBC.
Yeah.

[@1:09:08](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4148.17) - José Blanco
I use glasses, and I think I've heard one of those terms when I was trying to get context, but yeah, let's put a pin on it.
So I'll add a warning to follow up on that one.

[@1:09:29](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4169.98) - Anna.Fiske
It is in the SBC. It's considered a standard corrective lens. So it's in the same family as all the other ones above it.
But it is in the SBC.

[@1:09:40](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4180.65) - José Blanco
So the data comes from the SBC?

[@1:09:43](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4183.03) - Anna.Fiske
Mm-hmm. At least that term, yeah. But the cost is going to be the same for the other three, just like the in-network.

[@1:09:54](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4194.7) - José Blanco
Those other three each have different values, so it's... Or the out-of-network. The out-of-network also have different values, so we can't just choose one randomly, I don't think.

[@1:10:10](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4210.13) - Anna.Fiske
No. Yeah. Yeah, it's in the SBC, though.

[@1:10:13](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4213.99) - José Blanco
Okay. Let me add that in. Okay. The next one is the frequency for those. So these 412s, we already said that this just comes from the same value in the SBC?

[@1:10:51](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4251.14) - Anna.Fiske
Mm-hmm. I was thinking.

[@1:11:00](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4260.01) - José Blanco
You using this value, row 33?

[@1:11:04](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4264.75) - Anna.Fiske
Correct.

[@1:11:06](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4266.83) - José Blanco
Does that make sense? It does. Next question is, contact lenses allowance elective source. So that would be contact lenses allowance elective source.
So where is this coming from?

[@1:11:45](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4305.81) - Anna.Fiske
The SPC.

[@1:11:50](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4310.29) - José Blanco
Okay. I had a hunch of using column 20 for this one, which is this one. But I had to doubt of where is the percentage coming from.

[@1:12:07](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4327.58) - Anna.Fiske
Yeah, the percentage is coming from the SBC because we don't do the same allowance if you're going to a wholesaler such as Costco, Walmart, Sam's Club.
So there's a percentage instead for those instead of the dollar amount.

[@1:12:28](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4348.3) - José Blanco
But it says plus, not slash, so I'm confused by that.

[@1:12:41](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4361.64) - Anna.Fiske
Plus 20% off, 50% off balance. That makes me think this guide is not.

[@1:12:47](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4367.16) - Chad Gregory (LaunchPad Lab)
Yeah.

[@1:12:48](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4368.62) - Anna.Fiske
I'm very concerned about the guides that have been handed out. Yeah, sorry to have, uh... We could have used you guys this time last year.

[@1:13:00](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4380.77) - Chad Gregory (LaunchPad Lab)
Um, plus 15%.

[@1:13:04](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4384.01) - Anna.Fiske
And that's for contacts. Okay. Contacts, $200 allowance every 12 months. No additional cost effort. Okay. Get up to 20% savings on additional pairs of prescription glasses or sunglasses.
So that has to do, that shouldn't be there. should be with the second pair benefit at the bottom. It's above the picture, but it's like the last little gray section, that 15% should be in there, not on it.

[@1:13:40](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4420.37) - José Blanco
So that, that section should actually have like values for each of the in network, out of network. The table's wrong, basically.
Right. The table's wrong.

[@1:13:50](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4430.61) - Anna.Fiske
Yes. So the 15%, I mean, that's misleading because it does look like you get $130 plus 15% off your balance.
That's not really true. You get $130 off your first pair. And then if you want a second pair, a lot of people do the sunglasses, prescription sunglasses, then you get 15% off of those.
So it should really be in the second pair benefit because like an additional 20% off something like that. That's something I can kind of drill into this page.

[@1:14:20](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4460.02) - Chad Gregory (LaunchPad Lab)
Okay. Okay.

[@1:14:21](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4461.22) - José Blanco
So for my notes on how the correct value should be pulled for the elective should be row 33. And add a note that the table in the master guide is wrong.
Is that okay?

[@1:14:36](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4476.29) - Anna.Fiske
Yeah, that works totally fine. It would be row, not 33.

[@1:14:39](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4479.63) - José Blanco
It'd be. Sorry, is it a 20?

[@1:14:42](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4482.49) - Anna.Fiske
Yep, row 20. Yeah, I looked at the wrong thing on my table. good.

[@1:14:47](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4487.93) - José Blanco
Okay. So let me add what we found out here.

[@1:14:55](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4495.63) - Anna.Fiske
Jagger, this is something we're going to have to audit in the workbook too. So far, the workbook. Right? And the guide is not, but this is something I want to be extra vigilant on.

[@1:15:08](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4508.7) - Jagger Sturdivant (Questco Cos)
Yeah, we were doing that last year, too. We found issues in the workbook.

[@1:15:12](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4512.81) - Anna.Fiske
Like, there's an allowance plus 20% for the frames, but not contact lenses. So that just really sucks. That's in there.

[@1:15:25](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4525.36) - José Blanco
Okay, and then will we be building the correct table with the different sections for a second pair of benefits?
Okay.

[@1:15:38](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4538.38) - Anna.Fiske
Yeah, I'll probably just take this page myself, tear the table down, and make sure all the numbers are right, and then I can label it like, this is workbook, row, whatever, this is SPC.

[@1:15:49](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4549.26) - José Blanco
That would be really helpful.

[@1:15:51](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4551.38) - Anna.Fiske
Yeah, because this is just causing more confusion.

[@1:15:55](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4555.05) - José Blanco
Okay. Sorry about that, you guys.

[@1:15:57](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4557.99) - Chad Gregory (LaunchPad Lab)
No worries.

[@1:15:59](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4559.03) - José Blanco
I'm just going to highlight.

[@1:16:03](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4563.28) - Chad Gregory (LaunchPad Lab)
What is this vision benefits?

[@1:16:10](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4570.83) - José Blanco
Did we see it on any of the other issues? No. Okay. Okay. So for out of network, it's not hallucinating here, giving 15% off, but I have it as, would it be row 30?
So this?

[@1:16:37](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4597.01) - Anna.Fiske
For out of network, yes. Yep.

[@1:16:40](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4600.55) - José Blanco
Okay. Okay. And then I have the ones that I didn't find any references to, where the- Medically Necessary Values, so these come from the SBC?

[@1:17:08](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4628.74) - Anna.Fiske
Yes.

[@1:17:08](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4628.88) - José Blanco
It would be this value and this value.

[@1:17:11](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4631.56) - Anna.Fiske
Correct. Yep, that would be the SBC.

[@1:17:36](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4656.28) - José Blanco
I've said SBC so many times. What does SBC stand for? Summary of Benefits and Coverage. Okay, let me write that down somewhere.

[@1:17:49](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4669.34) - Chad Gregory (LaunchPad Lab)
I got it.

[@1:18:00](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4680.07) - José Blanco
Let's see, we were dental, because I have two questions here regarding the frequency for contact lenses allowance source, so it would be these two values, and I was considering, let me see, no, I actually didn't have a reference for those.
So, since they're not mentioned here, like, infrequency, replacement lenses, oh, wait, it doesn't say replacement contact, so I wasn't sure if I should use this value, but, like, these three values are redundant, basically, right?

[@1:18:47](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4727.67) - Anna.Fiske
Correct, yeah, if one's 12 months, they're all 12 months.

[@1:18:50](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4730.51) - José Blanco
So I could just use row 32 for all frequencies and be done, right?

[@1:18:55](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4735.89) - Anna.Fiske
Yep.

[@1:18:58](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4738.79) - José Blanco
Oh, well, I don't know. All right, I think for the mappings on vision, that was it. So how much
much time we got? We got seven minutes, I believe?

[@1:20:03](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4803.23) - Chad Gregory (LaunchPad Lab)
We have more time than that. We have 37.

[@1:20:05](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4805.93) - José Blanco
Okay, perfect. My brain's hurting a bit, though.

[@1:20:11](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4811.91) - Chad Gregory (LaunchPad Lab)
Your stuff is the most important here, José.

[@1:20:16](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4816.33) - José Blanco
Do you have things you need to cover as well?

[@1:20:20](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4820.95) - Chad Gregory (LaunchPad Lab)
I would rather get through this stuff. Yeah. Okay, I only have notes on five, four more pages, and then I still need to continue going through.
Yeah.

[@1:20:34](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4834.59) - José Blanco
But if you could tell me, like, if some of these are static or something, that would be very helpful in the meantime.

[@1:20:45](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4845.04) - Anna.Fiske
Yes.

[@1:20:48](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4848.19) - José Blanco
So vision for Aetna, it's the exact same page. There is a blank page for some reason that I wanted to ask about here.

[@1:20:58](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4858.37) - Anna.Fiske
Oh, no, we don't need them.

[@1:21:01](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4861.12) - José Blanco
Okay. That should not be fair.

[@1:21:03](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4863.18) - Anna.Fiske
Sorry.

[@1:21:04](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4864.1) - José Blanco
No worries. Remove. Okay. Then we have Flexible Spending Accounts. This is supposed to be the HSA page.

[@1:21:26](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4886.49) - Anna.Fiske
It's blank?

[@1:21:28](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4888.13) - José Blanco
Yes. Oh, no.

[@1:21:29](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4889.99) - Anna.Fiske
Okay. I'll get you the HSA page. But HSA, all the way down, if you can scroll down on your sidebar there on the left, all of these are going to be static.
Um, all of that's static. If you can keep going, it's all static. Yeah, everything is static all the way down.
It's just dependent on election. So if they elect it in the workbook, then they get this page and nothing changes on it.
Okay, so the health savings and the flexible spending account page, those we will need to update on our side and provide to you because the IRS changes those limits every year.
So we have to change the limits on those pages. But outside of that, they're static.

[@1:22:24](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4944.28) - José Blanco
Okay, let me add some notes here because I didn't realize that it had a title before. So I just titled it as blank page on my notes.

[@1:22:34](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4954.63) - Anna.Fiske
Let me try to find one for you now so I don't forget. Health Savings Account HSA.

[@1:22:43](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4963.89) - José Blanco
Okay, so notes for HSA is, what's the name of the plan? Conditionally rendered. Based on plan selection.

[@1:23:04](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4984.04) - Anna.Fiske
It's going to be the carrier's Thrive Pass, and the name is Health Savings Account.

[@1:23:19](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=4999.88) - José Blanco
How do you spell the carrier's name?

[@1:23:23](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5003.41) - Anna.Fiske
T-H-R-I-V-E, V as in Vicky, and then Pass, P-A-S-S.

[@1:23:46](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5026.86) - Chad Gregory (LaunchPad Lab)
Found it.

[@1:23:48](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5028.79) - José Blanco
Oh, it's a single word? All together, okay.

[@1:23:51](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5031.27) - Anna.Fiske
It's all together, mm-hmm.

[@1:23:53](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5033.82) - José Blanco
Oh, okay, so. Okay, so conditionally rendered based on plan selection, health savings account from Thrive Pass. So flexible spending accounts, conditionally rendered based on a plan with the same name as well?
Correct, yep. Was this the one that you mentioned that the IRS changes, these and the health savings as well?

[@1:24:29](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5069.53) - Anna.Fiske
Correct, yep, the flexible spending account that's beneath it.

[@1:24:34](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5074.72) - José Blanco
Okay. So those two would be dependent on the IRS. Nothing. Dynamic or Conditionally Rendered on this page, other than the fact that it changes every year.

[@1:25:06](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5106.53) - Anna.Fiske
Correct. So let me ask you this. I'm trying to find a help savings account one, the HSA one.

[@1:25:19](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5119.06) - Chad Gregory (LaunchPad Lab)
Yeah.

[@1:25:20](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5120.0) - Anna.Fiske
So in the workbook, we do have a spot. If the employer wants to contribute to that account, we have a spot in the workbook and the new one that Jagger made where they can type that in.
Would we be able to pull that from the workbook and put it on that page?

[@1:25:35](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5135.77) - José Blanco
That would make it a dynamic page. Right.

[@1:25:40](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5140.27) - Chad Gregory (LaunchPad Lab)
So yeah, it could be done.

[@1:25:42](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5142.71) - Anna.Fiske
Okay, because that's something they do request a lot, is to add that.

[@1:25:46](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5146.57) - Chad Gregory (LaunchPad Lab)
Where are going to show up? Oh, well, we don't have the example. Right. also, yeah. It would be around here, in this area.
Good. Good. Killing me.

[@1:26:18](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5178.44) - José Blanco
Which page on the, do you already have it like envisioned where you're going to be putting the data in the workbook that we'll be fetching from?

[@1:26:28](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5188.5) - Anna.Fiske
Yeah, Jagger has that built out. It's towards the bottom of the workbook.

[@1:26:32](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5192.52) - Chad Gregory (LaunchPad Lab)
On the class pages?

[@1:26:36](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5196.16) - Anna.Fiske
Correct.

[@1:26:37](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5197.5) - José Blanco
But it's not there in this example, José. Yeah, since you're, are you still building that out, Jagger?

[@1:26:54](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5214.43) - Jagger Sturdivant (Questco Cos)
That part's done, but you'll have the workbook template that has that later today. Yeah.

[@1:27:00](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5220.77) - Chad Gregory (LaunchPad Lab)
Okay.

[@1:27:01](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5221.45) - José Blanco
I just wanted to note something. We'll need some way of identifying which row it is in, mainly because the classes can shrink vertically.
So we'll need something like a header in a determined column, basically.

[@1:27:28](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5248.21) - Jagger Sturdivant (Questco Cos)
Yeah, you'll have a way. There's a HSA funding block in a specific column, so you could look for that, and then it would be relative to that.

[@1:27:39](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5259.37) - José Blanco
Okay. Similar to how we know to search for, like, a benefit class over here.

[@1:27:47](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5267.38) - Jagger Sturdivant (Questco Cos)
Yeah.

[@1:27:49](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5269.78) - José Blanco
Okay.

[@1:27:52](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5272.2) - Jagger Sturdivant (Questco Cos)
If I have time, I may actually update it where all of the data we need to extract from the workbook is put into its own sheet, so you don't have to look at each.
Each class individually, you just have to look at one sheet, and then that would be included on that.

[@1:28:10](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5290.12) - José Blanco
Could be explored, yeah, for sure. All right, let's see where we were. We're talking HSAs, flexible spending accounts. Nothing changes in this one, then?

[@1:28:35](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5315.28) - Anna.Fiske
Sorry, did you ask me something?

[@1:28:37](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5317.89) - Chad Gregory (LaunchPad Lab)
On the FSA, does anything change?

[@1:28:40](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5320.85) - José Blanco
Or is it still static, no new values, or anything like that?

[@1:28:44](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5324.09) - Anna.Fiske
It would just be that little blue box on the side, contribution limits, that'll change with the IRS, but everything else is static, yeah.
It would be static based off election in the workbook.

[@1:28:57](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5337.09) - José Blanco
But this changes, are you saying that that changes?

[@1:29:00](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5340.01) - Chad Gregory (LaunchPad Lab)
Each year, you mean?

[@1:29:01](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5341.37) - Anna.Fiske
Correct. Yeah, it's not client by client.

[@1:29:03](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5343.57) - Chad Gregory (LaunchPad Lab)
Yeah.

[@1:29:04](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5344.57) - José Blanco
Yeah, like we'll just update the template yearly, basically. Whatever the choice for templating ends up being. Okay, so after this we have voluntary STD, MetLife.
Okay.

[@1:29:31](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5371.88) - Anna.Fiske
That one's completely static.

[@1:29:38](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5378.68) - José Blanco
It is. What these values are in the STD summary?

[@1:29:45](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5385.87) - Anna.Fiske
This is similar to, hold on. I thought this was similar to the APL, where they can choose between the two plans.
Hmm.

[@1:29:58](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5398.11) - Chad Gregory (LaunchPad Lab)
Hmm.

[@1:29:59](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5399.67) - José Blanco
Hmm.

[@1:30:04](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5404.71) - Anna.Fiske
But this is, this page is showing the same plan twice.

[@1:30:10](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5410.59) - José Blanco
Um, yeah, but that could be just AI wonkiness, honestly.

[@1:30:15](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5415.87) - Anna.Fiske
Yeah. Um, hold on. It has to be, I'm sorry, let me look at the plans of present real quick.

[@1:30:32](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5432.27) - Chad Gregory (LaunchPad Lab)
Yeah. Because this is showing the plan in column D twice, the 7-7. Right.

[@1:30:54](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5454.88) - Anna.Fiske
They have to elect one. They have to elect if they want to offer a voluntary 7-7 or. Voluntary 714.
So, Jagger, that in your book thing, I don't know if you have it separated like that or not, is Voluntary 7-7 or Voluntary 7-14.

[@1:31:13](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5473.97) - Jagger Sturdivant (Questco Cos)
They are separate.

[@1:31:15](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5475.57) - Anna.Fiske
Okay. So, yes, this would be dynamic based off the election. And then whatever they select, yeah, off of these columns, C and D.

[@1:31:47](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5507.51) - José Blanco
Sorry, I got it sorted out a bit there. Okay, so they would choose one of these two plans, right?
And then we would go from there based on what they choose. It's the workbook, basically?

[@1:32:02](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5522.77) - Anna.Fiske
Yes, but because it's voluntary, they can offer both.

[@1:32:09](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5529.5) - Chad Gregory (LaunchPad Lab)
Okay, so we will show one or two of those two. This will be very similar to the dental and vision pages.
Yeah, I have some questions about the mapping here, though, on my tables.

[@1:32:24](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5544.71) - José Blanco
The accident and illness benefit begin date, is it accident slash illness? Or the other way around? It's accident slash illness.

[@1:32:42](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5562.49) - Chad Gregory (LaunchPad Lab)
Yeah. Okay.

[@1:32:45](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5565.03) - José Blanco
Oh, I don't know.

[@1:32:48](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5568.21) - Chad Gregory (LaunchPad Lab)
The same way it is in the title of the name of the plan, 714. Seven accident, 14 illness.

[@1:33:12](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5592.27) - José Blanco
Premium waived if disabled. I just have no idea where his value is coming from. There's a yes here in rehab services.
I don't know. No, it would be in the workbook.

[@1:33:28](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5608.04) - Anna.Fiske
That would have to be on the SBC. Let me get the SBC for you. I'm adding these SBCs to a folder in SharePoint for us.

[@1:33:39](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5619.33) - Chad Gregory (LaunchPad Lab)
Amazing. And beneath them.

[@1:33:45](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5625.01) - Anna.Fiske
Let me see.

[@1:33:48](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5628.23) - Chad Gregory (LaunchPad Lab)
I'm going to be tagging you guys in a comment on this, uh, on Asana, and then you can send the SharePoint link, uh, for links.
Whatever it ends up being. Nikki noticed something that I want to bring up after you're done with this page, José.

[@1:34:08](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5648.87) - José Blanco
Okay. So just remind me. This is the last page I have notes on, but it's been quite a while, so other questions are probably good or better saved for another time.

[@1:34:30](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5670.08) - Chad Gregory (LaunchPad Lab)
You know, and it sounds like we probably have enough to get an approach going, right? Like you're unblocked for a while.

[@1:34:41](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5681.17) - José Blanco
We, the main takeaway from all the questions today is that we need to take a look at SBCs and figure out an approach to them because we will need them and there's no way around them.

[@1:34:53](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5693.99) - Chad Gregory (LaunchPad Lab)
Correct. We will need. Them or the data out of them.

[@1:35:03](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5703.82) - José Blanco
Yeah, we need to normalize them.

[@1:35:43](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5743.38) - Anna.Fiske
You're not waiting on me?

[@1:35:45](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5745.43) - José Blanco
Yeah. Oh, I'm sorry.

[@1:35:47](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5747.05) - Anna.Fiske
What did you say?

[@1:35:48](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5748.63) - Chad Gregory (LaunchPad Lab)
I thought you were looking something up in the SPC about...

[@1:35:52](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5752.39) - Anna.Fiske
Oh, yeah. It's in the SPC, but I'm uploading all the SPCs to SharePoint for you guys to review.

[@1:35:57](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5757.27) - Chad Gregory (LaunchPad Lab)
Okay. Perfect. Sorry.

[@1:35:59](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5759.53) - Anna.Fiske
Okay.

[@1:36:00](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5760.01) - Chad Gregory (LaunchPad Lab)
So confirmed SVC.

[@1:36:03](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5763.43) - José Blanco
The last question I have here is, does the example section at the bottom of this page change dynamically somehow, some way?

[@1:36:15](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5775.81) - Chad Gregory (LaunchPad Lab)
It looks like it does, because that is also showing the two wrong plans.

[@1:36:21](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5781.65) - Anna.Fiske
Yeah, so it needs to change to reflect the 7.14 that's not in here.

[@1:36:27](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5787.7) - José Blanco
Yeah, I'm just curious if this was AI hallucination or not.

[@1:36:34](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5794.39) - Anna.Fiske
So, let me tell you guys this. We have had horrible experiences with this example in the benefit guide. I would love to not include it, because people take this as gospel, and they're like, oh, that's what my premium's going to be, that's what my benefit's going to be.
Even though we say it's illustrative based off your salary, I would love to just not include it, to be honest.

[@1:36:55](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5815.91) - Chad Gregory (LaunchPad Lab)
If you're good with that, we're good with that.

[@1:36:58](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5818.49) - Anna.Fiske
Okay, perfect. Yeah. I don't want to, if we can help it.

[@1:37:01](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5821.59) - Chad Gregory (LaunchPad Lab)
So would we end after earnings definition and then keep the click more and all that stuff in the footer there?

[@1:37:13](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5833.38) - Anna.Fiske
Yes, please.

[@1:37:15](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5835.16) - Chad Gregory (LaunchPad Lab)
Is that okay since you're already dynamically generating that table?

[@1:37:22](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5842.13) - José Blanco
I'm sorry, go again. I was tapping down the notes.

[@1:37:24](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5844.83) - Chad Gregory (LaunchPad Lab)
Is it okay to do that, to just remove that whole chunk, the example chunk?

[@1:37:32](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5852.09) - José Blanco
Oh, yes. Yes, absolutely.

[@1:37:34](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5854.81) - Chad Gregory (LaunchPad Lab)
So here's the question that I had, Anna, or, well, Nikki called this out. This Master Benefit Guide is called Master Benefit Guide-2026-English.

[@1:37:49](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5869.33) - José Blanco
Are there other languages that need to be generated?

[@1:37:56](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5876.19) - Anna.Fiske
Yes, but we didn't add that in the SOG. So I was thinking we take the guide that Taylor creates and give it to our third party to create the other languages.
Because we're also going to be sending the guide to them to create the Ucentisha, which is like an AI avatar to present the guide as a script.
So we're already going to continue using them. So I figured we'd just do that for the languages.

[@1:38:21](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5901.21) - Chad Gregory (LaunchPad Lab)
Okay, that's perfect.

[@1:38:22](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5902.93) - Anna.Fiske
Yeah, because we did not, I didn't even think about putting that in the SOW. So I was like, oh, that's not me.
I totally forgot about it.

[@1:38:27](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5907.73) - Chad Gregory (LaunchPad Lab)
We need in Spanish. If we need to do that when we go into V2 or V3 or something.

[@1:38:33](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5913.57) - Anna.Fiske
Definitely. Yeah.

[@1:38:36](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5916.86) - Chad Gregory (LaunchPad Lab)
Okay. José, that is a relief.

[@1:38:44](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5924.6) - Jagger Sturdivant (Questco Cos)
I can hear it in your voice.

[@1:38:46](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5926.7) - Chad Gregory (LaunchPad Lab)
Yeah. Nikki's Slack to me was like, oh my God, are you kidding me? But good catch.

[@1:39:01](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5941.57) - José Blanco
I honestly sound out when you mentioned that there was other languages.

[@1:39:06](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5946.11) - Chad Gregory (LaunchPad Lab)
So the answer is we're just doing English, José. Okay, thank you.

[@1:39:13](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5953.89) - José Blanco
Although you could whip up a Spanish version pretty quick, right?

[@1:39:16](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5956.71) - Anna.Fiske
could.

[@1:39:17](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5957.91) - Chad Gregory (LaunchPad Lab)
I could, yeah, but it'll take a while, you know?

[@1:39:22](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5962.41) - Nikki Dow
José is in charge of all benefit guides in Spanish. That's fine.

[@1:39:27](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5967.31) - José Blanco
All right, that was the last question that I had so far. Later on, I might come with questions regarding the remaining pages.
But for now, we have enough to figure out, honestly, especially regarding the SBCs and normalization and parsing. So if we can move with the rest of the agenda for this call.

[@1:39:58](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=5998.83) - Chad Gregory (LaunchPad Lab)
Okay. Okay. I honestly sound out when you mentioned that there was other languages. So the answer is we're just doing English, José.
Okay, thank you. Although you could whip up a Spanish version pretty quick, right? could. I could, yeah, but it'll take a while, you know?
José is in charge of all benefit guides in Spanish. That's fine. All right, that was the last question that I had so far.
Later on, I might come with questions regarding the remaining pages. But for now, we have enough to figure out, honestly, especially regarding the SBCs and normalization and parsing.
So if we can move with the rest of the agenda for this call. Okay. Okay. Yeah, honestly, it might be best if you just, when you have time, Anna, like, look at the, I'm going to tag you on this comment right now, look at the questions that we have in there and just make notes rather than us needing to go through it all after we've just been on this for an hour and 45 minutes.
Uh, they're all kind of things that I think we have already talked through and I really just wanted confirmation.
I put, like, my answers to the questions in italics. Uh, and, Nikki, I don't know how you feel, but I was, like, looking through all of the tickets and kind of thinking about the flow and I feel like we have a pretty good idea now that we can get tickets into a pretty good spot.
Uh, actually. I don't know. That's maybe like a crazy thing to say because this is just a pretty complicated project.
But that's going to be my goal for like Monday morning is just get as many tickets into a good spot as we can so I can start reviewing it with Nikki and Connor and José Tuesday, be able to give you guys an update on Wednesday of where everything is.
but because the goal of next week is by Friday, all of that is ready. We know what the timeline is.
We know what change order needs to happen if one needs to happen. And yeah, we have like the the target dates and everything.
Just for you, Anna and Jagger, so you know, like, I was trying to use the SOW item. map to vilified, don't make we
As tickets and like, it just wasn't great. So we're kind of, the reason Asana probably looks a little crazy is because we were slowly moving through the course of, through the course of Sprint 1 here and into Sprint 2, like an approach of getting rid of the SOW item tickets in favor of like part of the flow tickets, which is probably just what we should have done in the first place, but I'm feeling, I, after the last couple days, I'm feeling pretty good about knowing everything, or like, not all the details obviously, but everything that needs to be done.

[@1:43:49](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=6229.31) - Anna.Fiske
And that should get us to a part where, a point where we will have all the tickets as we get to the tickets or are getting ready to start different things.

[@1:44:00](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=6240.01) - Chad Gregory (LaunchPad Lab)
Obviously, there will be more questions, there will be testing, and that brings me to my last point, which again, I don't think we need to get into right now in the last 15 minutes, but maybe we set some time next week, or maybe this is on our grooming call next Friday, to talk about the approach to testing.
Yeah, Nikki, any comments? José, any last questions? Anna or Jagger, any questions or comments? think I'm going to.

[@1:44:41](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=6281.53) - Anna.Fiske
bit on my side.

[@1:44:42](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=6282.33) - Chad Gregory (LaunchPad Lab)
Yeah, I just appreciate all the tickets. That keeps me organized to make sure I get what you guys need.
And José, I only have three logos that I owe you, so I'll get those logos for you today, hopefully, but I'm getting all the reports that you need first, Chad.

[@1:44:57](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=6297.88) - Anna.Fiske
Oh, yeah, great. Thank you. Nothing else for me, I believe I've asked enough for a few weeks, so.

[@1:45:05](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=6305.55) - Nikki Dow
Yeah.

[@1:45:07](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=6307.36) - Anna.Fiske
Nikki, did you have anything else?

[@1:45:11](https://fathom.video/share/g8B-ZEhfvC5sasuJjxsPTqtya_7zHyEE?timestamp=6311.3) - José Blanco
No, I think I'm okay. Okay. And one other thing I am going to do on Monday is meet with Nico.
He's reviewing all of our admin console discussion from yesterday and going to make some progress. And then I'm going to talk to him about a few other things to add in there.
And then Anna, you and I probably with Nico just need to look at those designs again next week, but we'll make time for that.
If you have days or times that are best for you that you want to send over, that'd be good too.
Yeah, I'll do that because the earlier we can block it, the better because my calendar fills up pretty quick.
Yeah. Okay. I'll pop a note for that as well in here. Okay. Great. Thank you, guys. Yeah, thank you, guys.
Have a good Friday and a good weekend. you too. Bye. Thanks.
