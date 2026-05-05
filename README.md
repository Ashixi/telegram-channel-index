# Telegram Channel Index 📡

An open, community-driven index of public Telegram channels.

##  What is this?

This project is a simple open database of public Telegram channels, organized by topics.

The goal is to create a structured and searchable index of content sources from Telegram — because currently there is no clean, unified directory of public channels.

This is not a social network.  
This is not a messaging app.

It is an **open index layer on top of Telegram content**.

---

## Why this exists

Public Telegram content is fragmented:
- channels are hard to discover
- there is no global search
- quality sources are scattered
- categorization is inconsistent

This project tries to solve that by building a structured, open dataset.

---

##  Structure

Each entry in the dataset should follow this format:

```json
{
  "name": "Channel Name",
  "url": "https://t.me/channel_username",
  "category": "tech / news / crypto / memes / etc",
  "language": "en / ua / ru / etc",
  "description": "Short description of the channel(optional)"
}
