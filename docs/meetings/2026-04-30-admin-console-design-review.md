# Admin Console Design Review - April 30

[VIEW RECORDING - 44 mins (No highlights)](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY)

**Attendees:** Anna Fiske, Chad Gregory (LaunchPad Lab), Dimple Desai, Nikki Dow, Nico Zubía (referenced)

---

[@0:00](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=0.68) - Anna.Fiske
Right. Thankfully we don't have stairs.

[@0:03](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=3.62) - Chad Gregory (LaunchPad Lab)
Yeah. It's exciting. Yeah.

[@0:09](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=9.54) - Anna.Fiske
That's one thing where I'm like, that's why I prefer a nanny rather than do a daycare, because now I can be here for the stuff.

[@0:15](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=15.96) - Chad Gregory (LaunchPad Lab)
Totally. Yeah, we got very lucky that my wife's mom comes over and watches a lot, and then my wife only works like two or three days a week.
Um, so, yeah, it's, it's really good, but I'm like locked in here in the, in the office most of the time, so I get, I get the video, and then I go try to make her do it again.

[@0:41](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=41.92) - Anna.Fiske
That's it. My poor husband, he actually goes to work, and I'm like, she did this and this, and he's like, let me see, and she's like, what a liar, I didn't know such thing.

[@0:50](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=50.06) - Chad Gregory (LaunchPad Lab)
Yeah. Oh, man, now you're making me think like, okay, what, what has Nora done that's cool recently? Definitely.

[@0:58](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=58.22) - Anna.Fiske
She's like hitting huge. Milestones. that I can tell because she's not sleeping. So like her little brain is memorized.
She learned how to clap. She's learned her sign language.

[@1:06](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=66.6) - Chad Gregory (LaunchPad Lab)
Boom.

[@1:07](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=67.74) - Anna.Fiske
She's done all sorts of stuff. That's awesome.

[@1:12](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=72.3) - Chad Gregory (LaunchPad Lab)
Yeah. I mean, I just remember all that. It was like last year, basically. So cool. I think I added Dimple in here and I think she might be joining.
But oh, yeah, I see you're on there. So hopefully she'll she'll be able to hop in in a second.
But I'll pull up these designs. We just literally right before this, we're having a huddle about certain things. So then it's not all super, super clean.

SCREEN SHARING: Chad started screen sharing - [WATCH](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=105.232267)

Well, actually, I might be speaking incorrectly. Nico looks like you got them into a pretty good spot. But I wanted to kind of walk through what the flow of this is.
far, and primarily make sure that we're covering off on the stuff that you need in this phase of the admin console, and the information that you want to be able to see on there is there, and the functionality of things is there.
We're not really talking about specifics on the reports right now, but on that dashboard screen, I think it'll be key to get some thoughts on what you need to see there.
So I'll start with, there will be like a login page like this that will just have a button to log in with Intra.
I just noticed a typo here, Nico. Uh, with Intra, so that... When you click that, it'll go to like the Entra login piece, and then drop you in after you log in.
So then that means we don't need to have like password reset and all of that here, because that's all handled within Entra.
And same for like when somebody gets disabled from your guys' accounts, they won't be able to get in here either from Microsoft.
So then the first place that you land, I guess it's called the dashboard. I don't know if we want to give it a different name, but this is the full list of all of the clients and their current renewal or like the current year of their renewal.
A couple of things to call out here. We did add in something that we talked about last week, which was a refresh button so that that's kind of handled.
I don't remember. Dimple, if you were on that call, but trying to avoid issues with making, like running too many API calls to Prism and having to sync all the time and page load issues.
There is a refresh button here so that you can refresh if you need to. And obviously when you come to the page for the first time, it's going to refresh and sync everything.
But if you've been on this page for a while or whatever and you need to refresh it, you can.
We also have an export button to export not just what is on the screen here, but additional data from each of these into a spreadsheet.
So you can use that to deliver updates to management or you can use it for your own, your own needs as well.
Right now we have. Just kind of very limited info here, four columns, as you can see, plus a little icon.
That icon is indicating if the client got stuck, like with a job or something, so that you know something's up with that one.
We didn't want to use the stage column for that because we thought you still would want to see specifically what stage they are in when they got stuck.
So that is kind of like a note to go check the exceptions or go check Azure and see what's going on with that, whether you need to just hit regenerate or go fix something in the file or in Prism.
And hopefully that's like a pretty good indicator for you. The other columns, we've got renewal date, stage, and the last update on this renewal for the client.
So... So... Those were kind of the first things we thought of in terms of what you might need to see on this page.
Is there anything else that you think you need to see when you're like looking at things from a glance here?

