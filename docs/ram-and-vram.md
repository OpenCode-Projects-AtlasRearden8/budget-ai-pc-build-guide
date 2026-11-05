# RAM and VRAM, Explained

*The two numbers that decide which AI models can run on your machine — and how big each should be.*

Of all the confusing stuff in PC building, the RAM situation is the one that most reliably fries beginners' circuits, because there are **two kinds** with confusingly similar names, and local AI cares about both. This chapter makes it simple, permanent, and honest.

## The elevator version

- **RAM** is your computer's general workbench. Everything the CPU is actively working with sits there.
- **VRAM** is a smaller, *much faster* workbench that lives *on the graphics card itself*, for the graphics card's exclusive use. The AI model's math happens almost entirely on the graphics card, so the model's numbers live — or are supposed to live — in VRAM.

They are separate pots. Water doesn't flow between them. And when people online say *"no, your VRAM is full"* with an air of tragedy, this is why.

## Why VRAM size = model choice

An AI model is, deep down, an enormous table of numbers (weights) — a very long recipe of *what to pay attention to when something is mentioned*. When you run a model, all those numbers get loaded into fast memory, and then billions of small "look up and multiply" operations happen on them at speeds no general-purpose CPU can approach.

**So the first question is literally arithmetic: does the model's worth of numbers fit in the fast memory you have?**

A rough rule (approximate, human-scale, honest) for the standard way models are stored today:

- Model size in **billions of parameters** (the "7B", "13B" you see in model names) × roughly **0.6 GB per billion** = about how much VRAM it needs, leave a little headroom.

| VRAM you have | Roughly what runs | Feels like |
|---|---|---|
| 4 GB | Small models (up to ~7B) | Quick, snappy, occasionally shallow. Great for quick questions and drafting. |
| 8 GB | Small-to-mid models (up to ~13B) | The classic budget-build zone. Genuinely useful daily. |
| 12 GB | Midsize models comfortably | Answers noticeably more thoughtful; the sweet-spot build territory. |
| 16 GB+ | Midsize-plus models, longer documents | "Is this thing actually smart?" territory. Upper range of used-market frugality. |

(These are coarse ranges. Models vary — some are packed more cleverly than others, and the tools that run them compress differently. Treat the table as orientation, not law.)

**When VRAM runs out, the tool does a clever, slow fallback: it leaves part of the model in the graphics card's fast memory and shovels the overflow into your ordinary RAM.** This is called *offloading*. The model still runs! Answers are still right! They're just **much slower**, because an offload round-trip costs time. So "doesn't fit" doesn't mean "impossible" — it means "slow enough that you'll notice and probably not enjoy it."

This is the deep reason the [price chapter](price-targets.md) said **buy memory first, speed second**: a faster card that holds the whole model comfortably beats a slightly-faster card that has to spill half the model into regular RAM.

## How much RAM (the other pot) should you buy?

RAM matters in three ways, in this order of importance:

1. **Everything that isn't the model.** Your operating system, browser, the program serving the AI, your document editor, everything — all this claims RAM. When the OS runs out, it swaps to disk (slow, unpleasant). Wanting an AI tool and a browser open at once is RAM territory.
2. **Offloading overflow.** If a model doesn't quite fit in VRAM, the spill goes to RAM — a machine with generous RAM can *run* models that are a size class too big, slowly.
3. **Caching and wiggle room.** Tools that load documents for summarization put the document in RAM. Big documents want room.

Plain guidance by budget:

- **8 GB** — livable on the Floor build, with discipline (close the forty tabs).
- **16 GB** — the [sweet spot](price-targets.md) default. Comfortable for daily AI-plus-life use; worth stretching to if a deal appears.
- **32 GB** — the Comfort Zone. Lets you run midsize models with heavier offloading *without the machine feeling strangled*, and means you'll never think about RAM again for years.

## A note on the RAM buyer's checklist

Three things on a stick of RAM mean something:

- **DDR generation.** DDR3 vs DDR4 vs DDR5. Each is physically shaped to *not fit* in the others' slots. Motherboard and RAM must match. This is the single most common headache in used-parts shopping, because sellers of DDR3-era RAM describe it generously and the generation matters.
- **GB.** The number people actually understand. Two 8 GB sticks (16 total) is *better* than one 16 GB stick — RAM sticks have a feature where working in pairs doubles the speed of data in and out. Buy pairs, always.
- **Speed (like 2666, 3200)** — relevant but minor. Match it to your motherboard's supported range; don't pay extra for the top numbers.

One **free** habit that pays a couple of times over: when you're shopping used RAM, look up the exact model number printed on the sticker. Cheap, boring, uncontroversial. The one surprise that catches too many buyers is buying a stick that says a speed the motherboard doesn't officially support — usually fixable in settings, but easier to just check first.

## The one trap to avoid

Combine everything learned here today into the one purchase you must refuse to make: **a card with plenty of speed but too little VRAM.** We keep making the same joke here because it is genuinely *the whole strategy* of budget-AI shopping:

> The graphics card is a math engine that owns a private, fast, small memory. **Memory decides *what you can run*. Speed decides *how fast you can run it*.** Buy memory first.

Wait, that's almost exactly what we said before. That's fine. This entire hobby runs on it.

## A quick story to make it concrete

Here's the whole chapter as it actually happened to a beginner last month — with details changed but the math real:

They bought a [used-parts build on the Floor budget](price-targets.md) (~$300). 8 GB VRAM card. 16 GB RAM. They loaded a small 7B-class local model to test: it fit entirely in VRAM, and it whizzed — answers in a couple of seconds. They loaded a midsize 13B model out of curiosity: it *ran*, but with a big chunk offloaded to RAM, so answers took noticeably long and the fan turned up. Not a failure! But it told them exactly what to fix: next upgrade is the card's memory class, not anything else. **The build told them its next step.** That's what this hobby is like when the parts are chosen with memory first.

Now, [build day](first-boot-checklist.md) is closer than you think. Or if you're still shopping, take the [worksheet](shopping-worksheet.md).

---

*© Asdale Dynamics, LLC. Educational content only; parameter-count and memory figures are rough, human-scale approximations for orientation, not technical specifications.*
