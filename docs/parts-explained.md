# What Each Part Does

*Eight parts. One per plain-English explanation. Know what you're buying before you buy it.*

A desktop computer is exactly eight jobs stacked together in a box. Once you can name the jobs, every parts listing on every secondhand marketplace turns from alphabet soup into a short menu. That's the goal of this chapter: by the end, you should be able to look at any listing and say what it is and roughly why it matters to *you*.

We'll keep a constant steering note through this chapter, because it's the one idea that makes budget AI builds different from budget gaming builds:

> **In a gaming PC, the graphics card is for pictures. In an AI PC, the graphics card is for thinking.** Every AI model is a mountain of simple math, and the graphics card is a machine built to do exactly that kind of math, very fast, in parallel. Everything else in the box exists to keep it fed and supported.

## 1. The CPU — the manager

The **central processing unit** is the general-purpose worker. It runs your operating system, your browser, the tool that serves the AI, the input from your mouse — everything *except* the raw model math. It's also the fallback brain: some small models can run on the CPU alone, which is how even an old laptop manages anything at all.

For an AI desktop, the CPU is a supporting actor. You need *enough* cores (4 to 8 is plenty), reasonable age (under ~8 years old is fine), and no more money spent than that. A used mid-grade office-desktop CPU costs about as much as a pizza and does the job nearly as well as its fancy cousins.

**When listing-shopping, look for:** core count (4+), and anything described as mid-grade from the last several generations. Don't pay a premium for the top of any family — the graphics card does the heavy lifting.

## 2. The motherboard — the nervous system

The **motherboard** is the green (or now often black) board everything plugs into. It connects the CPU to the memory to the storage to the graphics card, and it decides, quietly, what upgrades are possible later.

Two spec lines matter for you:

- **Ram slots**: 2 or 4. More slots = easier future upgrades.
- **Socket type**: the physically shaped connector the CPU drops into. CPU and motherboard must *match* here. When buying used, an easy path is to buy the CPU and motherboard **as a matched pair** from one seller — it costs slightly more than separate but removes the single most common beginner mistake: buying parts that physically can't talk to each other.

Also check it has: a slot for your graphics card (nearly universal), an Ethernet port, and at least the number of ports your storage will use.

**When listing-shopping, look for:** the matching socket name for your CPU, "DDR4" or "DDR3" (this is the memory-generation label — more in the RAM section), and words like "micro-ATX" (a slightly smaller, cheaper size that fits normal towers).

## 3. RAM — the workbench

**RAM** (random access memory) is your computer's workbench: the space where whatever you're working on *right now* lives. It's not storage — turn the computer off and the workbench is wiped. It matters to local AI as the "overflow area" when a model doesn't entirely fit on the graphics card.

This is the cheapest place for a beginner to buy confidence:

- **8 GB** — works, feels cramped when multitasking.
- **16 GB** — the honest sweet spot for normal use and small-to-mid models.
- **32 GB** — the comfortable zone for pushing bigger models, at a used-market price that's usually modest.

