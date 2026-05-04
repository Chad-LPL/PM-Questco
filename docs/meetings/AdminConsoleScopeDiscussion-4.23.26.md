# Admin Console Scope Discussion - April 23, 2026

**Duration:** 57 mins
**Attendees:** Chad Gregory (LaunchPad Lab), Anna Fiske (Questco), Jagger Sturdivant (Questco), Nikki Dow (LaunchPad Lab), Conor Hawes (LaunchPad Lab)

---

## Transcript

**@0:00 — Anna Fiske:** That great with my music system, I really don't want that.

**@0:03 — Chad Gregory (LaunchPad Lab):** Yeah, I think it's just part of it, which is great. All right, looks like we got the crew here. I'll share my screen, got the recorder going. Oh yeah, no worries, folks. Okay, I posted these notes on the status call agenda yesterday, but obviously we didn't get to them.

*[SCREEN SHARING: Chad started screen sharing]*

We wanted to talk a little bit about like what we need to have in the admin console and really like kind of land on a scope with you guys for that. And some of this is around these three questions kind of being the biggest things or these three areas. Um, obviously I know for the rates themselves, the plan is to get those posted into, um, into Prism for the clients.

The rebanding files, we talked, uh, a week or so ago when we were re-starting on the admin console, that we would put rebanding into the admin console. Um, we've gone back and forth a little bit about this to, uh, think about, like, is that the best place? Is it the easiest place? Um, and I'll let, uh, like, Nikki and Connor as well jump in here to this conversation, but basically we're wondering if the best place is actually in SharePoint. And that's typically probably not something we would love to do. But one of the things that we were considering is sort of like banding changes and needing to change the rebanding file.

And like if you did that in the admin console, what like is would the expectation then be that we regenerate all of the bands for the for or sorry, regenerate all of the workbooks for all the clients for that year or or not. But a way that we kind of figured it might work better would be if you did plop it into SharePoint, then we would just look at the updated file when you were when we were generating one of the workbooks.

And if you needed to like regenerate a specific workbook, you could do that with a generate button in the admin console, but I wanted to see, like, is that tracking pretty well? The other thing was, like, just this factor of, like, how do we actually do it in the admin console if we go that route, but what's your thought, Anna, or, like, does it matter either way to you? Do you have a preference?

**@3:27 — Anna Fiske:** As far as where the rebanding file lives, I don't have a preference. I 100% agree with you. I would rather have just a generate button, and we regenerate the one workbook for the one client that got that rate reduced, and we had to re-band them. I would like it to, like, Taylor to reference that, just as, like, the source of truth, because the re-banding, the way that process works is it goes all the way up to, like, the C-suite level of management, and they re-band it. Then it goes to my boss, and then it comes to me, and then I have to give it to them. Analyst team to then put it into PRISM for Taylor to have that future rate band. So I think having it where Taylor can reference it, that's a lot of humans. So there's going to be errors. Somebody might get missed. Taylor can see the rebanding file and say, hey, that's not what's in PRISM. Like something's not matching up, but regenerating everybody. Absolutely not. No, just one at time would be nice because we really don't reband that many clients after the fact. We reband them before we'd even generate anything for any client.

**@4:34 — Chad Gregory (LaunchPad Lab):** Okay. Nikki, you have a thought?

**@4:39 — Nikki Dow:** Yeah. I was wondering if Anna could just go back to the rebanding process. You mentioned you or the analyst team is setting the future rate band in PRISM.

**@4:55 — Chad Gregory (LaunchPad Lab):** I was going to ask the same thing.

**@4:57 — Nikki Dow:** Yeah. I guess that doesn't align with how I thought the process worked. So you like receive the rebanding file, goes all the way up to the top at Questco, and it's like discussed and agreed upon, and then the analyst team goes into Prism and enters future rate bands based on that finalized rate band file.

**@5:17 — Anna Fiske:** Yes.

**@5:21 — Nikki Dow:** Okay. And then after that, workbooks are generated.

**@5:25 — Anna Fiske:** And the future rate band slot is what Taylor is going to read to generate the renewal rates in the workbook. The rebanding file is just client retention strategy. I mean, at the end of the day, it's not Questco wide by any means. It's just when they get an unfavorable renewal, we can see that ahead of time, say, okay, they're a really good client. We want to keep them. Let's go ahead and negotiate that rebanding and get a lower rate for them. And then we put that into the Future Band slot in PRISM for Taylor to read.

**@6:08 — Chad Gregory (LaunchPad Lab):** So they put that in there. Is the plan for them to still do that?

**@6:14 — Anna Fiske:** Well, it'd be an import, like we talked about before, we'd be importing all the Bands in to PRISM ahead of time in that future slot.

**@6:23 — Chad Gregory (LaunchPad Lab):** Okay, yeah, but the analysts won't be doing one by one or whatever they're doing today, right?

