# HugoAddons
Plugin repository for [Hugo Userbot](https://github.com/TeamHugoX/Hugo)


## Disclaimer ⚠️
```
If you want to add plugins and contribute please fork this RepositoryAnd don't forget to submit a pull request. 
Follow the format below if you don't follow the format below, the withdrawal request will be closed.
```
And if you want to add credit, please add it as below
```python
# Credits @username (creator of plugin and who ported)   
   
# Ported from (if ported else skip)   
   
# Ported for Hugo < https://github.com/TeamHugoX/Hugo >   
```

## Example Plugin
   Required Import are Automatically Done.

<kbd>This Example Works Everywhere. (e.g. Groups, Personal Chats ...)</kbd>
```python
@hugo_cmd(pattern="hoi")
async def hello_world_example(event):
    # As telethon is an asyncio based lib, you will have to use `async`/`await` Syntax.
    await event.reply("Hello **World**.")
```

<kbd>This Example Works Only In Groups.</kbd>
```python
@hugo_cmd(pattern="hoi", groups_only=True,)
async def hello_world_example(event):
    await event.reply("Hello **World**.")
```

If Your plugin need any additional requirements, it can be added to <a href="https://github.com/TeamHugoX/HugoAddons/blob/main/addons.txt">addons.txt

## Special thanks 💕
- [OMGHelo](https://github.com/OMGHelo) : Contributors and Hugo Dev
- [Ultroid](https://github.com/TeamUltroid/Ultroid) : Base code
- And all Dev Repositories Userbot



