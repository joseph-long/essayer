---
layout:   essai
title:    "Default feeds"
---

You know that feeling you get about a familiar word after saying it a couple of
times in rapid succession? As if it were a complete stranger you were now just
meeting for the first time? The word _default_ became such a familiar stranger
to me, as I was looking into referral sources to news websites[^ref]. Referral
traffic had been something of an evergreen subject while I was a data scientist
at Chartbeat[^cb]. Facing down the adpocalypse[^news], publishers were obsessed
with the latest referral trends, restless in their search for the next big
source of eyeballs. Part of my job was to wrangle a rubbery spaghetti of
referral URLs into comprehensible information about how much traffic each
website or app was sending to publishers.

Unsurprisingly, the top 2 spots in the referral rankings invariably went to the
duopoly, Google and Facebook, driving an order of magnitude more traffic than
any of the other individual referral sources.[^cilantro][^apple] But of ongoing
(and sometimes disproportionate) interest to publishers were also the referrers
a little further down the list. If there was an up and coming referral source,
they'd want to be the first to get a jump on.

One such referrer was [Google Chrome's _Articles for You_ (or Google Chrome
Suggestions, GCS, as Chartbeat dubbed it) on the browser's new tab
page](https://www.niemanlab.org/2018/03/this-is-the-next-major-traffic-driver-for-publishers-chromes-mobile-article-recommendations-up-2100-percent-in-one-year/)
[^afy]. The amount of monthly traffic it was referring had grown 21x over the
course of just a year, and had even surpassed even that of Twitter, then the
third largest (external) referrer after FB and GOOG. (You can see GCS just
barely peeking over the TWTR horizon in '18 in the chart below.)

<figure>
    <div style="width: 100%; height: 40ch;" id="viz"></div>
    <figcaption>Data: {% cite ona18 %}</figcaption>
</figure>

Although Chrome's *Articles for You* had, at the time, been limited to just
Android devices, the realization that this fast-growing feed was being shunted
by in front of people on the most popular browser in the world, by _default_,
got me thinking back to Microsoft's infamous Netscape murder. Back in the days
of the First Browser War, the death knell had sounded for Netscape (then the
most popular browswer) when Microsoft started bundling Internet Explorer into
Windows. That made IE the default, and hence the browser of (lazy consumer)
choice. All told, a stellar strategy for the lumbering tech giant attempting to
break into a new market; why bother developing a better product [when you can
just tack it on to your already-popular platform]({% link
/assets/images/flex_tape.gif %}), and make all your pre-existing users adopt
it?

A little ways down the referrers list, too, were other signs of default: [upday
news for
Samsung](https://play.google.com/store/apps/details?id=de.axelspringer.yana) (a
news app from the German Axel Springer publishing group) came pre-installed on
Samsung phones; Pocket, an app that allows you to save links you want to read
later, [started to surface link recommendations on each new tab Firefox users
opened](https://blog.getpocket.com/2017/11/introducing-pocket-recommendations-in-firefox-quantum/)—much
like *Articles for You*. But these referrers never broke the top 10—Samsung and
Firefox never had the manner of market monopoly Google did, and does.

It was also around this same time that Google launched their [feed for the
Google app (as well as the "left of home" feed on
Android)](https://www.blog.google/products/search/feed-your-need-know/), later
to be rebranded [Google
Discover](https://blog.google/products/search/introducing-google-discover/),
and expanded to google.com itself. Was it a product strategy, to consolidate
the recommendation experience across Google product surfaces? Was it an
advertising ploy, to nudge more eyeballs onto pages they were serving ads on?
Or perhaps an internet monopoly play, to ~~coerce~~ incentivise websites to use
Google AMP to be more likely to make it onto the feed and further entrench
their hold on the web? (Well, most likely, it just was a convenient confluence
of all of the above.)

Frustratingly, for people looking at the analytics coming out the other side,
there was no way to tell whether that traffic was coming from people actively
looking for information on Google Search, or if it was just coming from those
mindlessly scrolling the feed while stuck in line. Which just makes that
simultaneous increase in Google Search referred traffic that much more
mysterious—to what degree was it people actively seeking out news more, or did
that rise come mostly from people tapping through on that feed?

This question of attribution bugs publishers (judging by the number of times
Chartbeat was asked about that) because they don't know how to direct their
efforts in garnering more traffic. But it haunts me, because it is unclear to
what extent we have become mired in passively consuming from solely the feeds
that Google deigns to serve up in front of us. Searching for information and
news takes initiative, and an increase in search traffic could be pointing at
people more actively engaged with the world. But with the search/feed line thus
undefined, that supposed increase in "Google Search" traffic may just as well
have been people falling back *en masse* to being passive consumers.

Now, I hear you protesting: Su, what do you have against feeds? Feeds are
great! I want to be an empowered and informed member of society. News is by
definition that which I don't know about but should be apprised of, and feeds,
like how Google has so cleverly put it, feed my need to know with the lowest
level of requisite effort on my part. If I had to go out there and search out
the information I need to know all the time, I wouldn't have the time for
doing anything else—pragmatism, not idealism.

Think back for a moment to the last time you (doom)scrolled through a (news)
feed[^feed]; Facebook, Twitter, whichever, doesn't matter. Of the articles you
came across, how many did you simply scan the headlines of? How many did you
actually click through to read? Of those you read, how many would you say had a
direct impact on your life, that you've done something differently on account
of having read it? Or, was it just another piece of trivia you brought up as a
bit of idle chit-chat as you ran into other people that day?

What news, as we commonly encounter it today, does one actually _need_ to know?
For Neil Postman, the answer to this question is, not very much. Not because
we'd survive living under a rock, but because the news—that decontextualised,
objectivised view from nowhere, delivered on drip through the mass media—does
not contain information that most of us can realistically act on. In his 1985
(!) book _Amusing Ourselves to Death_[^amusing-ourselves-to-death], written in
the golden age of MTV, Postman coined the term _information-action ratio_ as a
précis for the phenomenon. Others have compared news consumption to an
[information diet](https://w.wiki/iAZ), which, like the stuff that we eat, has
increasingly come to be made up of junk: high in calories, low in actual
nutrition. Sadly, this is also a metaphor I've heard being employed
unironically: audience development people at publishers would make reference to
"snackable content", content that that the busy professional would be able to
presumably slurp up on the go like a little packet of informational
[soylent](w.wiki/iAg). Not that this is a view uniformly shared by all
publishers—[speaking to Time
magazine](https://time.com/5696968/a-g-sulzberger-new-york-times/), A.G.
Sulzberger, publisher of the NYT, insisted, "I actually hate the word content.
It’s a word for junk … the junk you shovel into Facebook. What we do is
journalism." But even with journalism—how many times have we delved into
stellar, hard-hitting investigative reporting, only to emerge feeling
concerned, but powerless?

How did we get this way, drowning in information and yet still so lost at sea?
Postman drew on Marshall McLuhan's theory that "the medium is the message" to
make his point about TV being a medium that inherently short-circuited any
attempt at measured discourse, tugging on the false visual intimacy created
between rapt viewer and the dazzling TV personality to convey its visceral
messages. But it is certainly not the case today that all feeds simply beam
autoplay videos into our eyeballs (even if there is an annoying tendency to
lean that way[^fb-vid]). Content™ comes at us in slideshows, videos, and
listicles alike. The medium being the message, in any case, doesn't explain
_why_ there's so much chum in those Outbrain buckets.

To do that, we need to, as fictional Deep Throat said, follow the money. For
decades, mass media companies had enjoyed the undivided attention of the
popular mind. The larger the circulation of a paper, the more a print
publication was able to charge advertisers for a spot between its sheets.
Circulation was king. The lifestyle section and the Sunday paper were just two
of the "innovations" that publications came up with in their drive to reach
ever widening audiences and demographics—to women, especially, who were known
as the ones to actually go out and spend money on the wares the advertisers
were hawking.

All this, obviously, changed with the internet. At first, the internet was just
this dinky little thing that everyone would just put their articles up on for
free, a [technological curiosity obsessed over by the IT nerds lurking in the
basement](https://www.niemanlab.org/2017/03/word-up-this-is-the-story-behind-the-new-york-times-most-famous-tweet-which-is-10-years-old-today/).
It seemed one day we were inking our fingers and smudging our cheeks with
powdery grey transfers from newsprint, and the very next, our eyes were glued
to our black mirrors, glassy-eyed captives in the walled gardens of the Books
of Faces, where the Content so hated by AG frolicked amidst the lush, green
shrubbery of the ad dollars that were now flitting into the pockets of the
social media giants instead.

But insofar as journalists have dutifully written up (rightly) critical
thinkpieces on the impacts that tech is having on our attention spans and our
mental health[^smartphones-destroyed-generation], as much as they have (also
rightly) bemoaned the ill-gotten gains of the tech behemoths, [engorged on the
appropriated labour of those engaged in the real work of newsgathering and
reporting](https://www.reuters.com/article/us-australia-media-regulator-idUSKCN24V3UP),
what they conveniently fail to mention in the midst of all this hullabaloo
about the exploitation of our minds under the attention economy is that the
attention economy was booming _decades_ before Tristan Harris started
pontificating about Time Well Spent.

What the *New York Times* doesn't tell you, when it propagates its
[*Truth*](https://www.nytco.com/press/nytimes-releases-new-ads-from-the-truth-is-hard-campaign-directed-by-darren-aronofsky/);
what the op-eds don't say, when they opine that ["You Are the
Product"](https://theconversation.com/if-its-free-online-you-are-the-product-95182)
of the social networks, is that the mass media in crisis today was *itself*
established on selling you, the consumer, as a
product[^television-delivers-people] to the advertiser. Not only were you
already the product, the mass media's claims to "truth" and "objectivity" were
instituted not so much on the grounds of some noble sense of journalistic
integrity, but more so out of fear of upsetting the paying
advertiser[^media-future-past]. As soon as the newspaper started to derive most
of its revenue from the advertiser[^ad-rev] and not from you, the reader, it had
already been defanged as a speaker of the people's truth[^manufacturing-consent].

Could it be, ultimately, that those randos you hear about from time to time
who choose to switch off from the news altogether, trusting that the important
bits would sooner or later make themselves known to them, were the ones getting
the news that they actually needed to know all along?

<!-- - google feed anecdote
- "page one" -> newspaper/reddit/hn/et al. homepages, news feeds
    - human editorial judgement: flawed and biased, but... still human??
        (facebook news "editors"), cf again the other news rant
    - algorithmic judgement: "paperclip maximizer"
 -->    


<div class="section-break">&</div>

It's a bit of a mystery how we came to use the word *default* to mean <span
class="sc">the standard fall-back option in the absence of an explicitly
declared choice</span>. But one can certainly *guess*: its Latin roots, *de*
'away' + *fallo* 'deceive, cheat, escape notice of', point their spindly
fingers at a slippery skiver. With its older senses, we speak of failure, of
negligence, in meeting any of a variety of obligations: failing to make
payments, we default on a loan; failing to show up, we default a game, or a
court summons.

When we think of defaults today--factory defaults, default search engines,
default home-pages, we think first and foremost of their pre-set nature. Yet,
buried underneath all those dusty menus full of configurable and untouched
options lies our true Default, that abdication of our responsibility as human
operators to specify an instruction for the machine.

Such a failure can sometimes be a good thing for wider society—for the organ
donor's registry, for example, even if controversial. But it is especially A
Very Good Thing for the . In the case of the 

The unflattering denotation of the default was probably not lost on early
designers of computer systems. Bruce Tognazzini, writing design guidelines for
the Apple *IIe*[^apple-iie-design], for instance, opens the section on
'Defaults' (p. 37) thus:

> Please do not ever use the word default in a program designed for humans.
> Default is something the mortgage went into right before the evil banker
> stole the Widow Parson's house. There is an exhaustive list of substitutes
> (previous, automatic, standard, etc.) in the Appendix to How to Write a 
> Manual.
>
> Defaults should be declared, not assumed. Undeclared (not displayed) defaults
> such as pressing `RETURN` for Yes (or for No?) will cause confusion and
> anger.

Bruce is probably out there somewhere today, spinning with confusion and
anger.

<!-- TK -->

Here's where the trap lies: in failing to specify an instruction for the
machine—a tool we are supposed to be using for our ends—we do not simply fall
prey to the control of the machine. In fact, such a statement is an absurdity;
the machine didn't build itself, people in search of profits built the machine.
What we in fact falling prey to, without realising, are the machinations of the
wizards behind the curtains: the tech executives and the product managers
dictating the default states of the apps and feeds that have come to occupy
every waking moment of our lives.


[^ad-rev]: As one point of reference: in 1966, the NYT was
    [N° 404 on the Fortune 500](https://archive.fortune.com/magazines/fortune/fortune500_archive/snapshots/1966/1380.html),
    that had a "350-man department that [brought] in more than $100 million a
    year by selling ads," and moreover, "the revenue derived from advertising
    [was] three times what the paper earn[ed] from its circulation sale and its
    other business ventures combined." {% cite kingdom-and-power -L chapter -l
    4 %}

[^afy]: This one kept popping up on people's dashboards as `googleapis.com`.
    Needless to say, that left many people scratching their heads--Google has
    so many APIs, so which one is it? As it turns out, the full URL for the
    referrer was `http://www.googleapis.com/auth/chrome-content-suggestions`,
    and some light google-ing of the <span class="sc">url</span> revealed
    forums full of disgruntled Chrome users asking how they might turn the
    damned thing off. (This was back in the days of when I was trying to figure
    out what it was; nowadays the search results are just full of articles
    claiming they'd discovered That One Weird Trick for getting your website on
    that feed.)

[^amusing-ourselves-to-death]: {% cite amusing-ourselves-to-death %}

[^apple]: "But what about Apple News?" I hear you ask. Well, as with all things
    Apple, I could tell you, but the itinerant ghost of Steve Jobs would send
    someone along in short order to kill you.

[^apple-iie-design]: {% cite apple-iie-design %}

[^cb]: What is a "Chartbeat"? Think of a major online news source. Any one
    would do. Chances are, on that website that you just thought of, Chartbeat
    is tracking your every move, on every visit. "Chartbeat is the leading
    provider of real-time analytics to major online publishers around the
    world, such as the New York Times and the BBC," et al., etc. More at
    [chartbeat.com](chartbeat.com).


[^cilantro]: Such was the mania amongst publishers that a rival analytics
    firm (let's call them _Cilantro_) began to make a regular hullabaloo in
    their newsletter every time Facebook and Google inevitably switched places
    again in the referral rankings that latest month.

[^feed]: Just the word _feed_ itself—like the word _default_—gives me the
    heebie-jeebies. (Whoever said wordnesia was simply a curio?) It's a word
    that puts me in mind of plugging ourselves into the socket on the wall as
    if we were machines running on centrally-generated electricity; of hooking
    ourselves up to an IV drip as if institutionalised in perpetuity; of animal
    feed; of a pig, in a cage, on antibiotics.[^fitter-happier]

[^fb-vid]: TK

[^fitter-happier]: {% cite fitter-happier %}

[^manufacturing-consent]: {% cite manufacturing-consent %}

[^media-future-past]: {% cite media-future-past %}

[^news]: **Adpocalypse** (_n._): the end of the ad-funded news business as we
    know it due to the recent ascendency of the Facebook/Google ads duopoly. A
    time of revelations; revelations about which outlets saw their readers as
    pairs of eyeballs to be trawled for their content farms, and which were
    actually producing journalism people cared about.

    (Too?) much more about the news business in
    [this other post]({% link _drafts/news.md %}).

[^ref]: When we access the news online, we can land on a news website by (a)
    typing in the url to a publisher's homepage, aka **direct** traffic, (b)
    searching for news about X and clicking links to news articles, (c) tapping
    on a news article that pops up on a social feed, (d) following a link from
    somewhere else on the internet, etc. etc. That place we first started from
    is called the _referral source_.

[^smartphones-destroyed-generation]: {% cite smartphones-destroyed-generation %}

[^television-delivers-people]: {% cite television-delivers-people %}
    AFAIK, this short video is the first time that the phrase, "you are the
    product" gets applied to a form of media. Although the video refers
    explicitly to TV, the same analysis can certainly apply to any form of
    media that is (nearly) free to consume—including the newspaper.

[^truth-is-paywalled-but-lies-are-free]: {% cite truth-is-paywalled-but-lies-are-free %}

<script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@4"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>
<script type="text/javascript">
function darkCharts(state) {
    if ( state ) {
        var viz = document.getElementById("viz")
        while (viz.firstChild) { viz.firstChild.remove(); }
        vegaEmbed("#viz", "{% link /assets/vega/ona18-dark.json %}", {"renderer": "svg", "actions": false});
    } else {
        var viz = document.getElementById("viz")
        while (viz.firstChild) { viz.firstChild.remove(); }
        vegaEmbed("#viz", "{% link /assets/vega/ona18-light.json %}", {"renderer": "svg", "actions": false});
    }
}
localStorage.dark == "true" ? darkCharts(true) : darkCharts(false);
</script>