[@6:16](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=376.63) - Dimple.Desai
Anna, would you want to see like the renewal rep or anything like that on the main page or like client rating?

[@6:25](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=385.38) - Anna.Fiske
I don't think so. I mean, once you click into the client, all that's going to be there. The only thing, and I think we talked about this last time, is if I was to click renewal date, like could it filter it down, like put them in chronological order or something like that?
Like that would make my life a lot more easier. But I think you said no on that last time, I can't remember.

[@6:46](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=406.56) - Chad Gregory (LaunchPad Lab)
Yeah, the thing that we said is that the sorting then requires another sync, but I agree that that would be helpful.

[@6:58](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=418.4) - Nikki Dow
Yeah, I'd be okay with. Sorting by stage, because that's something we said we're going to sync.

[@7:03](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=423.9) - Chad Gregory (LaunchPad Lab)
By stage?

[@7:05](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=425.89) - Nikki Dow
Yeah. How does that help?

[@7:08](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=428.51) - Chad Gregory (LaunchPad Lab)
Does that help, Anna? Or is, like, renewal date is more key? Oh, sorry.

[@7:14](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=434.35) - Nikki Dow
I should have said, like, the three items here, I think, are okay to sort by. Yeah. I just didn't want us to, like, add sorting by items that we're not syncing, if that makes sense.

[@7:28](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=448.49) - Chad Gregory (LaunchPad Lab)
Okay. Yeah, that would be perfect.

[@7:29](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=449.97) - Anna.Fiske
I would love that.

[@7:32](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=452.54) - Chad Gregory (LaunchPad Lab)
Nico, I'll add in a comment here for you. And then for the client names here, are those, like, links to anything?
Each of these are links to their details page, so I'll show that next. Okay. Add sorting for the overcommonstivity here.
Okay. If... If this feels pretty good, then I'll move on to what that details page looks like here. And this is one where I'm not sure if I'm guessing there probably is more stuff to add than what we have currently.
But you can see at the top, the client name, a back button to go back to the dashboard, the stage.
You can see the current renewal year. And this is a dropdown so that you can go look at the previous years if you needed to.
And that'll just refresh the page with all the data and information from that previous year. I'm not sure like in this first year, I guess we probably won't have all of that, I would think.
But obviously for future years, that'll be super helpful to you. We have a little action button, which I'll get to in a second.
But in terms of the other information that we have. On the page right now, we did include the renewal rep and a note, like an OMQ field here.
I was thinking this is kind of just like yes or no or yes or blank, but you tell me like maybe it should just be, maybe it should be the plan.

[@9:19](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=559.101) - Dimple.Desai
Should it be yes pending or no? Like if a client requested an open market quote and there's like a consultation going on, would that be pending?

[@9:27](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=567.361) - Chad Gregory (LaunchPad Lab)
Hmm, how would we know that? We would need to give them a place to, we need to give somebody a place to update it?

[@9:38](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=578.361) - Anna.Fiske
Yeah, I think it's in the BSR though.

[@9:41](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=581.181) - Dimple.Desai
Correct. Yeah, so there's like a checkbox on the benefit setup and rules data form where when a client requests an open market quote, it launches some cases or tasks to, I forgot who it was, Anna.
But then when it gets approved, there's another place on the BSR where... The person who had the task can mark whether or not the open market quote was approved.

[@10:09](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=609.491) - Chad Gregory (LaunchPad Lab)
So should it be like no consulting and approved?

[@10:13](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=613.431) - Dimple.Desai
Yes.

[@10:15](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=615.361) - Chad Gregory (LaunchPad Lab)
And then the reason I just had it as just this field versus like showing anything else about the OMQ is that once you, we give you this spot to upload the template that we've talked about, or you or Betty or somebody like that.
And then you can regenerate all the files. So then the workbook will have all of those OMQ details. We could throw in some more of the details potentially here, but it's already kind of getting crowded.
So I didn't want to do that from the jump. Is there anything else that might be really important to know?
Just. Just. From like a scan of this page that you would need to be able to see about the OMQ?

[@11:12](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=672.361) - Anna.Fiske
Like without digging into the workbook? Yeah, really just those three things. Like did they request it? Was it presented or we received it?
And are they going with it?

[@11:26](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=686.581) - Chad Gregory (LaunchPad Lab)
Should this actually be requested?

[@11:34](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=694.801) - Anna.Fiske
So the no would be no, they didn't ask for it. And then.

[@11:38](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=698.261) - Chad Gregory (LaunchPad Lab)
Yeah.