**@6:33 — Anna Fiske:** Right, I might be having a memory issue. Jagger, can you help me out here? Have we been saying that Taylor's going to do it?

**@6:41 — Jagger Sturdivant (Questco):** This is different than what I thought, because I didn't think we were using the future Band in PRISM, because isn't that plan specific? And so if you're going to like switch to Kaiser, those plans aren't going to be at the client level, so you can't set up a future Band for those yet.

**@7:01 — Anna Fiske:** You're right, you're right.

**@7:02 — Jagger Sturdivant (Questco):** So I thought the prism imports is what sets the future rate band, because that's you create the workbook. I'm sorry, y'all.

**@7:17 — Anna Fiske:** Yeah, Jagger's right.

**@7:20 — Chad Gregory (LaunchPad Lab):** Okay, so let's think about this then. Can you remind me which column I need to look at here for the updated one?

**@7:37 — Nikki Dow:** Might be Y.

**@7:38 — Chad Gregory (LaunchPad Lab):** Oh. Oh, that's T. That's current rate band. Y. It's not Y.

**@7:45 — Jagger Sturdivant (Questco):** It might be hidden. might be between Y and AK. Yeah, there it is. Final rate band, AC.

**@8:00 — Chad Gregory (LaunchPad Lab):** Okay, so like, if we had this rateband file in SharePoint, and every time that we went to generate a workbook, we looked at this sheet and the other carrier rebanding file sheets, and we found in this one at least, AC, and popped the rateband for, whoever this is, I think that's hidden too, or it's like just this ID, but popped that into the client, for that client, for that carrier, well actually, is that what you want? Do we want to push that? Yeah, into Prism right then, or?

**@9:02 — Anna Fiske:** No, because Jagger's right. we need that, they're changing plans or something like that. It doesn't matter.

**@9:08 — Chad Gregory (LaunchPad Lab):** Yeah, you want to. Oh, yeah. Sorry, because what you said, Jagger, is they have one right band for the client, so depending on which carrier they choose is the one that we want to put in there.

**@9:21 — Jagger Sturdivant (Questco):** Yeah. Even if they change plans, would be a problem. So you're not going to be able to upload into Prism until after they've chosen everything.

**@9:29 — Chad Gregory (LaunchPad Lab):** Okay. So then in that case, all we're using this rate band for is on the actual generation of the workbook to determine the plans that need to show.

**@9:48 — Jagger Sturdivant (Questco):** Well, determine the rates of the plans that do show.

**@9:51 — Chad Gregory (LaunchPad Lab):** Yeah, both of those. Okay. So then going back to the question at hand, it seems like we can keep it in SharePoint as long as in the process that you were talking about at the beginning, Anna, that I guess once it goes to you or something, then you can put it into the SharePoint folder that we need it to be in. And then if it gets updated at some point, you just replace it, and we would reference the file based on the name for any upcoming generations, whether that was like you hitting the button again to regenerate it, or if there was other generations to be done later on. How does that sound to the dev team? I think that's kind of what we talked about.

**@11:10 — Conor Hawes:** Yeah, I mean, I think we'll kind of have to see how it plays out using SharePoint as a source of truth. There's a lot of information in that spreadsheet that we don't need. mean, like, ideally, we'd be pulling down, like, a single spreadsheet that had compliance and their rate bans per year.

**@11:35 — Chad Gregory (LaunchPad Lab):** Yeah, Anna, like, how bad do you think that would be to, like, pare it down to just the couple columns or whatever that we need after you get it from whoever above?

**@11:54 — Anna Fiske:** That would be fine with me. Whatever you guys, however you guys need it to be just letting me know because then I'll set that template and expectation with upper management like, hey, you can't just submit any kind of format I need to fill out this way so that we can plug it into Taylor. So I'm fine with that, whatever Taylor needs, whatever we need, and then we'll just set that expectation moving forward.

**@12:19 — Chad Gregory (LaunchPad Lab):** Let me go back to this real quick. I mean, part of the problem is the different carriers are still going to probably be a little, well, I don't know. Go ahead, Nikki. Sorry.

**@12:33 — Nikki Dow:** I guess I'm wondering, so after like this rate band file for the year has been like finalized and you upload it to SharePoint, what like, like how common is it that you would after that go back and change a band?

**@13:01 — Anna Fiske:** I'm think of past year.

**@13:03 — Nikki Dow:** Like is that like maybe one or two clients do it or like need a change or is that like you're changing bands all the time?

**@13:10 — Anna Fiske:** It would not be all the time. I think it was like 10 clients that we changed after the fact. And it really comes down to just what kind of subsidy they're requesting, that kind of stuff. And we go back and negotiate with the carrier carriers, really don't budge that much. So I would say 10. I feel like it was 10 last year that we actually had to go back after the fact. After workbooks were created and we talked to the client and we had to go back and re-band them.

