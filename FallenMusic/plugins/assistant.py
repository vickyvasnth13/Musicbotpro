from pyrogram import filters
from pyrogram.types import Message

from FallenMusic import app, userbot as app2
from config import OWNER_ID as SUDOERS


@app.on_message(filters.command(["asspfp", "setpfp"]) & filters.user(SUDOERS))
async def set_pfp(_, message: Message):
    if message.reply_to_message.photo:
        fuk = await message.reply_text("» ᴄʜᴀɴɢɪɴɢ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ...")
        img = await message.reply_to_message.download()
        try:
            await app2.one.set_profile_photo(photo=img)
            return await fuk.edit_text(f"» {app2.one.name} ᴘʀᴏғɪʟᴇ ᴘɪᴄ ᴄʜᴀɴɢᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ.")
        except:
            return await fuk.edit_text("» ғᴀɪʟᴇᴅ ᴛᴏ ᴄʜᴀɴɢᴇ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ.")
    else:
        await message.reply_text("» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ғᴏʀ ᴄʜᴀɴɢɪɴɢ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ.")


@app.on_message(filters.command(["delpfp", "delasspfp"]) & filters.user(SUDOERS))
async def set_pfp(_, message: Message):
    try:
        pfp = [p async for p in app2.one.get_chat_photos("me")]
        await app2.one.delete_profile_photos(pfp[0].file_id)
        return await message.reply_text("» sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ.")
    except Exception as ex:
        print(ex)
        await message.reply_text("» ғᴀɪʟᴇᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀssɪsᴛᴀɴᴛ's ᴘʀᴏғɪʟᴇ ᴘɪᴄ.")


@app.on_message(filters.command(["assbio", "setbio"]) & filters.user(SUDOERS))
async def set_bio(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            newbio = msg.text
            await app2.one.update_profile(bio=newbio)
            return await message.reply_text(f"» {app2.one.name} ʙɪᴏ ᴄʜᴀɴɢᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ.")
    elif len(message.command) != 1:
        newbio = message.text.split(None, 1)[1]
        await app2.one.update_profile(bio=newbio)
        return await message.reply_text(f"» {app2.one.name} ʙɪᴏ ᴄʜᴀɴɢᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ.")
    else:
        return await message.reply_text("» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ sᴇᴛ ɪᴛ ᴀs ᴀssɪsᴛᴀɴᴛ's ʙɪᴏ.")


@app.on_message(filters.command(["assname", "setname"]) & filters.user(SUDOERS))
async def set_name(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            name = msg.text
            await app2.one.update_profile(first_name=name)
            return await message.reply_text(f"» {app2.one.name} ɴᴀᴍᴇ ᴄʜᴀɴɢᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ.")
    elif len(message.command) != 1:
        name = message.text.split(None, 1)[1]
        await app2.one.update_profile(first_name=name, last_name="")
        return await message.reply_text(f"» {app2.one.name} ɴᴀᴍᴇ ᴄʜᴀɴɢᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ.")
    else:
        return await message.reply_text("» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ sᴇᴛ ɪᴛ ᴀs ᴀssɪsᴛᴀɴᴛ's ɴᴇᴡ ɴᴀᴍᴇ.")
