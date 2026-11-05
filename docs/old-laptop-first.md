# Try Your Old Laptop First

*The most expensive PC you can buy is one you don't actually need. Here's how to find out — for free — before you spend a dime.*

Here's the advice nobody selling you hardware wants to give: **before you budget a single dollar, spend one evening testing what you already own.** A surprising number of people who "need a new PC for AI" already own a machine that runs small local models perfectly well for the things they actually do — and finding that out costs nothing but a download.

This chapter is short on purpose. If the old laptop wins, you've saved yourself several hundred dollars and a weekend. If it loses, you'll have concrete numbers to shop with, which makes every later chapter in this guide easier.

## The two-minute honest check

You need two facts about your current machine. No jargon required, we'll walk it through.

### Fact 1: How much RAM do you have?

RAM is your computer's working memory — the space it uses while doing things. On **Windows**: press `Ctrl+Shift+Esc` to open Task Manager, look at the Performance tab, and find "Memory." On **macOS**: click the Apple menu, choose "About This Mac," and read the "Memory" line. On **Linux**: open a terminal and type `free -h`, reading the "total" line.

- **4 GB or less** — Your laptop is running on fumes even for everyday tasks. Keep reading this guide; a build will genuinely help.
- **8 GB** — Borderline. Small local AI models can run, but you should close everything else. Also fine to keep reading.
- **16 GB or more** — Interesting! Write that down. You may already have a usable machine.

### Fact 2: What graphics capability do you have?

The key question is whether you have a **dedicated graphics card with its own memory (VRAM)** — the thing that makes local AI fast — or just the basic graphics built into your computer's main chip. On Task Manager's Performance tab (Windows), look for two different entries: "GPU 0" and possibly "GPU 1" or a listing with a large "Dedicated GPU memory" number. On macOS, the About This Mac window shows the graphics chip name; any Apple-silicon Mac counts as a generally capable machine for its class. On Linux, run `lspci | grep -i vga` and see whether anything beyond the default paperwork name appears.

- **Dedicated graphics with 6 GB of VRAM or more** — Stop here first. Install a local AI tool (see the [Ollama chapter](ollama-install-day.md) for the step-by-step) and just try it.
- **Any Apple-silicon Mac (M1, M2, etc.) with 16 GB unified memory** — Also stop. These machines run small models surprisingly well; the memory is shared between "graphics" and "general" duty, which is fine for AI work.
- **Built-in graphics only, 8 GB RAM** — You're in "it will run, slowly" territory. Try a very small model with everything else closed. If it feels like watching paint dry, that's your answer too.

## The free experiment

If either check came back "interesting," do this before shopping:

1. **Back up anything you care about.** Standard advice, applies to every computer, laptop or new. One USB drive is enough.
2. **Install a local AI tool the easy way.** The [Ollama install day chapter](ollama-install-day.md) walks through this for real computers, and the same process works on a laptop — the steps are nearly identical.
3. **Load the smallest model offered.** Small models are a few gigabytes and are genuinely useful for everyday questions, summarizing, and drafting.
4. **Use it for a real evening of real work.** Not a benchmark — actual tasks. Draft an email. Summarize a document you needed to read anyway. Ask the questions you'd normally type into a search bar.

Then judge it like a human, not a reviewer:

- Was it fast enough that you *forgot* it was slow? (This is the magic threshold. "Annoyingly slow" is different from "imperceptibly slow.")
- Did it ever say it "ran out of memory" or refuse a slightly bigger task?
- Did your browser survive at the same time, or did everything grind?

If the answers are: forgot it was slow, never ran out, and the machine lived — **stop shopping.** Buy yourself a nice keyboard instead. That money is now free for something that isn't a computer.

## When the laptop genuinely loses

It will lose if you find yourself wanting any of these:

- **Bigger, smarter models.** If the small models keep giving answers that miss the point, a machine with more VRAM lets you run better ones.
- **Always-summarizing big documents.** Feeding it a 60-page PDF and getting useful output back needs memory in a way laptops rarely have.
- **Doing it all day without noise complaints.** Laptop fans scream under AI load. A desktop with the right (see: [quiet](silent-vs-speed.md)) parts hums.
- **A real desktop setup** — you're sitting at the same desk most of the time anyway, and the cyclone of heat from an overworked laptop on a duvet is not a lifestyle.

If any of those sound like you, congratulations: you now know **why** you're building, which is exactly what the next chapter assumes you know. Write down one sentence like *"My laptop can't summarize big documents and the fan is a jet engine"* — that's the true north for every purchase you're about to make.

## One more honest point: the laptop is still worth keeping

Even in the worst case, that laptop is not dead. It becomes:

- **A quiet companion screen** for looking up parts lists while your PC is in pieces on the floor.
- **The machine you install Ollama on today anyway**, so you learn the tool while your parts are in the mail.
- **A backup.** Computer parts fail eventually, even new ones. Having any working computer means a failed part is an inconvenience, not a crisis.

Test it. Time it. Take notes. And only then open your wallet — with a number in mind, which is where [the next chapter](parts-explained.md) begins.

---

*© Asdale Dynamics, LLC. Educational content only. Your machines are your responsibility — back up before any experiment, laptop or otherwise.*