**@13:43 — Nikki Dow:** Okay. Because I think like as a dev team, there's definitely a lot of concerns we have about like holding this in SharePoint. Like I know Conor's raised a lot of those concerns. Like someone can edit it and make a typo or, you know, someone could even delete the file or, and then also it's like for every workbook run, we have to download and parse this file and maybe that's a performance concern. So I know we've also like thrown around the idea of, you know, the admin panel has an import button where you upload this file and then basically the rates are saved and then there's like a form if they need to be changed. I think our concern with the import process was like if you were trying to like import rebanding files like multiple times to make changes and like kind of all the complexity around that. But if there's only maybe 10 times that you need to change a band, maybe it's okay that like that's a form.

**@14:49 — Chad Gregory (LaunchPad Lab):** You would just change it for the individual client and then we would know, regenerate for that individual client. Potentially. Or, you know, don't regenerate at all when this changes and let Anna or whoever still, like, just hit the button. Right.

**@15:11 — Nikki Dow:** Like, maybe the initial import just happens once before all the open enrollment stuff starts. And then if Anna knows client X needs to have their band updated, like, she can edit that in the admin console.

**@15:28 — Anna Fiske:** I'm fine with that. I think that's a great concern that you both brought up. Like, someone deleting it.

**@15:33 — Chad Gregory (LaunchPad Lab):** mean, that's happened in the past for other things, so. Well, let's look at this real quick. know Nico's not on. He wasn't able to make it today. But this would not be on the individual client, actually. We have a separate page, probably, to import the rebanding files for the various carriers. And then here, probably, we would just want to show the rebanding, the band for this client, or the bands, I should say. Do you need it to have both the band and the actual factor? Or, like, I guess, actually, a question of mine is, like, do we care about the band name itself, or, like, do we just care about the factor? You know what I mean? Like, I know the band is, like, associated with this, but, like, we really just care about the rate band factor itself here, right?

**@16:57 — Jagger Sturdivant (Questco):** I think so. Sorry.

**@17:00 — Anna Fiske:** Go ahead, Jagger.

**@17:02 — Jagger Sturdivant (Questco):** The only problem is going to be when you're getting the rates from Prism, it uses the name, but I think it might also give you the factor, which if it does, then yeah, you don't ever care about what the name is.

**@17:16 — Chad Gregory (LaunchPad Lab):** Oh, yeah.

**@17:17 — Jagger Sturdivant (Questco):** If it doesn't give you the factor in the API call, then you do need the name. I mean, the admin console won't need the name.

**@17:29 — Chad Gregory (LaunchPad Lab):** Yeah, but we might, well, it would probably be easier for us if we put two fields on there so that you could put in the factor.

**@17:41 — Conor Hawes:** Yeah, it looks like it just returns the rate group, not the factor.

**@17:44 — Chad Gregory (LaunchPad Lab):** In Prism, Conor. Yeah. So if we put both fields, the actual name and the factor for each of the carriers on this screen, if NextSol had an update to those bans, somebody could come in, update both fields as appropriate. Because it sounds like we'll need the name to associate it in PRISM, but we need the Factor itself to do the generation of the workbook, right? Or does that not, does the Factor actually not matter if we're just going to PRISM and getting, looking up the name and getting the rate, actually?

**@18:36 — Jagger Sturdivant (Questco):** Yeah, the Factor wouldn't matter. But the problem you're going to run into is for Aetna, there's different names for the rate groups for each plan. It's not like a global 865 for each plan. It's like the plan ID dash 865.

**@18:54 — Chad Gregory (LaunchPad Lab):** Oh, yeah, in PRISM.

**@18:56 — Jagger Sturdivant (Questco):** Yeah.

**@19:01 — Anna Fiske:** And if we make the rate ban field editable in the admin console, I would want that locked down to just me and Jagger, so people don't go in there and accidentally change it for their client.

**@19:16 — Chad Gregory (LaunchPad Lab):** That's actually probably a question coming up, is like, who else do we actually think is going to be in the admin console other than you guys? Sorry, I just want to finish this thought on this field. Nikki or Conor, do you have any thoughts on what Jagger just said about the name and like matching that to a name in PRISM that doesn't actually match? Because it has the plan name and the band.

**@20:04 — Nikki Dow:** Um, so you're asking this question so we know, like, what this form would.

**@20:10 — Chad Gregory (LaunchPad Lab):** Basically, I'm just asking, like, is it okay? I don't know what, I think it's just work to be done, is maybe my question doesn't actually make sense. Just trying to think, like, do we need to include anything else on there to make it easier or something? Um, but I don't think we can really.

**@20:35 — Nikki Dow:** Yeah, I don't think I can answer that at the moment, but can definitely, um, like, get a better understanding of how bands map to rates so we know, like, what information we would need.

**@20:52 — Chad Gregory (LaunchPad Lab):** Okay.

**@20:53 — Jagger Sturdivant (Questco):** Yeah, I just want to mention, we can't, like, in the admin console, we're changing a band, we can't give you the rate group name, basically, because it's different for every plan.