[@11:39](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=699.621) - Dimple.Desai
Or would it be no, they didn't get it? Would it be like rejected?

[@11:42](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=702.401) - Chad Gregory (LaunchPad Lab)
Oh, yeah. So should it be blank? If not requested. Yeah, I like that. Then consulting when requested. Then. uh, approved or rejected and all of that can be found in the BSR, Dimple?

[@12:10](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=730.971) - Dimple.Desai
Yes, that's correct. Okay.

[@12:13](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=733.531) - Anna.Fiske
Can we change the consulting to requested please?

[@12:15](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=735.991) - Chad Gregory (LaunchPad Lab)
I feel like that's gonna confuse people.

[@12:18](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=738.091) - Anna.Fiske
They're gonna think that the agency's having the conversation with the client.

[@12:24](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=744.921) - Chad Gregory (LaunchPad Lab)
Perfect.

[@12:27](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=747.541) - Dimple.Desai
Here, let me get you guys like a screenshot of where that is in client space.

[@12:31](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=751.461) - Anna.Fiske
I tried. Zoom won't let me upload it.

[@12:34](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=754.361) - Dimple.Desai
Oh.

[@12:34](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=754.881) - Anna.Fiske
you put it in Azure? Yeah, you can put it in.

[@12:38](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=758.801) - Dimple.Desai
Uh, Asana or.

[@12:40](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=760.461) - Chad Gregory (LaunchPad Lab)
Oh, Asana.

[@12:41](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=761.721) - Anna.Fiske
Just kidding. Not Azure.

[@12:43](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=763.541) - Chad Gregory (LaunchPad Lab)
Um, and then that's good. Um, I'll just keep talking about what is here so far and then we can get back to like what else is missing.
So we have all of these links. Links. Not all of them will show up at the moment of, you know, right when the renewal starts, obviously.
The workbook will be there first. So clicking on that will let you go download the workbook, or we'll download the workbook for you.
When the executed workbook lands in SharePoint, we have that, then we'll be able to pull that in. Then all of these other files get generated.
So we have the CBE Prism Imports for the rules, plans, and the enrollment grid. And because we have different sheets for each class for the Cost Sheets and Benefit Guide, we added this sort of section down here.
I do wonder if it takes up too much room, or if we should, I don't know, do something a little bit different with like moving the links.
Down here too, or something into like this box, Nico, especially if we need to add more information up here.
But right now, all of this information is available to you. So you would be able to download the workbook, executed workbook, CDB, all the Prism imports, any cost sheets, and any benefit guides.
One thing that I did just realize is probably missing is the combined packets. Then we have these rate bands.
So on the client, you can see any of the band names and the, oh, Nico, I just noticed this little thing.
I don't know if that's right. But we can put carrier here, rate band name, rate band factor. Because each of these, we've got each of the carriers, the band names, and the factors for those.
And we get those from this screen. So when you have a new rebanding file, you can select the carrier that you're uploading, the time period that it belongs to, and then upload that.
And we'll process it, and each of the individual clients will get updated with the band name and factor for that carrier for the appropriate year.
And if you needed to make a change to that, you could come to the actual client themselves and update that.
But, and then if you needed to regenerate the files, you could by clicking. Other the Regenerate Files button. If you needed to just update the entire file, you could do that by going back down here so that, you know, if you uploaded the at now on for, I mean, that might break actually if you uploaded the wrong file.
But if you uploaded the wrong year, for example, you could redo that here and then I would just overwrite everything.
How is everything sounding so far?

[@16:32](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=992.921) - Anna.Fiske
Really good. The only thing that I would probably want added to this page for the client specific is like a notes box.
Okay. So I like your idea of moving the links down to that, like, scoop maybe classes over and put the links down there.
And just add like a little notes box. Because sometimes, like, people just like to make notes. And sometimes it's novels, but, you know, each their own.
What do you think about that demo? Well, do you think we should put the notes in here or keep pushing them to client space to make the notes?
Because I don't want them to have, like, the notes just to stay here for no reason if it doesn't feed into the CBE, because the CBE has a notes section on the second page.

[@17:18](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1038.62) - Chad Gregory (LaunchPad Lab)
Oh, yeah. Well, that's in the workbook, actually. And would the notes be pulling from client space?

[@17:24](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1044.7) - Dimple.Desai
Like, are we encouraging people to enter the notes?

[@17:26](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1046.72) - Chad Gregory (LaunchPad Lab)
We moved it to the workbook on purpose, actually, right?

