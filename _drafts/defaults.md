---
layout:   essai
title:    "Defaults"
---

It's a bit of a mystery how we came to use the word *default* to mean <span
class="sc">the standard fall-back option in the absence of an explicitly
declared choice</span>. But one can certainly *guess*; its Latin roots, *de*
'away' + *fallo* 'deceive, cheat, escape notice of', point their spindly
fingers at a slippery swindler. With its older senses, we speak of failure, of
negligence, in meeting any of a variety of obligations: failing to make
payments, we default on a loan; failing to show up, we default a game, or a
court summons.

When we think of defaults today--factory defaults, default search engines,
default home-pages, we think first and foremost of their pre-set nature. Yet,
buried underneath all those dusty menus full of configurable and untouched
options lies our true Default, that abdication of our responsibility as human
operators to specify an instruction for the machine.

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

Such a failure can sometimes be a good thing for wider society—for the organ
donor's registry, for example, even if controversial. But it is especially A
Very Good Thing for the lumbering tech giant attempting to break into a new
market. In the case of the First Browser War, the death knell sounded for
Netscape when Microsoft bundled Internet Explorer into Windows, effectively
making IE the default, and hence the browser of (lazy consumer) choice. Why
bother developing a better product [when you can just tack it on to your
already-popular platform]({% link /assets/images/flex_tape.gif %}), and make
all your pre-existing users adopt it?

<div class="section-break">&</div>

Referral sources[^ref] were something of an evergreen subject while I was a
data scientist at Chartbeat[^cb]. Facing down the adpocalypse[^news], 
publishers were obsessed with the latest referral trends, restless in their
search for the next big source of eyeballs. Part of my job was to
wrangle an unruly spaghetti of referral <span class="sc">url</span>s into
comprehensible information about how much traffic each website or app was
sending to publishers. 

Unsurprisingly there, the top 2 spots in the referral rankings invariably went
to the duopoly: Google and Facebook.[^cilantro][^apple] But of greater ongoing
interest to publishers were the referrers a little further down the list:
referral channels on the up and up where publishers wanted to get a jump on
early in promoting their content. <!-- TK: pls rewrite this awful sentence -->

One such referrer was [Google Chrome's _Articles for You_ feed on their new tab
page](https://blog.chartbeat.com/2018/04/11/google-chrome-suggestions-in-more-detail-than-you-could-want/)
[^gcs]. The amount of monthly traffic it was referring had grown 21x over just
the course of a year, and had even surpassed even that of Twitter (then the
third largest referrer after <span class="sc">fb</span> and <span
class="sc">goog</span>).

<div style="margin-top: 2em; margin-bottom: 2em; width: 100%; height: 40ch;" class="vega" id="viz"></div>
{% cite ona18 %}

<div class="section-break">&</div>

Here's where the trap lies: in failing to specify an instruction for the
machine—a tool we are supposed to be using for our ends—we do not simply fall
prey to the control of the machine. In fact, such a statement is an absurdity;
the machine didn't build itself, people in search of profits built the machine.
What we in fact falling prey to, without realising, are the machinations of the
wizards behind the curtains: the tech executives and the product managers
dictating the default states of the apps and feeds that have come to occupy
every waking moment of our lives.

[^apple-iie-design]: {% cite apple-iie-design %}

[^cb]: "Chartbeat is the leading provider of real-time analytics to major
    online publishers around the world, such as the New York Times and the
    BBC," et al., etc. More at [chartbeat.com](chartbeat.com).

[^news]: **Adpocalypse** (_n._): the end of the ad-funded news business as we
    know it due to the recent ascendency of the Facebook/Google ads duopoly.
    A time of revelations about which outlets saw their readers as pairs of
    eyeballs for their content farms, and which were actually producing
    journalism people cared about.

    (Too?) much more about the news business in
    [this other post]({% link _drafts/news.md %}).

[^ref]: When we access the news online, we can land on a news website by (a)
    typing in the url to a publisher's homepage, (b) searching for news about X
    and clicking links to news articles, (c) tapping on a news article that
    pops up on a social feed, (d) following a link from somewhere else on the
    internet, etc. etc. That place we first started from is called the
    _referral source_.

[^cilantro]: Such was the mania amongst publishers that a rival analytics
    company (let's call them _Cilantro_) began to make a regular hullabaloo in
    their newsletter every time Facebook and Google inevitably switched places
    again in the referral rankings that latest month.

[^apple]: "But what about Apple News?" I hear you ask. Welp, as with all things
    Apple, I could tell you, but the itinerant ghost of Steve Jobs will send
    someone along to kill you.

[^gcs]: This one kept popping up on people's dashboards as `googleapis.com`.
    Needless to say, that left many people scratching their heads--Google has
    so many <span class="sc">api</span>s, so which one is it? As it turns out,
    the full <span class="sc">url</span> for the referrer was
    `http://www.googleapis.com/auth/chrome-content-suggestions`, and some light
    google-ing of the <span class="sc">url</span> revealed forums full of
    disgruntled Chrome users asking how they might turn the damned thing off.
    (This was back in the days of when I was trying to figure out what it was;
    nowadays the search results are just full of articles claiming they've
    unlocked the secret to optimizing your website for getting on that feed.)

<!-- [^postman]: Postman, N. (2006). *Amusing ourselves to death:
    Public discourse in the age of show business*. Penguin. -->

<!-- [^truth-is-paywalled-but-lies-are-free] {% cite truth-is-paywalled-but-lies-are-free %} -->


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