**@21:05 — Chad Gregory (LaunchPad Lab):** Yeah, you can give the band name, which loosely ties to the...

**@21:13 — Jagger Sturdivant (Questco):** Yeah.

**@21:17 — Conor Hawes:** And it wouldn't be, it's not a single band per client, per carrier, like if you have a band for Kaiser and a band for Edna.

**@21:33 — Jagger Sturdivant (Questco):** Yeah, that's possible.

**@21:35 — Conor Hawes:** And it'd be, it's scoped to a renewal period. So Chad, I just, I guess in terms of the UX, like, I don't think it would just be a single rate band, like heading in value.

**@22:00 — Chad Gregory (LaunchPad Lab):** Uh, sorry, say that again? So, like, if I look at this, you don't think that it's just this for Agna, and then the same thing for BCBS, Kaiser, um, and I forget, wasn't there a fourth one?

**@22:26 — Conor Hawes:** I guess what I'm trying to say is, like, there could be up to three or four per renewal period. So I feel like, at least from the design that you pulled up, like, this is, like, client detail page.

**@22:42 — Chad Gregory (LaunchPad Lab):** Yeah, wouldn't the client, and maybe Jagger and Anna, I could be totally wrong, but it seems like we just need you to have a spot on here that shows what band names we have for the three carriers, which would be one per carrier, right? And then be able to edit those?

**@23:13 — Anna Fiske:** Yes. Right, Jagger? Yeah, that sounds right.

**@23:19 — Chad Gregory (LaunchPad Lab):** And Conor, I don't know if this is where maybe you're thinking, but that band, it would be associated, I think what Jagger is saying, would be associated to multiple plans, rates of plans in prism. And like the 835 or whatever it was.

**@23:38 — Conor Hawes:** No, I think the point that I was trying to make was the, at least like the wording that you had used, it sounded like you were saying there'd be a single field on this page for the rate.

**@23:47 — Chad Gregory (LaunchPad Lab):** Oh, sorry.

**@23:48 — Conor Hawes:** I was trying to make the point that there won't be. Three fields. And that like, it's not even like. It's per renewal period. So they will have quite possibly a different rate banner from 2025 to 2026. And so if we, yeah, sure. At first, when we launch and we import the file, we'll probably only have one renewal period's worth. But just, I guess, a heads up or something to think about in terms of design in the UX, that, like, renewal period will be, will play into it.

**@24:31 — Chad Gregory (LaunchPad Lab):** Yeah. Because you don't want to edit, well, honestly, you shouldn't be able to edit, like, 2025 at all. Even if you are Jagger and Anna.

**@24:40 — Conor Hawes:** And then if you, like, you want to make sure that you're, you're changing the right value in these, that you, like, know what, what is the latest.

**@24:59 — Chad Gregory (LaunchPad Lab):** Okay. Let me keep moving here. So I think we are going to end up moving rebanding into here. And then the next question that I had, I know you guys kind of went through reports a little bit on Monday. I'm trying to figure out one, I think a good way to like, save on scope here is if these reports are just exports, we can kind of get to that. But the other thing that I'm trying to figure out is if any of these reports listed here are truly like, hey, handled, I guess, by like this renewals screen. And if we gave you like an export of this table, if that solves, for example, the master renewal tracker and client-sponsored plan tracker, which are, according to this, like these sort of master trackers where each one has like a single client renewal and has the, I guess I don't know exactly what we mean by captures the full life cycle from initial setup through completion, if that's like a different column for each step or something, or if it works to just have like, here's this client, here's their like renewal dates, here's their status. Name, ID, Control Group, I'm not sure I know exactly what that is, and then Status, and Ownership. What's your thought on that? Like, do you need a separate report, or do you think that that actually does get handled with, like, a list that's sort of like this? We can add additional columns here.

**@27:29 — Anna Fiske:** I think it, I mean, it could be accomplished in one dashboard, I guess, like, Tracker. All we need is, like, that Detail Tracker. It's currently an export, how we have it, in Client Space, so I'm fine with that. But it's something where we can go to our dashboard in Client Space, see what's going on with the clients, but then we always export it and filter it down. So that one already exists in Client Space is what you're saying? Yeah, it's a dashboard. It's not the best. And we were trying to utilize the admin console over Client Space.

**@28:22 — Chad Gregory (LaunchPad Lab):** And the benefit of that is just to keep you guys out of Client Space mostly?

**@28:27 — Anna Fiske:** Yeah, for eventual decisions of leaving Client Space altogether, yeah.

**@28:33 — Chad Gregory (LaunchPad Lab):** Yeah. If it happens, I don't know. I'm trying to just figure out basically like, can we get this renewal list to serve as that, essentially? I think the answer might be yes, assuming we can add more of these columns on there. Can you explain, I don't know if I should know what if The control group is, is that like, whether it's like Questco master plans or client sponsored plans?