[@17:35](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1055.74) - Anna.Fiske
How about a notes section for the analyst team? Because this is where they're going to come in and pull their imports.
So if we can label the notes section, analyst notes. Because sometimes that's helpful as far as, like, they left a client-sponsored plan and they're moving to master.
Just to make things super clear. Yeah, are they going to have...

[@17:56](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1076.28) - Chad Gregory (LaunchPad Lab)
That leads into another question I have, Anna, is... Who all is actually accessing this? I mean, in the future, it could be everybody.
For this phase, like how many people are we actually thinking? Because I think we've said different things maybe. Like I know BDU, Dimple, and Jagger primarily probably to start.
And you would have some executives or managers who might just have access to get the reports. That's good point.

[@18:28](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1108.81) - Anna.Fiske
So let me ask you this. So all these links that are here, is Taylor going to drop those into Client Space also?

[@18:35](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1115.77) - Chad Gregory (LaunchPad Lab)
Yes. I believe that was the plan. Nikki, correct me if you think I'm wrong there. I believe that was the plan.

[@18:45](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1125.93) - Nikki Dow
Yeah, I think the links all get attached when tasks are created.

[@18:51](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1131.05) - Dimple.Desai
So then in that case, would, Anna, let me know if this is okay. I would recommend for the analyst notes to stay in Client Space and then put them in here.

[@19:00](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1140.0) - Anna.Fiske
If we need them. I wouldn't even put them in here. So maybe just scrap the whole notes section again.

[@19:07](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1147.98) - Chad Gregory (LaunchPad Lab)
Do you guys need notes?

[@19:13](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1153.05) - Dimple.Desai
I don't think I do. Anna, do you?

[@19:20](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1160.92) - Anna.Fiske
I don't know. I don't know. I'd like, I think so. I think I would like notes here just in case.
But the only note that I can see me putting in here is rebanded four times. Like we have touched this client a million times and we've rebanded it or have an issue or the client is shopping and we need to not do the renewal.

[@19:39](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1179.16) - Chad Gregory (LaunchPad Lab)
Or abandon the batch.

[@19:40](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1180.76) - Anna.Fiske
So that would be notes really for me, Jagger, and Dimple between each other. But now that you're saying you're reminding me that not everybody's going to be in here pulling their links because Taylor's going to drop in client space, then yeah.
It would really just be us three, me, Dimple, and Jagger. We could probably just get I would want Spencer to be in here as backup.
would want Natalia to be in here as backup. then, like, Lawanda and Sue should have access. I can get you a list.
Let me make that for myself.

[@20:12](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1212.7) - Chad Gregory (LaunchPad Lab)
Write that down. This actually does bring up a question that I don't think I've thought of. But once we generate all these files, we put them in client space.
I know specifically, like, the Prism import files are going to be reviewed and potentially updated. How do we get that back?
Or I guess we don't need to get back the latest, like, whatever they change. Like, they should be changing things in Prism or the workbook or something to get that so that we can regenerate it correctly, right?
Instead of them updating. And maybe they will... Maybe they will update the Prism import file just to make it quicker for them to get it up in Prism or something, but we want them to go through the other paths so that we get the right information is coming in.
Am I making any sense? Like what I'm wondering? Kind files are accurate here and are what the team is actually using.
Yeah, like where are they going to be pulling the files from then? They'll pull them from Client Space, but then if they make changes to it, to those files, I'm trying to say like, do we need to get those back here?

[@21:47](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1307.5) - Dimple.Desai
Yeah, and also like what if there's an open market quote for somebody to upload? Would it be me, Anna, or Jagger that would be uploading it?
Or would it be somebody on the analyst side? And like where would they be uploading it here? Here or in client space?
We moved it or we had it here.

[@22:04](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1324.46) - Chad Gregory (LaunchPad Lab)
Actually, I think that was in the SOW was that it would be here. But I think that could still be fine.
Either they have like a single person, like a Betty or somebody that we give an account to to do that, or they send it to you guys to drop it in.

[@22:30](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1350.62) - Dimple.Desai
Okay. Yeah, that makes sense. Sorry to go on a tangent. Yeah, I don't really know.

[@22:39](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1359.24) - Anna.Fiske
I guess it would just depend on what they're changing on the imports to go back to the PRISM imports.
Because we're going to have to, I get what you're saying, like it's easier for them to change it just to get the import in, get the client going, moving through open enrollment.
But they would need to like go back to the renewal rep and say, hey, had to change this, change it on the workbook.

[@22:58](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1378.28) - Chad Gregory (LaunchPad Lab)
Yeah. re-upload it to make sure.

