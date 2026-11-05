# Ollama Install Day

*Downloading the tool, pulling your first model, and the first real conversation with a machine that lives in your house.*

Parts are in, system boots, drivers are on. Today is the day you talk to an AI that runs entirely inside your own computer — no subscription, no account, no cloud, working with the Wi-Fi off. This chapter walks through it at walking pace. It uses **Ollama**, the free, open-source program that has quietly become the standard on-ramp for local AI: you type one short command, it downloads a model, and you can start chatting.

(Honest, non-endorsement note: Ollama is free software and this guide uses it because it's the simplest well-trodden path for beginners. Other good local-AI tools exist, and the *concepts* here — models, memory, chat — transfer to all of them.)

## What you're actually installing, in one paragraph

Ollama is a **model runner**: a small program that keeps downloaded models on your drive and handles the messy details of running them (loading into VRAM, keeping the memory tidy, answering). You interact with it in two ways: a **terminal command** (`ollama run whatever`) and a **local chat window** in your browser at an address like `localhost:11434`. "Localhost" means *your own machine* — the browser is just the friendly face it provides.

Everything it downloads lives in a folder on your machine. Nothing is sent anywhere. Turn off the internet after setup and it keeps working identically. **This is the whole point of the hobby**, and it's worth saying once: after today, your AI works the same at 2 PM on Wi-Fi and 3 AM in a snowstorm.

## Installing Ollama

**On Windows or Mac:** visit `ollama.com`, download the installer for your system, and run it like any normal program. It installs quietly and puts a small icon in your menu or system tray. That's the whole install — under two minutes, a few hundred megabytes.

**On Linux:** one command in a terminal (copied from the same website):

```
curl -fsSL https://ollama.com/install.sh | sh
```

It installs itself and usually starts automatically. If you're Linux-shy, the Windows/Mac installer exists precisely for you; either path ends in the same place.

**Check it works** by opening a terminal (or the Command Prompt on Windows) and typing:

```
ollama --version
```

A number that isn't an error means it's alive. First milestone. Take a sip of coffee.

## Pulling your first model

"Pulling" is the word the community uses for *downloading a model*. Models live in a searchable catalog on the same site, each with a name like `llama3.2` or `gemma3` or `qwen3` (those are family names, from different makers, all free to run locally).

**For your first pull, choose small.** A small model downloads in minutes, answers fast, and gives you the full experience without asking anything of your hardware. In the terminal:

```
ollama run llama3.2:3b
```

Translation of that line: "please run/download the 3-billion-parameter version of that model family." First time, it downloads (a couple of gigabytes; watch the progress bar), then it drops you into a **chat prompt** — meaning you can just type a sentence and press Enter. You're now talking to an AI that isn't on the internet anywhere.

Things worth trying for the first ten minutes, friend-to-friend:

- A question you'd have typed into a search engine: *"Explain why my kitchen sink gurgles."*
- A summarization job: paste a paragraph or two, ask for three bullet points.
- A translation or idiomatic-English check.
- And the personality test: *"Who are you? Who made you?"* — the answer ("I'm a local language model running on Ollama...") is a nice little confirmation that this is *yours*.

**Type `/bye` or press `Ctrl+D` to leave a chat session.** The model stays downloaded; you're just closing the conversation.

## Expect these three very normal things

1. **Small models are shallow.** They'll answer general questions well and mess up specialized ones, mix up small details, and lose their thread in very long conversations. That's a size class, not a bug — it's what a few billion numbers can and can't hold. (The spreadsheets in the [RAM/VRAM chapter](ram-and-vram.md) show what bigger classes do.)
2. **First answer is slow; the rest are fast.** The model loads into VRAM once — a pause of a few seconds up to a minute — then answers arrive quickly. If *every* answer feels slow, the model is bigger than your VRAM and offloading (long explanation in the last chapter's trap).
3. **It forgets everything between sessions.** Close a chat and the next one starts blank. This is normal for the default tool and is one of the genuinely useful properties — nothing you say is accumulating anywhere. Some more advanced setups add a "memory" feature; this guide's simpler philosophy is: **save what you want to keep into your own files**, and treat the chat like a very well-read friend who never gossips because they forget you.

## Leveling up: which model to try next

When the small model feels too shallow, size up **one class at a time**, based on your VRAM (table back in the [RAM/VRAM chapter](ram-and-vram.md)):

- **8 GB VRAM** — try the ~7–8B class models. Noticeably more capable, still fast.
- **12 GB VRAM** — the ~13–14B class starts. This is where local models start feeling genuinely helpful for real work like document summarizing and drafting.
- **16 GB+ VRAM** — welcome to the range where local models become proper assistants.

The command pattern stays identical (`ollama run <name>`), and the catalog on the website sorts models by size in a beginner-friendly way. One honest rule: **don't run models that clearly out-size your VRAM** "just to see." You'll spend twenty minutes watching a progress bar learn nothing. The right model lives just *under* your memory ceiling, and that's permanent wisdom for the whole hobby.

## Talking to it in a nicer window

The terminal works, but most people graduate to a friendlier chat interface in an afternoon. These work through a simple principle: a small program that draws a nicer chat window and talks to Ollama quietly in the background. Search terms that find good ones: **"local LLM chat interface for Ollama."** (Some are free, some ask for a few dollars. All of them keep everything local — that's the point of the ecosystem.)

One straight-faced note for security-conscious readers: all of this is your machine talking to your machine. Your prompts are processed on your CPU's and graphics card's own silicon, no cloud round-trips, nothing phoning home with your words. If you ever worry about that — and it's a reasonable thing to care about — the simple test is unplugging the internet (or using a firewall tool to block the app) and watching everything keep working. The snowstorm test, it's called, because that's how people *actually* use these machines.

## The end-of-day checklist

```
[ ] Installed and version-checked (ollama --version answered).
[ ] Pulled one small model and had a real conversation.
[ ] Tried summarizing a real document.
[ ] Time-trialed: noted roughly how long first-answer and later-answer take.
[ ] Determined (from speed) whether the model fits in VRAM or is offloading —
    very slow = too big; upgrade path noted for later.
[ ] Found the model's folder size on disk, just to know where your disk went.
[ ] (Optional) Installed a nicer chat interface and customized nothing yet.
[ ] (Optional) Closed the model with /bye and shut down the PC with your
    hard drive feeling a couple of gigabytes heavier and your brain a
    couple of IQ points lighter on the "huh, that's possible?" scale.
```

Tomorrow, you're a person with a local AI. What's left is keeping it healthy: dust, updates, backups, and the five-minute monthly check — which is the [final chapter](upkeep.md).

---

*© Asdale Dynamics, LLC. Educational content only. Ollama is free, open-source software by its own authors; this guide is independent of it and not affiliated with any model or tool maker.*
