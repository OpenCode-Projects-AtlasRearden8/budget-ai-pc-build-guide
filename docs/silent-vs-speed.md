# Quiet or Fast? The Silence-vs-Speed Tradeoff

*The spec sheet never tells you how loud it will be. This chapter does.*

You will live next to this machine. Every day, for years. And almost nothing in a parts listing tells you how much noise it will make — which is strange, because noise is one of the top three things people come to resent about their computers. This chapter is about the tradeoff hiding inside every cooling decision: **more cooling speed = more performance headroom, and more noise; slower cooling = quieter machine, hotter parts, capped performance.**

You cannot opt out of the tradeoff. You can only choose where to sit on it. Here's how to choose like a person, not a benchmark.

## Why this tradeoff exists

Computer chips turn electricity into math and **heat** — a lot of it, fast. Heat has to leave the chip, because hot chips slow themselves down (this is a safety feature called *thermal throttling*: the machine goes quiet and slow to protect itself) or eventually fail.

Heat leaves in exactly one direction: carried by moving air. So every cooling system is a question. Small fan, gentle spin: quiet, moves a little warm air at a time. Big fan, hard spin: loud, moves a lot of air at a time. There's no third option — heat is physically leaving only with the air.

The tradeoff:

- **Cool the parts generously (loud-ish):** parts never slow down. Maximum performance. The room audibly knows when you're using the computer.
- **Cool modestly (quiet):** the machine is pleasant to sit beside. Under heavy AI load, parts warm up and the machine *chooses* to run a bit slower than its paper stats. Everything still works.

For most people most of the time, **quiet wins by a landslide** — but there's a moment where loud is actually the right call, and it's covered near the end of this chapter.

## Where the noise comes from

Four sources, in the order they usually matter:

1. **The graphics card fans.** Under AI load, these are the loudest thing in the box. Answers to this come later in this chapter.
2. **The case fans.** The little fans on the case walls pushing air through. These run *constantly* — a slow, steady whir never really stops. These are the fans to make quiet first.
3. **The CPU cooler fan.** Usually the smallest. It spins up under load but is rarely uncomfortable.
4. **Everything else**, which is a short list: the hard drive, if you have one (a soft ticking), and coil whine (a faint electronic whine some cards make — annoying to a few people, most never hear it; not fixable, not dangerous).

**Free, powerful, and often forgotten:** your park-yourself test. Whatever machine you use daily — where does it sit relative to your ears? A PC under a desk three feet away is *much* more forgiving of modest noise than a PC you've put on the desk *beside the monitor you're looking at*. Placement is a free noise tool. Under the desk, on the floor, on a hard surface (not carpet directly — vents breathe), and you've already cut perceived noise noticeably.

## Buying for quiet: the checklist that fits on a napkin

You do not need exotic equipment. Only these four habits:

- **Big fans beat small fans, always.** A 120–140 mm case fan moving the same air as two 80 mm fans is dramatically quieter, because air physically cares about fan-blade speed, and big fans do the same *job* at slower spins. Whenever choosing between fan sizes at a given price, the bigger one is the quiet pick.
- **Fewer, larger, slower is best.** Two large case fans (one pulling air in at the front, one pushing it out at the back) cover all realistic needs. Four is not twice as quiet as two; it's twice as many chances for a whine.
- **"120 mm PWM" as a search term.** PWM simply means the motherboard can *dynamically* slow the fans when the machine is idle — which it almost always is. Honest used listings will say it.
- **The case itself matters less than people fear, but a real thing:** solid front panels (not full-holes mesh) block a surprising amount of fan noise from reaching your ears, at the cost of slightly-worse cooling airflow. If you know you need quiet more than max performance, the solid-panel case is the right pick. (Mesh breathes better. This is the entire trade.)

This is also the entire reason [price targets chapter](price-targets.md) allowed a cheap used case but emphasized fan quality: the fans are the parts that made that case's sound. Save happily on boxes, spend thoughtfully on the little motors you'll hear for years.

## The software half of quiet (the free 20 minutes)

After you build, there's a small, free, giant-wins morning-after task most people never do: **check the fan settings in the motherboard's own tool**, almost always found as a handful of sliders in a single settings page. Three sliders matter:

- A **temperature threshold**: the temp at which fans *start* above minimum speed. Nudge this modestly warmer than default.
- A **minimum fan speed**: set it as low as it will go (usually 20–30%). If the machine is silent at idle, you've won the day.
- A **fan curve**: several dots on a graph mapping temps to fan speeds. All it's doing is deciding how *eager* fans are to accelerate. Dropping that eagerness makes a computer dramatically more pleasant to share a room with, and — this is the beautiful part — **for AI workloads it costs you almost nothing** in actual results. AI runs are usually "load it, get an answer, stop" rather than "100% work for 45 minutes," so the fans genuinely don't need to panic.

We can't walk you through the exact menu because every motherboard maker names it something different. It appears in the [first-boot chapter's checklist](first-boot-checklist.md), and searching *"fan curve settings"* plus your motherboard's name finds your exact walkthrough in under a minute.

## The graphics card: one unavoidable, one workaround

The card's own fans are under the card's own control, and only two useful levers exist:

- **Buy cards known for cool, quiet operation.** This is guesswork in the used market unless you search review sites for the card's name plus the word "noise." One search, worth it. Workstation-class cards (the same "boring generation" bargain from the [price chapter](price-targets.md)) are frequently cool-and-quiet by design — another quiet argument for that value pocket.
- **Cap the card's power** in software. Most cards offer a "power limit" slider; dropping it 10–15% costs a few percent of speed and drops fan noise *sharply*, because heat and fan speed track each other almost linearly. This is a genuine free win for AI work, where a 5% slower answer changes nothing.

## When louder is the *right* call

The one loud setup we recommend without reservation: **a machine you're going to run AI on in the background all day, while you do other things at the same desk.** Background AI work means the computer is working long stretches under constant load, and a quiet-biased setup throttles — meaning longer runs, less throughput. There, favor cooling and airflow. Put it where the noise can't reach you (another room, if you can) and let it be a small, dignified jet engine.

For everyone else — the person who turns the machine on, chats with a local model for twenty minutes, then goes back to browsing — **quiet, always.** You will thank yourself every single day. Performance you sacrifice to noise is performance you weren't using.

**The one-line rule:** you can't hear benchmarks. You can always hear fans. Buy accordingly.

Next, the number that decides which models this thing can run: [RAM and VRAM](ram-and-vram.md).

---

*© Asdale Dynamics, LLC. Educational content only. If your machine ever smells like burning electronics, turn it off. That is never a "watch and see."*