[@23:00](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1380.0) - Anna.Fiske
Because Taylor's going to audit Prism and it's going to be wrong. It's going to not match because Taylor's sitting with the old import.
So we'll just have to put training in place, I think, for that to say, like, I get it, change it in the moment because the client's screaming and they want their portal open.

[@23:14](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1394.82) - Chad Gregory (LaunchPad Lab)
I get that.

[@23:15](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1395.38) - Anna.Fiske
But we do have to make sure the materials are right moving forward. And it could be a bug with Taylor, too.

[@23:21](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1401.6) - Chad Gregory (LaunchPad Lab)
Like, it probably could be a case-by-case basis. Right.

[@23:26](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1406.19) - Anna.Fiske
Yeah, they definitely need to report it when they're changing it to, like, me, Dimple, and Jagger. And we're like, okay, that's a user error.
The workbook wasn't filled out. Or this was, you know, it was kind of identified that way.

[@23:35](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1415.95) - Chad Gregory (LaunchPad Lab)
Yeah.

[@23:37](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1417.13) - Anna.Fiske
And then for the open market, quote, upload.

[@23:40](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1420.91) - Chad Gregory (LaunchPad Lab)
Dimple, I would like for that to be Betty at some point.

[@23:43](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1423.47) - Anna.Fiske
But I do think we're going to have to kind of gatekeep that a little bit just because they're going to be so slammed with work during open enrollment because it's also our new sales.
They call it champ season. So we're onboarding a ton of new clients. Oh, wow.

[@23:58](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1438.23) - Chad Gregory (LaunchPad Lab)
So we'll probably...

[@24:00](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1440.0) - Anna.Fiske
probably be the ones doing that for a while, but once they get comfortable with it, they should be able to upload the template.

[@24:05](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1445.62) - Dimple.Desai
Yeah, I don't want Betty to yell at us.

[@24:07](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1447.42) - Chad Gregory (LaunchPad Lab)
I always learn about these different industries and when everybody's super busy.

[@24:13](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1453.62) - Anna.Fiske
Ours, unfortunately, around the holidays. They're like, as soon as Halloween hits, say goodbye to your family.

[@24:18](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1458.32) - Chad Gregory (LaunchPad Lab)
That's the same as I had a client that does actuarial reports for municipalities, and they're busy from October until February.
Yeah, that's us.

[@24:31](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1471.64) - Anna.Fiske
Yep.

[@24:32](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1472.66) - Chad Gregory (LaunchPad Lab)
Yep.

[@24:33](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1473.32) - Anna.Fiske
We actually have like blackout days, like people can't take PTO, and it starts in September and ends in February.
So I'm like, yeah, that's tough.

[@24:40](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1480.36) - Chad Gregory (LaunchPad Lab)
My sister-in-law got married the week after Christmas last year, and I had my time off request rejected. Yeah. Here's just an example of when you want to save the changes, if you made changes here, like you went from Here's thing.
I'll How 1.126 to 1 or something. I mean, that's probably a massive change, but being able to save it.
This might be a silly question.

[@25:11](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1511.48) - Dimple.Desai
At what point is the workbook being generated? Is that after the consultation?

[@25:21](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1521.82) - Chad Gregory (LaunchPad Lab)
It would be right when the workbook would be generated, right when the... I'm sorry, sorry, the workbook is before the consultation.

[@25:36](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1536.25) - Dimple.Desai
I'm just trying to figure out, like, if a client decides to go with, like, an open market quote, or if the client changes their offerings and stuff like that after the consultation, and then the workbook is executed, but then they change their mind after that.

[@25:56](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1556.32) - Chad Gregory (LaunchPad Lab)
Is that kind of, like, what we were just talking about? Um, yes, so if they got the workbook, they executed the workbook, we generated all of these files for them, and then they were like, oh, I need to make a different, I need to make a change, like, this is not what I wanted to do, before they signed, obviously, uh, and they want to go for an open market quote.
There's nothing here stopping them from doing that. Uh, I guess you guys would flip back the status and client space, or not you guys, but whoever's working with them, they would, you would go get the open market quote, get that into a template, upload it here, and then we can regenerate the files.
So it would regenerate everything, I think. I mean, maybe if we have a new open market quote, we could not generate everything, but I don't know if it matters.
We would generate the workbook would, at that point, be regenerated with the open market. Quote in there as well.

[@27:01](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1621.72) - Dimple.Desai
You could go back through consultation.

[@27:03](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1623.82) - Chad Gregory (LaunchPad Lab)
You could re-execute the workbook. We would get a new executed workbook, and then that would trigger all of these others to get regenerated again then.

