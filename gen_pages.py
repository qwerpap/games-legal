#!/usr/bin/env python3
"""Generate the four legal pages for a game folder.

Rewritten 2026-08-23 because the pages that were live said things the apps
contradict: Terms claimed "no real-money purchases" for games that ship four
in-app purchases, Support claimed "no ads in the core experience" for games
that show AdMob banners and interstitials, and Privacy still named AppMetrica
after the publisher's analytics key was stripped out. A reviewer opens these
URLs from the App Store listing, so a page that disagrees with the listing is
a rejection waiting to happen.

    gen_pages.py                 # regenerate every game in GAMES
    gen_pages.py zenloop skywords
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
EMAIL = "netkaktakto@gmail.com"
OWNER = "Anastassiya Shugaley"
UPDATED = "August 23, 2026"
BASE = "https://qwerpap.github.io/games-legal"

# slug -> (display name, one-line genre, has real-money in-app purchases)
GAMES = {
    "zenloop": ("Zen Loop", "a calm loop-rotation puzzle", True),
    "frostbreak": ("Frost Break", "an arcade brick breaker", True),
    "wordvines": ("Word Vines", "a word-connect puzzle", True),
    "bloomsweep": ("Bloom Sweep", "a colour-flood puzzle", True),
    "tropiccatch": ("Tropic Catch", "a fruit-catching arcade game", True),
    "skywords": ("Sky Words", "a word-guessing game", False),
    "meowjump": ("Meow Jump", "a vertical jumping arcade game", False),
    "skydragon": ("Sky Dragon", "a one-touch flying arcade game", False),
    "petalmosaic": ("Petal Mosaic", "a pixel-art colouring game", False),
    "hooptap": ("Hoop Tap", "a basketball tap game", False),
    "starmatch": ("Star Match", "a match-3 puzzle", False),
    "cosmojump": ("Cosmo Jump", "a space platform jumper", False),
}

HEAD = """<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><style>
:root{{color-scheme:light dark}}
*{{box-sizing:border-box}}
body{{font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
margin:0;padding:0;background:#0f1116;color:#e7e9ee}}
.wrap{{max-width:720px;margin:0 auto;padding:40px 22px 80px}}
h1{{font-size:1.7rem;margin:0 0 .2em;letter-spacing:-.02em}}
h2{{font-size:1.15rem;margin:1.8em 0 .5em;color:#fff}}
.meta{{color:#9aa0ad;font-size:.9rem;margin-bottom:2em}}
a{{color:#8b9bff}}
p,li{{color:#cfd3dc}}
.card{{background:#171a22;border:1px solid #232734;border-radius:14px;padding:18px 20px;margin:1.2em 0}}
.nav{{margin-top:2.5em;padding-top:1.5em;border-top:1px solid #232734;font-size:.9rem;color:#9aa0ad}}
footer{{margin-top:3em;color:#6b7080;font-size:.82rem}}
</style></head>
<body><div class="wrap">
"""

FOOT = """<div class="nav"><a href="{base}/{slug}/privacy.html">Privacy</a> &middot;
<a href="{base}/{slug}/terms.html">Terms</a> &middot;
<a href="{base}/{slug}/support.html">Support</a></div>
<footer>&copy; 2026 {owner}. Contact: <a href="mailto:{email}">{email}</a></footer>
</div></body></html>
"""


def page(slug, title, body):
    return (HEAD.format(title=title) + body
            + FOOT.format(base=BASE, slug=slug, owner=OWNER, email=EMAIL))


def purchases_paragraph(name, has_iap):
    if has_iap:
        return (f"<p><strong>In-app purchases.</strong> {name} is free to download. It "
                "offers optional in-app purchases: coin packs, and a one-off "
                "&ldquo;Remove Ads&rdquo; product that turns off the banner and "
                "full-screen ads. Purchases are processed by Apple &mdash; we never "
                "see or store your payment details. Nothing in the game is gated "
                "behind a purchase; every level can be finished without spending "
                "money.</p>")
    return (f"<p><strong>No purchases.</strong> {name} is free and has no in-app "
            "purchases and no subscriptions. Coins are earned by playing and can "
            "only be spent inside the game.</p>")


def ads_paragraph(name):
    return (f"<p><strong>Advertising.</strong> {name} shows ads through "
            "<strong>Google AdMob</strong>: a banner, occasional full-screen ads "
            "between rounds, and optional rewarded videos you choose to watch for "
            "a bonus. Ad requests are sent as <em>non-personalised</em>, which asks "
            "AdMob not to use your data to profile you or target ads at you. AdMob "
            "may still process technical data &mdash; device type, coarse region and a "
            "resettable advertising identifier &mdash; to deliver and measure an ad and "
            "to prevent fraud. We show no App Tracking Transparency prompt because "
            "we do not track you across other companies&rsquo; apps or websites. "
            "Google&rsquo;s practices are described in the "
            "<a href=\"https://policies.google.com/technologies/partner-sites\">"
            "Google Privacy &amp; Terms</a>.</p>")


def privacy(slug, name, genre, has_iap):
    body = f"""<h1>{name}</h1>
<div class="meta">Privacy Policy &middot; Last updated {UPDATED}</div>

<div class="card"><strong>Short version:</strong> {name} has no accounts and no servers,
and we collect no personal data about you. The game does show ads through Google AdMob,
which processes some technical data in order to deliver them. Everything else stays on
your device.</div>

<h2>Information we collect</h2>
<p><strong>None.</strong> {name} does not ask for your name, email, phone number,
location or contacts, and there is no account to create or sign in to. We operate no
servers and receive no data from the game.</p>

<h2>On-device data</h2>
<p>Your progress, settings, statistics, coin balance and any purchases are stored
<em>locally on your device</em>. Deleting the app removes them.</p>

<h2>Third parties</h2>
{ads_paragraph(name)}
{purchases_paragraph(name, has_iap)}
<p>The game itself is fully playable offline; ads simply do not load without a
connection. We use no analytics SDK.</p>

<h2>Children&rsquo;s privacy</h2>
<p>{name} is rated 4+ and is suitable for all ages. We do not knowingly collect any
data from anyone, including children under 13.</p>

<h2>Your choices</h2>
<p>You can reset or limit the advertising identifier at any time in iOS
Settings &rarr; Privacy &amp; Security &rarr; Tracking and &rarr; Apple Advertising.</p>

<h2>Changes</h2>
<p>If this policy changes, the updated version is posted on this page with a new date.</p>

<h2>Contact</h2>
<p>Questions about privacy? Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

"""
    return page(slug, f"{name} — Privacy Policy", body)


def terms(slug, name, genre, has_iap):
    money = ("""<h2>Purchases</h2>
<p>The app is free to download. It offers optional in-app purchases &mdash; coin packs and
a one-off &ldquo;Remove Ads&rdquo; product. All purchases are sold and processed by Apple
under the App Store Terms of Service; refunds are handled by Apple, not by us. Coin
packs are consumable and are not restorable; &ldquo;Remove Ads&rdquo; is a non-consumable
product and can be restored with <em>Restore Purchases</em> in the shop.</p>"""
             if has_iap else
             """<h2>The app is free</h2>
<p>The app is free to play and contains no in-app purchases and no subscriptions.
Coins are earned by playing and have no monetary value; they cannot be bought, sold or
exchanged for money.</p>""")
    body = f"""<h1>{name}</h1>
<div class="meta">Terms of Use &middot; Last updated {UPDATED}</div>

<h2>Acceptance</h2>
<p>By downloading or using {name} (&ldquo;the app&rdquo;), you agree to these terms. If
you do not agree, please do not use the app.</p>

<h2>License</h2>
<p>You are granted a personal, non-transferable, non-exclusive license to use {name} for
your own entertainment on devices you own or control, in accordance with the Apple App
Store Terms of Service.</p>

{money}

<h2>Advertising</h2>
<p>The app is supported by advertising served through Google AdMob. Some ads are optional
and rewarded &mdash; you choose whether to watch them.</p>

<h2>Acceptable use</h2>
<p>You agree not to reverse engineer, modify or attempt to extract the source code of the
app, except as permitted by law.</p>

<h2>No warranty</h2>
<p>The app is provided &ldquo;as is&rdquo; without warranties of any kind. To the maximum
extent permitted by law, the developer is not liable for any damages arising from your use
of the app.</p>

<h2>Changes</h2>
<p>These terms may be updated from time to time; the current version is always available
on this page.</p>

<h2>Contact</h2>
<p>Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

"""
    return page(slug, f"{name} — Terms of Use", body)


def support(slug, name, genre, has_iap):
    coins = ("""<p><strong>How do coins and purchases work?</strong> You earn coins by
playing, and you can also buy coin packs or remove the ads. Purchases go through your
Apple ID; to restore &ldquo;Remove Ads&rdquo; on a new device, open the shop and tap
<em>Restore Purchases</em>. Coin packs are consumable and cannot be restored.</p>"""
             if has_iap else
             """<p><strong>How do coins work?</strong> You earn coins by playing. They can
only be spent inside the game and cannot be bought.</p>""")
    body = f"""<h1>{name}</h1>
<div class="meta">Support &middot; Last updated {UPDATED}</div>

<div class="card">Need help with {name}? Email
<a href="mailto:{EMAIL}">{EMAIL}</a> and we&rsquo;ll get back to you.</div>

<h2>About {name}</h2>
<p>{name} is {genre} for iPhone. It is free, plays fully offline, has no account and
collects no personal data. It is supported by ads.</p>

<h2>Common questions</h2>
<p><strong>I lost my progress / changed phones.</strong> Game data is stored on your
device, so reinstalling or switching devices starts a fresh game.</p>
{coins}
<p><strong>How do I get rid of the ads?</strong>
{"Open the shop and buy &ldquo;Remove Ads&rdquo;; it disables the banner and the full-screen ads permanently on that Apple ID." if has_iap else "The ads are how the game stays free, so there is no paid option to remove them."}</p>
<p><strong>Something isn&rsquo;t working.</strong> Make sure you are on the latest version
from the App Store, then email us with your device model and iOS version.</p>

<h2>Contact</h2>
<p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> &mdash; we read every message.</p>

"""
    return page(slug, f"{name} — Support", body)


def index(slug, name, genre, has_iap):
    body = f"""<h1>{name}</h1>
<div class="meta">{genre.capitalize()} for iPhone. Free, with ads.</div>
<div class="card">{name} is available on the App Store. Questions or feedback? Email
<a href="mailto:{EMAIL}">{EMAIL}</a>.</div>
<h2>Legal &amp; support</h2>
<ul>
<li><a href="privacy.html">Privacy Policy</a></li>
<li><a href="terms.html">Terms of Use</a></li>
<li><a href="support.html">Support</a></li>
</ul>
<div class="nav"><a href="../">All games</a></div>
"""
    return page(slug, f"{name} — iOS Game", body)


def main(slugs):
    for slug in slugs:
        name, genre, has_iap = GAMES[slug]
        folder = os.path.join(HERE, slug)
        os.makedirs(folder, exist_ok=True)
        for filename, builder in (("index.html", index), ("privacy.html", privacy),
                                  ("terms.html", terms), ("support.html", support)):
            with open(os.path.join(folder, filename), "w") as handle:
                handle.write(builder(slug, name, genre, has_iap))
        print(f"{slug}: 4 pages")


if __name__ == "__main__":
    main(sys.argv[1:] or list(GAMES))