**When listing-shopping, look for:** the DDR generation matching your motherboard (DDR3 vs DDR4 vs DDR5 — they're shaped differently and physically cannot cross over), and matching speed is nice-to-have but not a priority number one. Buying a pair of identical sticks ("a matched pair of 8 GB") is the correct beginner move, because pairs run faster than single sticks on most boards.

Deeper detail on how RAM and the graphics card's memory share the AI burden lives in the [RAM and VRAM chapter](ram-and-vram.md).

## 4. The graphics card — the thinking engine

This is the star of the show and the part to spend on. The **graphics card** (also called the video card or "GPU") is a specialized parallel-math machine. Every AI model you care about runs primarily on it — the speed you'll feel and the model sizes you can handle both come from it.

Two numbers control your entire experience:

- **VRAM**: the card's own fast memory (see next chapter) — decides **which** models can run.
- **Speed class**: how fast the card's math is — decides **how fast** those models answer.

Used-market reality check, said plainly and without naming any product: a used mid-grade, work-oriented, or previous-generation graphics card with **8–12 GB of VRAM** is the target for a first AI build. Cards with 6 GB can be excellent value. Cards below 6 GB deserve a deep discount and a modest role. Cards marketed as "gaming flagships from the last two years" are almost always sold at prices a frugal builder should refuse.

**When listing-shopping, look for:** the VRAM number *first*, then the age of the card. Prefer listings from someone who used the card in an office or home machine over listings photographed half-installed in a mining rig (more on why in the [price chapter](price-targets.md)).

## 5. Storage — the bookshelf

**Storage** (a drive, usually an SSD) is where files live permanently: the operating system, your AI models, your documents. Unlike RAM, it survives power-off. You will be surprised how fast AI models eat disk space — they range from a few gigabytes to tens of gigabytes each.

Plain-English guidance:

- **SSD vs HDD**: an SSD (silent, fast, no moving parts) is worth nearly any price difference for your main drive. An HDD (older, slower, noisy, cheap) is acceptable *only* as secondary storage for files you rarely touch.
- **Size**: 256 GB works but you'll feel the wall in a year. **512 GB** is realistic. **1 TB** is generous peace-of-mind, and used drives of this size usually aren't much more.

**When listing-shopping, look for:** "SSD" and the word "SATA" or "NVMe" (both are fine types; NVMe is a bit faster). Beware sellers listing HDDs as though their cheapness were a virtue — it is, but you'll regret making one your main drive.

## 6. The power supply — the heart

The **power supply unit (PSU)** converts wall electricity into the steady, safe, several-voltage meal your parts eat. It's the part with the largest gap between "boring" and "critically important." A bad PSU doesn't just fail — a *cheap, worn-out* one can damage other parts on its way out.

Budget-build guidance:

- Size (measured in watts): 450–550 W is comfortably enough for most AI builds; 650 W only if your graphics card is a power-hungry one.
- **Buy used-ish, not used-hard.** PSUs wear out silently. The used-market value of a PSU is modest; a *new*, reputable-but-inexpensive one costs roughly a dinner out and is one of the two parts (with the case) we give you permission to buy new. This is worth saying plainly: **new PSU** is a budget-build cheat code.

**When listing-shopping (if you do go used), look for:** known-brand names, an "80 Plus" sticker (any color level — it just means it's efficient enough not to waste heat), and who is selling. Avoid mystery brands and photo-blurry wires.

## 7. The case — the skeleton (and the noise chamber)

The **case** is a metal box: it holds everything, protects it from dust and cats, and — this is the part beginners learn the hard way — it makes most of the **noise**.

Case shopping is almost entirely about practicality:

- **Standard "mid-tower" size** — fits all normal parts, easy to work in, cheap used.
- **Includes at least one fan** — the case usually comes with one or two. Fans are how air moves; air is how heat leaves; heat is how electronics die young.
- **Front panel has USB ports** — small daily quality-of-life win.
- **Bonus, if you can find it cheap: "sound-dampened" panels** — foam-lined, genuinely quieter. Not essential; the same result can come from choosing slow, quiet case fans, which is covered in the [silent vs. speed chapter](silent-vs-speed.md).

Shopping note: cases are one of the most commonly *given away* parts — people upgrade for aesthetics and their old black boxes sit in a closet. Ask downright politely; a building's worth of people have one.

## 8. The cooler — the little fan on the CPU

The last part is the **CPU cooler**: a small heat sink and fan that sits directly on top of the CPU. Sometimes the user manually attaches it; sometimes the CPU comes with one in the box (an "included stock cooler" — perfectly usable). It is not optional, even briefly: a CPU with no cooler on top of it will overheat in seconds of operation.

You will rarely think about this part again after installation. Use the free one if it's in the box; buy a basic one (~$15–25 range at the writing of this guide) if not. The performance ceiling of a budget AI build is set by the graphics card, and the graphics card cools itself.

---

That's the whole box. Eight jobs: **manage** (CPU), **connect** (motherboard), **hold your workspace** (RAM), **think** (graphics card), **remember** (storage), **feed** (power supply), **house and quiet** (case), **keep cool** (cooler).

Next up: the money. [How much each part should actually cost, and three total budgets that respect you.](price-targets.md)

---

*© Asdale Dynamics, LLC. Educational content only — this guide describes part categories, not specific products. Local sellers, local listings, your local prices.*