[@27:15](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1635.22) - Dimple.Desai
Okay, okay. that make sense?

[@27:16](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1636.88) - Chad Gregory (LaunchPad Lab)
Yeah, that makes sense.

[@27:18](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1638.12) - Dimple.Desai
Okay. Is it possible for the batch statuses to be automatically adjusted at certain points? Like, I know, like, we discussed when the DocuSign is voided, like, the batch status changes to that and stuff like that.
But what about, like, after a client is out of consultation, the DocuSign has been sent. Will the batch status automatically switch over to DocuSign sent?
Yeah.

[@27:51](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1671.63) - Chad Gregory (LaunchPad Lab)
I think moving backwards, we typically won't be able to pick that up. Automatically, but I think the goal is when something is done, we move it to the next stage as appropriate, basically, not needing somebody to manually flip that.
So I know you've got a lot of that already set up in client space. Yeah. We generally would just be reading those things, but we would obviously be filling out the fields in client space to move things along as well.
Okay, gotcha.

[@28:36](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1716.25) - Dimple.Desai
Yeah.

[@28:38](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1718.96) - Chad Gregory (LaunchPad Lab)
What else do you need to see on this page?

[@28:48](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1728.98) - Anna.Fiske
I don't think anything.

[@28:59](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1739.6) - Chad Gregory (LaunchPad Lab)
Okay.

[@29:00](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1740.18) - Anna.Fiske
Because it's pretty surface level because, I mean, the report tab and all that good stuff is where I'll be living mostly.
Yeah, this looks fine to me, I think.

[@29:12](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1752.99) - Chad Gregory (LaunchPad Lab)
And then, yeah, obviously you can jump into the workbook to grab details to or the executed workbook if you wanted to look at specific things.
Nico, does what we've talked about make sense down here? Like, I think what we can do is push this over so that it's like this wide or something, and we can have the class Kashi Benefit Guide in like one half of this, and then put the other links over here.
So it's like all the links are in the box at the bottom, and then that gives us room here for like a little notes field.
Does that make sense, Nico? Okay. Yes. And I'm not the designer, so if you think of something that's nicer, let me know.
Just to, so there is a like, add user step to grant access to people. You would just enter the email, pick the role that you wanted to pick, and then hit grant access.
And then when they go to the login screen, and log in with Entra, Entra would know that they have been granted access, and can come in.
The reports, we talked about last time, trying to make these generally just like downloads. So I think we're going to need to get into these a little bit more, specifically in a later conversation.
But from a design vantage point, it'll basically just be a list of things that you can click on to open up.
We need to talk about the exceptions page eventually as well. I think this will, again, just kind of be a list that will show what the exception is, which client it affected, and potentially link to that client so you can look at things.
You're also going to still get errors in Azure, but we think that everything probably should still show up here, too.
And one thing that I feel like I don't have a full grasp on, which I don't need this for writing up some tickets, really, and we'll get to this towards the end of the project.
Bye. Bye. I don't know that much about, like, the post-enrollment stuff and audits and everything. I feel like we just need to do a deep dive on that at some point in the next couple weeks.
Do you have any first thoughts on, like, what was in your head for the exceptions here?

[@32:25](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1945.18) - Anna.Fiske
You know, I was going to ask you that because I don't remember what I said about exceptions.

[@32:30](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1950.2) - Chad Gregory (LaunchPad Lab)
That's all right. This is why Dimple needs to take better notes. I'm sure we have these notes, but we've just had so many conversations.
I know.

[@32:40](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1960.04) - Anna.Fiske
I'm trying to think, like, we have an exception tracker that I could share with you guys, but the exception tracker is going to be the rebanding file and or subsidies.
And let me pull that now, because I think that's what I was referring to, because we put notes in there of, like, why we said no or why they request.
And they request it every year, and we say no every year, and it's no heartburn, you know?

[@33:04](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1984.64) - Chad Gregory (LaunchPad Lab)
Yeah. Let me try to find that.

[@33:06](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1986.12) - Anna.Fiske
And so I think that's what I was thinking about.

[@33:08](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=1988.26) - Chad Gregory (LaunchPad Lab)
Okay. Yeah, I may just not really know what those steps mean, really, but that would be good. And we can just have a different conversation about that then.
I showed this uploading screen for the rebranding.