**@29:10 — Conor Hawes:** I believe it's the parent.

**@29:11 — Anna Fiske:** Yeah, that's the parent. KFC.

**@29:15 — Conor Hawes:** Oh, got it.

**@29:16 — Chad Gregory (LaunchPad Lab):** Yep.

**@29:18 — Anna Fiske:** I do remember that.

**@29:19 — Chad Gregory (LaunchPad Lab):** So like, if it, yeah, okay. Conor, based on what you just said, does that feel reasonably easy to access that data?

**@29:36 — Conor Hawes:** The control group data? Yeah. To be honest, I haven't looked into like where it would be.

**@29:45 — Chad Gregory (LaunchPad Lab):** Okay. I think it's in the client master in Prism.

**@29:49 — Conor Hawes:** Yeah, it's in Prism and in board space.

**@29:54 — Jagger Sturdivant (Questco):** It's in there somewhere. I think it's the client master, but don't quote me on that one.

**@30:00 — Chad Gregory (LaunchPad Lab):** Are all these dates, pre-renewal meeting, consultation date, OE window, batch effective date, those all in client space?

**@30:11 — Anna Fiske:** They are.

**@30:16 — Chad Gregory (LaunchPad Lab):** Additional indicators should track whether a subsidy was requested and approved and whether an OMQ was requested, which I think...

**@30:26 — Conor Hawes:** That's a checkbox, right?

**@30:28 — Anna Fiske:** Those are all in the BSR, in client space.

**@30:31 — Conor Hawes:** So, and the BSR and the batch, those are two separate data forms, right?

**@30:39 — Anna Fiske:** Correct, yep, but they're linked, so you can link them together.

**@30:45 — Conor Hawes:** Could you give me, like, a one-sentence refresh on the distinction between the two?

**@30:53 — Anna Fiske:** The batch is where we update all the plans and make the renewal changes. The BSR is where we document everything that we did in the batch, and any client communication gets documented in the BSR.

**@31:08 — Chad Gregory (LaunchPad Lab):** BSR is like the workflow of the batch, basically, right? Sure, yeah.

**@31:14 — Anna Fiske:** I think. It's a shame they both start with B.

**@31:22 — Chad Gregory (LaunchPad Lab):** Okay, thank you.

**@31:23 — Conor Hawes:** That's helpful.

**@31:24 — Anna Fiske:** They do have some repetitive information between the two of them, yes.

**@31:28 — Conor Hawes:** Okay, so when we're generating these reports, we're probably pulling down both, is my working assumption.

**@31:38 — Anna Fiske:** be a mixture between the two, yeah. You'll get most of it from the BSR, but, like, the batch status obviously comes from the batch. Certain things will come from the batch.

**@31:46 — Chad Gregory (LaunchPad Lab):** Perfect, okay. Additionally, this next one, a report that identifies clients currently in implementation status who do not yet have a benefit renewal batch set up. I think you guys talked about this on Monday, and I can't remember if I read what this meant.

**@32:09 — Anna Fiske:** So that would be our new clients coming out of onboarding. Oh, implementation.

**@32:15 — Chad Gregory (LaunchPad Lab):** Yeah, that makes sense.

**@32:17 — Anna Fiske:** Yeah, so sometimes they get a renewal, sometimes they don't. So we need to kind of have that list and just have our implement. We have implementation specialists on our team that just handle those clients, and they need to have that list to check in. So here, they're getting a renewal. Yes, let's make a batch. Let's get that information set up. They're not getting a renewal. We just push them through.

**@32:37 — Chad Gregory (LaunchPad Lab):** Should we, is there any rule for us to like set up a renewal for a new client? Like when a client comes in, create a batch immediately if they're new?

**@32:53 — Anna Fiske:** Yes. Every new client is getting a batch. Yes. Like immediately? Mm-hmm. Okay.

**@33:02 — Chad Gregory (LaunchPad Lab):** Conor, that probably factors into what we were talking about this morning. And then in that case, they should all have a benefit renewal batch set up. But I think this would also be kind of handled by the table here. The client would be in here. We would have their dates. We would have a stage of, I guess it would be called, yeah, whatever. I mean, basically everything is going to go, like, we're going to kind of skip set up and workbook prep. Well, those will be the status. I guess like most of the year until the batch gets created and when the time hits. Workbook prep will be very short.

**@34:16 — Anna Fiske:** I guess something might be in workbook prep if there was an issue or something. Yeah, I guess if it aired out and Taylor could create a workbook. Yeah.

**@34:25 — Chad Gregory (LaunchPad Lab):** Yeah. Okay. Report that shows in the client workflow grid goes live along with defined window length. I need to refresh my memory if that's something we are going to generate a file for that. I can't remember if we if Taylor actually is going to import it or if it gets imported by. Yeah, it'll be the analysts.

**@35:04 — Anna Fiske:** They're also putting like a human stop on that one just so they can put their hands on it for a little while.