[@33:29](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2009.14) - Nikki Dow
Sorry, can we go back to the exceptions for a second? Yeah. I guess in my mind, I was interpreting this as basically failed, like failed generations of some document or failed parsing of the workbook.
So I know we already, like, showed the dashboard where, you know, there's that little icon that tells you, like, a client is stuck.
it's not. Okay. Because of some, like, either bad data or a technical issue. So I guess what I'm wondering is, like, is that icon, if it, like, was populated with, like, the reason why it's showing, is that enough to just know the current issue?
Or are we trying to have, like, a historical log in the exceptions so that we know, like, last week, NextSoul had this issue.
It's been resolved.

[@34:34](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2074.5) - Anna.Fiske
I would 100% prefer that over the report that I was going to send you. Because now that I'm looking at the exceptions report, this has to be managed outside of Taylor.
Like, this would be, like, C-suite people sending approvals to each other. It goes into, like, the Questco budget and profit and stakeholder.
Like, it goes into a whole detail. That would not want to be in Taylor.

[@34:56](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2096.34) - Chad Gregory (LaunchPad Lab)
Okay. I would love Nikki's idea.

[@34:58](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2098.72) - Anna.Fiske
Yeah. Especially, like... I'm thinking when I come in every morning during open enrollment, that's the first thing I'm going to check is like, what's failing on the clients?
What needs to be addressed first? And like you said, historical would be great where it's like, okay, we're constantly failing on this client.
That's when I know I need to call you guys and we need to have like a consultation to see what's going on to address this.
I would love that instead. Okay.

[@35:22](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2122.74) - Chad Gregory (LaunchPad Lab)
So maybe it's a table with like, like date and time of when the exception occurred or error. Maybe it makes, maybe it's better to just call it an error, uh, error log or something.
Yeah. Yeah.

[@35:39](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2139.79) - Anna.Fiske
Failure error or something like that.

[@35:41](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2141.37) - Chad Gregory (LaunchPad Lab)
Yeah. Um, and then the client name and like the message of what went wrong. Uh, and maybe it links to, again, the client name links to the page so that you can then like.
Like the workbook or whichever thing.

[@36:04](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2164.68) - Anna.Fiske
And speaking of errors also, was going to ask this, with the open market quote template, if it's not filled out correctly and it tries to be uploaded, is Taylor going to be able to tell us like, hey, you're missing this?
Like, is it going to be able to tell us what's wrong with it?

[@36:18](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2178.76) - Chad Gregory (LaunchPad Lab)
I think we can definitely throw an error like right at the time for this or the rebranding file that says like could not be, you know, processed or something.
Getting granular to Y might be a little bit more work. But Nikki, I'm not sure. Like, in terms of just like something's missing.

[@36:49](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2209.38) - Nikki Dow
Yeah, I think there's definitely like a certain level we can get to. Like, obviously, the first thing we're going to do is like check all the required fields.
And if you left something empty. You can say, we can't accept this because you forgot X, Y, Z.

[@37:05](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2225.33) - Chad Gregory (LaunchPad Lab)
Yeah. Yeah, that'd be ideal. Is that enough there? Yeah, absolutely. I can't really even think of like, I don't know, like if you tried uploading it and your internet craps out, then I don't know, maybe we would still be able to show a validation message, but we wouldn't have like, I don't know.
I'm just trying to think of other reasons why it might not, why it might fail, but. Would there be like any formatting issues?

[@37:34](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2254.56) - Dimple.Desai
Like if somebody puts in a certain type of character into a column that doesn't need to be there?

[@37:41](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2261.29) - Chad Gregory (LaunchPad Lab)
That could be something. Yeah. That does get a little, like we were saying, a little bit more tricky than just like if it's filled out, but.

[@37:52](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2272.29) - Dimple.Desai
If that's not possible, I was wondering, is it, Anna, would you be okay with if potentially if there was like a.
Saved open market quote, like, sample header file that's just, like, here for people to reference that tells them, like, this is what needs to go into every single column and this is the format.

[@38:11](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2291.74) - Chad Gregory (LaunchPad Lab)
I think that's a great idea regardless. Yeah, same.

[@38:16](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2296.76) - Anna.Fiske
Yeah, I think that's a great idea, Dimple. And I see what Dimple's saying. Like, if someone was to type the number nine out instead of putting the number nine in there, like, would it be able to say, like, eh, can't take that?
Even if it was just to call out the cell, that's incorrect. If it's not in normal language, we'd be okay with that.

[@38:38](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2318.0) - Chad Gregory (LaunchPad Lab)
Okay. Let's, let us think a little bit more about that as we get into this and blend on, like, the fidelity of those, uh, of those error messages.
Nico and Nikki, what other questions do you guys have on the admin console as we start, um, getting here?
And then I think maybe... Next week, maybe we can get, like, thumbs up approval on all of this, but I did want to call out, maybe you guys can give a thumbs up approval on this screen, because I think Jose is probably going to jump on it next week, even if we don't get a chance to touch base again on it.