**@35:11 — Chad Gregory (LaunchPad Lab):** And then, so for this report, we would need to like check PRISM to see when that happened, I guess.

**@35:26 — Anna Fiske:** Yeah, so it'll have on the workflow grid, it'll have what workflow they have, when it opens, when it closes, and how many days it was open. Yeah, Taylor could look at that and pull that information into a report here. That would help the analyst make sure nobody got left behind.

**@35:44 — Chad Gregory (LaunchPad Lab):** Everybody got their window opened. Yeah, that makes sense. And that does feel like maybe it's separate from this, but, well, it could be on this, depending on how many columns we can add and reasonably show. So maybe it could be on the same thing. I was going to also ask about this. Well, let me finish and then I'll get back to this. I report this shows open batch counts by RenewalRep. This one probably should be separate. Although RenewalRep will be on this list. But I think giving you something like this is, oh wait, yeah, like segmenting by carrier. So this would be like after, I don't open batch counts. How do we know how to segment it by carrier? Just like which rate band they have?

**@36:56 — Anna Fiske:** Yeah, yeah. Okay.

**@37:03 — Chad Gregory (LaunchPad Lab):** So this report would basically look like, hmm.

**@37:12 — Anna Fiske:** The purpose of that report is for us to be able to pull and see, okay, 90% of Aetna is ahead of schedule. They're accepting their renewals. Blue Choice, nobody's accepted their renewal. We're getting, you know, we're falling behind on that one. And it's more so for upper management to pull that and see what carriers are being accepted faster and which ones aren't. So the reason that we did have like these little reports separated out from the big master tracker was so that we wouldn't have to pull the big tracker, filter it down, separate out the executive information and send it out.

**@37:47 — Chad Gregory (LaunchPad Lab):** Uh, yeah.

**@37:54 — Nikki Dow:** So is that report just showing all the batches? It's where like the given carrier was an option because like if I work for KFC and we have rate bans for Aetna and Blue Choice, my batch would show up in the report for Aetna and the report for Blue Choice.

**@38:19 — Anna Fiske:** I would want it to be on what they currently offer, not what they're renewing with or like what's being offered as a renewal. Oh, okay.

**@38:28 — Nikki Dow:** What they have, okay, what they've had in the past year.

**@38:31 — Anna Fiske:** Yeah, what their current year is.

**@38:33 — Chad Gregory (LaunchPad Lab):** The band isn't what's important. It's the last year or the current year. Right. Yeah, I'm sorry.

**@38:39 — Anna Fiske:** That's good.

**@38:41 — Chad Gregory (LaunchPad Lab):** I'm trying to think of the best way to like show that in an Excel file, but maybe we just need to think about it. Do you have like examples of these reports that you've built before at all? Yes.

**@38:56 — Anna Fiske:** Okay, that would be great to have.

**@39:00 — Chad Gregory (LaunchPad Lab):** I'll put a note to ask you for that. And then, reporting that breaks down batch status count by control group, including indicators for whether the renewal is a master renewal, CSP, ancillary only, deduct or remit. Can you explain this last one? And then, I mean, maybe the example is going to make more sense, but what is this trying to get at?

**@39:37 — Anna Fiske:** I'm honored to answer your question. It's in the BSR. Reporting that breaks down batch status count by control group, including indicators under the rules, master, CSP, ancillary, or deduct or remit. So that's going to be pulled out of the BSR as one of the checkboxes. If it's a master CSP, ancillary, and it should say and or deduct. Deductant Remit, because you can be a CSP and Deductant Remit, and it would be the status counts of the batch. So like how many master renewals are sitting in workbook prep or consultation? How many CSPs are sitting of what status? And it kind of, again, this is another executive report where they're weighing the success.

**@40:30 — Chad Gregory (LaunchPad Lab):** Yeah, this makes a little bit more sense. It's really just like basically column headers, for these different types and the counts of the batches in different statuses along the rows or something.

**@40:43 — Anna Fiske:** Okay.

**@40:45 — Chad Gregory (LaunchPad Lab):** Yeah, if they want client information, they're going to pull the tracker. Yeah. So then kind of a question that we're trying to figure out a little bit about the admin console is bit let's give a little let's you a little getting the data synced reasonably so that we aren't like constantly pinging PRISM and client space for data and so that you have the freshest data that you would need. And these reports obviously have a play a role in that. We don't want you to like run a report, but it's out of date.

Do we think, and one of the areas that we're specifically thinking about that is like this live table of like, to get the table in the first place, we need to get all the data synced from the different sources. But then if you wanted to search for sort, I think it would be great if we didn't do sort. I don't know how needed that would be, but trying to then sync it again, if any of those actions were taken.

I don't know, Nikki, I think you were more eloquent about this topic than I am being. So I don't know if you want to take over, but one of the things that we were thinking is like, if it synced nightly, and then if you went in to actually click on next sol, then we sync just next sol. So you see all the correct data here. Is that okay? Okay, and then if you... We're over here and ran a report, like actually export it, then we sync again. Would that work versus like every time the page loads or something?

**@43:15 — Anna Fiske:** I'm going to say no, but I know that's a big ask on you guys. Especially once we get deeper into open enrollment, they're wanting us to update them every 30 minutes, hour. So yeah, we would need as close to live information as possible, honestly.

**@43:35 — Chad Gregory (LaunchPad Lab):** Who is asking you to update who?

**@43:38 — Anna Fiske:** It's upper management. They're weighing the success of open enrollment, so they're wanting to know. And then the renewal reps, they also want to make sure that, you know, which clients are you left behind? Where are they at? Did they submit their DocuSign? Did they sign it?

**@43:50 — Chad Gregory (LaunchPad Lab):** You know, that kind of stuff. So, I mean, with 1,500 plus clients, gets a lot to drill in individually. So if you... Had upper management asking you about one of the reporting areas. Like, yeah, I guess part of the problem would be like you guys needing to run that export like over and over and over again.

**@44:23 — Anna Fiske:** Over again. Yep.

**@44:31 — Jagger Sturdivant (Questco):** Could we have like a status somewhere on here that just says when it was last synced?

**@44:38 — Chad Gregory (LaunchPad Lab):** Yeah, I think we could do that depending on how much that helps. What's your thought on that, Jagger?

**@44:49 — Jagger Sturdivant (Questco):** Like, because you said you don't want to refresh it every time we go to the page, and I get why.

**@44:57 — Chad Gregory (LaunchPad Lab):** Yeah.

**@44:58 — Jagger Sturdivant (Questco):** So could we have like a... Manual Refresh button with a last synced timestamp. And then if we need to repull the report, we'll just manually re-sync it and then download the report.

**@45:09 — Anna Fiske:** I like that.

**@45:12 — Chad Gregory (LaunchPad Lab):** Yeah, does that help because you could manually re-sync it but still see it here versus... Right. Okay. Nikki, how are you feeling about something like that? Like, give them a manual refresh button. And that way they can refresh and see the refreshed data in the table on this page. They could, like, you know, go through here and find whatever they needed to find. But then, obviously, they could still export. We would even get the most recent when they export again, I think. Well, maybe we don't have to if we do the refresh. Bye. I guess it depends on how long it takes to refresh. Yeah.

**@46:04 — Anna Fiske:** And if we can still...

**@46:06 — Conor Hawes:** Well, yeah, the contents of the file, we're not showcasing that all here, right?

**@46:16 — Chad Gregory (LaunchPad Lab):** Say that again, Conor? What do you mean?

**@46:23 — Conor Hawes:** Like, so were you envisioning like just pulling this subset of data and that's what would be syncing and keeping up to date or reusing and pulling down all of the data points for all of the reports?

**@46:40 — Chad Gregory (LaunchPad Lab):** Just the report that would be this page and everything that was like noted here, I guess, was what I was thinking.

**@46:52 — Nikki Dow:** Yeah, I think my mind was maybe going to the same place Conor's is. Can you show the list again? If we were like just trying to live sync, you know, like the client name and the current stage, I could see that, you know, being feasible. And like, like Jagger said, maybe we have like a last synced at shown somewhere and the option to re-sync. All of those data points that were on that big like tracker report, I'd be really hesitant to be like saving those in Taylor and trying to keep all those in sync, I think. I don't know. So I'm wondering if like we can have this renewals list as it appears here with just that limited information that's being kept in sync. But if you export the full report, we would then be able to like fetch the full set of data and generate this CSV or spreadsheet or whatever it's going to be. I think I would be hesitant to add all those data points onto this page here and then try to sync those constantly, if that makes sense.

**@48:26 — Anna Fiske:** So you're saying the list as it sits now, that's what we would see on the dashboard, and then we would have an export button to kind of pull this into that full tracker report that we needed?

**@48:38 — Nikki Dow:** Right, and then that export would have, like, that big list of data points we discussed.

**@48:46 — Chad Gregory (LaunchPad Lab):** Hmm.

**@48:54 — Anna Fiske:** Who was thinking that term?

**@48:57 — Chad Gregory (LaunchPad Lab):** Yeah, I think this doesn't have to be the four things that you see would be maybe the important thing for you, Anna. Like, if there are other more important things to see here, like the rep or something, maybe that helps.

**@49:23 — Anna Fiske:** I don't see any negative side to doing what Nikki said. I need to think that one through a little bit. I don't see any negative.

**@49:35 — Chad Gregory (LaunchPad Lab):** What do you think, what do the requests from the management look like, mostly? Like, I guess that's the question. It's like, are you going to have to export something for them every time anyway? Or do they sometimes just say, tell me this about this client?