[@39:22](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2362.29) - Anna.Fiske
Okay. Looks good to me.

[@39:25](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2365.92) - Dimple.Desai
Yeah, looks good to you. Okay.

[@39:28](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2368.42) - Chad Gregory (LaunchPad Lab)
Perfect.

[@39:28](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2368.8) - Anna.Fiske
I don't know how to, oh, there it is, the React. Camera's off, but I have my thumbs up.

[@39:33](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2373.0) - Dimple.Desai
Awesome.

[@39:34](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2374.62) - Chad Gregory (LaunchPad Lab)
Um.

[@39:36](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2376.04) - Dimple.Desai
Um, Anna, is this subsidy process that's going to be outside of Taylor, correct, you said?

[@39:40](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2380.76) - Anna.Fiske
It is, because it has to go to our, um, to Angelica to do the calculations to see, like, yeah, it goes completely outside of benefits, open enrollment, Taylor, so.

[@39:49](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2389.78) - Dimple.Desai
Okay.

[@39:50](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2390.5) - Anna.Fiske
And then it's not, it doesn't have anything to do with benefits, then we submit it to payroll to do whatever the subsidy is, admin fee relief, workers' comp relief.

[@40:00](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2400.0) - Dimple.Desai
Leave something. And is that all like after, like is that all like post-enrollment stuff or will that affect any kinds of like files or anything that we're building?

[@40:10](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2410.68) - Anna.Fiske
It shouldn't affect any of the files because again it's outside of the process so it'd be set up as a subsidy and it can only be set up by specific people because it has to be approved.
And then what was the first part of your question? I don't even remember.

[@40:28](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2428.38) - Dimple.Desai
Me either.

[@40:29](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2429.08) - Anna.Fiske
Okay we'll just keep moving.

[@40:29](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2429.98) - Chad Gregory (LaunchPad Lab)
Well I think it would be good to have like maybe think about that a little bit more like I think we can keep going with the admin console approach of like this error log but there is all this stuff in in our scope and I'm not sure what should actually be in the admin console based on what we just just mentioned like.
If these don't need to happen within Taylor, truly, it's possible that this is cutting some scope and might be the good trade-off, quote-unquote, for some of the benefit guide stuff.

[@41:24](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2484.34) - Anna.Fiske
We will need Jagger to look at this one because he does a lot of the pre-enrollment auditing, and Baby Taylor does post-enrollment audits now.
So we will need him to go over this because I always forget what's certain, like, orphan audits. Yeah. It's like people being enrolled in terminated plans and they never got moved over because they didn't do the enrollment.
So yeah, post-enrollment audit we would need.

[@41:54](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2514.03) - Chad Gregory (LaunchPad Lab)
Or does that truly mean, like, after they've already... Already signed their CBE and everything.

[@42:03](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2523.15) - Anna.Fiske
Yes, it's post-enrollment. So it's after the employees enroll, after we post them, send it to the carrier, everything. Like the very last thing, they're waiting on their cards in the mail during Christmas.

[@42:11](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2531.91) - Chad Gregory (LaunchPad Lab)
And we're doing this post-enrollment all during December. And people get signed up into plans that are not active anymore still?

[@42:23](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2543.95) - Anna.Fiske
They wouldn't be enrolling in it, but it'd be, I've been in this plan for six years. I'm not doing enrollment.
I don't log into the portal. And then not knowing that my client or my employer has terminated it. So I never got moved over.
Yeah. So then we, we ended up doing like auto-mapping where we're like, Hey, you didn't do your enrollment. We auto-mapped you here.
Here's what's different. Premium plan-wise, we kind of just do that. So people don't go without coverage.

[@42:48](https://fathom.video/share/cpjWpTcNJAwZmQoXU6RUfkzz8R2QsFmY?timestamp=2568.45) - Chad Gregory (LaunchPad Lab)
Yeah, that makes sense. I never knew what happened if somebody didn't go through and do enrollment. Okay. Yeah. Let's talk to Jagger more about this stuff.
If it makes sense for some of this to be in the admin console, great. Maybe it does fit on that error logging page still.
They're just kind of a different error. They're not like, you know, a job failed. They're like, this needs addressed though.
So, okay. I know we're at time. So I appreciate everybody's time this morning. And we're making good progress, I think.
I agree. Cool. Thanks, everybody. We'll talk to you tomorrow. Thank you, guys. Have a great day. everyone.