**@49:54 — Anna Fiske:** Yeah. So the goal was, is to have within the admin console, the dashboard. And it's got that master tracker, and then it's got, based off that master tracker, there's widgets below it that are pulling information from that master tracker that kind of sums up different areas. So all the, you have that big chunk that we went over the master tracker request, and then all those little ones underneath it should be pulling off of the tracker. And that's where they're trying to weigh the success of open enrollment. So what we did last year is we'd have to pull that massive tracker down, filter it down, figure it out, like, what they're asking for specifically, and then send them that report. The goal this year was, like, hey, go to the admin console. Your widget is sitting there. It'll tell you what's going on from that level, and we don't have to pull these reports constantly for them. They can pull it themselves if they want to report to all their bosses, but it kind of was, the goal was to alleviate that from us.

**@50:53 — Chad Gregory (LaunchPad Lab):** Because they were asking, do you think these people would be, would they actually be in the admin console? Then?

**@51:01 — Anna Fiske:** I would want them to be able to see it, but not do anything other than download a report.

**@51:05 — Chad Gregory (LaunchPad Lab):** Okay.

**@51:07 — Anna Fiske:** Because they're going to touch stuff and break it.

**@51:17 — Chad Gregory (LaunchPad Lab):** I'm just like throwing this out there and the devs can tell me I'm a jerk and a horrible person. But if you didn't actually have, if like you just had this list with the columns, like a subset of columns with an export button that had all of the data for this master tracker. And then I guess something like this, not this, I think. Not these master tracker numbers probably, but really more of like what you were saying, like number of clients currently in implementation status who do not have a benefit renewal batch set up, which would hopefully be zero, but I guess an error could happen. And number of, or I'm not sure exactly what this would be, report that shows when the client, like how would this one look in a.

**@52:32 — Anna Fiske:** That would show like the client and then another column for when the window was open, when it was closed, and how many days is that, how many days was it open, which is all pulled off the grid.

**@52:44 — Chad Gregory (LaunchPad Lab):** How do you show that in a widget? That one might be is not really a widget.

**@52:51 — Anna Fiske:** Oh, good point. Yeah, you're right.

**@52:53 — Chad Gregory (LaunchPad Lab):** Okay. Because that's too many dates.

**@52:55 — Anna Fiske:** It's not a count.

**@52:57 — Chad Gregory (LaunchPad Lab):** This one is a count. It is several. Several counts. How many renewal reps do you guys have?

**@53:04 — Anna Fiske:** 60 something? Would it be able to be like, instead of a widget, which I guess was a bad term to use for that, like just, it's the name of the report and it's a link where they can click it and it pulls that report for them?

**@53:24 — Chad Gregory (LaunchPad Lab):** That was what I was thinking, would be, but I was, yeah, trying to fit it into your widget idea, sort of. Yeah, throw that away if you want, it doesn't have to be a widget. Uh, well, okay, never mind the path that I was going on. So it sounds like, because we only have four minutes, it sounds like we can get by at the moment, maybe you need to put a little bit more thought into this, Anna, that we can get by with a table with limited columns, similar to what we're seeing here, with an option and refresh, and like the last refresh timestamp, an export button for the master list, basically. And a place that you can go, like a reports page that would have links for, I think we would do, well, I don't know. I guess I was thinking like we could probably skip this one. Maybe we have the Master Tracker link in there still, but like we could give them the workflow grid one, this batch counts, and this batch status counts by control group as like links here.

**@54:52 — Anna Fiske:** Okay.

**@54:55 — Chad Gregory (LaunchPad Lab):** And then if, yeah, if you can get me the examples, I'll try to pop some. That'd be great, otherwise I'll forget. Nikki and Conor, how does that feel to you right now?

**@55:17 — Conor Hawes:** I think we should figure out how to generate the master tracker, and from there, how much compute is required, and how resource of intent is, and how long it takes. I think that kind of will dictate some of the UX questions we have, and the frequency that something can be synced, and how realistic it would be to sync all of that data, versus only trying to have a subset of it, and then relying on the export. I don't want us to, like, box ourselves into a particular user experience, kind of like on speculation.

**@56:11 — Chad Gregory (LaunchPad Lab):** Yeah. Okay. Well, Anna, I'm thinking, like, maybe next week, you and me and maybe, like, Dimple and Nico get together just to make sure that we have, like, all the right information that you need on the details page and that you're liking the general style of this, so that we're, like, close to approval, but, like, exactly what Conor said, like, I have concerns about, like, the specific columns, for example, and the approach to the exports a little bit, but hopefully you feel like it's on a relatively good path right now, since you showed it to some folks the other day. It looks great.

**@56:57 — Anna Fiske:** Yeah. Okay.

**@56:59 — Chad Gregory (LaunchPad Lab):** That's good. Okay. Thank you guys so much. We'll keep making progress here and we'll talk to you guys tomorrow.

**@57:09 — Anna Fiske:** All right. Thank you guys. Thanks everybody.

**@57:11 — Nikki Dow:** Bye. Thank you.
